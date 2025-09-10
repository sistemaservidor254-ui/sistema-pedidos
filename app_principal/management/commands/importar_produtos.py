from django.core.management.base import BaseCommand
import openpyxl
from app_principal.models import Produto

class Command(BaseCommand):
    help = 'Importa produtos a partir de uma planilha Excel'

    def add_arguments(self, parser):
        parser.add_argument('arquivo', type=str, help='Caminho para o arquivo Excel')

    def handle(self, *args, **kwargs):
        arquivo = kwargs['arquivo']
        wb = openpyxl.load_workbook(arquivo)
        sheet = wb.active

        for row in sheet.iter_rows(min_row=2, values_only=True):
            nome, preco, estoque = row
            Produto.objects.get_or_create(nome=nome, preco=preco, estoque=estoque)

        self.stdout.write(self.style.SUCCESS('Produtos importados com sucesso!'))