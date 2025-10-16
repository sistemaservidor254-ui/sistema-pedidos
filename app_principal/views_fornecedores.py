from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods
from .models import Fornecedor
import json


def _query_fornecedores(q: str):
    """
    Monta a query base de fornecedores com ordenação e filtro opcional por razão social.
    """
    qs = Fornecedor.objects.all().order_by("-id")
    if q:
        qs = qs.filter(razao_social__icontains=q)
    return qs


def _pagina_segura(paginator: Paginator, page_number: str | None):
    """
    Retorna uma página válida mesmo se 'page_number' for inválida.
    """
    try:
        return paginator.get_page(page_number)
    except (PageNotAnInteger, EmptyPage):
        return paginator.get_page(1)


def lista_fornecedores(request: HttpRequest) -> HttpResponse:
    """
    Lista fornecedores com busca e paginação.
    - HTMX: retorna apenas _tabela.html
    - Acesso direto: retorna lista.html
    """
    q = request.GET.get("q", "").strip()
    fornecedores_qs = _query_fornecedores(q)
    paginator = Paginator(fornecedores_qs, 10)
    page_obj = _pagina_segura(paginator, request.GET.get("page"))

    context = {"page_obj": page_obj, "q": q}

    if request.headers.get("HX-Request"):
        return render(request, "fornecedores/_tabela.html", context)

    return render(request, "fornecedores/lista.html", context)


@require_http_methods(["GET", "POST"])
def form_fornecedor(request: HttpRequest, pk: int | None = None) -> HttpResponse:
    """
    Cria ou edita fornecedor.
    """
    q = request.GET.get("q", "").strip()

    if request.method == "GET":
        fornecedor = None if pk is None else get_object_or_404(Fornecedor, pk=pk)
        return render(
            request, "fornecedores/_form.html", {"fornecedor": fornecedor, "q": q}
        )

    # POST
    razao_social = request.POST.get("razao_social", "").strip()
    cnpj = request.POST.get("cnpj", "").strip()
    endereco = request.POST.get("endereco", "").strip()
    cidade = request.POST.get("cidade", "").strip()
    estado = request.POST.get("estado", "").strip()
    telefone = request.POST.get("telefone", "").strip()
    email = request.POST.get("email", "").strip()

    errors: dict[str, str] = {}
    if not razao_social:
        errors["razao_social"] = "Informe a razão social."
    if not cnpj:
        errors["cnpj"] = "Informe o CNPJ."

    fornecedor = get_object_or_404(Fornecedor, pk=pk) if pk else None

    if errors:
        return render(
            request,
            "fornecedores/_form.html",
            {"fornecedor": fornecedor, "errors": errors, "q": q},
        )

    if fornecedor:
        fornecedor.razao_social = razao_social
        fornecedor.cnpj = cnpj
        fornecedor.endereco = endereco
        fornecedor.cidade = cidade
        fornecedor.estado = estado
        fornecedor.telefone = telefone
        fornecedor.email = email
        fornecedor.save()
        action = "updated"
    else:
        Fornecedor.objects.create(
            razao_social=razao_social,
            cnpj=cnpj,
            endereco=endereco,
            cidade=cidade,
            estado=estado,
            telefone=telefone,
            email=email,
        )
        action = "created"

    fornecedores_qs = _query_fornecedores(q)
    paginator = Paginator(fornecedores_qs, 10)
    page_obj = _pagina_segura(paginator, request.GET.get("page"))

    response = render(
        request, "fornecedores/_tabela.html", {"page_obj": page_obj, "q": q}
    )
    response["HX-Trigger"] = json.dumps(
        {"fornecedor:saved": {"action": action, "nome": razao_social}}
    )
    return response


@require_http_methods(["DELETE", "POST"])
def excluir_fornecedor(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Exclui fornecedor e retorna tabela atualizada.
    """
    q = request.GET.get("q", "").strip()
    page_number = request.GET.get("page")

    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    nome_fornecedor = fornecedor.razao_social
    fornecedor.delete()

    fornecedores_qs = _query_fornecedores(q)
    paginator = Paginator(fornecedores_qs, 10)
    page_obj = _pagina_segura(paginator, page_number)

    if not page_obj.object_list and page_obj.number > 1:
        page_obj = _pagina_segura(paginator, str(page_obj.number - 1))

    response = render(
        request, "fornecedores/_tabela.html", {"page_obj": page_obj, "q": q}
    )
    response["HX-Trigger"] = json.dumps(
        {"fornecedor:deleted": {"nome": nome_fornecedor}}
    )
    return response
