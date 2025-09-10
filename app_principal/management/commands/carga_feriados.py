from django.core.management.base import BaseCommand
from datetime import date
from app_principal.models import Feriado

class Command(BaseCommand):
    help = 'Carrega feriados fixos no banco de dados'

    def handle(self, *args, **kwargs):
        feriados = [
            ("Ano Novo", date(2025, 1, 1)),
            ("Dia do Trabalho", date(2025, 5, 1)),
            ("Natal", date(2025, 12, 25)),
        ]
        for nome, data_feriado in feriados:
            Feriado.objects.get_or_create(nome=nome, data=data_feriado)
        self.stdout.write(self.style.SUCCESS('Feriados carregados com sucesso!'))