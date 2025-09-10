import xml.etree.ElementTree as ET
from decimal import Decimal
from django.shortcuts import render, redirect
from django.utils import timezone
from django.core.files import File
from django.contrib import messages
from .forms import ImportarNFeForm
from .models import MovimentoEstoque, ItemLicitado, Fornecedor


def importar_nfe_view(request, admin_site):
    if request.method == "POST":
        form = ImportarNFeForm(request.POST, request.FILES)
        if form.is_valid():
            arquivo = form.cleaned_data["arquivo_xml"]

            tree = ET.parse(arquivo)
            root = tree.getroot()
            ns = {"nfe": "http://www.portalfiscal.inf.br/nfe"}

            emit = root.find(".//nfe:emit", ns)
            cnpj = emit.find("nfe:CNPJ", ns).text
            razao_social = emit.find("nfe:xNome", ns).text

            fornecedor, _ = Fornecedor.objects.get_or_create(
                cnpj=cnpj, defaults={"razao_social": razao_social}
            )

            for det in root.findall(".//nfe:det", ns):
                codigo_item = det.find("nfe:prod/nfe:cProd", ns).text
                quantidade = Decimal(det.find("nfe:prod/nfe:qCom", ns).text)

                try:
                    item = ItemLicitado.objects.get(codigo=codigo_item)
                except ItemLicitado.DoesNotExist:
                    messages.warning(
                        request, f"Item {codigo_item} não encontrado. Pulando..."
                    )
                    continue

                movimento = MovimentoEstoque.objects.create(
                    item=item,
                    tipo="ENTRADA",
                    quantidade=quantidade,
                    fornecedor=fornecedor,
                    documento=f"NF-e {root.find('.//nfe:ide/nfe:nNF', ns).text}",
                    data_movimento=timezone.now(),
                )

                # Salva o XML no campo arquivo_nf
                arquivo.seek(0)
                movimento.arquivo_nf.save(arquivo.name, File(arquivo), save=True)

            messages.success(request, "NF-e importada com sucesso!")
            return redirect("..")
    else:
        form = ImportarNFeForm()

    return render(
        request, "admin/importar_nfe.html", {"form": form, "title": "Importar NF-e"}
    )
