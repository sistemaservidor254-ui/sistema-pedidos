from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import Cliente  # ajuste se o model tiver outro nome


def excluir_cliente(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Remove o cliente identificado por pk e redireciona para a lista de clientes.
    Requer método POST para efetivar deleção; GET mostra página de confirmação simples.
    """
    cliente = get_object_or_404(Cliente, pk=pk)

    if request.method == "POST":
        cliente.delete()
        messages.success(request, "Cliente excluído com sucesso.")
        return redirect("lista_clientes")  # ajuste o nome da URL se diferente

    # GET: renderizar confirmação simples (opcional: criar template app_principal/confirm_delete.html)

    return render(request, "app_principal/confirm_delete.html", {"object": cliente})


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
