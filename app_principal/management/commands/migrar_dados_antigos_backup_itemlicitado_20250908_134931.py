import os
import sys
from decimal import Decimal
from django.core.management.base import BaseCommand

# 🔹 Ajuste para o Pylance e execução direta no VS Code
# Isso garante que a raiz do projeto esteja no sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from app_principal.models import Edital, Fornecedor, ItemLicitado


class Command(BaseCommand):
    help = "Migra os dados antigos dos editais 000016/25 (Medicamentos) e 000027/25 (Itens de Enfermagem)"

    def handle(self, *args, **options):
        # Garantir que o edital de itens de enfermagem existe
        tender_enf, _ = Edital.objects.get_or_create(
            numero="000027/25", defaults={"tipo": "ENFERMAGEM"}
        )

        # Garantir que o edital de medicamentos existe
        tender_med, _ = Edital.objects.get_or_create(
            numero="000016/25", defaults={"tipo": "MEDICAMENTOS"}
        )

        # Empresa LUMAR
        lumar, _ = Fornecedor.objects.get_or_create(
            cnpj="49.228.695/0001-52",
            defaults={
                "razao_social": "LUMAR COMÉRCIO DE PRODUTOS FARMACÊUTICOS LTDA",
                "email": "licitacoes@lumarfranca.com.br",
                "telefone": "(16) 3721-1102",
                "endereco": "Av. Wilson Bego, 745, Bairro Distrito Industrial Antônio Della Torres, Franca-SP, CEP 14406-091",
            },
        )

        # Itens da LUMAR – Parte 1
        ItemLicitado.objects.update_or_create(
    edital=tender_enf,
    codigo="014.001.004",
    defaults={
        "fornecedor": lumar,
"descricao": "AGULHA 13/4.5 CX 100",
                "unidade": "CX",
                "quantidade": 300,
                "valor_unitario": Decimal("6.83"),
                "valor_total": Decimal("2049.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="014.001.005",
            defaults={
                "descricao": "AGULHA 25/7 CX 100",
                "unidade": "CX",
                "quantidade": 200,
                "valor_unitario": Decimal("6.83"),
                "valor_total": Decimal("1366.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="014.001.007",
            defaults={
                "descricao": "AGULHA 30/7 100 CX",
                "unidade": "CX",
                "quantidade": 500,
                "valor_unitario": Decimal("6.83"),
                "valor_total": Decimal("3415.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="014.001.008",
            defaults={
                "descricao": "AGULHA 30/8 100 CX",
                "unidade": "CX",
                "quantidade": 500,
                "valor_unitario": Decimal("6.83"),
                "valor_total": Decimal("3415.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="014.001.009",
            defaults={
                "descricao": "AGULHA 40/12 CX 100",
                "unidade": "CX",
                "quantidade": 500,
                "valor_unitario": Decimal("7.799"),
                "valor_total": Decimal("3899.50"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="014.001.010",
            defaults={
                "descricao": "ALCOOL 70% 1L",
                "unidade": "LT",
                "quantidade": 1000,
                "valor_unitario": Decimal("5.40"),
                "valor_total": Decimal("5400.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="014.001.076",
            defaults={
                "descricao": "ALGODÃO 500 G",
                "unidade": "ROLO",
                "quantidade": 500,
                "valor_unitario": Decimal("13.40"),
                "valor_total": Decimal("6700.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="014.001.011",
            defaults={
                "descricao": "ALMOTOLIA COR ÂMBAR 125 ML",
                "unidade": "UNI",
                "quantidade": 100,
                "valor_unitario": Decimal("2.50"),
                "valor_total": Decimal("250.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="014.001.012",
            defaults={
                "descricao": "ALMOTOLIA TRANSPARENTE 125 ML",
                "unidade": "UNI",
                "quantidade": 100,
                "valor_unitario": Decimal("2.50"),
                "valor_total": Decimal("250.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="014.000.502",
            defaults={
                "descricao": "APARELHO DE PRESSÃO P/OBESO",
                "unidade": "UN",
                "quantidade": 10,
                "valor_unitario": Decimal("77.98"),
                "valor_total": Decimal("779.80"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="013.000.729",
            defaults={
                "descricao": "BORRIFADOR 500 ML",
                "unidade": "UNI",
                "quantidade": 1000,
                "valor_unitario": Decimal("6.50"),
                "valor_total": Decimal("6500.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="023.001.002",
            defaults={
                "descricao": "CABO DE BISTURI Nº 4",
                "unidade": "UNI",
                "quantidade": 10,
                "valor_unitario": Decimal("7.70"),
                "valor_total": Decimal("77.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="023.001.004",
            defaults={
                "descricao": "CATÉTER NASAL TIPO ÓCULOS (ADULTO)",
                "unidade": "UNI",
                "quantidade": 1000,
                "valor_unitario": Decimal("0.87"),
                "valor_total": Decimal("870.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="023.001.032",
            defaults={
                "descricao": "CATÉTER PERIFÉRICO I.V Nº 18",
                "unidade": "UNI",
                "quantidade": 100,
                "valor_unitario": Decimal("0.79"),
                "valor_total": Decimal("79.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="014.001.021",
            defaults={
                "descricao": "CATETER PERIFÉRICO I.V 24",
                "unidade": "UNI",
                "quantidade": 3000,
                "valor_unitario": Decimal("0.94"),
                "valor_total": Decimal("2820.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="014.001.023",
            defaults={
                "descricao": "COLETOR DE URINA E SECREÇÃO TIPO SACO- 2 LITROS C/BARBANTE",
                "unidade": "UNI",
                "quantidade": 5000,
                "valor_unitario": Decimal("0.33"),
                "valor_total": Decimal("1650.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="014.001.086",
            defaults={
                "descricao": "COMPRESSA DE GAZE 7.5 CM/7.5 CM FECHADA 13 FIOS (ESTÉRIL) PCT C/ 10 UNI",
                "unidade": "PCT",
                "quantidade": 100000,
                "valor_unitario": Decimal("0.55"),
                "valor_total": Decimal("55000.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="023.001.036",
            defaults={
                "descricao": "CONJUNTO DE NEBULIZAÇÃO/OXIGÊNIO/ADULTO",
                "unidade": "UNI",
                "quantidade": 100,
                "valor_unitario": Decimal("5.75"),
                "valor_total": Decimal("575.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="023.001.037",
            defaults={
                "descricao": "CONJUNTO DE NEBULIZAÇÃO/OXIGÊNIO/INFANTIL",
                "unidade": "UNI",
                "quantidade": 70,
                "valor_unitario": Decimal("5.75"),
                "valor_total": Decimal("402.50"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="014.001.174",
            defaults={
                "descricao": "ELETRODO P/ECG",
                "unidade": "UN",
                "quantidade": 200,
                "valor_unitario": Decimal("0.22"),
                "valor_total": Decimal("44.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="014.001.029",
            defaults={
                "descricao": "ESCOVAS CERVICAL GINECOLÓGICA PACOTES COM 100 UNIDADES",
                "unidade": "PCT",
                "quantidade": 30,
                "valor_unitario": Decimal("24.00"),
                "valor_total": Decimal("720.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="014.000.521",
            defaults={
                "descricao": "ESPARADRAPO 10 CM X 4,5 M",
                "unidade": "UN",
                "quantidade": 1000,
                "valor_unitario": Decimal("8.80"),
                "valor_total": Decimal("8800.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="014.000.055",
            defaults={
                "descricao": "FIO DE NYLON 4.0",
                "unidade": "CX",
                "quantidade": 10,
                "valor_unitario": Decimal("27.99"),
                "valor_total": Decimal("279.90"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="014.001.037",
            defaults={
                "descricao": "FIO DE NYLON 2.0",
                "unidade": "CX",
                "quantidade": 50,
                "valor_unitario": Decimal("28.60"),
                "valor_total": Decimal("1430.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="014.001.038",
            defaults={
                "descricao": "FIO DE NYLON 3.0",
                "unidade": "CX",
                "quantidade": 50,
                "valor_unitario": Decimal("28.60"),
                "valor_total": Decimal("1430.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="014.000.527",
            defaults={
                "descricao": "GARROTE P/ COLETAS DE SANGUE",
                "unidade": "UN",
                "quantidade": 100,
                "valor_unitario": Decimal("6.42"),
                "valor_total": Decimal("642.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="023.001.007",
            defaults={
                "descricao": "GEL P/ECG FRASCO 100 ML",
                "unidade": "FRC",
                "quantidade": 50,
                "valor_unitario": Decimal("1.54"),
                "valor_total": Decimal("77.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="014.000.231",
            defaults={
                "descricao": "GORRO",
                "unidade": "UNI",
                "quantidade": 10000,
                "valor_unitario": Decimal("0.06"),
                "valor_total": Decimal("600.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="014.001.046",
            defaults={
                "descricao": "LÂMINA DE BISTURI Nº11",
                "unidade": "CX",
                "quantidade": 20,
                "valor_unitario": Decimal("23.40"),
                "valor_total": Decimal("468.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="014.001.047",
            defaults={
                "descricao": "LÂMINA DE BISTURI Nº21 CAIXA COM 100",
                "unidade": "CX",
                "quantidade": 20,
                "valor_unitario": Decimal("23.40"),
                "valor_total": Decimal("468.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="013.013.100",
            defaults={
                "descricao": "LANTERNA CLÍNICA",
                "unidade": "UN",
                "quantidade": 10,
                "valor_unitario": Decimal("16.90"),
                "valor_total": Decimal("169.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="014.001.050",
            defaults={
                "descricao": "LUVA CIRÚRGICA 7.5",
                "unidade": "PAR",
                "quantidade": 2000,
                "valor_unitario": Decimal("1.36"),
                "valor_total": Decimal("2720.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="014.001.051",
            defaults={
                "descricao": "LUVAS DE PROCEDIMENTOS (G) CAIXAS COM 100",
                "unidade": "CX",
                "quantidade": 300,
                "valor_unitario": Decimal("22.90"),
                "valor_total": Decimal("6870.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="014.001.052",
            defaults={
                "descricao": "LUVAS DE PROCEDIMENTOS (M) CAIXA COM 100",
                "unidade": "CX",
                "quantidade": 600,
                "valor_unitario": Decimal("22.90"),
                "valor_total": Decimal("13740.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="014.001.053",
            defaults={
                "descricao": "LUVAS DE PROCEDIMENTOS (P) CAIXA COM 100",
                "unidade": "CX",
                "quantidade": 600,
                "valor_unitario": Decimal("22.90"),
                "valor_total": Decimal("13740.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="014.000.086",
            defaults={
                "descricao": "MÁSCARA N 95",
                "unidade": "UN",
                "quantidade": 1000,
                "valor_unitario": Decimal("0.65"),
                "valor_total": Decimal("650.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="014.002.073",
            defaults={
                "descricao": "ÓLEO DE GIRASSOL 100ML",
                "unidade": "FR",
                "quantidade": 1000,
                "valor_unitario": Decimal("2.85"),
                "valor_total": Decimal("2850.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="014.001.071",
            defaults={
                "descricao": "SCALPS N 23",
                "unidade": "UN",
                "quantidade": 15000,
                "valor_unitario": Decimal("0,22"),
                "valor_total": Decimal("3300.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="023.001.015",
            defaults={
                "descricao": "SERINGAS DESC. 1 ML C/AG ULTRAFINE",
                "unidade": "UNI",
                "quantidade": 15000,
                "valor_unitario": Decimal("0.20"),
                "valor_total": Decimal("3000.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="014.001.058",
            defaults={
                "descricao": "SERINGAS DESC. 3 ML S/AG",
                "unidade": "UNI",
                "quantidade": 10000,
                "valor_unitario": Decimal("0.11"),
                "valor_total": Decimal("1100.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="014.001.059",
            defaults={
                "descricao": "SERINGAS DESC. 5 ML S/AG",
                "unidade": "UNI",
                "quantidade": 15000,
                "valor_unitario": Decimal("0.14"),
                "valor_total": Decimal("2100.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="014.001.060",
            defaults={
                "descricao": "SERINGAS DESC. 10 ML S/AG",
                "unidade": "UNI",
                "quantidade": 15000,
                "valor_unitario": Decimal("0.21"),
                "valor_total": Decimal("3150.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="014.001.062",
            defaults={
                "descricao": "SOLUÇÃO DE HIPOCLORITO DE SÓDIO 1% P/P",
                "unidade": "UNI",
                "quantidade": 40,
                "valor_unitario": Decimal("10.98"),
                "valor_total": Decimal("439.20"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="014.001.063",
            defaults={
                "descricao": "SONDA DE FAWLEY Nº 14",
                "unidade": "UNI",
                "quantidade": 20,
                "valor_unitario": Decimal("2.50"),
                "valor_total": Decimal("50.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="014.001.064",
            defaults={
                "descricao": "SONDA DE FAWLEY Nº 16",
                "unidade": "UNI",
                "quantidade": 80,
                "valor_unitario": Decimal("2.45"),
                "valor_total": Decimal("196.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="014.001.065",
            defaults={
                "descricao": "SONDA DE FAWLEY Nº 18",
                "unidade": "UNI",
                "quantidade": 30,
                "valor_unitario": Decimal("2.36"),
                "valor_total": Decimal("70.80"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="014.001.066",
            defaults={
                "descricao": "SONDA DE FAWLEY Nº 20",
                "unidade": "UNI",
                "quantidade": 30,
                "valor_unitario": Decimal("2.36"),
                "valor_total": Decimal("70.80"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="014.001.091",
            defaults={
                "descricao": "SONDA DE FAWLEY Nº 22",
                "unidade": "UNI",
                "quantidade": 20,
                "valor_unitario": Decimal("2.50"),
                "valor_total": Decimal("50.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="014.000.551",
            defaults={
                "descricao": "TESOURA DE ÍRIS 12 CM",
                "unidade": "UN",
                "quantidade": 2,
                "valor_unitario": Decimal("18.00"),
                "valor_total": Decimal("36.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lumar,
            codigo="014.000.555",
            defaults={
                "descricao": "TESTE DE GRAVIDEZ EM TIRA C/FRASCO COLETOR",
                "unidade": "UN",
                "quantidade": 1000,
                "valor_unitario": Decimal("1.81"),
                "valor_total": Decimal("1810.00"),
            },
        )

        # Garantir que o edital existe
        tender_enf, _ = Edital.objects.get_or_create(
            numero="000027/25", defaults={"tipo": "ENFERMAGEM"
    }
)

        # Empresa
        cirurgica_uniao, _ = Fornecedor.objects.get_or_create(
            cnpj="04.063.331/0001-21",
            defaults={
                "razao_social": "CIRÚRGICA UNIÃO LTDA",
                "email": "uniao@cirurgicauniao.com.br",
                "telefone": "(19) 3526-1900",
                "endereco": "Rua 25, N 1908/1928, Bairro Jardim São Paulo, Rio Claro-SP, CEP 13503-010",
            },
        )

        # Itens da CIRÚRGICA UNIÃO – Parte 1
        # Itens — Parte 1

        ItemLicitado.objects.update_or_create(
    edital=tender_enf,
    codigo="014.000.034",
    defaults={
        "fornecedor": cirurgica_uniao,
"descricao": "ABAIXADOR DE LINGUA",
                "unidade": "PCT",
                "quantidade": 100,
                "valor_unitario": Decimal("4.999"),
                "valor_total": Decimal("499.90"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=cirurgica_uniao,
            codigo="006.001.030",
            defaults={
                "descricao": "ÁGUA OXIGENADA 10 VOL.",
                "unidade": "LT",
                "quantidade": 50,
                "valor_unitario": Decimal("4.50"),
                "valor_total": Decimal("225.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=cirurgica_uniao,
            codigo="014.001.006",
            defaults={
                "descricao": "AGULHA 25/8 CX 100",
                "unidade": "CX",
                "quantidade": 500,
                "valor_unitario": Decimal("7.39"),
                "valor_total": Decimal("3695.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=cirurgica_uniao,
            codigo="023.001.025",
            defaults={
                "descricao": "AVENTAL GRAMATURA 40 MANGA LONGA",
                "unidade": "UNI",
                "quantidade": 10000,
                "valor_unitario": Decimal("2.15"),
                "valor_total": Decimal("21500.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=cirurgica_uniao,
            codigo="014.001.019",
            defaults={
                "descricao": "BANDAGEM ANTISSÉPTICA CAIXA COM 500 UNIDADES",
                "unidade": "UNI",
                "quantidade": 100,
                "valor_unitario": Decimal("10.30"),
                "valor_total": Decimal("1030.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=cirurgica_uniao,
            codigo="014.002.037",
            defaults={
                "descricao": "BANDEJA INOX LISA 22 X 17 X 1,5 CM",
                "unidade": "UNI",
                "quantidade": 20,
                "valor_unitario": Decimal("33.50"),
                "valor_total": Decimal("670.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=cirurgica_uniao,
            codigo="014.000.505",
            defaults={
                "descricao": "CAMISOLAS DE PACIENTES P/EXAMES",
                "unidade": "UN",
                "quantidade": 500,
                "valor_unitario": Decimal("1.49"),
                "valor_total": Decimal("745.00"),
            },
        )

        # Itens — Parte 2
        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=cirurgica_uniao,
            codigo="014.001.162",
            defaults={
                "descricao": "CAMPO CIRÚRGICO 1 MT X 1MT FENESTRADO SM",
                "unidade": "UN",
                "quantidade": 500,
                "valor_unitario": Decimal("3.82"),
                "valor_total": Decimal("1910.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=cirurgica_uniao,
            codigo="023.001.033",
            defaults={
                "descricao": "CATÉTER PERIFÉRICO I.V Nº 20",
                "unidade": "UNI",
                "quantidade": 3000,
                "valor_unitario": Decimal("0.859"),
                "valor_total": Decimal("2577.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=cirurgica_uniao,
            codigo="023.001.034",
            defaults={
                "descricao": "CATÉTER PERIFÉRICO I.V Nº 22",
                "unidade": "UNI",
                "quantidade": 3000,
                "valor_unitario": Decimal("0.859"),
                "valor_total": Decimal("2577.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=cirurgica_uniao,
            codigo="014.000.506",
            defaults={
                "descricao": "CINTO DE SEGURANÇA P/AMBULÂNCIA",
                "unidade": "UN",
                "quantidade": 20,
                "valor_unitario": Decimal("355.76"),
                "valor_total": Decimal("7115.20"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=cirurgica_uniao,
            codigo="014.001.022",
            defaults={
                "descricao": "COLETOR DE MATERIAL PERFURO CORTANTE 13 L",
                "unidade": "UNI",
                "quantidade": 500,
                "valor_unitario": Decimal("4.93"),
                "valor_total": Decimal("2465.00"),
            },
        )

        # Itens — Parte 3
        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=cirurgica_uniao,
            codigo="023.001.035",
            defaults={
                "descricao": "COMADRE DE INOX 40X30 CM",
                "unidade": "UNI",
                "quantidade": 5,
                "valor_unitario": Decimal("192.10"),
                "valor_total": Decimal("960.50"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=cirurgica_uniao,
            codigo="014.000.512",
            defaults={
                "descricao": "COMPRESSA P/CURATIVOS CIRÚRGICO ESTÉRIL",
                "unidade": "UN",
                "quantidade": 1000,
                "valor_unitario": Decimal("0.90"),
                "valor_total": Decimal("900.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=cirurgica_uniao,
            codigo="014.002.039",
            defaults={
                "descricao": "CUBA RIM INOX 26 X 12 X 6 CM",
                "unidade": "UN",
                "quantidade": 10,
                "valor_unitario": Decimal("37.00"),
                "valor_total": Decimal("370.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=cirurgica_uniao,
            codigo="014.001.032",
            defaults={
                "descricao": "ESPÉCULO VAGINAL DESCARTÁVEL (G)",
                "unidade": "UNI",
                "quantidade": 1000,
                "valor_unitario": Decimal("1.40"),
                "valor_total": Decimal("1400.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=cirurgica_uniao,
            codigo="014.001.033",
            defaults={
                "descricao": "ESPÉCULOS VAGINAL DESCARTÁVEL (M)",
                "unidade": "UNI",
                "quantidade": 1000,
                "valor_unitario": Decimal("1.19"),
                "valor_total": Decimal("1190.00"),
            },
        )

        # Itens — Parte 4
        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=cirurgica_uniao,
            codigo="014.001.034",
            defaults={
                "descricao": "ESPÉCULOS VAGINAL DESCARTÁVEL (P)",
                "unidade": "UNI",
                "quantidade": 1000,
                "valor_unitario": Decimal("1.13"),
                "valor_total": Decimal("1130.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=cirurgica_uniao,
            codigo="014.000.523",
            defaults={
                "descricao": "FITA ADESIVA 16MM X 50M",
                "unidade": "UN",
                "quantidade": 500,
                "valor_unitario": Decimal("3.20"),
                "valor_total": Decimal("1600.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=cirurgica_uniao,
            codigo="014.000.524",
            defaults={
                "descricao": "FITA DE AUTOCLAVE 19MM X 30M",
                "unidade": "RL",
                "quantidade": 200,
                "valor_unitario": Decimal("3.72"),
                "valor_total": Decimal("744.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=cirurgica_uniao,
            codigo="014.000.525",
            defaults={
                "descricao": "FITA DE MICROPORE 25MM X 4.5M",
                "unidade": "RL",
                "quantidade": 5000,
                "valor_unitario": Decimal("1.969"),
                "valor_total": Decimal("9845.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=cirurgica_uniao,
            codigo="014.000.526",
            defaults={
                "descricao": "FITA DE MICROPORE 50MM X 10M",
                "unidade": "UN",
                "quantidade": 200,
                "valor_unitario": Decimal("4.30"),
                "valor_total": Decimal("860.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=cirurgica_uniao,
            codigo="023.001.040",
            defaults={
                "descricao": "FITA P/CERTIFICAÇÃO DE GLICEMIA CAPILAR C/ 50 UNI",
                "unidade": "UN",
                "quantidade": 150000,
                "valor_unitario": Decimal("0.47"),
                "valor_total": Decimal("70500.00"),
            },
        )

        # Itens — Parte 5
        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=cirurgica_uniao,
            codigo="014.001.043",
            defaults={
                "descricao": "FRASCO P/ALIMENTAÇÃO 300ML",
                "unidade": "UNI",
                "quantidade": 5000,
                "valor_unitario": Decimal("0.729"),
                "valor_total": Decimal("3645.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=cirurgica_uniao,
            codigo="023.001.006",
            defaults={
                "descricao": "GEL P/DETECTOR FETAL FRASCO 100ML",
                "unidade": "FRC",
                "quantidade": 100,
                "valor_unitario": Decimal("1.68"),
                "valor_total": Decimal("168.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=cirurgica_uniao,
            codigo="014.001.048",
            defaults={
                "descricao": "LANCETAS C/ DISPOSITIVO",
                "unidade": "UNI",
                "quantidade": 30000,
                "valor_unitario": Decimal("0.11"),
                "valor_total": Decimal("3300.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=cirurgica_uniao,
            codigo="013.007.523",
            defaults={
                "descricao": "LIXEIRA DE PEDAL 100 LITROS",
                "unidade": "UN",
                "quantidade": 50,
                "valor_unitario": Decimal("220.90"),
                "valor_total": Decimal("11045.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=cirurgica_uniao,
            codigo="003.000.228",
            defaults={
                "descricao": "LIXEIRA DE PEDAL 30 LITROS",
                "unidade": "UN",
                "quantidade": 50,
                "valor_unitario": Decimal("67.76"),
                "valor_total": Decimal("3388.00"),
            },
        )

        # Itens — Parte 6
        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=cirurgica_uniao,
            codigo="023.001.008",
            defaults={
                "descricao": "MÁSCARA CIRÚRGICA TRIPLA C/ELÁSTICO CAIXA",
                "unidade": "CX",
                "quantidade": 50000,
                "valor_unitario": Decimal("0.092"),
                "valor_total": Decimal("4600.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=cirurgica_uniao,
            codigo="014.000.532",
            defaults={
                "descricao": "MÁSCARA DE ALTA CONCENTRAÇÃO OXIGÊNIO",
                "unidade": "UN",
                "quantidade": 1000,
                "valor_unitario": Decimal("5.88"),
                "valor_total": Decimal("5880.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=cirurgica_uniao,
            codigo="014.000.534",
            defaults={
                "descricao": "MÁSCARA FACIAL PARA NEBULIZAÇÃO CONTÍNUA",
                "unidade": "UN",
                "quantidade": 30,
                "valor_unitario": Decimal("6.38"),
                "valor_total": Decimal("191.40"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=cirurgica_uniao,
            codigo="014.001.054",
            defaults={
                "descricao": "PAPEL CREPADO 40CM/40 CAIXA COM 500",
                "unidade": "CX",
                "quantidade": 2,
                "valor_unitario": Decimal("128.50"),
                "valor_total": Decimal("257.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=cirurgica_uniao,
            codigo="014.001.090",
            defaults={
                "descricao": "PAPEL GRAU CIRÚRGICO 25/100",
                "unidade": "BO",
                "quantidade": 10,
                "valor_unitario": Decimal("119.04"),
                "valor_total": Decimal("1190.40"),
            },
        )

        # Itens — Parte 7
        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=cirurgica_uniao,
            codigo="014.000.359",
            defaults={
                "descricao": "PINÇA CHERON 24 CM EM AÇO INOX.",
                "unidade": "UNI",
                "quantidade": 4,
                "valor_unitario": Decimal("48.00"),
                "valor_total": Decimal("192.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=cirurgica_uniao,
            codigo="023.001.013",
            defaults={
                "descricao": "PINÇA KELLY RETA",
                "unidade": "UNI",
                "quantidade": 10,
                "valor_unitario": Decimal("29.70"),
                "valor_total": Decimal("297.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=cirurgica_uniao,
            codigo="014.000.087",
            defaults={
                "descricao": "POLIFIX ADULTO",
                "unidade": "UN",
                "quantidade": 100,
                "valor_unitario": Decimal("0.63"),
                "valor_total": Decimal("63.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=cirurgica_uniao,
            codigo="014.001.061",
            defaults={
                "descricao": "SERINGAS DESC. 20 ML S/AG",
                "unidade": "UNI",
                "quantidade": 15000,
                "valor_unitario": Decimal("0.33"),
                "valor_total": Decimal("4950.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=cirurgica_uniao,
            codigo="014.002.019",
            defaults={
                "descricao": "SONDA DE ASPIRAÇÃO TRAQUEAL Nº 12",
                "unidade": "UN",
                "quantidade": 10000,
                "valor_unitario": Decimal("0.52"),
                "valor_total": Decimal("5200.00"),
            },
        )

        # Itens — Parte 8 (final)
        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=cirurgica_uniao,
            codigo="014.001.068",
            defaults={
                "descricao": "SONDA URETRAL Nº 12",
                "unidade": "UNI",
                "quantidade": 15000,
                "valor_unitario": Decimal("0.50"),
                "valor_total": Decimal("7500.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=cirurgica_uniao,
            codigo="014.000.547",
            defaults={
                "descricao": "SUPORTE P/ MATERIAIS PERFURO CORTANTE P/1",
                "unidade": "UN",
                "quantidade": 10,
                "valor_unitario": Decimal("21.00"),
                "valor_total": Decimal("210.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=cirurgica_uniao,
            codigo="006.000.295",
            defaults={
                "descricao": "TERMOMETRO DIGITAL",
                "unidade": "UN",
                "quantidade": 100,
                "valor_unitario": Decimal("9.999"),
                "valor_total": Decimal("999.90"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=cirurgica_uniao,
            codigo="014.002.052",
            defaults={
                "descricao": "VASELINA LIQUIDA",
                "unidade": "L",
                "quantidade": 10,
                "valor_unitario": Decimal("29.80"),
                "valor_total": Decimal("298.00"),
            },
        )

        # Garantir que o edital existe e buscar/criar a empresa
        tender_enf, _ = Edital.objects.get_or_create(
            numero="000027/25", defaults={"tipo": "ENFERMAGEM"
    }
)

        placido, _ = Fornecedor.objects.get_or_create(
            cnpj="25.123.729/0001-86",
            defaults={
                "razao_social": "PLACIDO COM. DE MAT. CIR. E HOSP. EIRELI-ME",
                "email": "vendas.placido@hotmail.com",
                "telefone": "(14) 3413-9949",
                "endereco": "Rua Av. Tiradentes, N 1321, Bairro Fragata, Marília-SP, CEP 17519-000",
            },
        )

        # Itens da PLACIDO – Parte 1
        ItemLicitado.objects.update_or_create(
    edital=tender_enf,
    codigo="014.000.500",
    defaults={
        "fornecedor": placido,
"descricao": "ABAIXADOR DE LÍNGUA COLORIDO AROMADO LIS",
                "unidade": "UN",
                "quantidade": 100,
                "valor_unitario": Decimal("37.998"),
                "valor_total": Decimal("3799.80"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=placido,
            codigo="014.001.015",
            defaults={
                "descricao": "ATADURA DE CREPE 10 CM 13 FIOS PACOTES COM",
                "unidade": "PCT",
                "quantidade": 1000,
                "valor_unitario": Decimal("4.80"),
                "valor_total": Decimal("4800.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=placido,
            codigo="014.001.016",
            defaults={
                "descricao": "ATADURA DE CREPE 15 CM 13 FIOS PACOTES COM",
                "unidade": "PCT",
                "quantidade": 1000,
                "valor_unitario": Decimal("7.10"),
                "valor_total": Decimal("7100.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=placido,
            codigo="014.001.017",
            defaults={
                "descricao": "ATADURA DE CREPE 20 CM 13 FIOS PACOTES COM",
                "unidade": "PCT",
                "quantidade": 1000,
                "valor_unitario": Decimal("9.689"),
                "valor_total": Decimal("9689.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=placido,
            codigo="014.001.018",
            defaults={
                "descricao": "ATADURA DE CREPE 6 CM 13 FIOS PACOTES COM",
                "unidade": "PCT",
                "quantidade": 1000,
                "valor_unitario": Decimal("2.98"),
                "valor_total": Decimal("2980.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=placido,
            codigo="014.000.511",
            defaults={
                "descricao": "COLETOR DE URINA INFANTIL UNISSEX ESTÉRIL 100 ML",
                "unidade": "UN",
                "quantidade": 3000,
                "valor_unitario": Decimal("0.35"),
                "valor_total": Decimal("1050.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=placido,
            codigo="023.001.038",
            defaults={
                "descricao": "ESCADA 2 DEGRAUS ANTIDERRAPANTE",
                "unidade": "UN",
                "quantidade": 12,
                "valor_unitario": Decimal("121.999"),
                "valor_total": Decimal("1463.99"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=placido,
            codigo="014.002.042",
            defaults={
                "descricao": "FIO GUIA P/ ENTUBAÇÃO ADULTO",
                "unidade": "UN",
                "quantidade": 5,
                "valor_unitario": Decimal("11.00"),
                "valor_total": Decimal("55.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=placido,
            codigo="014.000.078",
            defaults={
                "descricao": "LENÇOL DESCARTÁVEL PARA MACA",
                "unidade": "UN",
                "quantidade": 5000,
                "valor_unitario": Decimal("0.88"),
                "valor_total": Decimal("4400.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=placido,
            codigo="014.000.533",
            defaults={
                "descricao": "MANGUEIRA DE O2",
                "unidade": "UN",
                "quantidade": 100,
                "valor_unitario": Decimal("4.50"),
                "valor_total": Decimal("450.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=placido,
            codigo="014.005.088",
            defaults={
                "descricao": "PAPEL P/ECG 216 MM X 30MT",
                "unidade": "UN",
                "quantidade": 500,
                "valor_unitario": Decimal("22.32"),
                "valor_total": Decimal("11160.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=placido,
            codigo="014.001.055",
            defaults={
                "descricao": "PAPEL P/ECG 58/30",
                "unidade": "RL",
                "quantidade": 500,
                "valor_unitario": Decimal("7.35"),
                "valor_total": Decimal("3675.00"),
            },
        )

        # Garantir que o edital existe e buscar/criar a empresa
        tender_enf, _ = Edital.objects.get_or_create(
            numero="000027/25", defaults={"tipo": "ENFERMAGEM"
    }
)

        rosicler, _ = Fornecedor.objects.get_or_create(
            cnpj="57.365.116/0001-41",
            defaults={
                "razao_social": "ROSICLER CIRÚRGICA LTDA",
                "email": "vendas@rosiclercirurgica.com.br, licitacao@rosiclercirurgica.com.br",
                "telefone": "(19) 3023-3480, (19) 3534-5162",
                "endereco": "Avenida 12, Nº 2606, Bairro Jardim São Paulo, Rio Claro-SP, CEP 13503-019",
            },
        )

        # Itens da ROSICLER – Parte 1
        ItemLicitado.objects.update_or_create(
    edital=tender_enf,
    codigo="014.001.077",
    defaults={
        "fornecedor": rosicler,
"descricao": "APARELHO DE PRESSÃO (INFANTIL) COMPLETO",
                "unidade": "UN",
                "quantidade": 10,
                "valor_unitario": Decimal("67.40"),
                "valor_total": Decimal("674.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=rosicler,
            codigo="014.001.014",
            defaults={
                "descricao": "APARELHO DE PRESSÃO (ADULTO) COMPLETO",
                "unidade": "UN",
                "quantidade": 100,
                "valor_unitario": Decimal("67.40"),
                "valor_total": Decimal("6740.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=rosicler,
            codigo="023.001.003",
            defaults={
                "descricao": "CABO DE BISTURI Nº 5",
                "unidade": "UN",
                "quantidade": 10,
                "valor_unitario": Decimal("11.00"),
                "valor_total": Decimal("110.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=rosicler,
            codigo="014.000.517",
            defaults={
                "descricao": "CINTO DE SEGURANÇA P/MACA DE AMBULÂNCIA",
                "unidade": "UN",
                "quantidade": 20,
                "valor_unitario": Decimal("21.50"),
                "valor_total": Decimal("430.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=rosicler,
            codigo="014.000.200",
            defaults={
                "descricao": "COLAR CERVICAL FIBRA CIRÚRGICA (P)",
                "unidade": "UN",
                "quantidade": 10,
                "valor_unitario": Decimal("10.95"),
                "valor_total": Decimal("109.50"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=rosicler,
            codigo="014.000.395",
            defaults={
                "descricao": "COLAR CERVICAL FIBRA CIRÚRGICA (G)",
                "unidade": "UN",
                "quantidade": 10,
                "valor_unitario": Decimal("10.95"),
                "valor_total": Decimal("109.50"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=rosicler,
            codigo="014.000.509",
            defaults={
                "descricao": "COLAR CERVICAL FIBRA CIRÚRGICA (M)",
                "unidade": "UN",
                "quantidade": 10,
                "valor_unitario": Decimal("10.95"),
                "valor_total": Decimal("109.50"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=rosicler,
            codigo="014.000.510",
            defaults={
                "descricao": "COLAR CERVICAL P/RESGATE (M)",
                "unidade": "UN",
                "quantidade": 10,
                "valor_unitario": Decimal("10.95"),
                "valor_total": Decimal("109.50"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=rosicler,
            codigo="014.000.518",
            defaults={
                "descricao": "DEGERMANTE PVPI",
                "unidade": "UN",
                "quantidade": 50,
                "valor_unitario": Decimal("44.80"),
                "valor_total": Decimal("2240.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=rosicler,
            codigo="014.000.425",
            defaults={
                "descricao": "DETERGENTE ENZIMÁTICO GALÃO DE 5 LITROS",
                "unidade": "UN",
                "quantidade": 20,
                "valor_unitario": Decimal("83.90"),
                "valor_total": Decimal("1678.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=rosicler,
            codigo="014.000.035",
            defaults={
                "descricao": "ÉTER",
                "unidade": "LT",
                "quantidade": 100,
                "valor_unitario": Decimal("38.70"),
                "valor_total": Decimal("3870.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=rosicler,
            codigo="014.000.522",
            defaults={
                "descricao": "FIO GUIA P/ENTUBAÇÃO INFANTIL",
                "unidade": "UN",
                "quantidade": 5,
                "valor_unitario": Decimal("12.00"),
                "valor_total": Decimal("60.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=rosicler,
            codigo="014.000.536",
            defaults={
                "descricao": "OTOSCÓPIO INFANTIL",
                "unidade": "UN",
                "quantidade": 5,
                "valor_unitario": Decimal("196.90"),
                "valor_total": Decimal("984.50"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=rosicler,
            codigo="014.000.537",
            defaults={
                "descricao": "OTOSCÓPIO ADULTO",
                "unidade": "UN",
                "quantidade": 10,
                "valor_unitario": Decimal("196.90"),
                "valor_total": Decimal("1969.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=rosicler,
            codigo="014.000.538",
            defaults={
                "descricao": "PAPAGAIO INOX 1000 ML",
                "unidade": "UN",
                "quantidade": 5,
                "valor_unitario": Decimal("111.90"),
                "valor_total": Decimal("559.50"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=rosicler,
            codigo="023.001.011",
            defaults={
                "descricao": "PINÇA ANATÔMICA DENTE DE RATO",
                "unidade": "UN",
                "quantidade": 10,
                "valor_unitario": Decimal("10.50"),
                "valor_total": Decimal("105.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=rosicler,
            codigo="023.001.012",
            defaults={
                "descricao": "PINÇA KELLY CURVA",
                "unidade": "UN",
                "quantidade": 10,
                "valor_unitario": Decimal("29.80"),
                "valor_total": Decimal("298.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=rosicler,
            codigo="014.000.552",
            defaults={
                "descricao": "TESOURA DE MAYO 16 CM PONTA FINA",
                "unidade": "UN",
                "quantidade": 4,
                "valor_unitario": Decimal("24.85"),
                "valor_total": Decimal("99.40"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=rosicler,
            codigo="014.000.553",
            defaults={
                "descricao": "TESOURA DE MAYO 16 CM PONTA ROMBA",
                "unidade": "UN",
                "quantidade": 2,
                "valor_unitario": Decimal("24.85"),
                "valor_total": Decimal("49.70"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=rosicler,
            codigo="023.001.019",
            defaults={
                "descricao": "TESOURA DE MAYO Nº 12",
                "unidade": "UN",
                "quantidade": 20,
                "valor_unitario": Decimal("28.00"),
                "valor_total": Decimal("560.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=rosicler,
            codigo="014.000.554",
            defaults={
                "descricao": "TESOURA MULTIUSO PONTA REDONDA",
                "unidade": "UN",
                "quantidade": 20,
                "valor_unitario": Decimal("32.00"),
                "valor_total": Decimal("640.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=rosicler,
            codigo="014.001.070",
            defaults={
                "descricao": "TÓPICO PVPI",
                "unidade": "LT",
                "quantidade": 100,
                "valor_unitario": Decimal("43.90"),
                "valor_total": Decimal("4390.00"),
            },
        )

        # Garantir que o edital existe e buscar/criar a empresa
        tender_enf, _ = Edital.objects.get_or_create(
            numero="000027/25", defaults={"tipo": "ENFERMAGEM"
    }
)

        nossa_senhora, _ = Fornecedor.objects.get_or_create(
            cnpj="24.586.988/0001-80",
            defaults={
                "razao_social": "CIRÚRGICA NOSSA SENHORA EIRELI",
                "email": "cirnossasenhora@hotmail.com",
                "telefone": "(43) 3252-9947",
                "endereco": "Rua Pavão, Nº 540, Bairro Jardim Bandeirantes, Arapongas-PR, CEP 86703-250",
            },
        )

        # Itens – Parte 1
        ItemLicitado.objects.update_or_create(
    edital=tender_enf,
    codigo="014.000.503",
    defaults={
        "fornecedor": nossa_senhora,
"descricao": "BOLSA COLETORA ESTÉRIL DE URINA - SISTEMA FECHADO",
                "unidade": "UN",
                "quantidade": 600,
                "valor_unitario": Decimal("3.32"),
                "valor_total": Decimal("1992.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=nossa_senhora,
            codigo="023.001.005",
            defaults={
                "descricao": "CATÉTER NASAL TIPO ÓCULOS (INFANTIL)",
                "unidade": "UNI",
                "quantidade": 1000,
                "valor_unitario": Decimal("1.16"),
                "valor_total": Decimal("1160.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=nossa_senhora,
            codigo="014.001.031",
            defaults={
                "descricao": "ESPÁTULAS DE AYRES C/100",
                "unidade": "PCT",
                "quantidade": 20,
                "valor_unitario": Decimal("10.61"),
                "valor_total": Decimal("212.20"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=nossa_senhora,
            codigo="006.001.718",
            defaults={
                "descricao": "LÂMINA P/ MICROSCOPIA FOSCA",
                "unidade": "UN",
                "quantidade": 20,
                "valor_unitario": Decimal("5.53"),
                "valor_total": Decimal("110.60"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=nossa_senhora,
            codigo="014.000.447",
            defaults={
                "descricao": "MÁSCARA DE ALTA CONCENTRAÇÃO OXIGÊNIO C/ RESERVATÓRIO",
                "unidade": "UN",
                "quantidade": 1000,
                "valor_unitario": Decimal("4.94"),
                "valor_total": Decimal("4940.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=nossa_senhora,
            codigo="014.000.544",
            defaults={
                "descricao": "SACO BRANCO INFECTANTE 100 LITROS",
                "unidade": "UN",
                "quantidade": 5000,
                "valor_unitario": Decimal("0.33"),
                "valor_total": Decimal("1650.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=nossa_senhora,
            codigo="014.005.056",
            defaults={
                "descricao": "SACO BRANCO INFECTANTE 30 LITROS",
                "unidade": "UN",
                "quantidade": 5000,
                "valor_unitario": Decimal("0.14"),
                "valor_total": Decimal("700.00"),
            },
        )

        # Garantir que o edital existe e buscar/criar a empresa
        tender_enf, _ = Edital.objects.get_or_create(
            numero="000027/25", defaults={"tipo": "ENFERMAGEM"
    }
)

        dora, _ = Fornecedor.objects.get_or_create(
            cnpj="30.936.479/0001-33",
            defaults={
                "razao_social": "DORA MEDICAMENTOS LTDA EPP",
                "email": "licitacao@triunfal.com.br",
                "telefone": "(14) 3413-5243",
                "endereco": "Avenida Silvio Bertonha, Nº 533, Parque das Indústrias, CEP 17519-690, Marília-SP",
            },
        )

        # Itens – Parte 1
        ItemLicitado.objects.update_or_create(
    edital=tender_enf,
    codigo="014.001.026",
    defaults={
        "fornecedor": dora,
"descricao": "EQUIPO MACRO-GOTAS",
                "unidade": "UNI",
                "quantidade": 5000,
                "valor_unitario": Decimal("0.909"),
                "valor_total": Decimal("4545.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=dora,
            codigo="014.001.028",
            defaults={
                "descricao": "EQUIPO P/NUTRIÇÃO ENTERAL (AZUL)",
                "unidade": "UNI",
                "quantidade": 5000,
                "valor_unitario": Decimal("0.93"),
                "valor_total": Decimal("4650.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=dora,
            codigo="014.001.035",
            defaults={
                "descricao": "ESTETOSCÓPIO (ADULTO)",
                "unidade": "UNI",
                "quantidade": 100,
                "valor_unitario": Decimal("10.88"),
                "valor_total": Decimal("1088.00"),
            },
        )

        # Garantir que o edital existe e buscar/criar a empresa
        tender_enf, _ = Edital.objects.get_or_create(
            numero="000027/25", defaults={"tipo": "ENFERMAGEM"
    }
)

        lc_med, _ = Fornecedor.objects.get_or_create(
            cnpj="25.245.772/0001-14",
            defaults={
                "razao_social": "LC MED MATERIAIS MÉDICOS E HOSPITALARES LTDA",
                "email": "lcmed1@hotmail.com",
                "telefone": "(18) 3622-7366",
                "endereco": "Rua Saverio Safiotti, Nº 48, Bairro Paraíso, CEP 16050-130, Araçatuba-SP",
            },
        )

        # Itens da LC MED
        ItemLicitado.objects.update_or_create(
    edital=tender_enf,
    codigo="023.001.009",
    defaults={
        "fornecedor": lc_med,
"descricao": "OXÍMETRO DE BOLSO",
                "unidade": "UNI",
                "quantidade": 100,
                "valor_unitario": Decimal("31.42"),
                "valor_total": Decimal("3142.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_enf,
            fornecedor=lc_med,
            codigo="014.002.020",
            defaults={
                "descricao": "TERMÔMETRO DIGITAL LASER INFRAVERMELHO",
                "unidade": "UN",
                "quantidade": 200,
                "valor_unitario": Decimal("45.71"),
                "valor_total": Decimal("9142.00"),
            },
        )

        # Garantir que o edital existe e buscar/criar a empresa
        tender_enf, _ = Edital.objects.get_or_create(
            numero="000027/25", defaults={"tipo": "ENFERMAGEM"
    }
)

        easy, _ = Fornecedor.objects.get_or_create(
            cnpj="35.113.338/0001-34",
            defaults={
                "razao_social": "EASY INDÚSTRIA E COMÉRCIO DE DESCARTÁVEIS LTDA",
                "email": "vendas@easypell.com.br",
                "telefone": "(19) 3531-2347",
                "endereco": "Avenida 51, Nº 1036, Bairro Jardim Kennedy, CEP: 13501-520, Rio Claro-SP",
            },
        )

        # Único item da EASY
        ItemLicitado.objects.update_or_create(
    edital=tender_enf,
    codigo="014.001.049",
    defaults={
        "fornecedor": easy,
"descricao": "LENÇOL DE PAPEL DESCARTÁVEL 70CM/50M",
                "unidade": "RL",
                "quantidade": 6000,
                "valor_unitario": Decimal("7.20"),
                "valor_total": Decimal("43200.00"),
            },
        )

        # Empresa (dados do contrato)
        olimpio, _ = Fornecedor.objects.get_or_create(
            cnpj="01.140.868/0001-50",
            defaults={
                "razao_social": "CIRURGICA OLIMPIO EIRELLI EPP",
                "email": "cirurgicaolimpio@cirurgicaolimpio.com.br",
                "telefone": "(17) 3201-1270",
                "endereco": "Rua João Antonio Sicoli, 560, Jardim Maracanã, São José do Rio Preto-SP, CEP 15092-050",
            },
        )

        # Itens — parte 1
        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=olimpio,
            codigo="006.001.020",
            defaults={
                "descricao": "ACEBROFILINA 25MG/5ML",
                "unidade": "FRC",
                "quantidade": 3000,
                "valor_unitario": Decimal("5.14"),
                "valor_total": Decimal("15420.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=olimpio,
            codigo="006.001.329",
            defaults={
                "descricao": "CLINDAMICINA 300 MG",
                "unidade": "CPR",
                "quantidade": 100000,
                "valor_unitario": Decimal("0.88"),
                "valor_total": Decimal("88000.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=olimpio,
            codigo="006.001.090",
            defaults={
                "descricao": "CLORIDRATO DE AMBROXOL 15MG/5ML FRS/120ML",
                "unidade": "FRC",
                "quantidade": 3000,
                "valor_unitario": Decimal("2.25"),
                "valor_total": Decimal("6750.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=olimpio,
            codigo="006.001.099",
            defaults={
                "descricao": "CLORIDRATO DE CLORPROMAZINA 100MG",
                "unidade": "CPR",
                "quantidade": 10000,
                "valor_unitario": Decimal("0.30"),
                "valor_total": Decimal("3000.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=olimpio,
            codigo="006.001.505",
            defaults={
                "descricao": "DEXCLOR+BETAMETASONA 2MG/5ML+0,25MG/5ML",
                "unidade": "FRC",
                "quantidade": 3000,
                "valor_unitario": Decimal("2.75"),
                "valor_total": Decimal("8250.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=olimpio,
            codigo="006.001.135",
            defaults={
                "descricao": "DICLOFENACO DIETILAMÔNEO GEL 11,6MG/G TBS",
                "unidade": "TUB",
                "quantidade": 300,
                "valor_unitario": Decimal("3.38"),
                "valor_total": Decimal("1014.00"),
            },
        )

        # Itens — parte 2
        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=olimpio,
            codigo="006.001.645",
            defaults={
                "descricao": "DIPROPIONATO DE BETAMETASONA+FOSFATO DIA",
                "unidade": "AMP",
                "quantidade": 2000,
                "valor_unitario": Decimal("2.89"),
                "valor_total": Decimal("5780.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=olimpio,
            codigo="006.001.899",
            defaults={
                "descricao": "FOSFATO DE SÓDIO MONOBÁSICO (0,16G/ML)+FO",
                "unidade": "FRC",
                "quantidade": 100,
                "valor_unitario": Decimal("5.70"),
                "valor_total": Decimal("570.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=olimpio,
            codigo="006.001.901",
            defaults={
                "descricao": "HALOPERIDOL 5 MG",
                "unidade": "CPR",
                "quantidade": 10000,
                "valor_unitario": Decimal("0.11"),
                "valor_total": Decimal("1100.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=olimpio,
            codigo="006.001.908",
            defaults={
                "descricao": "LORATADINA 10 MG",
                "unidade": "CPR",
                "quantidade": 20000,
                "valor_unitario": Decimal("0.07"),
                "valor_total": Decimal("1400.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=olimpio,
            codigo="006.001.415",
            defaults={
                "descricao": "ÓXIDO DE ZINCO 100MG/G+COLECALCIFEROL 400",
                "unidade": "TUB",
                "quantidade": 2000,
                "valor_unitario": Decimal("3.11"),
                "valor_total": Decimal("6220.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=olimpio,
            codigo="006.002.369",
            defaults={
                "descricao": "PREDNISONA 5MG",
                "unidade": "CPR",
                "quantidade": 10000,
                "valor_unitario": Decimal("0.05"),
                "valor_total": Decimal("500.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=olimpio,
            codigo="006.002.970",
            defaults={
                "descricao": "SOL. GLICOFISIOLÓGICA S.F - I.V",
                "unidade": "FRC",
                "quantidade": 200,
                "valor_unitario": Decimal("4.90"),
                "valor_total": Decimal("980.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=olimpio,
            codigo="006.001.261",
            defaults={
                "descricao": "SOLUÇÃO RINGER+ LACTATO FRS/500ML",
                "unidade": "FRC",
                "quantidade": 200,
                "valor_unitario": Decimal("5.19"),
                "valor_total": Decimal("1038.00"),
            },
        )

        # Empresa (dados do contrato)
        lumar_meds, _ = Fornecedor.objects.get_or_create(
            cnpj="49.228.695/0001-52",
            defaults={
                "razao_social": "LUMAR COMERCIO DE PRODUTOS FARMACEUTICOS LTDA",
                "email": "licitacoes@lumarfranca.com.br",
                "telefone": "(16) 3721-1102",
                "endereco": "Av. Wilson Bego, 745, Distrito Industrial Antônio Della Torres, Franca-SP, CEP 14406-091",
            },
        )

        # Itens
        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=lumar_meds,
            codigo="006.001.479",
            defaults={
                "descricao": "ALOGLIPTINA 12,50 MG",
                "unidade": "CPR",
                "quantidade": 12000,
                "valor_unitario": Decimal("4.20"),
                "valor_total": Decimal("50400.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=lumar_meds,
            codigo="006.001.140",
            defaults={
                "descricao": "DIMENIDRINATO 30MG; CLORIDRATO DE PIRIDOXINA",
                "unidade": "AMP",
                "quantidade": 2000,
                "valor_unitario": Decimal("8.56"),
                "valor_total": Decimal("17120.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=lumar_meds,
            codigo="006.001.141",
            defaults={
                "descricao": "DIMENIDRINATO 50MG; CLOR. DE PIRIDOXINA 10",
                "unidade": "CPR",
                "quantidade": 30000,
                "valor_unitario": Decimal("0.63"),
                "valor_total": Decimal("18900.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=lumar_meds,
            codigo="006.001.389",
            defaults={
                "descricao": "IBUPROFENO 50MG/ML",
                "unidade": "FRC",
                "quantidade": 5000,
                "valor_unitario": Decimal("2.43"),
                "valor_total": Decimal("12150.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=lumar_meds,
            codigo="006.001.918",
            defaults={
                "descricao": "MOMETASONA 1MG/G POMADA",
                "unidade": "TUB",
                "quantidade": 300,
                "valor_unitario": Decimal("9.40"),
                "valor_total": Decimal("2820.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=lumar_meds,
            codigo="006.001.530",
            defaults={
                "descricao": "PROPIONATO DE CLOBETASOL 0,5MG/G CREME",
                "unidade": "TUB",
                "quantidade": 300,
                "valor_unitario": Decimal("4.15"),
                "valor_total": Decimal("1245.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=lumar_meds,
            codigo="006.003.414",
            defaults={
                "descricao": "VITAMINA D3 50.000 UI",
                "unidade": "CPR",
                "quantidade": 10000,
                "valor_unitario": Decimal("0.74"),
                "valor_total": Decimal("7400.00"),
            },
        )

        # Empresa (dados do contrato)
        aglon = Fornecedor.objects.get_or_create(
            razao_social="AGLON COMERCIO E REPRESENTAÇÕES LTDA",
            cnpj="65.817.900/0001-71",
            email="aglon@aglon.com.br",
            telefone="(19) 3573-7300",
            endereco="Av. Visconde de Nova Granada, 1105, Vila Grossklauss, Leme-SP, CEP 13617-400",
        )

        # Itens — parte 1
        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=aglon,
            codigo="006.001.300",
            defaults={
                "descricao": "ÁCIDO VALPROICO 250 MG",
                "unidade": "CPR",
                "quantidade": 20000,
                "valor_unitario": Decimal("0.30"),
                "valor_total": Decimal("6000.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=aglon,
            codigo="006.001.301",
            defaults={
                "descricao": "ÁCIDO VALPROICO 500 MG",
                "unidade": "CPR",
                "quantidade": 5000,
                "valor_unitario": Decimal("0.60"),
                "valor_total": Decimal("3000.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=aglon,
            codigo="006.003.354",
            defaults={
                "descricao": "ATOMOXETINA 10 MG",
                "unidade": "CPR",
                "quantidade": 6000,
                "valor_unitario": Decimal("0.80"),
                "valor_total": Decimal("4800.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=aglon,
            codigo="006.003.222",
            defaults={
                "descricao": "ATOMOXETINA 40MG",
                "unidade": "CPR",
                "quantidade": 6000,
                "valor_unitario": Decimal("3.22"),
                "valor_total": Decimal("19320.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=aglon,
            codigo="006.003.336",
            defaults={
                "descricao": "ATOMOXETINA 60MG",
                "unidade": "CPR",
                "quantidade": 6000,
                "valor_unitario": Decimal("4.83"),
                "valor_total": Decimal("28980.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=aglon,
            codigo="006.001.490",
            defaults={
                "descricao": "CITRATO DE POTÁSSIO 10 MEQ",
                "unidade": "CPR",
                "quantidade": 3000,
                "valor_unitario": Decimal("1.07"),
                "valor_total": Decimal("3210.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=aglon,
            codigo="006.001.123",
            defaults={
                "descricao": "COLAGENASE C/CLORANF. TBS/30G",
                "unidade": "TUB",
                "quantidade": 1000,
                "valor_unitario": Decimal("12.80"),
                "valor_total": Decimal("12800.00"),
            },
        )

        # Itens — parte 2
        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=aglon,
            codigo="006.001.466",
            defaults={
                "descricao": "DUTASTERIDA 0,5MG+TANSULOSINA 0,4MG",
                "unidade": "CPR",
                "quantidade": 20000,
                "valor_unitario": Decimal("2.64"),
                "valor_total": Decimal("52800.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=aglon,
            codigo="006.001.894",
            defaults={
                "descricao": "FLUVOXAMINA 100 MG",
                "unidade": "CPR",
                "quantidade": 3000,
                "valor_unitario": Decimal("3.96"),
                "valor_total": Decimal("11880.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=aglon,
            codigo="006.001.655",
            defaults={
                "descricao": "FOSFOMICINA TROMETAMOL ENV. 8 G GRANULADO",
                "unidade": "ENV",
                "quantidade": 200,
                "valor_unitario": Decimal("17.90"),
                "valor_total": Decimal("3580.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=aglon,
            codigo="006.003.392",
            defaults={
                "descricao": "OXIBUTININA 5 MG",
                "unidade": "CPR",
                "quantidade": 3000,
                "valor_unitario": Decimal("0.90"),
                "valor_total": Decimal("2700.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=aglon,
            codigo="006.001.678",
            defaults={
                "descricao": "PERINDOPRIL ARGININA 10 MG",
                "unidade": "CPR",
                "quantidade": 2000,
                "valor_unitario": Decimal("2.10"),
                "valor_total": Decimal("4200.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=aglon,
            codigo="006.003.395",
            defaults={
                "descricao": "PERINDOPRIL ARGININA 10MG+INDAPAMIDA 2,5MG",
                "unidade": "CPR",
                "quantidade": 3000,
                "valor_unitario": Decimal("2.90"),
                "valor_total": Decimal("8700.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=aglon,
            codigo="006.001.242",
            defaults={
                "descricao": "PROPATIL NITRATO 10MG",
                "unidade": "CPR",
                "quantidade": 10000,
                "valor_unitario": Decimal("0.575"),
                "valor_total": Decimal("5750.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=aglon,
            codigo="006.001.941",
            defaults={
                "descricao": "TRAZODONA 100 MG",
                "unidade": "CPR",
                "quantidade": 20000,
                "valor_unitario": Decimal("0.439"),
                "valor_total": Decimal("8780.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=aglon,
            codigo="006.001.942",
            defaults={
                "descricao": "TRAZODONA 50 MG",
                "unidade": "UN",
                "quantidade": 20000,
                "valor_unitario": Decimal("0.25"),
                "valor_total": Decimal("5000.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=aglon,
            codigo="002.001.784",
            defaults={
                "descricao": "TRIMETAZIDINA LP 80 MG",
                "unidade": "CPR",
                "quantidade": 2000,
                "valor_unitario": Decimal("3.80"),
                "valor_total": Decimal("7600.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=aglon,
            codigo="006.001.281",
            defaults={
                "descricao": "VILDAGLIPTINA 50 MG",
                "unidade": "CPR",
                "quantidade": 50000,
                "valor_unitario": Decimal("0.45"),
                "valor_total": Decimal("22500.00"),
            },
        )

        # Empresa (dados do contrato)
        rioclarense = Fornecedor.objects.get_or_create(
            razao_social="COMERCIAL CIRÚRGICA RIOCLARENSE LTDA",
            cnpj="67.729.178/0004-91",
            email="vendas@rioclarense.com.br",
            telefone="(19) 3522-5800",
            endereco="Praça Emílio Marconato, 1000, Galpões 22 e 27, Jardim Primavera, Jaguariúna-SP, CEP 13916-074",
        )

        # Itens – Parte 1
        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rioclarense,
            codigo="006.001.475",
            defaults={
                "descricao": "ACETATO DE PREDNISOLONA 1% SUSP. OFTÁLMICA",
                "unidade": "FR",
                "quantidade": 100,
                "valor_unitario": Decimal("16.29"),
                "valor_total": Decimal("1629.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rioclarense,
            codigo="006.001.290",
            defaults={
                "descricao": "ÁCIDO ACETIL SALICÍLICO 100MG",
                "unidade": "CPR",
                "quantidade": 200000,
                "valor_unitario": Decimal("0.029"),
                "valor_total": Decimal("5800.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rioclarense,
            codigo="006.001.044",
            defaults={
                "descricao": "BACLOFENO 10MG",
                "unidade": "CPR",
                "quantidade": 6000,
                "valor_unitario": Decimal("0.12"),
                "valor_total": Decimal("720.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rioclarense,
            codigo="006.002.167",
            defaults={
                "descricao": "BROMAZEPAM 6MG",
                "unidade": "CPR",
                "quantidade": 30000,
                "valor_unitario": Decimal("0.13"),
                "valor_total": Decimal("3900.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rioclarense,
            codigo="006.001.055",
            defaults={
                "descricao": "BUDESONIDA 50MCG",
                "unidade": "FRC",
                "quantidade": 500,
                "valor_unitario": Decimal("15.90"),
                "valor_total": Decimal("7950.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rioclarense,
            codigo="006.001.056",
            defaults={
                "descricao": "BUDESONIDA 64MCG",
                "unidade": "FRC",
                "quantidade": 500,
                "valor_unitario": Decimal("16.40"),
                "valor_total": Decimal("8200.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rioclarense,
            codigo="006.000.186",
            defaults={
                "descricao": "CEFALEXINA 500 MG",
                "unidade": "CX",
                "quantidade": 10000,
                "valor_unitario": Decimal("0.45"),
                "valor_total": Decimal("4500.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rioclarense,
            codigo="006.001.080",
            defaults={
                "descricao": "CETOPROFENO 100MG - I.V FRS/AMP",
                "unidade": "AMP",
                "quantidade": 1000,
                "valor_unitario": Decimal("3.999"),
                "valor_total": Decimal("3999.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rioclarense,
            codigo="006.001.093",
            defaults={
                "descricao": "CLORIDRATO DE AMITRIPTILINA 25MG",
                "unidade": "CPR",
                "quantidade": 30000,
                "valor_unitario": Decimal("0.04"),
                "valor_total": Decimal("1200.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rioclarense,
            codigo="006.001.095",
            defaults={
                "descricao": "CLORIDRATO DE BIPERIDENO 2MG",
                "unidade": "CPR",
                "quantidade": 6000,
                "valor_unitario": Decimal("0.28"),
                "valor_total": Decimal("1680.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rioclarense,
            codigo="006.001.642",
            defaults={
                "descricao": "CLORIDRATO DE CICLOBENZAPRINA 5 MG",
                "unidade": "CPR",
                "quantidade": 20000,
                "valor_unitario": Decimal("0.06"),
                "valor_total": Decimal("1200.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rioclarense,
            codigo="006.001.098",
            defaults={
                "descricao": "CLORIDRATO DE CLONIDINA 0.100 MG",
                "unidade": "CPR",
                "quantidade": 20000,
                "valor_unitario": Decimal("0.25"),
                "valor_total": Decimal("5000.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rioclarense,
            codigo="006.001.339",
            defaults={
                "descricao": "CLORIDRATO DE CLONIDINA 0.150 MG",
                "unidade": "CPR",
                "quantidade": 20000,
                "valor_unitario": Decimal("0.31"),
                "valor_total": Decimal("6200.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rioclarense,
            codigo="006.001.102",
            defaults={
                "descricao": "CLORIDRATO DE FLUOXETINA 20MG",
                "unidade": "CAP",
                "quantidade": 30000,
                "valor_unitario": Decimal("0.059"),
                "valor_total": Decimal("1770.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rioclarense,
            codigo="006.001.112",
            defaults={
                "descricao": "CLORIDRATO DE PROMETAZINA 25MG",
                "unidade": "CPR",
                "quantidade": 10000,
                "valor_unitario": Decimal("0.13"),
                "valor_total": Decimal("1300.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rioclarense,
            codigo="006.001.113",
            defaults={
                "descricao": "CLORIDRATO DE PROMETAZINA 50MG/2ML",
                "unidade": "AMP",
                "quantidade": 300,
                "valor_unitario": Decimal("3.25"),
                "valor_total": Decimal("975.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rioclarense,
            codigo="006.002.995",
            defaults={
                "descricao": "CLORIDRATO DE TRAMADOL 50MG/ML",
                "unidade": "CPR",
                "quantidade": 600,
                "valor_unitario": Decimal("1.02"),
                "valor_total": Decimal("612.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rioclarense,
            codigo="006.001.143",
            defaults={
                "descricao": "DIMETICONA 75MG/ML FRS/10ML",
                "unidade": "FRC",
                "quantidade": 2000,
                "valor_unitario": Decimal("1.39"),
                "valor_total": Decimal("2780.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rioclarense,
            codigo="006.002.693",
            defaults={
                "descricao": "ESCITALOPRAM 20MG/ML GOTAS",
                "unidade": "FR",
                "quantidade": 50,
                "valor_unitario": Decimal("10.00"),
                "valor_total": Decimal("500.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rioclarense,
            codigo="006.002.392",
            defaults={
                "descricao": "HALOPERIDOL 1MG",
                "unidade": "CPR",
                "quantidade": 5000,
                "valor_unitario": Decimal("0.18"),
                "valor_total": Decimal("900.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rioclarense,
            codigo="006.003.381",
            defaults={
                "descricao": "IMIPRAMINA 25MG",
                "unidade": "CPR",
                "quantidade": 20000,
                "valor_unitario": Decimal("0.46"),
                "valor_total": Decimal("9200.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rioclarense,
            codigo="006.001.665",
            defaults={
                "descricao": "LEVODOPA+BENSERAZIDA BD 100MG+25MG",
                "unidade": "CPR",
                "quantidade": 10000,
                "valor_unitario": Decimal("1.00"),
                "valor_total": Decimal("10000.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rioclarense,
            codigo="006.001.394",
            defaults={
                "descricao": "LEVODOPA+BENZERAZIDA 200MG/50MG",
                "unidade": "CPR",
                "quantidade": 6000,
                "valor_unitario": Decimal("1.50"),
                "valor_total": Decimal("9000.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rioclarense,
            codigo="006.002.207",
            defaults={
                "descricao": "LEVOMEPROMAZINA 25MG",
                "unidade": "CPR",
                "quantidade": 20000,
                "valor_unitario": Decimal("0.49"),
                "valor_total": Decimal("9800.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rioclarense,
            codigo="006.001.396",
            defaults={
                "descricao": "LEVOMEPROMAZINA 40MG/ML",
                "unidade": "FRC",
                "quantidade": 200,
                "valor_unitario": Decimal("11.00"),
                "valor_total": Decimal("2200.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rioclarense,
            codigo="006.001.189",
            defaults={
                "descricao": "LEVOTIROXINA SÓDICA 100MCG",
                "unidade": "CPR",
                "quantidade": 50000,
                "valor_unitario": Decimal("0.12"),
                "valor_total": Decimal("6000.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rioclarense,
            codigo="006.001.190",
            defaults={
                "descricao": "LEVOTIROXINA SÓDICA 25MCG",
                "unidade": "CPR",
                "quantidade": 50000,
                "valor_unitario": Decimal("0.16"),
                "valor_total": Decimal("8000.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rioclarense,
            codigo="006.001.191",
            defaults={
                "descricao": "LEVOTIROXINA SÓDICA 50MCG",
                "unidade": "CPR",
                "quantidade": 50000,
                "valor_unitario": Decimal("0.11"),
                "valor_total": Decimal("5500.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rioclarense,
            codigo="006.001.193",
            defaults={
                "descricao": "LIDOCAINA GELEIA 2%",
                "unidade": "TUB",
                "quantidade": 600,
                "valor_unitario": Decimal("5.00"),
                "valor_total": Decimal("3000.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rioclarense,
            codigo="006.001.197",
            defaults={
                "descricao": "LOÇÃO OLEOSA À BASE DE ÁCIDOS GRAXOS ESSENCIAIS",
                "unidade": "FRC",
                "quantidade": 1000,
                "valor_unitario": Decimal("2.76"),
                "valor_total": Decimal("2760.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rioclarense,
            codigo="006.001.208",
            defaults={
                "descricao": "MELOXICAM 15MG",
                "unidade": "CPR",
                "quantidade": 30000,
                "valor_unitario": Decimal("0.119"),
                "valor_total": Decimal("3570.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rioclarense,
            codigo="006.001.402",
            defaults={
                "descricao": "METILDOPA 250 MG",
                "unidade": "CPR",
                "quantidade": 10000,
                "valor_unitario": Decimal("0.32"),
                "valor_total": Decimal("3200.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rioclarense,
            codigo="006.001.916",
            defaults={
                "descricao": "METILDOPA 500 MG",
                "unidade": "CPR",
                "quantidade": 3000,
                "valor_unitario": Decimal("0.82"),
                "valor_total": Decimal("2460.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rioclarense,
            codigo="006.001.673",
            defaults={
                "descricao": "MONTELUCASTE DE SÓDIO 4 MG",
                "unidade": "CPR",
                "quantidade": 3000,
                "valor_unitario": Decimal("0.379"),
                "valor_total": Decimal("1137.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rioclarense,
            codigo="006.002.966",
            defaults={
                "descricao": "OLANZAPINA 10 MG",
                "unidade": "CPR",
                "quantidade": 30000,
                "valor_unitario": Decimal("0.359"),
                "valor_total": Decimal("10770.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rioclarense,
            codigo="006.002.829",
            defaults={
                "descricao": "OLANZAPINA 2,5 MG",
                "unidade": "UN",
                "quantidade": 20000,
                "valor_unitario": Decimal("0.15"),
                "valor_total": Decimal("3000.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rioclarense,
            codigo="006.001.224",
            defaults={
                "descricao": "OMEPRAZOL 20MG",
                "unidade": "CAP",
                "quantidade": 200000,
                "valor_unitario": Decimal("0.069"),
                "valor_total": Decimal("13800.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rioclarense,
            codigo="006.001.532",
            defaults={
                "descricao": "QUETIAPINA 25 MG",
                "unidade": "CPR",
                "quantidade": 50000,
                "valor_unitario": Decimal("0.12"),
                "valor_total": Decimal("6000.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rioclarense,
            codigo="006.001.426",
            defaults={
                "descricao": "RISPERIDONA 1MG/ML SOL. ORAL",
                "unidade": "FRC",
                "quantidade": 500,
                "valor_unitario": Decimal("9.95"),
                "valor_total": Decimal("4975.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rioclarense,
            codigo="006.002.491",
            defaults={
                "descricao": "ROSUVASTATINA 40 MG",
                "unidade": "CPR",
                "quantidade": 10000,
                "valor_unitario": Decimal("1.30"),
                "valor_total": Decimal("13000.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rioclarense,
            codigo="002.001.780",
            defaults={
                "descricao": "SULFATO DE AMICACINA 500 MG INJETÁVEL",
                "unidade": "AMP",
                "quantidade": 300,
                "valor_unitario": Decimal("3.80"),
                "valor_total": Decimal("1140.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rioclarense,
            codigo="006.001.275",
            defaults={
                "descricao": "VALPROATO DE SÓDIO 250MG/5ML XPE FRS/100 ML",
                "unidade": "FRC",
                "quantidade": 500,
                "valor_unitario": Decimal("5.40"),
                "valor_total": Decimal("2700.00"),
            },
        )

        # Garantir que o edital de medicamentos existe e buscar/criar a empresa
        tender_med, _ = Edital.objects.get_or_create(
            numero="000016/25", defaults={"tipo": "Medicamentos"
    }
)
        rap, _ = Fornecedor.objects.get_or_create(
            razao_social="RAP APARECIDA COMERCIO DE MEDICAMENTOS LTDA",
            cnpj="06.968.107/0001-04",
            email="rap@drogaaparecida.com.br",
            telefone="(14) 3811-8800",
            endereco="Rua Rodrigues Cesar, 174, Vila dos Lavradores, Botucatu-SP, CEP 18609-082",
        )

        # Itens – Parte 1
        ItemLicitado.objects.update_or_create(
    edital=tender_med,
    codigo="006.001.288",
    defaults={
        "fornecedor": rap,
"descricao": "ACETATO DE RETINOL 5500UI/ML, COLECALCIFEROL 1000UI/ML",
                "unidade": "FRC",
                "quantidade": 600,
                "valor_unitario": Decimal("8.86"),
                "valor_total": Decimal("5316.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.850",
            defaults={
                "descricao": "ACETILCISTEINA 20MG/ML XAROPE",
                "unidade": "FRC",
                "quantidade": 1000,
                "valor_unitario": Decimal("3.95"),
                "valor_total": Decimal("3950.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.852",
            defaults={
                "descricao": "ACETILCISTEINA 600 MG GRANULADO",
                "unidade": "ENV",
                "quantidade": 100000,
                "valor_unitario": Decimal("0.71"),
                "valor_total": Decimal("71000.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.293",
            defaults={
                "descricao": "ÁCIDO ASCÓRBICO 500MG",
                "unidade": "CPR",
                "quantidade": 20000,
                "valor_unitario": Decimal("0.18"),
                "valor_total": Decimal("3600.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.853",
            defaults={
                "descricao": "ÁCIDO ASCÓRBICO GOTAS 200MG/ML",
                "unidade": "FRC",
                "quantidade": 300,
                "valor_unitario": Decimal("1.45"),
                "valor_total": Decimal("435.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.308",
            defaults={
                "descricao": "ANLODIPINO 5MG",
                "unidade": "CPR",
                "quantidade": 50000,
                "valor_unitario": Decimal("0.027"),
                "valor_total": Decimal("1350.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.002.161",
            defaults={
                "descricao": "ATENOLOL 50MG",
                "unidade": "CPR",
                "quantidade": 50000,
                "valor_unitario": Decimal("0.049"),
                "valor_total": Decimal("2450.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.633",
            defaults={
                "descricao": "ATENOLOL+CLORTALIDONA 50MG/12,5MG",
                "unidade": "CPR",
                "quantidade": 10000,
                "valor_unitario": Decimal("0.20"),
                "valor_total": Decimal("2000.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.002.275",
            defaults={
                "descricao": "AZITROMICINA 500MG",
                "unidade": "CPR",
                "quantidade": 50000,
                "valor_unitario": Decimal("0.72"),
                "valor_total": Decimal("36000.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.864",
            defaults={
                "descricao": "BILASTINA 20 MG",
                "unidade": "CPR",
                "quantidade": 3000,
                "valor_unitario": Decimal("1.40"),
                "valor_total": Decimal("4200.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.002.236",
            defaults={
                "descricao": "BROMAZEPAM 3MG",
                "unidade": "CPR",
                "quantidade": 30000,
                "valor_unitario": Decimal("0.10"),
                "valor_total": Decimal("3000.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.317",
            defaults={
                "descricao": "CALCITRIOL 0,25 MCG CPS GEL",
                "unidade": "CAP",
                "quantidade": 10000,
                "valor_unitario": Decimal("4.47"),
                "valor_total": Decimal("44700.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.637",
            defaults={
                "descricao": "CARBIDOPA+LEVODOPA 25/250 MG",
                "unidade": "CPR",
                "quantidade": 6000,
                "valor_unitario": Decimal("0.64"),
                "valor_total": Decimal("3840.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.072",
            defaults={
                "descricao": "CARVEDILOL 3.125MG",
                "unidade": "CPR",
                "quantidade": 6000,
                "valor_unitario": Decimal("0.08"),
                "valor_total": Decimal("480.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.073",
            defaults={
                "descricao": "CARVEDILOL 6.25 MG",
                "unidade": "CAP",
                "quantidade": 20000,
                "valor_unitario": Decimal("0.09"),
                "valor_total": Decimal("1800.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.871",
            defaults={
                "descricao": "CEFADROXILA 500 MG",
                "unidade": "CAP",
                "quantidade": 3000,
                "valor_unitario": Decimal("1.77"),
                "valor_total": Decimal("5310.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.003.360",
            defaults={
                "descricao": "CETOPROFENO 150 MG",
                "unidade": "CPR",
                "quantidade": 10000,
                "valor_unitario": Decimal("0.58"),
                "valor_total": Decimal("5800.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.003.362",
            defaults={
                "descricao": "CIMICIFUGA 150 MG RACEMOSA",
                "unidade": "CAP",
                "quantidade": 1200,
                "valor_unitario": Decimal("4.70"),
                "valor_total": Decimal("5640.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.326",
            defaults={
                "descricao": "CIPROFIBRATO 100 MG",
                "unidade": "CPR",
                "quantidade": 50000,
                "valor_unitario": Decimal("0.29"),
                "valor_total": Decimal("14500.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.086",
            defaults={
                "descricao": "CLOBAZAM 20MG",
                "unidade": "CPR",
                "quantidade": 5000,
                "valor_unitario": Decimal("1.59"),
                "valor_total": Decimal("7950.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.492",
            defaults={
                "descricao": "CLONAZEPAM 0,5 MG",
                "unidade": "CPR",
                "quantidade": 10000,
                "valor_unitario": Decimal("0.052"),
                "valor_total": Decimal("520.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.003.364",
            defaults={
                "descricao": "CLOR.DE SÓDIO 0,9% GOTAS INFANTIL",
                "unidade": "FR",
                "quantidade": 1000,
                "valor_unitario": Decimal("0.913"),
                "valor_total": Decimal("913.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.641",
            defaults={
                "descricao": "CLORIDRATO DE BROMEXINA 4MG/5 ML XAROPE",
                "unidade": "FRC",
                "quantidade": 500,
                "valor_unitario": Decimal("7.80"),
                "valor_total": Decimal("3900.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.104",
            defaults={
                "descricao": "CLORIDRATO DE METFORMINA 500MG",
                "unidade": "CPR",
                "quantidade": 60000,
                "valor_unitario": Decimal("0.11"),
                "valor_total": Decimal("6600.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.877",
            defaults={
                "descricao": "CLORIDRATO DE NEBIVOLOL 5 MG",
                "unidade": "CPR",
                "quantidade": 6000,
                "valor_unitario": Decimal("0.43"),
                "valor_total": Decimal("2580.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.111",
            defaults={
                "descricao": "CLORIDRATO DE PAROXETINA 20MG",
                "unidade": "CPR",
                "quantidade": 20000,
                "valor_unitario": Decimal("0.19"),
                "valor_total": Decimal("3800.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.345",
            defaults={
                "descricao": "CODEINA 30 MG",
                "unidade": "CPR",
                "quantidade": 2000,
                "valor_unitario": Decimal("0.85"),
                "valor_total": Decimal("1700.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.002.997",
            defaults={
                "descricao": "DAPAGLIFLOZINA 10 MG",
                "unidade": "CPR",
                "quantidade": 50000,
                "valor_unitario": Decimal("5.60"),
                "valor_total": Decimal("280000.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.500",
            defaults={
                "descricao": "DESVENLAFAXINA 100 MG",
                "unidade": "CPR",
                "quantidade": 20000,
                "valor_unitario": Decimal("1.00"),
                "valor_total": Decimal("20000.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.506",
            defaults={
                "descricao": "DEXCLORFENIRAMINA 0,4MG/ML",
                "unidade": "FRC",
                "quantidade": 3000,
                "valor_unitario": Decimal("1.78"),
                "valor_total": Decimal("5340.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.884",
            defaults={
                "descricao": "DEXPANTENOL GEL 50MG/G BISNAGAS 10G",
                "unidade": "BG",
                "quantidade": 100,
                "valor_unitario": Decimal("48.00"),
                "valor_total": Decimal("4800.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.003.370",
            defaults={
                "descricao": "DOXICICLINA 100 MG",
                "unidade": "CPR",
                "quantidade": 10000,
                "valor_unitario": Decimal("0.51"),
                "valor_total": Decimal("5100.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.467",
            defaults={
                "descricao": "EMPAGLIFLOZINA 25 MG",
                "unidade": "CPR",
                "quantidade": 20000,
                "valor_unitario": Decimal("8.20"),
                "valor_total": Decimal("164000.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.153",
            defaults={
                "descricao": "ENALAPRIL 10MG, MALEATO DE",
                "unidade": "CPR",
                "quantidade": 30000,
                "valor_unitario": Decimal("0.035"),
                "valor_total": Decimal("1050.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.154",
            defaults={
                "descricao": "ENALAPRIL 20MG, MALEATO DE",
                "unidade": "CPR",
                "quantidade": 50000,
                "valor_unitario": Decimal("0.05"),
                "valor_total": Decimal("2500.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.002.254",
            defaults={
                "descricao": "ESCITALOPRAM 10MG",
                "unidade": "CPR",
                "quantidade": 50000,
                "valor_unitario": Decimal("0.12"),
                "valor_total": Decimal("6000.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.649",
            defaults={
                "descricao": "ESCITALOPRAM 15 MG",
                "unidade": "CPR",
                "quantidade": 20000,
                "valor_unitario": Decimal("0.22"),
                "valor_total": Decimal("4400.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.002.178",
            defaults={
                "descricao": "ESPIRONOLACTONA 25MG",
                "unidade": "CPR",
                "quantidade": 50000,
                "valor_unitario": Decimal("0.19"),
                "valor_total": Decimal("9500.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.468",
            defaults={
                "descricao": "EZETIMIBA 10 MG",
                "unidade": "CPR",
                "quantidade": 30000,
                "valor_unitario": Decimal("0.48"),
                "valor_total": Decimal("14400.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.003.373",
            defaults={
                "descricao": "FENAZOPIRIDINA 200 MG",
                "unidade": "CPR",
                "quantidade": 6000,
                "valor_unitario": Decimal("1.49"),
                "valor_total": Decimal("8940.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.003.374",
            defaults={
                "descricao": "FERRIPOLIMALTOSE 400 MG",
                "unidade": "CPR",
                "quantidade": 6000,
                "valor_unitario": Decimal("1.87"),
                "valor_total": Decimal("11220.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.516",
            defaults={
                "descricao": "FEXOFENADINA SUSP. ORAL 6MG/60ML",
                "unidade": "FRC",
                "quantidade": 500,
                "valor_unitario": Decimal("11.80"),
                "valor_total": Decimal("5900.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.003.376",
            defaults={
                "descricao": "FLUNARIZINA 10 MG",
                "unidade": "CPR",
                "quantidade": 10000,
                "valor_unitario": Decimal("0.09"),
                "valor_total": Decimal("900.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.895",
            defaults={
                "descricao": "FLUVOXAMINA 50 MG",
                "unidade": "CPR",
                "quantidade": 3000,
                "valor_unitario": Decimal("2.09"),
                "valor_total": Decimal("6270.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.003.211",
            defaults={
                "descricao": "GALANTAMINA 24 MG",
                "unidade": "CPR",
                "quantidade": 10000,
                "valor_unitario": Decimal("4.80"),
                "valor_total": Decimal("48000.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.003.378",
            defaults={
                "descricao": "GALANTAMINA 8 MG",
                "unidade": "CPR",
                "quantidade": 10000,
                "valor_unitario": Decimal("3.40"),
                "valor_total": Decimal("34000.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.002.286",
            defaults={
                "descricao": "GLIMEPIRIDA 4MG",
                "unidade": "CPR",
                "quantidade": 5000,
                "valor_unitario": Decimal("0.17"),
                "valor_total": Decimal("850.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.520",
            defaults={
                "descricao": "HIALURONATO DE SÓDIO 0,15% 10 ML SOL. OFTÁLMICA",
                "unidade": "FRC",
                "quantidade": 200,
                "valor_unitario": Decimal("39.00"),
                "valor_total": Decimal("7800.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.002.710",
            defaults={
                "descricao": "HIDROXIZINA 25MG C/30 CPR",
                "unidade": "UN",
                "quantidade": 2000,
                "valor_unitario": Decimal("1.09"),
                "valor_total": Decimal("2180.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.387",
            defaults={
                "descricao": "IBUPROFENO 100MG/ML",
                "unidade": "FRC",
                "quantidade": 1000,
                "valor_unitario": Decimal("1.90"),
                "valor_total": Decimal("1900.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.660",
            defaults={
                "descricao": "INDAPAMIDA 1,5 MG",
                "unidade": "CPR",
                "quantidade": 10000,
                "valor_unitario": Decimal("0.17"),
                "valor_total": Decimal("1700.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.391",
            defaults={
                "descricao": "INSULINA LANTUS SOLOSTAR (GLARGINA) 100UI",
                "unidade": "CNT",
                "quantidade": 500,
                "valor_unitario": Decimal("51.00"),
                "valor_total": Decimal("25500.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.395",
            defaults={
                "descricao": "LEVODOPA+BENZERAZIDA HBS 100MG/25MG",
                "unidade": "CPR",
                "quantidade": 10000,
                "valor_unitario": Decimal("2.90"),
                "valor_total": Decimal("29000.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.668",
            defaults={
                "descricao": "LUTEÍNA 10 MG + ZEAXANTINA 2 MG C/VITAMINAS",
                "unidade": "CAP",
                "quantidade": 3000,
                "valor_unitario": Decimal("1.65"),
                "valor_total": Decimal("4950.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.403",
            defaults={
                "descricao": "METILFENIDATO 36 MG",
                "unidade": "CPR",
                "quantidade": 10000,
                "valor_unitario": Decimal("6.90"),
                "valor_total": Decimal("69000.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.003.388",
            defaults={
                "descricao": "METILFENIDATO 54 MG",
                "unidade": "CPR",
                "quantidade": 3000,
                "valor_unitario": Decimal("6.90"),
                "valor_total": Decimal("20700.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.671",
            defaults={
                "descricao": "METILFENIDATO 10 MG LA",
                "unidade": "CPR",
                "quantidade": 3000,
                "valor_unitario": Decimal("3.60"),
                "valor_total": Decimal("10800.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.527",
            defaults={
                "descricao": "METILFENIDATO 18 MG",
                "unidade": "CPR",
                "quantidade": 6000,
                "valor_unitario": Decimal("5.27"),
                "valor_total": Decimal("31620.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.003.389",
            defaults={
                "descricao": "MONTELUCASTE DE SÓDIO 5 MG",
                "unidade": "CPR",
                "quantidade": 3000,
                "valor_unitario": Decimal("0.439"),
                "valor_total": Decimal("1317.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.216",
            defaults={
                "descricao": "NIMESULIDA 100MG",
                "unidade": "CPR",
                "quantidade": 50000,
                "valor_unitario": Decimal("0.06"),
                "valor_total": Decimal("3000.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.002.965",
            defaults={
                "descricao": "NITRENDIPINO 10 MG",
                "unidade": "CPR",
                "quantidade": 3000,
                "valor_unitario": Decimal("2.66"),
                "valor_total": Decimal("7980.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.409",
            defaults={
                "descricao": "NITRENDIPINO 20 MG",
                "unidade": "CPR",
                "quantidade": 3000,
                "valor_unitario": Decimal("5.00"),
                "valor_total": Decimal("15000.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.231",
            defaults={
                "descricao": "PANTOPRAZOL SÓDICO 40MG",
                "unidade": "CPR",
                "quantidade": 60000,
                "valor_unitario": Decimal("0.15"),
                "valor_total": Decimal("9000.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.003.393",
            defaults={
                "descricao": "PASSIFLORA INCARNATA L 360 MG",
                "unidade": "CPR",
                "quantidade": 10000,
                "valor_unitario": Decimal("2.14"),
                "valor_total": Decimal("21400.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.236",
            defaults={
                "descricao": "PERMANGANATO DE POTÁSSIO 100MG",
                "unidade": "CPR",
                "quantidade": 1000,
                "valor_unitario": Decimal("0.50"),
                "valor_total": Decimal("500.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.238",
            defaults={
                "descricao": "POLIVITAMÍNICO DO COMPLEXO B",
                "unidade": "CPR",
                "quantidade": 50000,
                "valor_unitario": Decimal("0.035"),
                "valor_total": Decimal("1750.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="002.001.774",
            defaults={
                "descricao": "PREGABALINA 150 MG",
                "unidade": "CPR",
                "quantidade": 20000,
                "valor_unitario": Decimal("0.36"),
                "valor_total": Decimal("7200.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="002.001.775",
            defaults={
                "descricao": "PREGABALINA 50 MG",
                "unidade": "CPR",
                "quantidade": 10000,
                "valor_unitario": Decimal("0.56"),
                "valor_total": Decimal("5600.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.003.403",
            defaults={
                "descricao": "ROSUVASTATINA 10 MG",
                "unidade": "CPR",
                "quantidade": 60000,
                "valor_unitario": Decimal("0.17"),
                "valor_total": Decimal("10200.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.251",
            defaults={
                "descricao": "SAXAGLIPTINA 5MG",
                "unidade": "CPR",
                "quantidade": 10000,
                "valor_unitario": Decimal("5.40"),
                "valor_total": Decimal("54000.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.794",
            defaults={
                "descricao": "SOTALOL 160 MG",
                "unidade": "CX",
                "quantidade": 2000,
                "valor_unitario": Decimal("0.90"),
                "valor_total": Decimal("1800.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.002.971",
            defaults={
                "descricao": "SULFADIAZINA DE PRATA+NITRATO DE CÉRIO",
                "unidade": "TUB",
                "quantidade": 200,
                "valor_unitario": Decimal("88.00"),
                "valor_total": Decimal("17600.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.003.409",
            defaults={
                "descricao": "SUPLEMENTO PARA GESTANTE",
                "unidade": "FRC",
                "quantidade": 500,
                "valor_unitario": Decimal("9.89"),
                "valor_total": Decimal("4945.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.002.973",
            defaults={
                "descricao": "SULPIRIDA 50 MG",
                "unidade": "CPR",
                "quantidade": 6000,
                "valor_unitario": Decimal("0.90"),
                "valor_total": Decimal("5400.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.539",
            defaults={
                "descricao": "TOPIRAMATO 25 MG",
                "unidade": "CAP",
                "quantidade": 20000,
                "valor_unitario": Decimal("0.17"),
                "valor_total": Decimal("3400.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.277",
            defaults={
                "descricao": "VALSARTANA 320 MG",
                "unidade": "CPR",
                "quantidade": 100000,
                "valor_unitario": Decimal("1.20"),
                "valor_total": Decimal("120000.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.943",
            defaults={
                "descricao": "VENLAFAXINA 37.5 MG",
                "unidade": "CPR",
                "quantidade": 10000,
                "valor_unitario": Decimal("0.30"),
                "valor_total": Decimal("3000.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.003.413",
            defaults={
                "descricao": "VILDAGLIPTINA 50MG+METFORMINA 1000 MG",
                "unidade": "CPR",
                "quantidade": 1200,
                "valor_unitario": Decimal("1.23"),
                "valor_total": Decimal("1476.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.003.417",
            defaults={
                "descricao": "VITAMINA D3 2.000 UI",
                "unidade": "CPR",
                "quantidade": 10000,
                "valor_unitario": Decimal("0.15"),
                "valor_total": Decimal("1500.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=rap,
            codigo="006.001.449",
            defaults={
                "descricao": "VITAMINAS E SAIS MINERAIS",
                "unidade": "CPR",
                "quantidade": 30000,
                "valor_unitario": Decimal("0.06"),
                "valor_total": Decimal("1800.00"),
            },
        )

        # Garantir que o edital de medicamentos existe e buscar/criar a empresa
        tender_med, _ = Edital.objects.get_or_create(
            numero="000016/25", defaults={"tipo": "MEDICAMENTOS"
    }
)

        fragnari, _ = Fornecedor.objects.get_or_create(
            razao_social="FRAGNARI DISTRIBUIDORA DE MEDICAMENTOS LTDA",
            cnpj="14.271.474/0001-82",
            email="licitacoes@fragnari.com.br",
            telefone="(14) 3814-0512 / (14) 3814-5572",
            endereco="Rua Manoel Deodoro Pinheiro Machado, 1218, Vila Santa Terezinha, Botucatu-SP, CEP 18606-710",
        )

        # Itens – Parte 1
        ItemLicitado.objects.update_or_create(
    edital=tender_med,
    codigo="006.001.854",
    defaults={
        "fornecedor": fragnari,
"descricao": "ÁCIDO MEFENÂMICO 500 MG",
                "unidade": "CPR",
                "quantidade": 5000,
                "valor_unitario": Decimal("0.43"),
                "valor_total": Decimal("2150.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.002.408",
            defaults={
                "descricao": "ALOPURINOL 100MG",
                "unidade": "CPR",
                "quantidade": 20000,
                "valor_unitario": Decimal("0.12"),
                "valor_total": Decimal("2400.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.001.630",
            defaults={
                "descricao": "ALPRAZOLAM 0.5 MG",
                "unidade": "CPR",
                "quantidade": 10000,
                "valor_unitario": Decimal("0.06"),
                "valor_total": Decimal("600.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.001.483",
            defaults={
                "descricao": "BETAMETASONA+GENTAMICINA POMADA TBS/30",
                "unidade": "TUB",
                "quantidade": 200,
                "valor_unitario": Decimal("6.199"),
                "valor_total": Decimal("1239.80"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.001.636",
            defaults={
                "descricao": "BROMETO DE ESCOPOLAMINA+PARACETAMOL 10 MG",
                "unidade": "CPR",
                "quantidade": 6000,
                "valor_unitario": Decimal("1.45"),
                "valor_total": Decimal("8700.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.001.314",
            defaults={
                "descricao": "BUPROPIONA XL 300 MG",
                "unidade": "CPR",
                "quantidade": 10000,
                "valor_unitario": Decimal("3.03"),
                "valor_total": Decimal("30300.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.001.488",
            defaults={
                "descricao": "CEFTRIAXONA 500MG I.M",
                "unidade": "FRC",
                "quantidade": 1000,
                "valor_unitario": Decimal("10.25"),
                "valor_total": Decimal("10250.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.001.322",
            defaults={
                "descricao": "CETOPROFENO 20MG/ML SOL. ORAL",
                "unidade": "FRC",
                "quantidade": 300,
                "valor_unitario": Decimal("2.30"),
                "valor_total": Decimal("690.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.001.875",
            defaults={
                "descricao": "CIMETIDINA 200 MG",
                "unidade": "CPR",
                "quantidade": 20000,
                "valor_unitario": Decimal("0.36"),
                "valor_total": Decimal("7200.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.001.491",
            defaults={
                "descricao": "CLONAZEPAM 0,25 MG SL",
                "unidade": "CPR",
                "quantidade": 20000,
                "valor_unitario": Decimal("0.273"),
                "valor_total": Decimal("5460.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.001.876",
            defaults={
                "descricao": "CLORETO DE POTÁSSIO 600 MG",
                "unidade": "CPR",
                "quantidade": 6000,
                "valor_unitario": Decimal("0.815"),
                "valor_total": Decimal("4890.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.001.493",
            defaults={
                "descricao": "CLORIDRATO DE BUSPIRONA 10 MG",
                "unidade": "CPR",
                "quantidade": 3000,
                "valor_unitario": Decimal("2.44"),
                "valor_total": Decimal("7320.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.002.994",
            defaults={
                "descricao": "CLORIDRATO DE PAROXETINA XR 25 MG",
                "unidade": "CPR",
                "quantidade": 6000,
                "valor_unitario": Decimal("3.66"),
                "valor_total": Decimal("21960.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.003.366",
            defaults={
                "descricao": "COLÁGENO TIPO II",
                "unidade": "FR",
                "quantidade": 300,
                "valor_unitario": Decimal("20.90"),
                "valor_total": Decimal("6270.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.001.496",
            defaults={
                "descricao": "CORIDRATO DE MOXIFLOXAXINO 5,45 MG/ML+ FO",
                "unidade": "FRC",
                "quantidade": 100,
                "valor_unitario": Decimal("38.50"),
                "valor_total": Decimal("3850.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.001.497",
            defaults={
                "descricao": "CUMARINA+TROXERRUTINA 15/90 MG",
                "unidade": "CPR",
                "quantidade": 30000,
                "valor_unitario": Decimal("0.32"),
                "valor_total": Decimal("9600.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.001.346",
            defaults={
                "descricao": "DABIGATRANA 110 MG",
                "unidade": "CPR",
                "quantidade": 1000,
                "valor_unitario": Decimal("5.68"),
                "valor_total": Decimal("5680.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.001.347",
            defaults={
                "descricao": "DABIGATRANA 150 MG",
                "unidade": "CPR",
                "quantidade": 3000,
                "valor_unitario": Decimal("5.68"),
                "valor_total": Decimal("17040.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.003.367",
            defaults={
                "descricao": "DAPAGLIFLOZINA+METFORMINA 10MG/1000 XR",
                "unidade": "CPR",
                "quantidade": 2000,
                "valor_unitario": Decimal("7.68"),
                "valor_total": Decimal("15360.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.003.368",
            defaults={
                "descricao": "DAPAGLIFLOZINA+METFORMINA 5MG/1000 XR",
                "unidade": "CPR",
                "quantidade": 6000,
                "valor_unitario": Decimal("3.86"),
                "valor_total": Decimal("23160.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.001.501",
            defaults={
                "descricao": "DESVENLAFAXINA 50 MG",
                "unidade": "CPR",
                "quantidade": 10000,
                "valor_unitario": Decimal("0.639"),
                "valor_total": Decimal("6390.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.003.369",
            defaults={
                "descricao": "DIACEREINA 50 MG",
                "unidade": "CPR",
                "quantidade": 2000,
                "valor_unitario": Decimal("5.09"),
                "valor_total": Decimal("10180.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.001.356",
            defaults={
                "descricao": "DICLOFENACO DIETILAMÔNIO AEROSSOL 11,6 MG/G",
                "unidade": "FRC",
                "quantidade": 300,
                "valor_unitario": Decimal("20.90"),
                "valor_total": Decimal("6270.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.001.510",
            defaults={
                "descricao": "DICLORIDRATO DE MANIDIPINO 10 MG",
                "unidade": "CPR",
                "quantidade": 2000,
                "valor_unitario": Decimal("2.69"),
                "valor_total": Decimal("5380.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.001.886",
            defaults={
                "descricao": "DIMESILATO DE LISDEXANFETAMINA 70 MG",
                "unidade": "CPR",
                "quantidade": 2800,
                "valor_unitario": Decimal("6.07"),
                "valor_total": Decimal("16996.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.001.465",
            defaults={
                "descricao": "DIMESILATO LISDEXANFETAMINA 50 MG",
                "unidade": "CPR",
                "quantidade": 2800,
                "valor_unitario": Decimal("4.50"),
                "valor_total": Decimal("12600.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.001.144",
            defaults={
                "descricao": "DIOSMINA+HISPERIDINA 450/50 MG",
                "unidade": "CPR",
                "quantidade": 100000,
                "valor_unitario": Decimal("0.38"),
                "valor_total": Decimal("38000.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.001.514",
            defaults={
                "descricao": "DIVALPROATO DE SÓDIO 500 MG ER",
                "unidade": "CPR",
                "quantidade": 10000,
                "valor_unitario": Decimal("0.93"),
                "valor_total": Decimal("9300.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.001.359",
            defaults={
                "descricao": "DOXASOZINA 2MG",
                "unidade": "CPR",
                "quantidade": 30000,
                "valor_unitario": Decimal("0.086"),
                "valor_total": Decimal("2580.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.001.653",
            defaults={
                "descricao": "ESZOPICLONA 3 MG",
                "unidade": "CPR",
                "quantidade": 6000,
                "valor_unitario": Decimal("3.37"),
                "valor_total": Decimal("20220.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.003.377",
            defaults={
                "descricao": "FUMARATO DE MOMETASONA 50 MCG SPRAY NASAL",
                "unidade": "FRC",
                "quantidade": 100,
                "valor_unitario": Decimal("22.25"),
                "valor_total": Decimal("2225.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.001.656",
            defaults={
                "descricao": "FUROATO DE FLUTICASONA 27,5 MCG SPRAY NASAL",
                "unidade": "FRC",
                "quantidade": 100,
                "valor_unitario": Decimal("62.00"),
                "valor_total": Decimal("6200.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.001.658",
            defaults={
                "descricao": "GLICINATO DE MAGNÉSIO (722,2 MG)+ CLORIDRATO DE PIRIDOXINA 1 MG",
                "unidade": "CPR",
                "quantidade": 6000,
                "valor_unitario": Decimal("3.30"),
                "valor_total": Decimal("19800.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.001.659",
            defaults={
                "descricao": "HIDRALAZINA 50 MG",
                "unidade": "CPR",
                "quantidade": 20000,
                "valor_unitario": Decimal("0.578"),
                "valor_total": Decimal("11560.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.001.523",
            defaults={
                "descricao": "INSULINA DEGLUDECA+LIRAGLUTIDA",
                "unidade": "CNT",
                "quantidade": 300,
                "valor_unitario": Decimal("281.30"),
                "valor_total": Decimal("84390.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.001.906",
            defaults={
                "descricao": "INSULINA NOVORAPID FLEXPEN",
                "unidade": "CNT",
                "quantidade": 100,
                "valor_unitario": Decimal("57.70"),
                "valor_total": Decimal("5770.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.001.470",
            defaults={
                "descricao": "INSULINA SOLIQUA 10-40 SOLOSTAR",
                "unidade": "CNT",
                "quantidade": 100,
                "valor_unitario": Decimal("210.15"),
                "valor_total": Decimal("21015.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.001.663",
            defaults={
                "descricao": "LEVETIRACETAM 100 MG/ML",
                "unidade": "FRC",
                "quantidade": 50,
                "valor_unitario": Decimal("57.20"),
                "valor_total": Decimal("2860.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.001.664",
            defaults={
                "descricao": "LEVETIRACETAM 250 MG",
                "unidade": "CPR",
                "quantidade": 3000,
                "valor_unitario": Decimal("0.66"),
                "valor_total": Decimal("1980.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.001.192",
            defaults={
                "descricao": "LEVOTIROXINA SÓDICA 75MCG",
                "unidade": "CPR",
                "quantidade": 50000,
                "valor_unitario": Decimal("0.32"),
                "valor_total": Decimal("16000.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.001.524",
            defaults={
                "descricao": "LINAGLIPTINA 5 MG",
                "unidade": "CPR",
                "quantidade": 6000,
                "valor_unitario": Decimal("3.70"),
                "valor_total": Decimal("22200.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.003.386",
            defaults={
                "descricao": "LINAGLIPTINA 2.5 MG+METFORMINA 1000 MG",
                "unidade": "CPR",
                "quantidade": 1200,
                "valor_unitario": Decimal("2.05"),
                "valor_total": Decimal("2460.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.002.144",
            defaults={
                "descricao": "MIRTAZAPINA 15 MG",
                "unidade": "CX",
                "quantidade": 20000,
                "valor_unitario": Decimal("0.65"),
                "valor_total": Decimal("13000.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.001.213",
            defaults={
                "descricao": "MONTELUCASTE DE SÓDIO 10MG",
                "unidade": "CPR",
                "quantidade": 3000,
                "valor_unitario": Decimal("0.375"),
                "valor_total": Decimal("1125.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.001.675",
            defaults={
                "descricao": "NARATRIPTANA 2,5 MG",
                "unidade": "CPR",
                "quantidade": 20000,
                "valor_unitario": Decimal("1.90"),
                "valor_total": Decimal("38000.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.001.676",
            defaults={
                "descricao": "NITAZOXANIDA 20MG/ML",
                "unidade": "FRC",
                "quantidade": 200,
                "valor_unitario": Decimal("6.939"),
                "valor_total": Decimal("1387.80"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.001.413",
            defaults={
                "descricao": "OLMESARTANA 20 MG",
                "unidade": "CPR",
                "quantidade": 200000,
                "valor_unitario": Decimal("0.479"),
                "valor_total": Decimal("95800.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.003.391",
            defaults={
                "descricao": "ORLISTAT 120 MG",
                "unidade": "CX",
                "quantidade": 200,
                "valor_unitario": Decimal("89.00"),
                "valor_total": Decimal("17800.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.001.235",
            defaults={
                "descricao": "PERICIAZINA 4% FRS/20ML",
                "unidade": "FRC",
                "quantidade": 100,
                "valor_unitario": Decimal("23.90"),
                "valor_total": Decimal("2390.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.003.394",
            defaults={
                "descricao": "PERINDOPRIL ARGININA 10MG+INDAPAMIDA 2,5",
                "unidade": "CPR",
                "quantidade": 3000,
                "valor_unitario": Decimal("4.40"),
                "valor_total": Decimal("13200.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.001.929",
            defaults={
                "descricao": "POLICRESULENO 90 MG ÓVULOS CXS/6 ÓVULOS",
                "unidade": "CX",
                "quantidade": 100,
                "valor_unitario": Decimal("22.69"),
                "valor_total": Decimal("2269.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.003.398",
            defaults={
                "descricao": "POLISSULFATO DE MUCOPOLISSACARIDEO 5MG/",
                "unidade": "TUB",
                "quantidade": 200,
                "valor_unitario": Decimal("18.60"),
                "valor_total": Decimal("3720.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.003.399",
            defaults={
                "descricao": "PROGESTERONA MICRONIZADA 100 MG",
                "unidade": "CAP",
                "quantidade": 3000,
                "valor_unitario": Decimal("2.10"),
                "valor_total": Decimal("6300.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.003.400",
            defaults={
                "descricao": "PROGESTERONA MICRONIZADA 200 MG",
                "unidade": "CPR",
                "quantidade": 3000,
                "valor_unitario": Decimal("4.20"),
                "valor_total": Decimal("12600.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.001.424",
            defaults={
                "descricao": "QUETIAPINA XR 50 MG",
                "unidade": "CPR",
                "quantidade": 6000,
                "valor_unitario": Decimal("2.30"),
                "valor_total": Decimal("13800.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="002.001.777",
            defaults={
                "descricao": "RAMIPRIL 5 MG",
                "unidade": "CPR",
                "quantidade": 6000,
                "valor_unitario": Decimal("0.70"),
                "valor_total": Decimal("4200.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.001.935",
            defaults={
                "descricao": "ROSUVASTATINA 40 MG + EZETIMIBA 10 MG",
                "unidade": "UN",
                "quantidade": 3000,
                "valor_unitario": Decimal("5.219"),
                "valor_total": Decimal("15657.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.001.248",
            defaults={
                "descricao": "SACCHAROMYCES BOULARDII 100 MG",
                "unidade": "CAP",
                "quantidade": 20000,
                "valor_unitario": Decimal("0.86"),
                "valor_total": Decimal("17200.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.001.249",
            defaults={
                "descricao": "SACCHAROMYCES BOULARDII 200 MG",
                "unidade": "SAC",
                "quantidade": 10000,
                "valor_unitario": Decimal("1.44"),
                "valor_total": Decimal("14400.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.003.407",
            defaults={
                "descricao": "SILIMARINA 200 MG",
                "unidade": "CPR",
                "quantidade": 3000,
                "valor_unitario": Decimal("0.83"),
                "valor_total": Decimal("2490.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.002.969",
            defaults={
                "descricao": "SITAGLIPTINA + METFORMINA 50MG/1000 MG",
                "unidade": "CPR",
                "quantidade": 3000,
                "valor_unitario": Decimal("1.71"),
                "valor_total": Decimal("5130.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.002.974",
            defaults={
                "descricao": "SULPIRIDA + BROMAZEPAM 25 MG / 1 MG",
                "unidade": "CPR",
                "quantidade": 6000,
                "valor_unitario": Decimal("1.83"),
                "valor_total": Decimal("10980.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="002.001.782",
            defaults={
                "descricao": "TELMISARTANA 80 MG",
                "unidade": "CPR",
                "quantidade": 3000,
                "valor_unitario": Decimal("1.10"),
                "valor_total": Decimal("3300.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.001.443",
            defaults={
                "descricao": "TELMISARTANA + ANLODIPINO 80MG/5MG",
                "unidade": "CPR",
                "quantidade": 3000,
                "valor_unitario": Decimal("4.79"),
                "valor_total": Decimal("14370.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.001.537",
            defaults={
                "descricao": "TOBRAMICINA + DEXAMETASONA 0,3% / 0,1% SOL. OFTÁLMICA",
                "unidade": "FRC",
                "quantidade": 600,
                "valor_unitario": Decimal("34.19"),
                "valor_total": Decimal("20514.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="002.001.783",
            defaults={
                "descricao": "TRAZODONA RETARD 150 MG",
                "unidade": "CPR",
                "quantidade": 10000,
                "valor_unitario": Decimal("1.60"),
                "valor_total": Decimal("16000.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="002.001.785",
            defaults={
                "descricao": "TRIMETAZIDINA MR 35 MG",
                "unidade": "CPR",
                "quantidade": 30000,
                "valor_unitario": Decimal("0.799"),
                "valor_total": Decimal("23970.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.001.944",
            defaults={
                "descricao": "VIMPOCETINA 5 MG",
                "unidade": "CPR",
                "quantidade": 3000,
                "valor_unitario": Decimal("0.865"),
                "valor_total": Decimal("2595.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=fragnari,
            codigo="006.003.420",
            defaults={
                "descricao": "VORTIOXETINA 10 MG",
                "unidade": "CPR",
                "quantidade": 6000,
                "valor_unitario": Decimal("2.179"),
                "valor_total": Decimal("13074.00"),
            },
        )

        # Garantir que o edital de medicamentos existe e buscar/criar a empresa
        tender_med, _ = Edital.objects.get_or_create(
            numero="000016/25", defaults={"tipo": "MEDICAMENTOS"
    }
)
        mamed = Fornecedor.objects.get_or_create(
            razao_social="MAMED COMERCIAL LTDA - EPP",
            cnpj="21.608.296/0001-06",
            email="mamedvendas@gmail.com",
            telefone="(14) 3667-3865",
            endereco="Rua Antartica, 850, Jardim Vitória, Marília-SP, CEP 17520-130",
        )

        # Único item da MAMED
        ItemLicitado.objects.update_or_create(
    edital=tender_med,
    codigo="006.003.371",
    defaults={
        "fornecedor": mamed,
"descricao": "EMPAGLIFLOZINA 10 MG",
                "unidade": "CPR",
                "quantidade": 3000,
                "valor_unitario": Decimal("5.75"),
                "valor_total": Decimal("17250.00"),
            },
        )

        # Garantir que o edital de medicamentos existe e buscar/criar a empresa
        tender_med, _ = Edital.objects.get_or_create(
            numero="000016/25", defaults={"tipo": "MEDICAMENTOS"
    }
)
        dimeva = Fornecedor.objects.get_or_create(
            razao_social="DIMEVA DISTRIBUIDORA E IMPORTADORA LTDA",
            cnpj="76.386.283/0001-13",
            email="faturamento@dimeva.com.br",
            telefone="(46) 3224-3767",
            endereco="Rua José Fraron, 155, Bairro Fraron, Pato Branco-PR, CEP 85503-320",
        )

        # Itens – conforme PDF
        ItemLicitado.objects.update_or_create(
    edital=tender_med,
    codigo="006.001.287",
    defaults={
        "fornecedor": dimeva,
"descricao": "ACETATO DE CIPROTERONA 2MG, ETINILESTRADIOL 0,035MG",
                "unidade": "CPR",
                "quantidade": 20000,
                "valor_unitario": Decimal("0.21"),
                "valor_total": Decimal("4200.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=dimeva,
            codigo="006.001.861",
            defaults={
                "descricao": "BETAISTINA 24 MG",
                "unidade": "CPR",
                "quantidade": 20000,
                "valor_unitario": Decimal("0.26"),
                "valor_total": Decimal("5200.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=dimeva,
            codigo="006.001.862",
            defaults={
                "descricao": "BETAISTINA 16 MG",
                "unidade": "CPR",
                "quantidade": 30000,
                "valor_unitario": Decimal("0.22"),
                "valor_total": Decimal("6600.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=dimeva,
            codigo="006.001.462",
            defaults={
                "descricao": "CARBONATO DE LÍTIO CR 450 MG",
                "unidade": "CPR",
                "quantidade": 20000,
                "valor_unitario": Decimal("1.70"),
                "valor_total": Decimal("34000.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=dimeva,
            codigo="006.001.639",
            defaults={
                "descricao": "CILOSTAZOL 50 MG",
                "unidade": "CPR",
                "quantidade": 6000,
                "valor_unitario": Decimal("0.24"),
                "valor_total": Decimal("1440.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=dimeva,
            codigo="006.002.992",
            defaults={
                "descricao": "CLORIDRATO DE MOXIFLOXACINO 400 MG",
                "unidade": "CPR",
                "quantidade": 3000,
                "valor_unitario": Decimal("0.31"),
                "valor_total": Decimal("930.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=dimeva,
            codigo="006.001.349",
            defaults={
                "descricao": "DELTAMETRINA 0,02%",
                "unidade": "FRC",
                "quantidade": 600,
                "valor_unitario": Decimal("4.48"),
                "valor_total": Decimal("2688.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=dimeva,
            codigo="006.001.361",
            defaults={
                "descricao": "DULOXETINA 30 MG",
                "unidade": "CAP",
                "quantidade": 30000,
                "valor_unitario": Decimal("0.95"),
                "valor_total": Decimal("28500.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=dimeva,
            codigo="006.001.648",
            defaults={
                "descricao": "DULOXETINA 60 MG",
                "unidade": "CPR",
                "quantidade": 30000,
                "valor_unitario": Decimal("1.42"),
                "valor_total": Decimal("42600.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=dimeva,
            codigo="006.001.890",
            defaults={
                "descricao": "FENOBARBITAL 100 MG",
                "unidade": "CPR",
                "quantidade": 10000,
                "valor_unitario": Decimal("0.18"),
                "valor_total": Decimal("1800.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=dimeva,
            codigo="006.001.184",
            defaults={
                "descricao": "LEVOFLOXACINO 500 MG",
                "unidade": "CPR",
                "quantidade": 10000,
                "valor_unitario": Decimal("0.63"),
                "valor_total": Decimal("6300.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=dimeva,
            codigo="006.001.926",
            defaults={
                "descricao": "NITROFURANTOINA 100 MG",
                "unidade": "CAP",
                "quantidade": 10000,
                "valor_unitario": Decimal("0.25"),
                "valor_total": Decimal("2500.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=dimeva,
            codigo="006.001.266",
            defaults={
                "descricao": "SULFATO DE NEOMICINA+BACITRACINA 5MG/G+250UI/G",
                "unidade": "TUB",
                "quantidade": 3000,
                "valor_unitario": Decimal("2.12"),
                "valor_total": Decimal("6360.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=dimeva,
            codigo="006.001.278",
            defaults={
                "descricao": "VARFARINA SÓDICA 5 MG",
                "unidade": "CPR",
                "quantidade": 10000,
                "valor_unitario": Decimal("0.16"),
                "valor_total": Decimal("1600.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=dimeva,
            codigo="006.003.421",
            defaults={
                "descricao": "ZOLPIDEM 10 MG",
                "unidade": "CPR",
                "quantidade": 30000,
                "valor_unitario": Decimal("0.10"),
                "valor_total": Decimal("3000.00"),
            },
        )

        # Garantir que o edital de medicamentos existe e buscar/criar a empresa
        tender_med, _ = Edital.objects.get_or_create(
            numero="000016/25", defaults={"tipo": "Medicamentos"
    }
)
        dora = Fornecedor.objects.get_or_create(
            razao_social="DORA MEDICAMENTOS LTDA EPP",
            cnpj="30.936.479/0001-33",
            email="licitacao@triunfal.com.br",
            telefone="(14) 3413-5243",
            endereco="Avenida Silvio Bertonha, 533, Parque das Indústrias, Marília-SP, CEP 17519-690",
        )

        # Itens – conforme PDF
        ItemLicitado.objects.update_or_create(
    edital=tender_med,
    codigo="006.001.865",
    defaults={
        "fornecedor": dora,
"descricao": "BISACODIL 5MG",
                "unidade": "CPR",
                "quantidade": 5000,
                "valor_unitario": Decimal("0.149"),
                "valor_total": Decimal("745.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=dora,
            codigo="006.001.489",
            defaults={
                "descricao": "CIPROFLOXACINO+HIDROCORTISONA SUSP. OTOLÓGICA",
                "unidade": "FRC",
                "quantidade": 300,
                "valor_unitario": Decimal("18.19"),
                "valor_total": Decimal("5457.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=dora,
            codigo="006.001.666",
            defaults={
                "descricao": "LIRAGLUTIDA SOLUÇÃO INJETÁVEL 6 MG/ML CXS",
                "unidade": "CX",
                "quantidade": 100,
                "valor_unitario": Decimal("314.99"),
                "valor_total": Decimal("31499.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=dora,
            codigo="006.001.211",
            defaults={
                "descricao": "MONONITRATO DE ISOSSORBIDA 40MG",
                "unidade": "CPR",
                "quantidade": 50000,
                "valor_unitario": Decimal("0.41"),
                "valor_total": Decimal("20500.00"),
            },
        )

        ItemLicitado.objects.update_or_create(
            edital=tender_med,
            fornecedor=dora,
            codigo="006.002.357",
            defaults={
                "descricao": "RISPERIDONA 3 MG",
                "unidade": "CPR",
                "quantidade": 6000,
                "valor_unitario": Decimal("0.14"),
                "valor_total": Decimal("840.00"),
            },
        )


# Garantir que o edital de medicamentos existe e buscar/criar a empresa
tender_med, _ = Edital.objects.get_or_create(
    numero="000016/25", defaults={"tipo": "MEDICAMENTOS"
    }
)

comercial_mark, _ = Fornecedor.objects.get_or_create(
    cnpj="09.315.996/0001-07",
    defaults={
        "razao_social": "COMERCIAL MARK ATACADISTA EIRELI",
        "email": "comercialmark@outlook.com,  faturamento.mark@outlook.com, licitacao.mark@outlook.com",
        "telefone": "(44) 3528-5085",
        "endereco": "Rua Presidente Costa e Silva, 231, Centro, Assis Chateaubriand-PR, CEP 85935-000",
    },
)

# Itens – conforme PDF
ItemLicitado.objects.update_or_create(
    edital=tender_med,
    codigo="006.003.353",
    defaults={
        "fornecedor": comercial_mark,
"descricao": "ACEBROFILINA 25MG/5ML",
        "unidade": "UN",
        "quantidade": 3000,
        "valor_unitario": Decimal("4.71"),
        "valor_total": Decimal("14130.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=comercial_mark,
    codigo="006.001.289",
    defaults={
        "descricao": "ACICLOVIR 50MG/G",
        "unidade": "TUB",
        "quantidade": 600,
        "valor_unitario": Decimal("2.36"),
        "valor_total": Decimal("1416.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=comercial_mark,
    codigo="006.001.631",
    defaults={
        "descricao": "ALPRAZOLAM 2 MG",
        "unidade": "CPR",
        "quantidade": 20000,
        "valor_unitario": Decimal("0.12"),
        "valor_total": Decimal("2400.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=comercial_mark,
    codigo="006.001.306",
    defaults={
        "descricao": "AMOX+CLAVULANATO 250MG+62,50MG/5ML",
        "unidade": "FRC",
        "quantidade": 3000,
        "valor_unitario": Decimal("15.65"),
        "valor_total": Decimal("46950.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=comercial_mark,
    codigo="006.001.041",
    defaults={
        "descricao": "AMPICILINA 500MG",
        "unidade": "CAP",
        "quantidade": 2000,
        "valor_unitario": Decimal("0.48"),
        "valor_total": Decimal("960.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=comercial_mark,
    codigo="006.001.859",
    defaults={
        "descricao": "ATORVASTATINA CÁLCICA 20 MG",
        "unidade": "CPR",
        "quantidade": 30000,
        "valor_unitario": Decimal("0.16"),
        "valor_total": Decimal("4800.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=comercial_mark,
    codigo="006.001.860",
    defaults={
        "descricao": "ATORVASTATINA CÁLCICA 40 MG",
        "unidade": "CAP",
        "quantidade": 30000,
        "valor_unitario": Decimal("0.43"),
        "valor_total": Decimal("12900.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=comercial_mark,
    codigo="006.001.634",
    defaults={
        "descricao": "BISOPROLOL 1,25 MG",
        "unidade": "CPR",
        "quantidade": 3000,
        "valor_unitario": Decimal("0.25"),
        "valor_total": Decimal("750.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=comercial_mark,
    codigo="006.001.635",
    defaults={
        "descricao": "BISOPROLOL 2,5 MG",
        "unidade": "CPR",
        "quantidade": 6000,
        "valor_unitario": Decimal("0.28"),
        "valor_total": Decimal("1680.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=comercial_mark,
    codigo="006.001.054",
    defaults={
        "descricao": "BUDESONIDA 32MCG",
        "unidade": "FRC",
        "quantidade": 500,
        "valor_unitario": Decimal("13.20"),
        "valor_total": Decimal("6600.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=comercial_mark,
    codigo="006.001.071",
    defaults={
        "descricao": "CARVEDILOL 12,5 MG",
        "unidade": "CAP",
        "quantidade": 20000,
        "valor_unitario": Decimal("0.08"),
        "valor_total": Decimal("1600.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=comercial_mark,
    codigo="006.001.874",
    defaults={
        "descricao": "CILOSTAZOL 100 MG",
        "unidade": "CPR",
        "quantidade": 10000,
        "valor_unitario": Decimal("0.42"),
        "valor_total": Decimal("4200.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=comercial_mark,
    codigo="006.003.363",
    defaults={
        "descricao": "CLARITROMICINA 250 MG/5ML SUSP.",
        "unidade": "FR",
        "quantidade": 200,
        "valor_unitario": Decimal("56.64"),
        "valor_total": Decimal("11328.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=comercial_mark,
    codigo="006.002.428",
    defaults={
        "descricao": "CLARITROMICINA 500MG",
        "unidade": "CPR",
        "quantidade": 3000,
        "valor_unitario": Decimal("1.70"),
        "valor_total": Decimal("5100.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=comercial_mark,
    codigo="006.001.878",
    defaults={
        "descricao": "CLORIDRATO DE ONDANSETRONA 4 MG",
        "unidade": "CPR",
        "quantidade": 10000,
        "valor_unitario": Decimal("0.25"),
        "valor_total": Decimal("2500.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=comercial_mark,
    codigo="006.001.110",
    defaults={
        "descricao": "CLORIDRATO DE ONDANSETRONA 8MG",
        "unidade": "CPR",
        "quantidade": 10000,
        "valor_unitario": Decimal("0.29"),
        "valor_total": Decimal("2900.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=comercial_mark,
    codigo="006.002.998",
    defaults={
        "descricao": "DESLORATADINA 0,5 MG/ML",
        "unidade": "FRC",
        "quantidade": 1000,
        "valor_unitario": Decimal("6.85"),
        "valor_total": Decimal("6850.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=comercial_mark,
    codigo="006.001.503",
    defaults={
        "descricao": "DEXAMETASONA 4,0 MG",
        "unidade": "CPR",
        "quantidade": 1000,
        "valor_unitario": Decimal("0.18"),
        "valor_total": Decimal("180.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=comercial_mark,
    codigo="006.001.147",
    defaults={
        "descricao": "DIVALPROATO DE SÓDIO 250MG",
        "unidade": "CPR",
        "quantidade": 20000,
        "valor_unitario": Decimal("0.63"),
        "valor_total": Decimal("12600.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=comercial_mark,
    codigo="006.001.888",
    defaults={
        "descricao": "ESCITALOPRAM 20 MG",
        "unidade": "CPR",
        "quantidade": 20000,
        "valor_unitario": Decimal("0.18"),
        "valor_total": Decimal("3600.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=comercial_mark,
    codigo="006.001.365",
    defaults={
        "descricao": "ESPIRONOLACTONA 50 MG",
        "unidade": "CPR",
        "quantidade": 10000,
        "valor_unitario": Decimal("0.31"),
        "valor_total": Decimal("3100.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=comercial_mark,
    codigo="006.003.375",
    defaults={
        "descricao": "FINASTERIDA 5 MG",
        "unidade": "CPR",
        "quantidade": 3000,
        "valor_unitario": Decimal("0.24"),
        "valor_total": Decimal("720.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=comercial_mark,
    codigo="006.003.380",
    defaults={
        "descricao": "GINKO BILOBA 80 MG",
        "unidade": "CPR",
        "quantidade": 10000,
        "valor_unitario": Decimal("0.28"),
        "valor_total": Decimal("2800.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=comercial_mark,
    codigo="006.002.079",
    defaults={
        "descricao": "HIDROCLOROTIAZIDA 25 MG 20 COMP.",
        "unidade": "CPR",
        "quantidade": 100000,
        "valor_unitario": Decimal("0.02"),
        "valor_total": Decimal("2000.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=comercial_mark,
    codigo="006.001.181",
    defaults={
        "descricao": "IVERMECTINA 6 MG",
        "unidade": "CPR",
        "quantidade": 10000,
        "valor_unitario": Decimal("0.30"),
        "valor_total": Decimal("3000.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=comercial_mark,
    codigo="006.003.382",
    defaults={
        "descricao": "LAMOTRIGINA 100 MG CPR",
        "unidade": "CPR",
        "quantidade": 10000,
        "valor_unitario": Decimal("0.18"),
        "valor_total": Decimal("1800.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=comercial_mark,
    codigo="006.001.915",
    defaults={
        "descricao": "MEMANTINA 10 MG",
        "unidade": "CPR",
        "quantidade": 10000,
        "valor_unitario": Decimal("0.18"),
        "valor_total": Decimal("1800.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=comercial_mark,
    codigo="006.001.210",
    defaults={
        "descricao": "MONONITRATO DE ISOSSORBIDA 20MG",
        "unidade": "CPR",
        "quantidade": 50000,
        "valor_unitario": Decimal("0.19"),
        "valor_total": Decimal("9500.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=comercial_mark,
    codigo="006.002.827",
    defaults={
        "descricao": "OLANZAPINA 5 MG",
        "unidade": "CPR",
        "quantidade": 30000,
        "valor_unitario": Decimal("0.27"),
        "valor_total": Decimal("8100.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=comercial_mark,
    codigo="006.001.232",
    defaults={
        "descricao": "PARACETAMOL SOL. ORAL 200MG/ML FRS/15 ML",
        "unidade": "FRC",
        "quantidade": 5000,
        "valor_unitario": Decimal("1.30"),
        "valor_total": Decimal("6500.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=comercial_mark,
    codigo="006.002.968",
    defaults={
        "descricao": "PIOGLITAZONA 30 MG",
        "unidade": "CPR",
        "quantidade": 6000,
        "valor_unitario": Decimal("0.81"),
        "valor_total": Decimal("4860.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=comercial_mark,
    codigo="006.001.418",
    defaults={
        "descricao": "POLIVITAMINICO DO COMPLEXO B GTS",
        "unidade": "FRC",
        "quantidade": 200,
        "valor_unitario": Decimal("2.18"),
        "valor_total": Decimal("436.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=comercial_mark,
    codigo="006.001.423",
    defaults={
        "descricao": "QUETIAPINA 100 MG",
        "unidade": "CPR",
        "quantidade": 20000,
        "valor_unitario": Decimal("0.41"),
        "valor_total": Decimal("8200.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=comercial_mark,
    codigo="006.003.401",
    defaults={
        "descricao": "QUETIAPINA 200 MG",
        "unidade": "CPR",
        "quantidade": 20000,
        "valor_unitario": Decimal("0.79"),
        "valor_total": Decimal("15800.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=comercial_mark,
    codigo="002.001.778",
    defaults={
        "descricao": "RIVAROXABANA 10 MG",
        "unidade": "CPR",
        "quantidade": 20000,
        "valor_unitario": Decimal("0.19"),
        "valor_total": Decimal("3800.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=comercial_mark,
    codigo="002.001.779",
    defaults={
        "descricao": "RIVAROXABANA 15 MG",
        "unidade": "CPR",
        "quantidade": 10000,
        "valor_unitario": Decimal("0.23"),
        "valor_total": Decimal("2300.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=comercial_mark,
    codigo="006.001.254",
    defaults={
        "descricao": "SINVASTATINA 40 MG",
        "unidade": "CPR",
        "quantidade": 20000,
        "valor_unitario": Decimal("0.14"),
        "valor_total": Decimal("2800.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=comercial_mark,
    codigo="006.003.408",
    defaults={
        "descricao": "SULFAMETOXAZOL 200 MG+TRIMETROPIMA 40MG",
        "unidade": "FRC",
        "quantidade": 500,
        "valor_unitario": Decimal("3.38"),
        "valor_total": Decimal("1690.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=comercial_mark,
    codigo="006.001.442",
    defaults={
        "descricao": "TANSULOSINA 0,4 MG",
        "unidade": "CPR",
        "quantidade": 20000,
        "valor_unitario": Decimal("0.65"),
        "valor_total": Decimal("13000.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=comercial_mark,
    codigo="006.003.410",
    defaults={
        "descricao": "TIABENDAZOL 50MG/G",
        "unidade": "TUB",
        "quantidade": 300,
        "valor_unitario": Decimal("7.49"),
        "valor_total": Decimal("2247.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=comercial_mark,
    codigo="006.001.538",
    defaults={
        "descricao": "TOPIRAMATO 100 MG",
        "unidade": "CPR",
        "quantidade": 20000,
        "valor_unitario": Decimal("0.34"),
        "valor_total": Decimal("6800.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=comercial_mark,
    codigo="006.001.540",
    defaults={
        "descricao": "TOPIRAMATO 50 MG",
        "unidade": "CPR",
        "quantidade": 20000,
        "valor_unitario": Decimal("0.21"),
        "valor_total": Decimal("4200.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=comercial_mark,
    codigo="006.001.279",
    defaults={
        "descricao": "VENLAFAXINA 150 MG",
        "unidade": "CAP",
        "quantidade": 20000,
        "valor_unitario": Decimal("0.76"),
        "valor_total": Decimal("15200.00"),
    },
)

# Garantir que o edital de medicamentos existe e buscar/criar a empresa
tender_med, _ = Edital.objects.get_or_create(
    numero="000016/25", defaults={"tipo": "MEDICAMENTOS"
    }
)

interlab, _ = Fornecedor.objects.get_or_create(
    cnpj="43.295.831/0001-40",
    defaults={
        "razao_social": "INTERLAB FARMACEUTICA LTDA",
        "email": "elcio@interlab.com.br",
        "telefone": "(11) 2997-9177 / (11) 2204-5996",
        "endereco": "Av. Água Fria, 981/985, São Paulo-SP, CEP 02333-001",
    },
)

# Itens – 006.001.458 até 006.003.418
ItemLicitado.objects.update_or_create(
    edital=tender_med,
    codigo="006.001.458",
    defaults={
        "fornecedor": interlab,
"descricao": "ÁCIDO TIÓCTICO 600 MG",
        "unidade": "CPR",
        "quantidade": 1000,
        "valor_unitario": Decimal("5.47"),
        "valor_total": Decimal("5470.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=interlab,
    codigo="006.001.484",
    defaults={
        "descricao": "CARBAMAZEPINA CR 400 MG",
        "unidade": "CPR",
        "quantidade": 6000,
        "valor_unitario": Decimal("2.84"),
        "valor_total": Decimal("17040.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=interlab,
    codigo="006.001.495",
    defaults={
        "descricao": "CLORIDRATO DE LURASIDONA 20 MG",
        "unidade": "CPR",
        "quantidade": 6000,
        "valor_unitario": Decimal("4.65"),
        "valor_total": Decimal("27900.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=interlab,
    codigo="006.001.392",
    defaults={
        "descricao": "INSULINA LISPRO HUMALOG KWIK PEN",
        "unidade": "CNT",
        "quantidade": 200,
        "valor_unitario": Decimal("36.05"),
        "valor_total": Decimal("7210.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=interlab,
    codigo="006.003.404",
    defaults={
        "descricao": "SACUBITRIL VALSARTANA 100 MG",
        "unidade": "CPR",
        "quantidade": 20000,
        "valor_unitario": Decimal("4.22"),
        "valor_total": Decimal("84400.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=interlab,
    codigo="006.003.405",
    defaults={
        "descricao": "SACUBITRIL VALSARTANA 50 MG",
        "unidade": "CPR",
        "quantidade": 20000,
        "valor_unitario": Decimal("4.22"),
        "valor_total": Decimal("84400.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=interlab,
    codigo="006.003.406",
    defaults={
        "descricao": "SACUBITRIL VALSARTANA 200 MG",
        "unidade": "CPR",
        "quantidade": 10000,
        "valor_unitario": Decimal("4.22"),
        "valor_total": Decimal("42200.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=interlab,
    codigo="006.003.415",
    defaults={
        "descricao": "VITAMINA D3 1.000 UI",
        "unidade": "CPR",
        "quantidade": 10000,
        "valor_unitario": Decimal("0.23"),
        "valor_total": Decimal("2300.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=interlab,
    codigo="006.003.416",
    defaults={
        "descricao": "VITAMINA D3 10.000 UI",
        "unidade": "CPR",
        "quantidade": 10000,
        "valor_unitario": Decimal("0.42"),
        "valor_total": Decimal("4200.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=interlab,
    codigo="006.003.418",
    defaults={
        "descricao": "VITAMINA D3 5.000 UI",
        "unidade": "CPR",
        "quantidade": 10000,
        "valor_unitario": Decimal("0.24"),
        "valor_total": Decimal("2400.00"),
    },
)

# Garantir que o edital de medicamentos existe e buscar/criar a empresa
tender_med, _ = Edital.objects.get_or_create(
    numero="000016/25", defaults={"tipo": "MEDICAMENTOS"
    }
)

classmed, _ = Fornecedor.objects.get_or_create(
    cnpj="01.328.535/0001-59",
    defaults={
        "razao_social": "CLASSMED PRODUTOS HOSPITALARES LTDA",
        "email": "classmed@outlook.com.br",
        "telefone": "(43) 3275-3105",
        "endereco": "Rua Pica Pau, 1211, Centro, Arapongas-PR, CEP 86700-100",
    },
)

# Itens – conforme edital
ItemLicitado.objects.update_or_create(
    edital=tender_med,
    codigo="006.001.297",
    defaults={
        "fornecedor": classmed,
"descricao": "ÁCIDO TRANEXÂMICO 250MG",
        "unidade": "CPR",
        "quantidade": 3000,
        "valor_unitario": Decimal("1.41"),
        "valor_total": Decimal("4230.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=classmed,
    codigo="006.001.477",
    defaults={
        "descricao": "ÁGUA DESTILADA 300 FRS/1000 ML",
        "unidade": "FRC",
        "quantidade": 300,
        "valor_unitario": Decimal("8.09"),
        "valor_total": Decimal("2427.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=classmed,
    codigo="006.001.036",
    defaults={
        "descricao": "ALPRAZOLAM 1MG",
        "unidade": "CPR",
        "quantidade": 20000,
        "valor_unitario": Decimal("0.079"),
        "valor_total": Decimal("1580.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=classmed,
    codigo="006.001.863",
    defaults={
        "descricao": "BETAMETASONA POMADA 1MG/G",
        "unidade": "TUB",
        "quantidade": 100,
        "valor_unitario": Decimal("8.69"),
        "valor_total": Decimal("869.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=classmed,
    codigo="006.001.461",
    defaults={
        "descricao": "BISOPROLOL 5 MG",
        "unidade": "CPR",
        "quantidade": 10000,
        "valor_unitario": Decimal("0.299"),
        "valor_total": Decimal("2990.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=classmed,
    codigo="006.001.320",
    defaults={
        "descricao": "CARVEDILOL 25MG",
        "unidade": "CAP",
        "quantidade": 30000,
        "valor_unitario": Decimal("0.149"),
        "valor_total": Decimal("4470.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=classmed,
    codigo="006.003.359",
    defaults={
        "descricao": "CEFTRIAXONA 1G I.M",
        "unidade": "FR",
        "quantidade": 600,
        "valor_unitario": Decimal("6.50"),
        "valor_total": Decimal("3900.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=classmed,
    codigo="006.001.082",
    defaults={
        "descricao": "CETOPROFENO 50MG",
        "unidade": "CPR",
        "quantidade": 20000,
        "valor_unitario": Decimal("0.249"),
        "valor_total": Decimal("4980.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=classmed,
    codigo="006.001.088",
    defaults={
        "descricao": "CLORETO DE POTÁSSIO 19,1% AMP/10ML",
        "unidade": "AMP",
        "quantidade": 100,
        "valor_unitario": Decimal("0.46"),
        "valor_total": Decimal("46.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=classmed,
    codigo="006.001.091",
    defaults={
        "descricao": "CLORIDRATO DE AMBROXOL 30 MG/5 ML",
        "unidade": "FRC",
        "quantidade": 3000,
        "valor_unitario": Decimal("2.599"),
        "valor_total": Decimal("7797.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=classmed,
    codigo="006.001.097",
    defaults={
        "descricao": "CLORIDRATO DE CLOMIPRAMINA 25MG",
        "unidade": "CPR",
        "quantidade": 20000,
        "valor_unitario": Decimal("1.099"),
        "valor_total": Decimal("21980.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=classmed,
    codigo="006.001.100",
    defaults={
        "descricao": "CLORIDRATO DE CLORPROMAZINA 25MG",
        "unidade": "CPR",
        "quantidade": 10000,
        "valor_unitario": Decimal("0.38"),
        "valor_total": Decimal("3800.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=classmed,
    codigo="006.003.365",
    defaults={
        "descricao": "CLORIDRATO DE CLORPROMAZINA 40MG SOLUÇÃO/FR",
        "unidade": "FR",
        "quantidade": 100,
        "valor_unitario": Decimal("9.358"),
        "valor_total": Decimal("935.80"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=classmed,
    codigo="006.001.889",
    defaults={
        "descricao": "FENITOINA SÓDICA 50MG/ML IV/IM",
        "unidade": "AMP",
        "quantidade": 50,
        "valor_unitario": Decimal("2.86"),
        "valor_total": Decimal("143.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=classmed,
    codigo="006.001.367",
    defaults={
        "descricao": "FENOBARBITAL 40 MG/ML GOTAS",
        "unidade": "FRC",
        "quantidade": 200,
        "valor_unitario": Decimal("4.439"),
        "valor_total": Decimal("887.80"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=classmed,
    codigo="006.001.380",
    defaults={
        "descricao": "GLICOSE 25% SOLUÇÃO INJETÁVEL AMP/10ML",
        "unidade": "AMP",
        "quantidade": 200,
        "valor_unitario": Decimal("0.62"),
        "valor_total": Decimal("124.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=classmed,
    codigo="006.001.381",
    defaults={
        "descricao": "GLICOSE 50% SOLUÇÃO INJETÁVEL AMP/10ML",
        "unidade": "AMP",
        "quantidade": 200,
        "valor_unitario": Decimal("0.68"),
        "valor_total": Decimal("136.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=classmed,
    codigo="006.001.171",
    defaults={
        "descricao": "HALOPERIDOL 2MG/ML SOL. ORAL FRS/20ML",
        "unidade": "FRC",
        "quantidade": 300,
        "valor_unitario": Decimal("3.739"),
        "valor_total": Decimal("1121.70"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=classmed,
    codigo="006.001.382",
    defaults={
        "descricao": "HALOPERIDOL DECANOATO 70,52MG/ML SOL. INJETÁVEL",
        "unidade": "AMP",
        "quantidade": 200,
        "valor_unitario": Decimal("6.399"),
        "valor_total": Decimal("1279.80"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=classmed,
    codigo="006.001.386",
    defaults={
        "descricao": "HIDRÓXIDO DE ALUMÍNIO 60 MG/ML SUSP. FRS/100ML",
        "unidade": "FRC",
        "quantidade": 600,
        "valor_unitario": Decimal("2.479"),
        "valor_total": Decimal("1487.40"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=classmed,
    codigo="006.001.200",
    defaults={
        "descricao": "LORAZEPAM 2 MG",
        "unidade": "CPR",
        "quantidade": 10000,
        "valor_unitario": Decimal("0.139"),
        "valor_total": Decimal("1390.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=classmed,
    codigo="006.001.670",
    defaults={
        "descricao": "METILFENIDATO 10 MG",
        "unidade": "CPR",
        "quantidade": 20000,
        "valor_unitario": Decimal("0.33"),
        "valor_total": Decimal("6600.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=classmed,
    codigo="006.001.917",
    defaults={
        "descricao": "MIRTAZAPINA 30 MG",
        "unidade": "CPR",
        "quantidade": 10000,
        "valor_unitario": Decimal("0.65"),
        "valor_total": Decimal("6500.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=classmed,
    codigo="006.001.212",
    defaults={
        "descricao": "MONONITRATO DE ISOSSORBIDA 5MG SL",
        "unidade": "CPR",
        "quantidade": 3000,
        "valor_unitario": Decimal("0.35"),
        "valor_total": Decimal("1050.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=classmed,
    codigo="006.001.921",
    defaults={
        "descricao": "NALTREXONA 50 MG",
        "unidade": "CPR",
        "quantidade": 20000,
        "valor_unitario": Decimal("4.03"),
        "valor_total": Decimal("80600.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=classmed,
    codigo="006.001.925",
    defaults={
        "descricao": "NITRATO DE MICONAZOL CREME VAGINAL",
        "unidade": "TUB",
        "quantidade": 300,
        "valor_unitario": Decimal("9.499"),
        "valor_total": Decimal("2849.70"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=classmed,
    codigo="006.001.412",
    defaults={
        "descricao": "OLEO MINERAL 100 ML",
        "unidade": "FRC",
        "quantidade": 600,
        "valor_unitario": Decimal("3.129"),
        "valor_total": Decimal("1877.40"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=classmed,
    codigo="006.001.234",
    defaults={
        "descricao": "PENTOXIFILINA 400MG",
        "unidade": "CPR",
        "quantidade": 10000,
        "valor_unitario": Decimal("1.899"),
        "valor_total": Decimal("18990.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=classmed,
    codigo="006.001.246",
    defaults={
        "descricao": "RIVAROXABANA 20 MG",
        "unidade": "CPR",
        "quantidade": 20000,
        "valor_unitario": Decimal("0.279"),
        "valor_total": Decimal("5580.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=classmed,
    codigo="006.003.402",
    defaults={
        "descricao": "ROSUVASTATINA 20 MG",
        "unidade": "CPR",
        "quantidade": 60000,
        "valor_unitario": Decimal("0.24"),
        "valor_total": Decimal("14400.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=classmed,
    codigo="006.001.434",
    defaults={
        "descricao": "SOL. GLICOSADA 5% S.F - I.V FRS/500 ML",
        "unidade": "FRC",
        "quantidade": 200,
        "valor_unitario": Decimal("5.107"),
        "valor_total": Decimal("1021.40"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=classmed,
    codigo="006.001.262",
    defaults={
        "descricao": "SOLUÇÃO RINGER SEM LACTATO FRS/500 ML",
        "unidade": "FRC",
        "quantidade": 200,
        "valor_unitario": Decimal("4.899"),
        "valor_total": Decimal("979.80"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=classmed,
    codigo="006.001.263",
    defaults={
        "descricao": "SUCCINATO DE METOPROLOL 25 MG",
        "unidade": "CPR",
        "quantidade": 30000,
        "valor_unitario": Decimal("0.249"),
        "valor_total": Decimal("7470.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=classmed,
    codigo="006.001.264",
    defaults={
        "descricao": "SUCCINATO DE METOPROLOL 50 MG",
        "unidade": "CPR",
        "quantidade": 50000,
        "valor_unitario": Decimal("0.41"),
        "valor_total": Decimal("20500.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=classmed,
    codigo="006.001.938",
    defaults={
        "descricao": "SULFATO DE MORFINA 10 MG",
        "unidade": "CPR",
        "quantidade": 3000,
        "valor_unitario": Decimal("0.84"),
        "valor_total": Decimal("2520.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=classmed,
    codigo="006.003.411",
    defaults={
        "descricao": "TIAMAZOL 10 MG",
        "unidade": "CPR",
        "quantidade": 5000,
        "valor_unitario": Decimal("0.489"),
        "valor_total": Decimal("2445.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=classmed,
    codigo="006.003.412",
    defaults={
        "descricao": "TIAMAZOL 5 MG",
        "unidade": "CPR",
        "quantidade": 3000,
        "valor_unitario": Decimal("0.26"),
        "valor_total": Decimal("780.00"),
    },
)

# Garantir que o edital de medicamentos existe e buscar/criar a empresa
tender_med, _ = Edital.objects.get_or_create(
    numero="000016/25", defaults={"tipo": "MEDICAMENTOS"
    }
)

soma_sp, _ = Fornecedor.objects.get_or_create(
    cnpj="05.847.630/0001-20",
    defaults={
        "razao_social": "SOMA/SP PRODUTOS HOSPITALARES LTDA",
        "email": "soma.sp@somahospitalar.com.br",
        "telefone": "(11) 4122-9800",
        "endereco": "Estrada Samuel Aizemberg, 100, Bairro Alves Dias, São Bernardo do Campo-SP, CEP 09851-550",
    },
)

# Itens – conforme edital
ItemLicitado.objects.update_or_create(
    edital=tender_med,
    codigo="006.001.291",
    defaults={
        "fornecedor": soma_sp,
"descricao": "ÁCIDO ASCÓRBICO 100MG/ML",
        "unidade": "AMP",
        "quantidade": 2000,
        "valor_unitario": Decimal("0.74"),
        "valor_total": Decimal("1480.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.295",
    defaults={
        "descricao": "ÁCIDO FÓLICO 5MG",
        "unidade": "CPR",
        "quantidade": 5000,
        "valor_unitario": Decimal("0.03"),
        "valor_total": Decimal("150.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.298",
    defaults={
        "descricao": "ÁCIDO TRANEXÂMICO 250MG SOLUÇÃO INJETÁVEL",
        "unidade": "AMP",
        "quantidade": 1000,
        "valor_unitario": Decimal("3.90"),
        "valor_total": Decimal("3900.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.459",
    defaults={
        "descricao": "ÁGUA P/INJEÇÃO",
        "unidade": "FRC",
        "quantidade": 5000,
        "valor_unitario": Decimal("0.195"),
        "valor_total": Decimal("975.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.031",
    defaults={
        "descricao": "ALBENDAZOL 400MG",
        "unidade": "CPR",
        "quantidade": 3000,
        "valor_unitario": Decimal("0.439"),
        "valor_total": Decimal("1317.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.032",
    defaults={
        "descricao": "ALBENDAZOL 40MG/ML FRS/10ML",
        "unidade": "FRC",
        "quantidade": 3000,
        "valor_unitario": Decimal("1.11"),
        "valor_total": Decimal("3330.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.011",
    defaults={
        "descricao": "ALOPURINOL 300MG",
        "unidade": "CPR",
        "quantidade": 30000,
        "valor_unitario": Decimal("0.23"),
        "valor_total": Decimal("6900.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.857",
    defaults={
        "descricao": "AMOXICILINA 500 MG",
        "unidade": "CAP",
        "quantidade": 20000,
        "valor_unitario": Decimal("0.20"),
        "valor_total": Decimal("4000.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.481",
    defaults={
        "descricao": "ARIPIPRAZOL 10 MG",
        "unidade": "CPR",
        "quantidade": 10000,
        "valor_unitario": Decimal("0.395"),
        "valor_total": Decimal("3950.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.632",
    defaults={
        "descricao": "ARIPIPRAZOL 15 MG",
        "unidade": "CPR",
        "quantidade": 60000,
        "valor_unitario": Decimal("0.40"),
        "valor_total": Decimal("24000.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.048",
    defaults={
        "descricao": "BROMETO DE IPRATROPIO 0,250MG/ML FRS/20 ML",
        "unidade": "FRC",
        "quantidade": 500,
        "valor_unitario": Decimal("1.00"),
        "valor_total": Decimal("500.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.053",
    defaults={
        "descricao": "BROMOPRIDA 4MG/ML FRS/20ML",
        "unidade": "FRC",
        "quantidade": 2000,
        "valor_unitario": Decimal("2.00"),
        "valor_total": Decimal("4000.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.313",
    defaults={
        "descricao": "BROMOPRIDA 5MG/ML SOLUÇÃO INJETÁVEL",
        "unidade": "AMP",
        "quantidade": 2000,
        "valor_unitario": Decimal("1.15"),
        "valor_total": Decimal("2300.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.315",
    defaults={
        "descricao": "BUTIL BROMETO DE ESCOPOLAMINA 6,67MG/ML",
        "unidade": "FRC",
        "quantidade": 500,
        "valor_unitario": Decimal("5.50"),
        "valor_total": Decimal("2750.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.060",
    defaults={
        "descricao": "BUTILBROMETO DE ESCOPOLAMINA 20MG/ML",
        "unidade": "AMP",
        "quantidade": 1000,
        "valor_unitario": Decimal("1.00"),
        "valor_total": Decimal("1000.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.316",
    defaults={
        "descricao": "BUTILBROMETO DE ESCOPOLAMINA + DIPIRONA",
        "unidade": "AMP",
        "quantidade": 1000,
        "valor_unitario": Decimal("1.42"),
        "valor_total": Decimal("1420.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.002.165",
    defaults={
        "descricao": "CARBAMAZEPINA 200 MG",
        "unidade": "CPR",
        "quantidade": 20000,
        "valor_unitario": Decimal("0.16"),
        "valor_total": Decimal("3200.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.064",
    defaults={
        "descricao": "CARBAMAZEPINA 20MG/ML SUSP.ORAL FRS/100ML",
        "unidade": "FRC",
        "quantidade": 500,
        "valor_unitario": Decimal("7.00"),
        "valor_total": Decimal("3500.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.003.358",
    defaults={
        "descricao": "CARBOCISTEÍNA 20 MG/ML XPE",
        "unidade": "FR",
        "quantidade": 1000,
        "valor_unitario": Decimal("3.30"),
        "valor_total": Decimal("3300.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.003.357",
    defaults={
        "descricao": "CARBOCISTEÍNA 50 MG/ML XPE",
        "unidade": "FR",
        "quantidade": 1000,
        "valor_unitario": Decimal("4.55"),
        "valor_total": Decimal("4550.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.070",
    defaults={
        "descricao": "CARBONATO DE CÁLCIO 600MG; COLECALCIFEROL 400MG",
        "unidade": "CPR",
        "quantidade": 20000,
        "valor_unitario": Decimal("0.05"),
        "valor_total": Decimal("1000.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.002.336",
    defaults={
        "descricao": "CARBONATO DE LÍTIO 300MG",
        "unidade": "CPR",
        "quantidade": 6000,
        "valor_unitario": Decimal("0.21"),
        "valor_total": Decimal("1260.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.638",
    defaults={
        "descricao": "CARMELOSE SÓDICA 5MG/ML SOL. OFT.",
        "unidade": "FRC",
        "quantidade": 300,
        "valor_unitario": Decimal("6.95"),
        "valor_total": Decimal("2085.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.486",
    defaults={
        "descricao": "CEFALEXINA 250 MG SUSP.",
        "unidade": "FRC",
        "quantidade": 600,
        "valor_unitario": Decimal("10.00"),
        "valor_total": Decimal("6000.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.487",
    defaults={
        "descricao": "CEFTRIAXONA 1G I.V",
        "unidade": "FRC",
        "quantidade": 600,
        "valor_unitario": Decimal("4.40"),
        "valor_total": Decimal("2640.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.321",
    defaults={
        "descricao": "CETOCONAZOL CREME 20MG/G",
        "unidade": "TUB",
        "quantidade": 1000,
        "valor_unitario": Decimal("2.80"),
        "valor_total": Decimal("2800.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.323",
    defaults={
        "descricao": "CETOPROFENO 50MG/ML - I.M SOLUÇÃO INJETÁVEL",
        "unidade": "AMP",
        "quantidade": 5000,
        "valor_unitario": Decimal("1.18"),
        "valor_total": Decimal("5900.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.003.361",
    defaults={
        "descricao": "CIANOCOBALAMINA 2500 MCG/ML",
        "unidade": "AMP",
        "quantidade": 3000,
        "valor_unitario": Decimal("6.80"),
        "valor_total": Decimal("20400.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.330",
    defaults={
        "descricao": "CLONAZEPAM 2.5 MG/ML GOTAS",
        "unidade": "FRC",
        "quantidade": 200,
        "valor_unitario": Decimal("2.12"),
        "valor_total": Decimal("424.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.096",
    defaults={
        "descricao": "CLORIDRATO DE CIPROFLOXACINO 500MG",
        "unidade": "CPR",
        "quantidade": 20000,
        "valor_unitario": Decimal("0.16"),
        "valor_total": Decimal("3200.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.103",
    defaults={
        "descricao": "CLORIDRATO DE LIDOCAÍNA S/V 2% FRS/20ML",
        "unidade": "FRC",
        "quantidade": 200,
        "valor_unitario": Decimal("3.83"),
        "valor_total": Decimal("766.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.002.991",
    defaults={
        "descricao": "CLORIDRATO DE METFORMINA 500 MG XR",
        "unidade": "CPR",
        "quantidade": 100000,
        "valor_unitario": Decimal("0.15"),
        "valor_total": Decimal("15000.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.106",
    defaults={
        "descricao": "CLORIDRATO DE METFORMINA 850 MG",
        "unidade": "CPR",
        "quantidade": 100000,
        "valor_unitario": Decimal("0.109"),
        "valor_total": Decimal("10900.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.117",
    defaults={
        "descricao": "CLORIDRATO DE SERTRALINA 50MG",
        "unidade": "CPR",
        "quantidade": 30000,
        "valor_unitario": Decimal("0.10"),
        "valor_total": Decimal("3000.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.119",
    defaults={
        "descricao": "CLORIDRATO DE TIAMINA 300MG",
        "unidade": "CPR",
        "quantidade": 30000,
        "valor_unitario": Decimal("0.24"),
        "valor_total": Decimal("7200.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.120",
    defaults={
        "descricao": "CLORIDRATO DE TRAMADOL 50 MG",
        "unidade": "CPR",
        "quantidade": 30000,
        "valor_unitario": Decimal("0.12"),
        "valor_total": Decimal("3600.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.122",
    defaults={
        "descricao": "CLORIDRATO DE PROPAFENONA 300MG",
        "unidade": "CPR",
        "quantidade": 6000,
        "valor_unitario": Decimal("0.559"),
        "valor_total": Decimal("3354.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.883",
    defaults={
        "descricao": "DEXAMETASONA 1MG/G CREME",
        "unidade": "TUB",
        "quantidade": 1000,
        "valor_unitario": Decimal("1.65"),
        "valor_total": Decimal("1650.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.130",
    defaults={
        "descricao": "DEXAMETASONA 2MG/ML, FOSFATO DISSÓDICO",
        "unidade": "AMP",
        "quantidade": 5000,
        "valor_unitario": Decimal("0.70"),
        "valor_total": Decimal("3500.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.133",
    defaults={
        "descricao": "DIAZEPAM 5MG/ML AMP/2ML",
        "unidade": "AMP",
        "quantidade": 200,
        "valor_unitario": Decimal("0.78"),
        "valor_total": Decimal("156.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.134",
    defaults={
        "descricao": "DICLOFENACO SÓDICO 50 MG",
        "unidade": "CAP",
        "quantidade": 30000,
        "valor_unitario": Decimal("0.05"),
        "valor_total": Decimal("1500.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.145",
    defaults={
        "descricao": "DIPIRONA SÓDICA 500MG/ML FRS/10 ML",
        "unidade": "FRC",
        "quantidade": 10000,
        "valor_unitario": Decimal("1.17"),
        "valor_total": Decimal("11700.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.357",
    defaults={
        "descricao": "DIPIRONA SÓDICA 500MG/ML SOLUÇÃO INJETÁVEL",
        "unidade": "AMP",
        "quantidade": 5000,
        "valor_unitario": Decimal("0.65"),
        "valor_total": Decimal("3250.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.003.372",
    defaults={
        "descricao": "ENOXAPARINA SÓDICA 40 MG/0,4 ML",
        "unidade": "UN",
        "quantidade": 600,
        "valor_unitario": Decimal("13.90"),
        "valor_total": Decimal("8340.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.363",
    defaults={
        "descricao": "EPINEFRINA 1MG/ML",
        "unidade": "AMP",
        "quantidade": 300,
        "valor_unitario": Decimal("1.00"),
        "valor_total": Decimal("300.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.002.190",
    defaults={
        "descricao": "FLUCONAZOL 150MG",
        "unidade": "CAP",
        "quantidade": 10000,
        "valor_unitario": Decimal("0.43"),
        "valor_total": Decimal("4300.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.374",
    defaults={
        "descricao": "FOSFATO SÓDICO DE PREDNISOLONA 3 MG/ML",
        "unidade": "FRC",
        "quantidade": 5000,
        "valor_unitario": Decimal("4.00"),
        "valor_total": Decimal("20000.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.375",
    defaults={
        "descricao": "FUROSEMIDA 10 MG/ML",
        "unidade": "AMP",
        "quantidade": 1000,
        "valor_unitario": Decimal("0.64"),
        "valor_total": Decimal("640.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.003.379",
    defaults={
        "descricao": "GENTAMICINA 40 MG/ML",
        "unidade": "AMP",
        "quantidade": 200,
        "valor_unitario": Decimal("1.00"),
        "valor_total": Decimal("200.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.383",
    defaults={
        "descricao": "HIDROCORTISONA 500 MG I.M/I.V",
        "unidade": "FRC",
        "quantidade": 600,
        "valor_unitario": Decimal("4.50"),
        "valor_total": Decimal("2700.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.002.194",
    defaults={
        "descricao": "IBUPROFENO 600 MG",
        "unidade": "CPR",
        "quantidade": 100000,
        "valor_unitario": Decimal("0.13"),
        "valor_total": Decimal("13000.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.003.383",
    defaults={
        "descricao": "LAMOTRIGINA 25 MG CP",
        "unidade": "CPR",
        "quantidade": 10000,
        "valor_unitario": Decimal("0.129"),
        "valor_total": Decimal("1290.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.003.384",
    defaults={
        "descricao": "LAMOTRIGINA 50 MG CPR",
        "unidade": "CPR",
        "quantidade": 10000,
        "valor_unitario": Decimal("0.169"),
        "valor_total": Decimal("1690.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.003.387",
    defaults={
        "descricao": "LORATADINA 1 MG/ML XAROPE",
        "unidade": "FRC",
        "quantidade": 6000,
        "valor_unitario": Decimal("2.82"),
        "valor_total": Decimal("16920.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.672",
    defaults={
        "descricao": "MIRTAZAPINA 45 MG",
        "unidade": "CPR",
        "quantidade": 10000,
        "valor_unitario": Decimal("0.889"),
        "valor_total": Decimal("8890.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.219",
    defaults={
        "descricao": "NISTATINA CR. VG 25.000 UI/G TBS 60G",
        "unidade": "TUB",
        "quantidade": 1000,
        "valor_unitario": Decimal("6.24"),
        "valor_total": Decimal("6240.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.220",
    defaults={
        "descricao": "NISTATINA SUSP. ORAL 100.000 UI/ML FRS/50 ML",
        "unidade": "FRC",
        "quantidade": 300,
        "valor_unitario": Decimal("4.95"),
        "valor_total": Decimal("1485.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.002.206",
    defaults={
        "descricao": "NORFLOXACINO 400 MG",
        "unidade": "CPR",
        "quantidade": 10000,
        "valor_unitario": Decimal("0.309"),
        "valor_total": Decimal("3090.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.003.390",
    defaults={
        "descricao": "OMEPRAZOL SÓDICO 40 MG C/ DILUENTE DE 20 MG",
        "unidade": "FRC",
        "quantidade": 500,
        "valor_unitario": Decimal("8.70"),
        "valor_total": Decimal("4350.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.417",
    defaults={
        "descricao": "PARACETAMOL 500 MG",
        "unidade": "CPR",
        "quantidade": 30000,
        "valor_unitario": Decimal("0.06"),
        "valor_total": Decimal("1800.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.239",
    defaults={
        "descricao": "POLIVITAMINICO DO COMPLEXO B AMP/2ML",
        "unidade": "AMP",
        "quantidade": 5000,
        "valor_unitario": Decimal("0.98"),
        "valor_total": Decimal("4900.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.002.192",
    defaults={
        "descricao": "PREDNISONA 20 MG",
        "unidade": "CPR",
        "quantidade": 30000,
        "valor_unitario": Decimal("0.15"),
        "valor_total": Decimal("4500.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.421",
    defaults={
        "descricao": "PREGABALINA 75 MG",
        "unidade": "CPR",
        "quantidade": 30000,
        "valor_unitario": Decimal("0.209"),
        "valor_total": Decimal("6270.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.002.208",
    defaults={
        "descricao": "RISPERIDONA 1 MG",
        "unidade": "CPR",
        "quantidade": 30000,
        "valor_unitario": Decimal("0.09"),
        "valor_total": Decimal("2700.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.002.209",
    defaults={
        "descricao": "RISPERIDONA 2 MG",
        "unidade": "CPR",
        "quantidade": 30000,
        "valor_unitario": Decimal("0.10"),
        "valor_total": Decimal("3000.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.428",
    defaults={
        "descricao": "SACARATO DE HIDRÓXIDO FÉRRICO 20 MG/ML I.V",
        "unidade": "AMP",
        "quantidade": 1000,
        "valor_unitario": Decimal("10.20"),
        "valor_total": Decimal("10200.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.432",
    defaults={
        "descricao": "SOL. CLORETO DE SÓDIO 0,9% S.F - I.V FRS/100 ML",
        "unidade": "FRC",
        "quantidade": 5000,
        "valor_unitario": Decimal("3.20"),
        "valor_total": Decimal("16000.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.001.260",
    defaults={
        "descricao": "SOL. CLORETO DE SÓDIO 0,9% FRS/10 ML",
        "unidade": "FRC",
        "quantidade": 2000,
        "valor_unitario": Decimal("0.20"),
        "valor_total": Decimal("400.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.002.972",
    defaults={
        "descricao": "SULFATO DE SALBUTAMOL 100 MCG/DOSE AEROSOL",
        "unidade": "FRC",
        "quantidade": 300,
        "valor_unitario": Decimal("10.99"),
        "valor_total": Decimal("3297.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.002.977",
    defaults={
        "descricao": "TOBRAMICINA 3 MG/ML SOL. OFTÁLMICA",
        "unidade": "FRC",
        "quantidade": 300,
        "valor_unitario": Decimal("4.50"),
        "valor_total": Decimal("1350.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=soma_sp,
    codigo="006.003.419",
    defaults={
        "descricao": "VITAMINA D3 7.000 UI",
        "unidade": "CPR",
        "quantidade": 10000,
        "valor_unitario": Decimal("0.18"),
        "valor_total": Decimal("1800.00"),
    },
)

# Garantir que o edital de medicamentos existe e criar/buscar a empresa
tender_med, _ = Edital.objects.get_or_create(
    numero="000016/25", defaults={"tipo": "MEDICAMENTOS"
    }
)

dimaster, _ = Fornecedor.objects.get_or_create(
    cnpj="02.520.829/0004-93",
    defaults={
        "razao_social": "DIMASTER - COMERCIO DE PRODUTOS HOSPITALARES LTDA",
        "email": "pregao@dimaster.com.br, licitacao2@dimaster.com.br, faturamento@dimaster.com.br",
        "telefone": "(054) 3523-2600",
        "endereco": "Av. Cumbica, nº 429, Bairro Cidade Industrial de São Paulo, Guarulhos-SP, CEP 07223-300",
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=dimaster,
    codigo="006.001.851",
    defaults={
        "descricao": "ACETILCISTEINA 40MG/ML XAROPE",
        "unidade": "FRC",
        "quantidade": 1000,
        "valor_unitario": Decimal("4.37"),
        "valor_total": Decimal("4370.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=dimaster,
    codigo="006.002.213",
    defaults={
        "descricao": "ACICLOVIR 200MG",
        "unidade": "CPR",
        "quantidade": 10000,
        "valor_unitario": Decimal("0.169"),
        "valor_total": Decimal("1690.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=dimaster,
    codigo="006.001.027",
    defaults={
        "descricao": "ÁCIDO URSODESOXICÓLICO 300 MG",
        "unidade": "CPR",
        "quantidade": 2000,
        "valor_unitario": Decimal("1.60"),
        "valor_total": Decimal("3200.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=dimaster,
    codigo="006.002.215",
    defaults={
        "descricao": "AMIODARONA 200MG",
        "unidade": "CPR",
        "quantidade": 20000,
        "valor_unitario": Decimal("0.35"),
        "valor_total": Decimal("7000.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=dimaster,
    codigo="006.001.040",
    defaults={
        "descricao": "AMOX+CLAVULANATO POTÁSSIO 500 MG+125 MG",
        "unidade": "CAP",
        "quantidade": 30000,
        "valor_unitario": Decimal("1.00"),
        "valor_total": Decimal("30000.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=dimaster,
    codigo="006.001.855",
    defaults={
        "descricao": "AMOXICILINA + CLAVULANATO 872 MG+125 MG",
        "unidade": "CPR",
        "quantidade": 50000,
        "valor_unitario": Decimal("1.80"),
        "valor_total": Decimal("90000.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=dimaster,
    codigo="006.001.856",
    defaults={
        "descricao": "AMOXICILINA 250MG/5ML SUSP.",
        "unidade": "FRC",
        "quantidade": 1000,
        "valor_unitario": Decimal("5.40"),
        "valor_total": Decimal("5400.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=dimaster,
    codigo="006.003.355",
    defaults={
        "descricao": "AXETILCEFUROXIMA 250 MG",
        "unidade": "CPR",
        "quantidade": 3000,
        "valor_unitario": Decimal("2.59"),
        "valor_total": Decimal("7770.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=dimaster,
    codigo="006.003.356",
    defaults={
        "descricao": "AXETILCEFUROXIMA 500 MG",
        "unidade": "CPR",
        "quantidade": 3000,
        "valor_unitario": Decimal("3.54"),
        "valor_total": Decimal("10620.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=dimaster,
    codigo="006.001.043",
    defaults={
        "descricao": "AZITROMICINA 200MG/5ML SUSP. FRS/15ML",
        "unidade": "FRC",
        "quantidade": 3000,
        "valor_unitario": Decimal("7.07"),
        "valor_total": Decimal("21210.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=dimaster,
    codigo="006.001.047",
    defaults={
        "descricao": "BISSULFATO DE CLOPIDOGREL 75 MG",
        "unidade": "CPR",
        "quantidade": 20000,
        "valor_unitario": Decimal("0.24"),
        "valor_total": Decimal("4800.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=dimaster,
    codigo="006.001.050",
    defaults={
        "descricao": "BROMIDRATO DE CITALOPRAM 20MG",
        "unidade": "CPR",
        "quantidade": 20000,
        "valor_unitario": Decimal("0.099"),
        "valor_total": Decimal("1980.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=dimaster,
    codigo="006.001.057",
    defaults={
        "descricao": "BUPROPIONA LIBERAÇÃO PROLONGADA 150 MG",
        "unidade": "CPR",
        "quantidade": 30000,
        "valor_unitario": Decimal("0.36"),
        "valor_total": Decimal("10800.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=dimaster,
    codigo="006.001.059",
    defaults={
        "descricao": "BUTILBROMETO DE ESCOPALAMINA 10 MG, DIPIRONA 250 MG",
        "unidade": "CPR",
        "quantidade": 30000,
        "valor_unitario": Decimal("0.25"),
        "valor_total": Decimal("7500.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=dimaster,
    codigo="006.001.085",
    defaults={
        "descricao": "CINARIZINA 75 MG",
        "unidade": "CPR",
        "quantidade": 10000,
        "valor_unitario": Decimal("0.32"),
        "valor_total": Decimal("3200.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=dimaster,
    codigo="006.001.087",
    defaults={
        "descricao": "CLONAZEPAM 2MG",
        "unidade": "CPR",
        "quantidade": 60000,
        "valor_unitario": Decimal("0.049"),
        "valor_total": Decimal("2940.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=dimaster,
    codigo="006.000.902",
    defaults={
        "descricao": "DIPIRONA 500 MG",
        "unidade": "CPR",
        "quantidade": 200000,
        "valor_unitario": Decimal("0.11"),
        "valor_total": Decimal("22000.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=dimaster,
    codigo="006.002.649",
    defaults={
        "descricao": "DONEPEZILA 10 MG",
        "unidade": "CPR",
        "quantidade": 3000,
        "valor_unitario": Decimal("0.35"),
        "valor_total": Decimal("1050.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=dimaster,
    codigo="006.001.887",
    defaults={
        "descricao": "DONEPEZILA 5 MG",
        "unidade": "CPR",
        "quantidade": 2000,
        "valor_unitario": Decimal("0.30"),
        "valor_total": Decimal("600.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=dimaster,
    codigo="006.001.364",
    defaults={
        "descricao": "ESOMEPRAZOL MAGNÉSICO 40 MG",
        "unidade": "CPR",
        "quantidade": 6000,
        "valor_unitario": Decimal("1.00"),
        "valor_total": Decimal("6000.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=dimaster,
    codigo="006.001.169",
    defaults={
        "descricao": "GLICLAZIDA 30MG LIBERAÇÃO PROLONGADA",
        "unidade": "CPR",
        "quantidade": 200000,
        "valor_unitario": Decimal("0.12"),
        "valor_total": Decimal("24000.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=dimaster,
    codigo="006.001.393",
    defaults={
        "descricao": "LACTULOSE 667MG/ML",
        "unidade": "FRC",
        "quantidade": 1000,
        "valor_unitario": Decimal("3.69"),
        "valor_total": Decimal("3690.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=dimaster,
    codigo="006.002.277",
    defaults={
        "descricao": "LEVOMEPROMAZINA 100MG",
        "unidade": "CPR",
        "quantidade": 20000,
        "valor_unitario": Decimal("0.62"),
        "valor_total": Decimal("12400.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=dimaster,
    codigo="006.001.215",
    defaults={
        "descricao": "NIFEDIPINO 20MG",
        "unidade": "CPR",
        "quantidade": 20000,
        "valor_unitario": Decimal("0.09"),
        "valor_total": Decimal("1800.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=dimaster,
    codigo="006.001.226",
    defaults={
        "descricao": "OXCARBAZEPINA 300MG",
        "unidade": "CPR",
        "quantidade": 10000,
        "valor_unitario": Decimal("0.67"),
        "valor_total": Decimal("6700.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=dimaster,
    codigo="006.001.233",
    defaults={
        "descricao": "PARACETAMOL+FOSFATO DE CODEINA 500/30MG",
        "unidade": "CPR",
        "quantidade": 50000,
        "valor_unitario": Decimal("0.34"),
        "valor_total": Decimal("17000.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=dimaster,
    codigo="006.001.425",
    defaults={
        "descricao": "RIFAMICINA SPRAY",
        "unidade": "FRC",
        "quantidade": 1000,
        "valor_unitario": Decimal("4.14"),
        "valor_total": Decimal("4140.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=dimaster,
    codigo="006.001.430",
    defaults={
        "descricao": "SOL. CLORETO DE SÓDIO 0,9% S.F - I.V FRS/250 ML",
        "unidade": "FRC",
        "quantidade": 5000,
        "valor_unitario": Decimal("3.80"),
        "valor_total": Decimal("19000.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=dimaster,
    codigo="006.001.431",
    defaults={
        "descricao": "SOL. CLORETO DE SÓDIO 0,9% S.F - I.V FRS/500 ML",
        "unidade": "FRC",
        "quantidade": 5000,
        "valor_unitario": Decimal("4.37"),
        "valor_total": Decimal("21850.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=dimaster,
    codigo="006.001.265",
    defaults={
        "descricao": "SULFADIAZINA DE PRATA CREME 10 MG/G TBS 50 G",
        "unidade": "TUB",
        "quantidade": 1000,
        "valor_unitario": Decimal("6.48"),
        "valor_total": Decimal("6840.00"),
    },
)

ItemLicitado.objects.update_or_create(
    edital=tender_med,
    fornecedor=dimaster,
    codigo="006.001.280",
    defaults={
        "descricao": "VENLAFAXINA 75 MG",
        "unidade": "CPR",
        "quantidade": 30000,
        "valor_unitario": Decimal("0.339"),
        "valor_total": Decimal("10170.00"),
    },
)
