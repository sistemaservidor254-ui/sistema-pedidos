# Imports da biblioteca padrão
from pathlib import Path

# Imports de terceiros
from django.contrib import admin, messages
from django.utils.html import format_html
from django.urls import path
from django.core.files.base import ContentFile
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

# Imports locais (do próprio app)
from .models import (
    MovimentoEstoque,
    SaldoEstoque,
    Edital,
    Fornecedor,
    ARPContrato,
    ItemLicitado,
    Clausula,
    Feriado,
    Empresa,
    Produto,
    Pedido,
    ItemDoPedido,
    Usuario,
    Auditoria,
)
from . import admin_views
from .storage.mega_cmd import enviar_para_mega


import os


def enviar_para_google_drive(caminho_arquivo, nome_arquivo, pasta_id=None):
    # Se o arquivo de credenciais não existir, pula o upload
    if not os.path.exists("credenciais_drive.json"):
        print("Google Drive não configurado — pulando upload.")
        return None

    from pydrive.auth import GoogleAuth
    from pydrive.drive import GoogleDrive

    gauth = GoogleAuth()
    gauth.LoadServiceConfigFile("credenciais_drive.json")
    drive = GoogleDrive(gauth)

    arquivo = drive.CreateFile(
        {"title": nome_arquivo, "parents": [{"id": pasta_id}] if pasta_id else []}
    )
    arquivo.SetContentFile(caminho_arquivo)
    arquivo.Upload()
    arquivo.InsertPermission({"type": "anyone", "value": "anyone", "role": "reader"})

    return f"https://drive.google.com/file/d/{arquivo['id']}/view"


@admin.action(description="Reenviar NF-es selecionadas para MEGA e Google Drive")
def reenviar_links(modeladmin, request, queryset):
    """
    Ação em massa para reenviar arquivos para MEGA e Google Drive
    apenas para registros que ainda não têm link.
    """
    enviados = 0
    erros = 0

    for movimento in queryset:
        try:
            if not movimento.arquivo_nf:
                continue  # pula se não houver arquivo salvo localmente

            # Envia para MEGA se não tiver link
            if not movimento.arquivo_nf_url:
                link_mega = enviar_para_mega(
                    movimento.arquivo_nf.path, pasta_destino="/NF"
                )
                if link_mega:
                    movimento.arquivo_nf_url = link_mega

            # Envia para Google Drive se não tiver link
            if not movimento.arquivo_nf_url_drive:
                nome_arquivo = Path(movimento.arquivo_nf.name).name
                link_drive = enviar_para_google_drive(
                    movimento.arquivo_nf.path, nome_arquivo
                )
                if link_drive:
                    movimento.arquivo_nf_url_drive = link_drive

            movimento.save()
            enviados += 1

        except Exception as e:
            erros += 1
            messages.error(request, f"Erro ao enviar {movimento.id}: {e}")

    messages.success(request, f"Reenvio concluído: {enviados} enviados, {erros} erros.")


class LinkNFeFilter(admin.SimpleListFilter):
    """
    Filtro personalizado para exibir movimentos com ou sem links de NF-e.
    Permite filtrar por:
    - Apenas com link do MEGA
    - Apenas com link do Google Drive
    - Com ambos os links
    - Sem nenhum link
    """

    title = "Links NF-e"
    parameter_name = "links_nfe"

    def lookups(self, request, model_admin):
        """
        Define as opções que aparecerão no filtro lateral do admin.
        """
        return [
            ("mega", "Com link do MEGA"),
            ("drive", "Com link do Google Drive"),
            ("ambos", "Com ambos os links"),
            ("nenhum", "Sem link"),
        ]

    def queryset(self, request, queryset):
        """
        Aplica o filtro de acordo com a opção escolhida.
        """
        if self.value() == "mega":
            return queryset.exclude(arquivo_nf_url__isnull=True).exclude(
                arquivo_nf_url__exact=""
            )
        elif self.value() == "drive":
            return queryset.exclude(arquivo_nf_url_drive__isnull=True).exclude(
                arquivo_nf_url_drive__exact=""
            )
        elif self.value() == "ambos":
            return (
                queryset.exclude(arquivo_nf_url__isnull=True)
                .exclude(arquivo_nf_url__exact="")
                .exclude(arquivo_nf_url_drive__isnull=True)
                .exclude(arquivo_nf_url_drive__exact="")
            )
        elif self.value() == "nenhum":
            return queryset.filter(
                arquivo_nf_url__isnull=True, arquivo_nf_url_drive__isnull=True
            ) | queryset.filter(arquivo_nf_url="", arquivo_nf_url_drive="")
        return queryset


@admin.register(MovimentoEstoque)
class MovimentoEstoqueAdmin(admin.ModelAdmin):
    change_list_template = "admin/movimentoestoque_changelist.html"

    list_display = (
        "id",
        "item",
        "tipo",
        "quantidade",
        "fornecedor",
        "documento",
        "data_movimento",
        "link_nf",
        "links_nfe",
    )

    list_filter = (
        "tipo",
        "fornecedor",
        "data_movimento",
        LinkNFeFilter,  # 👈 nosso filtro personalizado
    )
    search_fields = (
        "item__codigo",
        "item__descricao",
        "documento",
        "fornecedor__razao_social",
    )
    readonly_fields = ("link_nf",)
    search_fields = (
        "item__codigo",
        "item__descricao",
        "documento",
        "fornecedor__razao_social",
    )
    readonly_fields = ("link_nf",)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                "importar-nfe/",
                self.admin_site.admin_view(
                    lambda r: admin_views.importar_nfe_view(r, self.admin_site)
                ),
                name="importar-nfe",
            ),
        ]
        return custom_urls + urls

    def link_nf(self, obj):
        url = obj.arquivo_nf_url or (obj.arquivo_nf.url if obj.arquivo_nf else None)
        if url:
            return format_html("<a href='{}' target='_blank'>📄 Baixar NF</a>", url)
        return "-"

    link_nf.short_description = "Nota Fiscal"

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # Se tiver arquivo e ainda não tiver link no MEGA
        if obj.arquivo_nf and not obj.arquivo_nf_url:
            caminho = obj.arquivo_nf.path
            link = enviar_para_mega(caminho, pasta_destino="/NF")
            if link:
                obj.arquivo_nf_url = link
                obj.save(update_fields=["arquivo_nf_url"])

    def links_nfe(self, obj):
        """
        Exibe ícones clicáveis para baixar a NF-e do MEGA e do Google Drive.
        Só mostra o link se ele existir no registro.
        """
        links = []

        # Link do MEGA
        if obj.arquivo_nf_url:
            links.append(
                f'<a href="{obj.arquivo_nf_url}" target="_blank" title="Baixar do MEGA">📦 MEGA</a>'
            )

        # Link do Google Drive
        if obj.arquivo_nf_url_drive:
            links.append(
                f'<a href="{obj.arquivo_nf_url_drive}" target="_blank" title="Baixar do Google Drive">☁️ Drive</a>'
            )

        # Junta os links com um separador
        return format_html(" | ".join(links))

    links_nfe.short_description = "Links NF-e"


@admin.register(SaldoEstoque)
class SaldoEstoqueAdmin(admin.ModelAdmin):
    list_display = ("item", "quantidade")
    search_fields = ("item__codigo", "item__descricao")


@admin.register(Edital)
class EditalAdmin(admin.ModelAdmin):
    list_display = ("numero", "tipo", "processo", "pregao")
    search_fields = ("numero", "processo", "pregao", "objeto")
    list_filter = ("tipo",)


@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ("razao_social", "cnpj", "cidade", "estado")
    search_fields = ("razao_social", "cnpj")
    list_filter = ("estado",)


@admin.register(ARPContrato)
class ARPContratoAdmin(admin.ModelAdmin):
    list_display = ("numero_arp", "edital", "fornecedor", "valor_total")
    search_fields = ("numero_arp", "fornecedor__razao_social")


@admin.register(ItemLicitado)
class ItemLicitadoAdmin(admin.ModelAdmin):
    list_display = (
        "codigo",
        "descricao",
        "edital",
        "fornecedor",
        "quantidade",
        "valor_unitario",
    )
    search_fields = ("codigo", "descricao")
    list_filter = ("edital", "fornecedor")


@admin.register(Clausula)
class ClausulaAdmin(admin.ModelAdmin):
    list_display = ("texto",)


@admin.register(Feriado)
class FeriadoAdmin(admin.ModelAdmin):
    list_display = ("descricao", "data")
    list_filter = ("data",)


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ("nome_empresa", "cnpj", "telefone", "email")
    search_fields = ("nome_empresa", "cnpj")


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("codigo_item", "descricao", "tipo_item", "edital_origem")
    search_fields = ("codigo_item", "descricao")
    list_filter = ("tipo_item",)


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("numero_pedido", "empresa", "data_pedido", "status")
    search_fields = ("numero_pedido", "empresa__nome_empresa")
    list_filter = ("status",)


@admin.register(ItemDoPedido)
class ItemDoPedidoAdmin(admin.ModelAdmin):
    list_display = (
        "pedido",
        "produto",
        "quantidade_solicitada",
        "quantidade_entregue",
        "status_entrega",
    )
    list_filter = ("status_entrega",)


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("username", "nome_completo", "email", "cargo", "setor")
    search_fields = ("username", "nome_completo", "email")
    list_filter = ("cargo", "setor")


@admin.register(Auditoria)
class AuditoriaAdmin(admin.ModelAdmin):
    list_display = ("tipo_acao", "usuario", "data_hora")
    search_fields = ("tipo_acao", "usuario__username")
    list_filter = ("data_hora",)
