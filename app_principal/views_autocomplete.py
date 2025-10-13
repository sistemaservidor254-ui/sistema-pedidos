import time
import requests
from django.conf import settings
from django.core.cache import cache
from django.http import JsonResponse
from django.views.decorators.http import require_GET


@require_GET
def autocomplete_endereco(request):
    """
    Endpoint intermediário para buscar sugestões de endereço no LocationIQ
    sem expor a chave no frontend.
    Aplica um rate limit simples por IP para evitar excesso de requisições.
    """
    query = request.GET.get("q", "").strip()
    if len(query) < 3:
        return JsonResponse([], safe=False)

    # Rate limit simples: máximo de 100 requisições/dia por IP
    ip = request.META.get("REMOTE_ADDR")
    chave_cache = f"autocomplete_count_{ip}_{time.strftime('%Y%m%d')}"
    count = cache.get(chave_cache, 0)

    if count >= 100:
        return JsonResponse({"error": "Limite diário atingido"}, status=429)

    cache.set(chave_cache, count + 1, 86400)  # expira em 1 dia

    url = "https://us1.locationiq.com/v1/autocomplete.php"
    params = {
        "key": settings.LOCATIONIQ_KEY,
        "q": query,
        "limit": 5,
        "countrycodes": "br",
        "format": "json",
    }

    try:
        r = requests.get(url, params=params, timeout=5)
        r.raise_for_status()
        return JsonResponse(r.json(), safe=False)
    except requests.RequestException:
        return JsonResponse({"error": "Falha ao buscar endereço"}, status=500)
