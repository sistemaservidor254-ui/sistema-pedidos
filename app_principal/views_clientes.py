# app_principal/views_clientes.py
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods
from .models import Cliente


def lista_clientes(request: HttpRequest) -> HttpResponse:
    """
    Retorna a lista de clientes como página inteira (se acesso direto)
    ou apenas o fragmento da tabela se chamado por HTMX (hx-get).
    """
    q = request.GET.get("q", "")
    clientes_qs = Cliente.objects.all().order_by("-criado_em")
    if q:
        clientes_qs = clientes_qs.filter(nome__icontains=q)

    paginator = Paginator(clientes_qs, 10)
    page_obj = paginator.get_page(request.GET.get("page"))

    context = {"page_obj": page_obj, "q": q}

    # Se for requisição HTMX, renderiza o parcial apenas
    if request.headers.get("HX-Request"):
        return render(request, "clientes/_tabela.html", context)

    # Caso contrário, renderiza uma página com a tabela embutida
    return render(request, "clientes/lista.html", context)


@require_http_methods(["GET", "POST"])
def form_cliente(request: HttpRequest, pk: int | None = None) -> HttpResponse:
    """
    Renderiza e processa o form de cliente para criação/edição.
    Responde com parciais para atualizar o modal ou a tabela.
    """
    if request.method == "GET":
        cliente = None if pk is None else get_object_or_404(Cliente, pk=pk)
        return render(request, "clientes/_form.html", {"cliente": cliente})

    # POST
    nome = request.POST.get("nome", "").strip()
    email = request.POST.get("email", "").strip()

    errors = {}
    if not nome:
        errors["nome"] = "Informe o nome."

    cliente = None
    if pk:
        cliente = get_object_or_404(Cliente, pk=pk)

    if errors:
        # Reenvia o form com erros
        return render(
            request, "clientes/_form.html", {"cliente": cliente, "errors": errors}
        )

    if cliente:
        cliente.nome = nome
        cliente.email = email
        cliente.save()
    else:
        cliente = Cliente.objects.create(nome=nome, email=email)

    # Após salvar, devolvemos a tabela atualizada (HTMX substituirá no alvo)
    q = request.GET.get("q", "")
    clientes_qs = Cliente.objects.all().order_by("-criado_em")
    if q:
        clientes_qs = clientes_qs.filter(nome__icontains=q)
    paginator = Paginator(clientes_qs, 10)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(request, "clientes/_tabela.html", {"page_obj": page_obj, "q": q})
