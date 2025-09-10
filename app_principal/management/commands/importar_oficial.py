from django.core.management.base import BaseCommand
from app_principal.models import Empresa, Produto
from decimal import Decimal
import re

# Funções auxiliares
def clean_cnpj(cnpj):
    if not cnpj:
        return ''
    return re.sub(r'\D+', '', str(cnpj))

def parse_brl(value):
    if value is None or value == '':
        return None
    s = str(value).strip()
    s = s.replace('.', '').replace(',', '.')
    try:
        return Decimal(s)
    except:
        return None

class Command(BaseCommand):
    help = "Importa empresas e produtos oficiais a partir de dados extraídos dos PDFs"

    def handle(self, *args, **kwargs):
        # Aqui simulamos a leitura dos PDFs que você enviou.
        # No seu caso, vamos substituir pelas listas extraídas dos documentos.

        # -------------------------
        # Exemplo: Empresas (extraídas dos contratos)
        # -------------------------
        empresas = [
            {
                "nome_empresa": "FARMACIA CENTRAL LTDA",
                "cnpj": "12.345.678/0001-99",
                "telefone": "(14) 3333-0000",
                "email": "contato@farmaciacentral.com",
                "edital_vencedor": "000016/25"
            },
            {
                "nome_empresa": "HOSPITALAR SUPRIMENTOS EIRELI",
                "cnpj": "98.765.432/0001-11",
                "telefone": "(14) 3222-1111",
                "email": "vendas@hospitalarsuprimentos.com",
                "edital_vencedor": "000027/25"
            }
        ]

        for emp in empresas:
            obj, created = Empresa.objects.get_or_create(
                cnpj=clean_cnpj(emp["cnpj"]),
                defaults={
                    "nome_empresa": emp["nome_empresa"],
                    "telefone": emp["telefone"],
                    "email": emp["email"],
                    "edital_vencedor": emp["edital_vencedor"]
                }
            )
            if not created:
                obj.nome_empresa = emp["nome_empresa"]
                obj.telefone = emp["telefone"]
                obj.email = emp["email"]
                obj.edital_vencedor = emp["edital_vencedor"]
                obj.save()

        # -------------------------
        # Exemplo: Produtos (extraídos das listas de itens)
        # -------------------------
        produtos = [
            {
                "codigo_item": "001.001.001",
                "descricao": "DIPIRONA SÓDICA 500MG COMPRIMIDO",
                "tipo_item": "MEDICAMENTO",
                "edital_origem": "000016/25"
            },
            {
                "codigo_item": "002.002.002",
                "descricao": "SERINGA DESCARTÁVEL 5ML",
                "tipo_item": "ENFERMAGEM",
                "edital_origem": "000027/25"
            }
        ]

        for prod in produtos:
            Produto.objects.get_or_create(
                codigo_item=prod["codigo_item"],
                descricao=prod["descricao"],
                tipo_item=prod["tipo_item"],
                edital_origem=prod["edital_origem"]
            )

        self.stdout.write(self.style.SUCCESS("Empresas e produtos importados com sucesso!"))