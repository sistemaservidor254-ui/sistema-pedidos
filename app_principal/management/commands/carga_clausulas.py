from django.core.management.base import BaseCommand
from app_principal.models import Clausula

class Command(BaseCommand):
    help = 'Carrega cláusulas padrão no banco de dados'

    def handle(self, *args, **kwargs):
        clausulas = [
            "O cliente concorda com os termos de uso.",
            "O pagamento deve ser efetuado em até 5 dias úteis.",
            "A entrega será realizada conforme disponibilidade de estoque."
        ]
        for texto in clausulas:
            Clausula.objects.get_or_create(texto=texto)
        self.stdout.write(self.style.SUCCESS('Cláusulas carregadas com sucesso!'))