from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods
from .models import Cliente


def lista_clientes(request: HttpRequest) -> HttpResponse:
    q = request.GET.get("q", "")
    clientes_qs = Cliente.objects.all().order_by("-criado_em")
    if q:
        clientes_qs = clientes_qs.filter(nome__icontains=q)
    paginator = Paginator(clientes_qs, 10)
    page_obj = paginator.get_page(request.GET.get("page"))
    context = {"page_obj": page_obj, "q": q}
    if request.headers.get("HX-Request"):
        return render(request, "clientes/_tabela.html", context)
    return render(request, "clientes/lista.html", context)


@require_http_methods(["GET", "POST"])
def form_cliente(request: HttpRequest, pk: int | None = None) -> HttpResponse:
    if request.method == "GET":
        cliente = None if pk is None else get_object_or_404(Cliente, pk=pk)
        return render(request, "clientes/_form.html", {"cliente": cliente})
    nome = request.POST.get("nome", "").strip()
    email = request.POST.get("email", "").strip()
    errors = {}
    if not nome:
        errors["nome"] = "Informe o nome."
    cliente = get_object_or_404(Cliente, pk=pk) if pk else None
    if errors:
        return render(
            request, "clientes/_form.html", {"cliente": cliente, "errors": errors}
        )
    if cliente:
        cliente.nome, cliente.email = nome, email
        cliente.save()
    else:
        Cliente.objects.create(nome=nome, email=email)
    q = request.GET.get("q", "")
    clientes_qs = Cliente.objects.all().order_by("-criado_em")
    if q:
        clientes_qs = clientes_qs.filter(nome__icontains=q)
    paginator = Paginator(clientes_qs, 10)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(request, "clientes/_tabela.html", {"page_obj": page_obj, "q": q})
