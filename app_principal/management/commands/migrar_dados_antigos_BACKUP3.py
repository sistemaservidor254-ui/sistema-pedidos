# Garantir que o edital existe
tender_enf = Tender.objects.get_or_create(number="000027/25", kind="Itens de Enfermagem")[0]

# Empresa LUMAR
lumar = Company.objects.get_or_create(
    name="LUMAR COMÉRCIO DE PRODUTOS FARMACÊUTICOS LTDA",
    cnpj="49.228.695/0001-52",
    email="licitacoes@lumarfranca.com.br",
    phone="(16) 3721-1102",
    address="Av. Wilson Bego, 745, Bairro Distrito Industrial Antônio Della Torres, Franca-SP, CEP 14406-091"
)[0]

# Itens da LUMAR – Parte 1
Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.004",
        description="AGULHA 13/4.5 CX 100",
        kind="Itens de Enfermagem",
        unit="CX"
    ),
    qty_awarded=300,
    unit_price=Decimal("6.83"),
    total_price=Decimal("2049.00")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.005",
        description="AGULHA 25/7 CX 100",
        kind="Itens de Enfermagem",
        unit="CX"
    ),
    qty_awarded=200,
    unit_price=Decimal("6.83"),
    total_price=Decimal("1366.00")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.007",
        description="AGULHA 30/7 100 CX",
        kind="Itens de Enfermagem",
        unit="CX"
    ),
    qty_awarded=500,
    unit_price=Decimal("6.83"),
    total_price=Decimal("3415.00")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.008",
        description="AGULHA 30/8 100 CX",
        kind="Itens de Enfermagem",
        unit="CX"
    ),
    qty_awarded=500,
    unit_price=Decimal("6.83"),
    total_price=Decimal("3415.00")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.009",
        description="AGULHA 40/12 CX 100",
        kind="Itens de Enfermagem",
        unit="CX"
    ),
    qty_awarded=500,
    unit_price=Decimal("7.799"),
    total_price=Decimal("3899.50")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.010",
        description="ALCOOL 70% 1L",
        kind="Itens de Enfermagem",
        unit="LT"
    ),
    qty_awarded=1000,
    unit_price=Decimal("5.40"),
    total_price=Decimal("5400.00")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.076",
        description="ALGODÃO 500 G",
        kind="Itens de Enfermagem",
        unit="ROLO"
    ),
    qty_awarded=500,
    unit_price=Decimal("13.40"),
    total_price=Decimal("6700.00")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.011",
        description="ALMOTOLIA COR ÂMBAR 125 ML",
        kind="Itens de Enfermagem",
        unit="UNI"
    ),
    qty_awarded=100,
    unit_price=Decimal("2.50"),
    total_price=Decimal("250.00")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.012",
        description="ALMOTOLIA TRANSPARENTE 125 ML",
        kind="Itens de Enfermagem",
        unit="UNI"
    ),
    qty_awarded=100,
    unit_price=Decimal("2.50"),
    total_price=Decimal("250.00")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.000.502",
        description="APARELHO DE PRESSÃO P/OBESO",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=10,
    unit_price=Decimal("77.98"),
    total_price=Decimal("779.80")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="013.000.729",
        description="BORRIFADOR 500 ML",
        kind="Itens de Enfermagem",
        unit="UNI"
    ),
    qty_awarded=1000,
    unit_price=Decimal("6.50"),
    total_price=Decimal("6500.00")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="023.001.002",
        description="CABO DE BISTURI Nº 4",
        kind="Itens de Enfermagem",
        unit="UNI"
    ),
    qty_awarded=10,
    unit_price=Decimal("7.70"),
    total_price=Decimal("77.00")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="023.001.004",
        description="CATÉTER NASAL TIPO ÓCULOS (ADULTO)",
        kind="Itens de Enfermagem",
        unit="UNI"
    ),
    qty_awarded=1000,
    unit_price=Decimal("0.87"),
    total_price=Decimal("870.00")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="023.001.032",
        description="CATÉTER PERIFÉRICO I.V Nº 18",
        kind="Itens de Enfermagem",
        unit="UNI"
    ),
    qty_awarded=100,
    unit_price=Decimal("0.79"),
    total_price=Decimal("79.00")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.021",
        description="CATETER PERIFÉRICO I.V 24",
        kind="Itens de Enfermagem",
        unit="UNI"
    ),
    qty_awarded=3000,
    unit_price=Decimal("0.94"),
    total_price=Decimal("2820.00")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.023",
        description="COLETOR DE URINA E SECREÇÃO TIPO SACO- 2 LITROS C/BARBANTE",
        kind="Itens de Enfermagem",
        unit="UNI"
    ),
    qty_awarded=5000,
    unit_price=Decimal("0.33"),
    total_price=Decimal("1650.00")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.086",
        description="COMPRESSA DE GAZE 7.5 CM/7.5 CM FECHADA 13 FIOS (ESTÉRIL) PCT C/ 10 UNI",
        kind="Itens de Enfermagem",
        unit="PCT"
    ),
    qty_awarded=100000,
    unit_price=Decimal("0.55"),
    total_price=Decimal("55000.00")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="023.001.036",
        description="CONJUNTO DE NEBULIZAÇÃO/OXIGÊNIO/ADULTO",
        kind="Itens de Enfermagem",
        unit="UNI"
    ),
    qty_awarded=100,
    unit_price=Decimal("5.75"),
    total_price=Decimal("575.00")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="023.001.037",
        description="CONJUNTO DE NEBULIZAÇÃO/OXIGÊNIO/INFANTIL",
        kind="Itens de Enfermagem",
        unit="UNI"
    ),
    qty_awarded=70,
    unit_price=Decimal("5.75"),
    total_price=Decimal("402.50")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.174",
        description="ELETRODO P/ECG",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=200,
    unit_price=Decimal("0.22"),
    total_price=Decimal("44.00")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.029",
        description="ESCOVAS CERVICAL GINECOLÓGICA PACOTES COM 100 UNIDADES",
        kind="Itens de Enfermagem",
        unit="PCT"
    ),
    qty_awarded=30,
    unit_price=Decimal("24.00"),
    total_price=Decimal("720.00")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.000.521",
        description="ESPARADRAPO 10 CM X 4,5 M",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=1000,
    unit_price=Decimal("8.80"),
    total_price=Decimal("8800.00")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.000.055",
        description="FIO DE NYLON 4.0",
        kind="Itens de Enfermagem",
        unit="CX"
    ),
    qty_awarded=10,
    unit_price=Decimal("27.99"),
    total_price=Decimal("279.90")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.037",
        description="FIO DE NYLON 2.0",
        kind="Itens de Enfermagem",
        unit="CX"
    ),
    qty_awarded=50,
    unit_price=Decimal("28.60"),
    total_price=Decimal("1430.00")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.038",
        description="FIO DE NYLON 3.0",
        kind="Itens de Enfermagem",
        unit="CX"
    ),
    qty_awarded=50,
    unit_price=Decimal("28.60"),
    total_price=Decimal("1430.00")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.000.527",
        description="GARROTE P/ COLETAS DE SANGUE",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=100,
    unit_price=Decimal("6.42"),
    total_price=Decimal("642.00")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="023.001.007",
        description="GEL P/ECG FRASCO 100 ML",
        kind="Itens de Enfermagem",
        unit="FRC"
    ),
    qty_awarded=50,
    unit_price=Decimal("1.54"),
    total_price=Decimal("77.00")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.000.231",
        description="GORRO",
        kind="Itens de Enfermagem",
        unit="UNI"
    ),
    qty_awarded=10000,
    unit_price=Decimal("0.06"),
    total_price=Decimal("600.00")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.046",
        description="LÂMINA DE BISTURI Nº11",
        kind="Itens de Enfermagem",
        unit="CX"
    ),
    qty_awarded=20,
    unit_price=Decimal("23.40"),
    total_price=Decimal("468.00")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.047",
        description="LÂMINA DE BISTURI Nº21 CAIXA COM 100",
        kind="Itens de Enfermagem",
        unit="CX"
    ),
    qty_awarded=20,
    unit_price=Decimal("23.40"),
    total_price=Decimal("468.00")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="013.013.100",
        description="LANTERNA CLÍNICA",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=10,
    unit_price=Decimal("16.90"),
    total_price=Decimal("169.00")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.050",
        description="LUVA CIRÚRGICA 7.5",
        kind="Itens de Enfermagem",
        unit="PAR"
    ),
    qty_awarded=2000,
    unit_price=Decimal("1.36"),
    total_price=Decimal("2720.00")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.051",
        description="LUVAS DE PROCEDIMENTOS (G) CAIXAS COM 100",
        kind="Itens de Enfermagem",
        unit="CX"
    ),
    qty_awarded=300,
    unit_price=Decimal("22.90"),
    total_price=Decimal("6870.00")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.052",
        description="LUVAS DE PROCEDIMENTOS (M) CAIXA COM 100",
        kind="Itens de Enfermagem",
        unit="CX"
    ),
    qty_awarded=600,
    unit_price=Decimal("22.90"),
    total_price=Decimal("13740.00")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.053",
        description="LUVAS DE PROCEDIMENTOS (P) CAIXA COM 100",
        kind="Itens de Enfermagem",
        unit="CX"
    ),
    qty_awarded=600,
    unit_price=Decimal("22.90"),
    total_price=Decimal("13740.00")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.000.086",
        description="MÁSCARA N 95",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=1000,
    unit_price=Decimal("0.65"),
    total_price=Decimal("650.00")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.002.073",
        description="ÓLEO DE GIRASSOL 100ML",
        kind="Itens de Enfermagem",
        unit="FR"
    ),
    qty_awarded=1000,
    unit_price=Decimal("2.85"),
    total_price=Decimal("2850.00")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.071",
        description="SCALPS N 23",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=15000,
    unit_price=Decimal("0,22"),
    total_price=Decimal("3300.00")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="023.001.015",
        description="SERINGAS DESC. 1 ML C/AG ULTRAFINE",
        kind="Itens de Enfermagem",
        unit="UNI"
    ),
    qty_awarded=15000,
    unit_price=Decimal("0.20"),
    total_price=Decimal("3000.00")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.058",
        description="SERINGAS DESC. 3 ML S/AG",
        kind="Itens de Enfermagem",
        unit="UNI"
    ),
    qty_awarded=10000,
    unit_price=Decimal("0.11"),
    total_price=Decimal("1100.00")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.059",
        description="SERINGAS DESC. 5 ML S/AG",
        kind="Itens de Enfermagem",
        unit="UNI"
    ),
    qty_awarded=15000,
    unit_price=Decimal("0.14"),
    total_price=Decimal("2100.00")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.060",
        description="SERINGAS DESC. 10 ML S/AG",
        kind="Itens de Enfermagem",
        unit="UNI"
    ),
    qty_awarded=15000,
    unit_price=Decimal("0.21"),
    total_price=Decimal("3150.00")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.062",
        description="SOLUÇÃO DE HIPOCLORITO DE SÓDIO 1% P/P",
        kind="Itens de Enfermagem",
        unit="UNI"
    ),
    qty_awarded=40,
    unit_price=Decimal("10.98"),
    total_price=Decimal("439.20")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.063",
        description="SONDA DE FAWLEY Nº 14",
        kind="Itens de Enfermagem",
        unit="UNI"
    ),
    qty_awarded=20,
    unit_price=Decimal("2.50"),
    total_price=Decimal("50.00")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.064",
        description="SONDA DE FAWLEY Nº 16",
        kind="Itens de Enfermagem",
        unit="UNI"
    ),
    qty_awarded=80,
    unit_price=Decimal("2.45"),
    total_price=Decimal("196.00")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.065",
        description="SONDA DE FAWLEY Nº 18",
        kind="Itens de Enfermagem",
        unit="UNI"
    ),
    qty_awarded=30,
    unit_price=Decimal("2.36"),
    total_price=Decimal("70.80")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.066",
        description="SONDA DE FAWLEY Nº 20",
        kind="Itens de Enfermagem",
        unit="UNI"
    ),
    qty_awarded=30,
    unit_price=Decimal("2.36"),
    total_price=Decimal("70.80")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.091",
        description="SONDA DE FAWLEY Nº 22",
        kind="Itens de Enfermagem",
        unit="UNI"
    ),
    qty_awarded=20,
    unit_price=Decimal("2.50"),
    total_price=Decimal("50.00")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.000.551",
        description="TESOURA DE ÍRIS 12 CM",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=2,
    unit_price=Decimal("18.00"),
    total_price=Decimal("36.00")
)

Award.objects.create(
    company=lumar,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.000.555",
        description="TESTE DE GRAVIDEZ EM TIRA C/FRASCO COLETOR",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=1000,
    unit_price=Decimal("1.81"),
    total_price=Decimal("1810.00")
)

# Garantir que o edital existe
tender_enf = Tender.objects.get_or_create(number="000027/25", kind="Itens de Enfermagem")[0]

# Empresa
cirurgica_uniao = Company.objects.get_or_create(
    name="CIRÚRGICA UNIÃO LTDA",
    cnpj="04.063.331/0001-21",
    email="uniao@cirurgicauniao.com.br",
    phone="(19) 3526-1900",
    address="Rua 25, N 1908/1928, Bairro Jardim São Paulo, Rio Claro-SP, CEP 13503-010"
)[0]

# Itens da CIRÚRGICA UNIÃO – Parte 1
# Itens — Parte 1

Award.objects.create(
    company=cirurgica_uniao,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.000.034",
        description="ABAIXADOR DE LINGUA",
        kind="Itens de Enfermagem",
        unit="PCT"
    ),
    qty_awarded=100,
    unit_price=Decimal("4.999"),
    total_price=Decimal("499.90")
)

Award.objects.create(
    company=cirurgica_uniao,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="006.001.030",
        description="ÁGUA OXIGENADA 10 VOL.",
        kind="Itens de Enfermagem",
        unit="LT"
    ),
    qty_awarded=50,
    unit_price=Decimal("4.50"),
    total_price=Decimal("225.00")
)

Award.objects.create(
    company=cirurgica_uniao,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.006",
        description="AGULHA 25/8 CX 100",
        kind="Itens de Enfermagem",
        unit="CX"
    ),
    qty_awarded=500,
    unit_price=Decimal("7.39"),
    total_price=Decimal("3695.00")
)

Award.objects.create(
    company=cirurgica_uniao,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="023.001.025",
        description="AVENTAL GRAMATURA 40 MANGA LONGA",
        kind="Itens de Enfermagem",
        unit="UNI"
    ),
    qty_awarded=10000,
    unit_price=Decimal("2.15"),
    total_price=Decimal("21500.00")
)

Award.objects.create(
    company=cirurgica_uniao,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.019",
        description="BANDAGEM ANTISSÉPTICA CAIXA COM 500 UNIDADES",
        kind="Itens de Enfermagem",
        unit="UNI"
    ),
    qty_awarded=100,
    unit_price=Decimal("10.30"),
    total_price=Decimal("1030.00")
)

Award.objects.create(
    company=cirurgica_uniao,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.002.037",
        description="BANDEJA INOX LISA 22 X 17 X 1,5 CM",
        kind="Itens de Enfermagem",
        unit="UNI"
    ),
    qty_awarded=20,
    unit_price=Decimal("33.50"),
    total_price=Decimal("670.00")
)

Award.objects.create(
    company=cirurgica_uniao,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.000.505",
        description="CAMISOLAS DE PACIENTES P/EXAMES",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=500,
    unit_price=Decimal("1.49"),
    total_price=Decimal("745.00")
)

# Itens — Parte 2
Award.objects.create(
    company=cirurgica_uniao,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.162",
        description="CAMPO CIRÚRGICO 1 MT X 1MT FENESTRADO SM",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=500,
    unit_price=Decimal("3.82"),
    total_price=Decimal("1910.00")
)

Award.objects.create(
    company=cirurgica_uniao,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="023.001.033",
        description="CATÉTER PERIFÉRICO I.V Nº 20",
        kind="Itens de Enfermagem",
        unit="UNI"
    ),
    qty_awarded=3000,
    unit_price=Decimal("0.859"),
    total_price=Decimal("2577.00")
)

Award.objects.create(
    company=cirurgica_uniao,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="023.001.034",
        description="CATÉTER PERIFÉRICO I.V Nº 22",
        kind="Itens de Enfermagem",
        unit="UNI"
    ),
    qty_awarded=3000,
    unit_price=Decimal("0.859"),
    total_price=Decimal("2577.00")
)

Award.objects.create(
    company=cirurgica_uniao,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.000.506",
        description="CINTO DE SEGURANÇA P/AMBULÂNCIA",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=20,
    unit_price=Decimal("355.76"),
    total_price=Decimal("7115.20")
)

Award.objects.create(
    company=cirurgica_uniao,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.022",
        description="COLETOR DE MATERIAL PERFURO CORTANTE 13 L",
        kind="Itens de Enfermagem",
        unit="UNI"
    ),
    qty_awarded=500,
    unit_price=Decimal("4.93"),
    total_price=Decimal("2465.00")
)

# Itens — Parte 3
Award.objects.create(
    company=cirurgica_uniao,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="023.001.035",
        description="COMADRE DE INOX 40X30 CM",
        kind="Itens de Enfermagem",
        unit="UNI"
    ),
    qty_awarded=5,
    unit_price=Decimal("192.10"),
    total_price=Decimal("960.50")
)

Award.objects.create(
    company=cirurgica_uniao,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.000.512",
        description="COMPRESSA P/CURATIVOS CIRÚRGICO ESTÉRIL",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=1000,
    unit_price=Decimal("0.90"),
    total_price=Decimal("900.00")
)

Award.objects.create(
    company=cirurgica_uniao,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.002.039",
        description="CUBA RIM INOX 26 X 12 X 6 CM",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=10,
    unit_price=Decimal("37.00"),
    total_price=Decimal("370.00")
)

Award.objects.create(
    company=cirurgica_uniao,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.032",
        description="ESPÉCULO VAGINAL DESCARTÁVEL (G)",
        kind="Itens de Enfermagem",
        unit="UNI"
    ),
    qty_awarded=1000,
    unit_price=Decimal("1.40"),
    total_price=Decimal("1400.00")
)

Award.objects.create(
    company=cirurgica_uniao,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.033",
        description="ESPÉCULOS VAGINAL DESCARTÁVEL (M)",
        kind="Itens de Enfermagem",
        unit="UNI"
    ),
    qty_awarded=1000,
    unit_price=Decimal("1.19"),
    total_price=Decimal("1190.00")
)

# Itens — Parte 4
Award.objects.create(
    company=cirurgica_uniao,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.034",
        description="ESPÉCULOS VAGINAL DESCARTÁVEL (P)",
        kind="Itens de Enfermagem",
        unit="UNI"
    ),
    qty_awarded=1000,
    unit_price=Decimal("1.13"),
    total_price=Decimal("1130.00")
)

Award.objects.create(
    company=cirurgica_uniao,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.000.523",
        description="FITA ADESIVA 16MM X 50M",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=500,
    unit_price=Decimal("3.20"),
    total_price=Decimal("1600.00")
)

Award.objects.create(
    company=cirurgica_uniao,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.000.524",
        description="FITA DE AUTOCLAVE 19MM X 30M",
        kind="Itens de Enfermagem",
        unit="RL"
    ),
    qty_awarded=200,
    unit_price=Decimal("3.72"),
    total_price=Decimal("744.00")
)

Award.objects.create(
    company=cirurgica_uniao,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.000.525",
        description="FITA DE MICROPORE 25MM X 4.5M",
        kind="Itens de Enfermagem",
        unit="RL"
    ),
    qty_awarded=5000,
    unit_price=Decimal("1.969"),
    total_price=Decimal("9845.00")
)

Award.objects.create(
    company=cirurgica_uniao,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.000.526",
        description="FITA DE MICROPORE 50MM X 10M",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=200,
    unit_price=Decimal("4.30"),
    total_price=Decimal("860.00")
)

Award.objects.create(
    company=cirurgica_uniao,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="023.001.040",
        description="FITA P/CERTIFICAÇÃO DE GLICEMIA CAPILAR C/ 50 UNI",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=150000,
    unit_price=Decimal("0.47"),
    total_price=Decimal("70500.00")
)

# Itens — Parte 5
Award.objects.create(
    company=cirurgica_uniao,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.043",
        description="FRASCO P/ALIMENTAÇÃO 300ML",
        kind="Itens de Enfermagem",
        unit="UNI"
    ),
    qty_awarded=5000,
    unit_price=Decimal("0.729"),
    total_price=Decimal("3645.00")
)

Award.objects.create(
    company=cirurgica_uniao,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="023.001.006",
        description="GEL P/DETECTOR FETAL FRASCO 100ML",
        kind="Itens de Enfermagem",
        unit="FRC"
    ),
    qty_awarded=100,
    unit_price=Decimal("1.68"),
    total_price=Decimal("168.00")
)

Award.objects.create(
    company=cirurgica_uniao,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.048",
        description="LANCETAS C/ DISPOSITIVO",
        kind="Itens de Enfermagem",
        unit="UNI"
    ),
    qty_awarded=30000,
    unit_price=Decimal("0.11"),
    total_price=Decimal("3300.00")
)

Award.objects.create(
    company=cirurgica_uniao,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="013.007.523",
        description="LIXEIRA DE PEDAL 100 LITROS",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=50,
    unit_price=Decimal("220.90"),
    total_price=Decimal("11045.00")
)

Award.objects.create(
    company=cirurgica_uniao,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="003.000.228",
        description="LIXEIRA DE PEDAL 30 LITROS",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=50,
    unit_price=Decimal("67.76"),
    total_price=Decimal("3388.00")
)

# Itens — Parte 6
Award.objects.create(
    company=cirurgica_uniao,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="023.001.008",
        description="MÁSCARA CIRÚRGICA TRIPLA C/ELÁSTICO CAIXA",
        kind="Itens de Enfermagem",
        unit="CX"
    ),
    qty_awarded=50000,
    unit_price=Decimal("0.092"),
    total_price=Decimal("4600.00")
)

Award.objects.create(
    company=cirurgica_uniao,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.000.532",
        description="MÁSCARA DE ALTA CONCENTRAÇÃO OXIGÊNIO",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=1000,
    unit_price=Decimal("5.88"),
    total_price=Decimal("5880.00")
)

Award.objects.create(
    company=cirurgica_uniao,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.000.534",
        description="MÁSCARA FACIAL PARA NEBULIZAÇÃO CONTÍNUA",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=30,
    unit_price=Decimal("6.38"),
    total_price=Decimal("191.40")
)

Award.objects.create(
    company=cirurgica_uniao,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.054",
        description="PAPEL CREPADO 40CM/40 CAIXA COM 500",
        kind="Itens de Enfermagem",
        unit="CX"
    ),
    qty_awarded=2,
    unit_price=Decimal("128.50"),
    total_price=Decimal("257.00")
)

Award.objects.create(
    company=cirurgica_uniao,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.090",
        description="PAPEL GRAU CIRÚRGICO 25/100",
        kind="Itens de Enfermagem",
        unit="BO"
    ),
    qty_awarded=10,
    unit_price=Decimal("119.04"),
    total_price=Decimal("1190.40")
)

# Itens — Parte 7
Award.objects.create(
    company=cirurgica_uniao,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.000.359",
        description="PINÇA CHERON 24 CM EM AÇO INOX.",
        kind="Itens de Enfermagem",
        unit="UNI"
    ),
    qty_awarded=4,
    unit_price=Decimal("48.00"),
    total_price=Decimal("192.00")
)

Award.objects.create(
    company=cirurgica_uniao,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="023.001.013",
        description="PINÇA KELLY RETA",
        kind="Itens de Enfermagem",
        unit="UNI"
    ),
    qty_awarded=10,
    unit_price=Decimal("29.70"),
    total_price=Decimal("297.00")
)

Award.objects.create(
    company=cirurgica_uniao,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.000.087",
        description="POLIFIX ADULTO",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=100,
    unit_price=Decimal("0.63"),
    total_price=Decimal("63.00")
)

Award.objects.create(
    company=cirurgica_uniao,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.061",
        description="SERINGAS DESC. 20 ML S/AG",
        kind="Itens de Enfermagem",
        unit="UNI"
    ),
    qty_awarded=15000,
    unit_price=Decimal("0.33"),
    total_price=Decimal("4950.00")
)

Award.objects.create(
    company=cirurgica_uniao,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.002.019",
        description="SONDA DE ASPIRAÇÃO TRAQUEAL Nº 12",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=10000,
    unit_price=Decimal("0.52"),
    total_price=Decimal("5200.00")
)

# Itens — Parte 8 (final)
Award.objects.create(
    company=cirurgica_uniao,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.068",
        description="SONDA URETRAL Nº 12",
        kind="Itens de Enfermagem",
        unit="UNI"
    ),
    qty_awarded=15000,
    unit_price=Decimal("0.50"),
    total_price=Decimal("7500.00")
)

Award.objects.create(
    company=cirurgica_uniao,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.000.547",
        description="SUPORTE P/ MATERIAIS PERFURO CORTANTE P/1",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=10,
    unit_price=Decimal("21.00"),
    total_price=Decimal("210.00")
)

Award.objects.create(
    company=cirurgica_uniao,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="006.000.295",
        description="TERMOMETRO DIGITAL",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=100,
    unit_price=Decimal("9.999"),
    total_price=Decimal("999.90")
)

Award.objects.create(
    company=cirurgica_uniao,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.002.052",
        description="VASELINA LIQUIDA",
        kind="Itens de Enfermagem",
        unit="L"
    ),
    qty_awarded=10,
    unit_price=Decimal("29.80"),
    total_price=Decimal("298.00")
)

# Garantir que o edital existe e buscar/criar a empresa
tender_enf = Tender.objects.get_or_create(number="000027/25", kind="Itens de Enfermagem")[0]
placido = Company.objects.get_or_create(
    name="PLACIDO COM. DE MAT. CIR. E HOSP. EIRELI-ME",
    cnpj="25.123.729/0001-86",
    email="vendas.placido@hotmail.com",
    phone="(14) 3413-9949",
    addres="Rua Av. Tiradentes, N 1321, Bairro Fragata, Marília-SP, CEP 17519-000"
)[0]

# Itens da PLACIDO – Parte 1
Award.objects.create(
    company=placido,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.000.500",
        description="ABAIXADOR DE LÍNGUA COLORIDO AROMADO LIS",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=100,
    unit_price=Decimal("37.998"),
    total_price=Decimal("3799.80")
)

Award.objects.create(
    company=placido,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.015",
        description="ATADURA DE CREPE 10 CM 13 FIOS PACOTES COM",
        kind="Itens de Enfermagem",
        unit="PCT"
    ),
    qty_awarded=1000,
    unit_price=Decimal("4.80"),
    total_price=Decimal("4800.00")
)

Award.objects.create(
    company=placido,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.016",
        description="ATADURA DE CREPE 15 CM 13 FIOS PACOTES COM",
        kind="Itens de Enfermagem",
        unit="PCT"
    ),
    qty_awarded=1000,
    unit_price=Decimal("7.10"),
    total_price=Decimal("7100.00")
)

Award.objects.create(
    company=placido,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.017",
        description="ATADURA DE CREPE 20 CM 13 FIOS PACOTES COM",
        kind="Itens de Enfermagem",
        unit="PCT"
    ),
    qty_awarded=1000,
    unit_price=Decimal("9.689"),
    total_price=Decimal("9689.00")
)

Award.objects.create(
    company=placido,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.018",
        description="ATADURA DE CREPE 6 CM 13 FIOS PACOTES COM",
        kind="Itens de Enfermagem",
        unit="PCT"
    ),
    qty_awarded=1000,
    unit_price=Decimal("2.98"),
    total_price=Decimal("2980.00")
)

Award.objects.create(
    company=placido,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.000.511",
        description="COLETOR DE URINA INFANTIL UNISSEX ESTÉRIL 100 ML",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=3000,
    unit_price=Decimal("0.35"),
    total_price=Decimal("1050.00")
)

Award.objects.create(
    company=placido,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="023.001.038",
        description="ESCADA 2 DEGRAUS ANTIDERRAPANTE",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=12,
    unit_price=Decimal("121.999"),
    total_price=Decimal("1463.99")
)

Award.objects.create(
    company=placido,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.002.042",
        description="FIO GUIA P/ ENTUBAÇÃO ADULTO",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=5,
    unit_price=Decimal("11.00"),
    total_price=Decimal("55.00")
)

Award.objects.create(
    company=placido,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.000.078",
        description="LENÇOL DESCARTÁVEL PARA MACA",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=5000,
    unit_price=Decimal("0.88"),
    total_price=Decimal("4400.00")
)

Award.objects.create(
    company=placido,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.000.533",
        description="MANGUEIRA DE O2",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=100,
    unit_price=Decimal("4.50"),
    total_price=Decimal("450.00")
)

Award.objects.create(
    company=placido,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.005.088",
        description="PAPEL P/ECG 216 MM X 30MT",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=500,
    unit_price=Decimal("22.32"),
    total_price=Decimal("11160.00")
)

Award.objects.create(
    company=placido,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.055",
        description="PAPEL P/ECG 58/30",
        kind="Itens de Enfermagem",
        unit="RL"
    ),
    qty_awarded=500,
    unit_price=Decimal("7.35"),
    total_price=Decimal("3675.00")
)

# Garantir que o edital existe e buscar/criar a empresa
tender_enf = Tender.objects.get_or_create(number="000027/25", kind="Itens de Enfermagem")[0]
rosicler = Company.objects.get_or_create(
    name="ROSICLER CIRÚRGICA LTDA",
    cnpj="57.365.116/0001-41",
    email="vendas@rosiclercirurgica.com.br, licitacao@rosiclercirurgica.com.br",
    phone="(19) 3023-3480, (19) 3534-5162",
    addres="Avenida 12, Nº 2606, Bairro Jardim São Paulo, Rio Claro-SP, CEP 13503-019"
)[0]

# Itens da ROSICLER – Parte 1
Award.objects.create(
    company=rosicler,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.077",
        description="APARELHO DE PRESSÃO (INFANTIL) COMPLETO",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=10,
    unit_price=Decimal("67.40"),
    total_price=Decimal("674.00")
)

Award.objects.create(
    company=rosicler,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.014",
        description="APARELHO DE PRESSÃO (ADULTO) COMPLETO",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=100,
    unit_price=Decimal("67.40"),
    total_price=Decimal("6740.00")
)

Award.objects.create(
    company=rosicler,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="023.001.003",
        description="CABO DE BISTURI Nº 5",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=10,
    unit_price=Decimal("11.00"),
    total_price=Decimal("110.00")
)

Award.objects.create(
    company=rosicler,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.000.517",
        description="CINTO DE SEGURANÇA P/MACA DE AMBULÂNCIA",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=20,
    unit_price=Decimal("21.50"),
    total_price=Decimal("430.00")
)

Award.objects.create(
    company=rosicler,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.000.200",
        description="COLAR CERVICAL FIBRA CIRÚRGICA (P)",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=10,
    unit_price=Decimal("10.95"),
    total_price=Decimal("109.50")
)

Award.objects.create(
    company=rosicler,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.000.395",
        description="COLAR CERVICAL FIBRA CIRÚRGICA (G)",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=10,
    unit_price=Decimal("10.95"),
    total_price=Decimal("109.50")
)

Award.objects.create(
    company=rosicler,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.000.509",
        description="COLAR CERVICAL FIBRA CIRÚRGICA (M)",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=10,
    unit_price=Decimal("10.95"),
    total_price=Decimal("109.50")
)

Award.objects.create(
    company=rosicler,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.000.510",
        description="COLAR CERVICAL P/RESGATE (M)",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=10,
    unit_price=Decimal("10.95"),
    total_price=Decimal("109.50")
)

Award.objects.create(
    company=rosicler,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.000.518",
        description="DEGERMANTE PVPI",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=50,
    unit_price=Decimal("44.80"),
    total_price=Decimal("2240.00")
)

Award.objects.create(
    company=rosicler,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.000.425",
        description="DETERGENTE ENZIMÁTICO GALÃO DE 5 LITROS",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=20,
    unit_price=Decimal("83.90"),
    total_price=Decimal("1678.00")
)

Award.objects.create(
    company=rosicler,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.000.035",
        description="ÉTER",
        kind="Itens de Enfermagem",
        unit="LT"
    ),
    qty_awarded=100,
    unit_price=Decimal("38.70"),
    total_price=Decimal("3870.00")
)

Award.objects.create(
    company=rosicler,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.000.522",
        description="FIO GUIA P/ENTUBAÇÃO INFANTIL",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=5,
    unit_price=Decimal("12.00"),
    total_price=Decimal("60.00")
)

Award.objects.create(
    company=rosicler,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.000.536",
        description="OTOSCÓPIO INFANTIL",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=5,
    unit_price=Decimal("196.90"),
    total_price=Decimal("984.50")
)

Award.objects.create(
    company=rosicler,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.000.537",
        description="OTOSCÓPIO ADULTO",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=10,
    unit_price=Decimal("196.90"),
    total_price=Decimal("1969.00")
)

Award.objects.create(
    company=rosicler,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.000.538",
        description="PAPAGAIO INOX 1000 ML",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=5,
    unit_price=Decimal("111.90"),
    total_price=Decimal("559.50")
)

Award.objects.create(
    company=rosicler,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="023.001.011",
        description="PINÇA ANATÔMICA DENTE DE RATO",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=10,
    unit_price=Decimal("10.50"),
    total_price=Decimal("105.00")
)

Award.objects.create(
    company=rosicler,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="023.001.012",
        description="PINÇA KELLY CURVA",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=10,
    unit_price=Decimal("29.80"),
    total_price=Decimal("298.00")
)

Award.objects.create(
    company=rosicler,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.000.552",
        description="TESOURA DE MAYO 16 CM PONTA FINA",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=4,
    unit_price=Decimal("24.85"),
    total_price=Decimal("99.40")
)

Award.objects.create(
    company=rosicler,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.000.553",
        description="TESOURA DE MAYO 16 CM PONTA ROMBA",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=2,
    unit_price=Decimal("24.85"),
    total_price=Decimal("49.70")
)

Award.objects.create(
    company=rosicler,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="023.001.019",
        description="TESOURA DE MAYO Nº 12",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=20,
    unit_price=Decimal("28.00"),
    total_price=Decimal("560.00")
)

Award.objects.create(
    company=rosicler,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.000.554",
        description="TESOURA MULTIUSO PONTA REDONDA",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=20,
    unit_price=Decimal("32.00"),
    total_price=Decimal("640.00")
)

Award.objects.create(
    company=rosicler,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.070",
        description="TÓPICO PVPI",
        kind="Itens de Enfermagem",
        unit="LT"
    ),
    qty_awarded=100,
    unit_price=Decimal("43.90"),
    total_price=Decimal("4390.00")
)

# Garantir que o edital existe e buscar/criar a empresa
tender_enf = Tender.objects.get_or_create(number="000027/25", kind="Itens de Enfermagem")[0]
nossa_senhora = Company.objects.get_or_create(
    name="CIRÚRGICA NOSSA SENHORA EIRELI",
    cnpj="24.586.988/0001-80",
    email="cirnossasenhora@hotmail.com",
    phone="(43) 3252-9947",
    addres="Rua Pavão, Nº 540, Bairro Jardim Bandeirantes, Arapongas-PR, CEP 86703-250"
)[0]

# Itens – Parte 1
Award.objects.create(
    company=nossa_senhora,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.000.503",
        description="BOLSA COLETORA ESTÉRIL DE URINA - SISTEMA FECHADO",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=600,
    unit_price=Decimal("3.32"),
    total_price=Decimal("1992.00")
)

Award.objects.create(
    company=nossa_senhora,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="023.001.005",
        description="CATÉTER NASAL TIPO ÓCULOS (INFANTIL)",
        kind="Itens de Enfermagem",
        unit="UNI"
    ),
    qty_awarded=1000,
    unit_price=Decimal("1.16"),
    total_price=Decimal("1160.00")
)

Award.objects.create(
    company=nossa_senhora,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.031",
        description="ESPÁTULAS DE AYRES C/100",
        kind="Itens de Enfermagem",
        unit="PCT"
    ),
    qty_awarded=20,
    unit_price=Decimal("10.61"),
    total_price=Decimal("212.20")
)

Award.objects.create(
    company=nossa_senhora,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="006.001.718",
        description="LÂMINA P/ MICROSCOPIA FOSCA",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=20,
    unit_price=Decimal("5.53"),
    total_price=Decimal("110.60")
)

Award.objects.create(
    company=nossa_senhora,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.000.447",
        description="MÁSCARA DE ALTA CONCENTRAÇÃO OXIGÊNIO C/ RESERVATÓRIO",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=1000,
    unit_price=Decimal("4.94"),
    total_price=Decimal("4940.00")
)

Award.objects.create(
    company=nossa_senhora,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.000.544",
        description="SACO BRANCO INFECTANTE 100 LITROS",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=5000,
    unit_price=Decimal("0.33"),
    total_price=Decimal("1650.00")
)

Award.objects.create(
    company=nossa_senhora,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.005.056",
        description="SACO BRANCO INFECTANTE 30 LITROS",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=5000,
    unit_price=Decimal("0.14"),
    total_price=Decimal("700.00")
)

# Garantir que o edital existe e buscar/criar a empresa
tender_enf = Tender.objects.get_or_create(number="000027/25", kind="Itens de Enfermagem")[0]
dora = Company.objects.get_or_create(
    name="DORA MEDICAMENTOS LTDA EPP",
    cnpj="30.936.479/0001-33",
    email="licitacao@triunfal.com.br",
    phone="(14) 3413-5243",
    addres="Avenida Silvio Bertonha, Nº 533, Parque das Indústrias, CEP 17519-690, Marília-SP"
)[0]

# Itens – Parte 1
Award.objects.create(
    company=dora,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.026",
        description="EQUIPO MACRO-GOTAS",
        kind="Itens de Enfermagem",
        unit="UNI"
    ),
    qty_awarded=5000,
    unit_price=Decimal("0.909"),
    total_price=Decimal("4545.00")
)

Award.objects.create(
    company=dora,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.028",
        description="EQUIPO P/NUTRIÇÃO ENTERAL (AZUL)",
        kind="Itens de Enfermagem",
        unit="UNI"
    ),
    qty_awarded=5000,
    unit_price=Decimal("0.93"),
    total_price=Decimal("4650.00")
)

Award.objects.create(
    company=dora,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.035",
        description="ESTETOSCÓPIO (ADULTO)",
        kind="Itens de Enfermagem",
        unit="UNI"
    ),
    qty_awarded=100,
    unit_price=Decimal("10.88"),
    total_price=Decimal("1088.00")
)

# Garantir que o edital existe e buscar/criar a empresa
tender_enf = Tender.objects.get_or_create(number="000027/25", kind="Itens de Enfermagem")[0]
lc_med = Company.objects.get_or_create(
    name="LC MED MATERIAIS MÉDICOS E HOSPITALARES LTDA",
    cnpj="25.245.772/0001-14",
    email="lcmed1@hotmail.com",
    phone="(18) 3622-7366",
    addres="Rua Saverio Safiotti, Nº 48, Bairro Paraíso, CEP 16050-130, Araçatuba-SP"

)[0]

# Itens da LC MED
Award.objects.create(
    company=lc_med,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="023.001.009",
        description="OXÍMETRO DE BOLSO",
        kind="Itens de Enfermagem",
        unit="UNI"
    ),
    qty_awarded=100,
    unit_price=Decimal("31.42"),
    total_price=Decimal("3142.00")
)

Award.objects.create(
    company=lc_med,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.002.020",
        description="TERMÔMETRO DIGITAL LASER INFRAVERMELHO",
        kind="Itens de Enfermagem",
        unit="UN"
    ),
    qty_awarded=200,
    unit_price=Decimal("45.71"),
    total_price=Decimal("9142.00")
)

# Garantir que o edital existe e buscar/criar a empresa
tender_enf = Tender.objects.get_or_create(number="000027/25", kind="Itens de Enfermagem")[0]
easy = Company.objects.get_or_create(
    name="EASY INDÚSTRIA E COMÉRCIO DE DESCARTÁVEIS LTDA",
    cnpj="35.113.338/0001-34",
    email="vendas@easypell.com.br",
    phone="(19) 3531-2347",
    addres="Avenida 51, Nº 1036, Bairro Jardim Kennedy, CEP: 13501-520, Rio Claro-SP"
)[0]

# Único item da EASY
Award.objects.create(
    company=easy,
    tender=tender_enf,
    item=ItemCatalog.objects.create(
        code="014.001.049",
        description="LENÇOL DE PAPEL DESCARTÁVEL 70CM/50M",
        kind="Itens de Enfermagem",
        unit="RL"
    ),
    qty_awarded=6000,
    unit_price=Decimal("7.20"),
    total_price=Decimal("43200.00")
)

# Empresa (dados do contrato)
olimpio = Company.objects.get_or_create(
    name="CIRURGICA OLIMPIO EIRELLI EPP",
    cnpj="01.140.868/0001-50",
    email="cirurgicaolimpio@cirurgicaolimpio.com.br",
    phone="(17) 3201-1270",
    address="Rua João Antonio Sicoli, 560, Jardim Maracanã, São José do Rio Preto-SP, CEP 15092-050"
)[0]

# Itens — parte 1
Award.objects.create(company=olimpio, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.020", description="ACEBROFILINA 25MG/5ML", kind="Medicamentos", unit="FRC"),
    qty_awarded=3000, unit_price=Decimal("5.14"), total_price=Decimal("15420.00"))

Award.objects.create(company=olimpio, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.329", description="CLINDAMICINA 300 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=100000, unit_price=Decimal("0.88"), total_price=Decimal("88000.00"))

Award.objects.create(company=olimpio, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.090", description="CLORIDRATO DE AMBROXOL 15MG/5ML FRS/120ML", kind="Medicamentos", unit="FRC"),
    qty_awarded=3000, unit_price=Decimal("2.25"), total_price=Decimal("6750.00"))

Award.objects.create(company=olimpio, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.099", description="CLORIDRATO DE CLORPROMAZINA 100MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.30"), total_price=Decimal("3000.00"))

Award.objects.create(company=olimpio, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.505", description="DEXCLOR+BETAMETASONA 2MG/5ML+0,25MG/5ML", kind="Medicamentos", unit="FRC"),
    qty_awarded=3000, unit_price=Decimal("2.75"), total_price=Decimal("8250.00"))

Award.objects.create(company=olimpio, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.135", description="DICLOFENACO DIETILAMÔNEO GEL 11,6MG/G TBS", kind="Medicamentos", unit="TUB"),
    qty_awarded=300, unit_price=Decimal("3.38"), total_price=Decimal("1014.00"))

# Itens — parte 2
Award.objects.create(company=olimpio, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.645", description="DIPROPIONATO DE BETAMETASONA+FOSFATO DIA", kind="Medicamentos", unit="AMP"),
    qty_awarded=2000, unit_price=Decimal("2.89"), total_price=Decimal("5780.00"))

Award.objects.create(company=olimpio, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.899", description="FOSFATO DE SÓDIO MONOBÁSICO (0,16G/ML)+FO", kind="Medicamentos", unit="FRC"),
    qty_awarded=100, unit_price=Decimal("5.70"), total_price=Decimal("570.00"))

Award.objects.create(company=olimpio, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.901", description="HALOPERIDOL 5 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.11"), total_price=Decimal("1100.00"))

Award.objects.create(company=olimpio, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.908", description="LORATADINA 10 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("0.07"), total_price=Decimal("1400.00"))

Award.objects.create(company=olimpio, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.415", description="ÓXIDO DE ZINCO 100MG/G+COLECALCIFEROL 400", kind="Medicamentos", unit="TUB"),
    qty_awarded=2000, unit_price=Decimal("3.11"), total_price=Decimal("6220.00"))

Award.objects.create(company=olimpio, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.369", description="PREDNISONA 5MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.05"), total_price=Decimal("500.00"))

Award.objects.create(company=olimpio, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.970", description="SOL. GLICOFISIOLÓGICA S.F - I.V", kind="Medicamentos", unit="FRC"),
    qty_awarded=200, unit_price=Decimal("4.90"), total_price=Decimal("980.00"))

Award.objects.create(company=olimpio, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.261", description="SOLUÇÃO RINGER+ LACTATO FRS/500ML", kind="Medicamentos", unit="FRC"),
    qty_awarded=200, unit_price=Decimal("5.19"), total_price=Decimal("1038.00"))

# Empresa (dados do contrato)
lumar_meds = Company.objects.get_or_create(
    name="LUMAR COMERCIO DE PRODUTOS FARMACEUTICOS LTDA",
    cnpj="49.228.695/0001-52",
    email="licitacoes@lumarfranca.com.br",
    phone="(16) 3721-1102",
    address="Av. Wilson Bego, 745, Distrito Industrial Antônio Della Torres, Franca-SP, CEP 14406-091"
)[0]

# Itens
Award.objects.create(company=lumar_meds, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.479", description="ALOGLIPTINA 12,50 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=12000, unit_price=Decimal("4.20"), total_price=Decimal("50400.00"))

Award.objects.create(company=lumar_meds, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.140", description="DIMENIDRINATO 30MG; CLORIDRATO DE PIRIDOXINA", kind="Medicamentos", unit="AMP"),
    qty_awarded=2000, unit_price=Decimal("8.56"), total_price=Decimal("17120.00"))

Award.objects.create(company=lumar_meds, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.141", description="DIMENIDRINATO 50MG; CLOR. DE PIRIDOXINA 10", kind="Medicamentos", unit="CPR"),
    qty_awarded=30000, unit_price=Decimal("0.63"), total_price=Decimal("18900.00"))

Award.objects.create(company=lumar_meds, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.389", description="IBUPROFENO 50MG/ML", kind="Medicamentos", unit="FRC"),
    qty_awarded=5000, unit_price=Decimal("2.43"), total_price=Decimal("12150.00"))

Award.objects.create(company=lumar_meds, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.918", description="MOMETASONA 1MG/G POMADA", kind="Medicamentos", unit="TUB"),
    qty_awarded=300, unit_price=Decimal("9.40"), total_price=Decimal("2820.00"))

Award.objects.create(company=lumar_meds, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.530", description="PROPIONATO DE CLOBETASOL 0,5MG/G CREME", kind="Medicamentos", unit="TUB"),
    qty_awarded=300, unit_price=Decimal("4.15"), total_price=Decimal("1245.00"))

Award.objects.create(company=lumar_meds, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.414", description="VITAMINA D3 50.000 UI", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.74"), total_price=Decimal("7400.00"))

# Empresa (dados do contrato)
aglon = Company.objects.get_or_create(
    name="AGLON COMERCIO E REPRESENTAÇÕES LTDA",
    cnpj="65.817.900/0001-71",
    email="aglon@aglon.com.br",
    phone="(19) 3573-7300",
    address="Av. Visconde de Nova Granada, 1105, Vila Grossklauss, Leme-SP, CEP 13617-400"
)[0]

# Itens — parte 1
Award.objects.create(company=aglon, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.300", description="ÁCIDO VALPROICO 250 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("0.30"), total_price=Decimal("6000.00"))

Award.objects.create(company=aglon, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.301", description="ÁCIDO VALPROICO 500 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=5000, unit_price=Decimal("0.60"), total_price=Decimal("3000.00"))

Award.objects.create(company=aglon, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.354", description="ATOMOXETINA 10 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=6000, unit_price=Decimal("0.80"), total_price=Decimal("4800.00"))

Award.objects.create(company=aglon, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.222", description="ATOMOXETINA 40MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=6000, unit_price=Decimal("3.22"), total_price=Decimal("19320.00"))

Award.objects.create(company=aglon, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.336", description="ATOMOXETINA 60MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=6000, unit_price=Decimal("4.83"), total_price=Decimal("28980.00"))

Award.objects.create(company=aglon, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.490", description="CITRATO DE POTÁSSIO 10 MEQ", kind="Medicamentos", unit="CPR"),
    qty_awarded=3000, unit_price=Decimal("1.07"), total_price=Decimal("3210.00"))

Award.objects.create(company=aglon, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.123", description="COLAGENASE C/CLORANF. TBS/30G", kind="Medicamentos", unit="TUB"),
    qty_awarded=1000, unit_price=Decimal("12.80"), total_price=Decimal("12800.00"))

# Itens — parte 2
Award.objects.create(company=aglon, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.466", description="DUTASTERIDA 0,5MG+TANSULOSINA 0,4MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("2.64"), total_price=Decimal("52800.00"))

Award.objects.create(company=aglon, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.894", description="FLUVOXAMINA 100 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=3000, unit_price=Decimal("3.96"), total_price=Decimal("11880.00"))

Award.objects.create(company=aglon, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.655", description="FOSFOMICINA TROMETAMOL ENV. 8 G GRANULADO", kind="Medicamentos", unit="ENV"),
    qty_awarded=200, unit_price=Decimal("17.90"), total_price=Decimal("3580.00"))

Award.objects.create(company=aglon, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.392", description="OXIBUTININA 5 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=3000, unit_price=Decimal("0.90"), total_price=Decimal("2700.00"))

Award.objects.create(company=aglon, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.678", description="PERINDOPRIL ARGININA 10 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=2000, unit_price=Decimal("2.10"), total_price=Decimal("4200.00"))

Award.objects.create(company=aglon, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.395", description="PERINDOPRIL ARGININA 10MG+INDAPAMIDA 2,5MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=3000, unit_price=Decimal("2.90"), total_price=Decimal("8700.00"))

Award.objects.create(company=aglon, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.242", description="PROPATIL NITRATO 10MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.575"), total_price=Decimal("5750.00"))

Award.objects.create(company=aglon, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.941", description="TRAZODONA 100 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("0.439"), total_price=Decimal("8780.00"))

Award.objects.create(company=aglon, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.942", description="TRAZODONA 50 MG", kind="Medicamentos", unit="UN"),
    qty_awarded=20000, unit_price=Decimal("0.25"), total_price=Decimal("5000.00"))

Award.objects.create(company=aglon, tender=tender_med,
    item=ItemCatalog.objects.create(code="002.001.784", description="TRIMETAZIDINA LP 80 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=2000, unit_price=Decimal("3.80"), total_price=Decimal("7600.00"))

Award.objects.create(company=aglon, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.281", description="VILDAGLIPTINA 50 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=50000, unit_price=Decimal("0.45"), total_price=Decimal("22500.00"))

# Empresa (dados do contrato)
rioclarense = Company.objects.get_or_create(
    name="COMERCIAL CIRÚRGICA RIOCLARENSE LTDA",
    cnpj="67.729.178/0004-91",
    email="vendas@rioclarense.com.br",
    phone="(19) 3522-5800",
    address="Praça Emílio Marconato, 1000, Galpões 22 e 27, Jardim Primavera, Jaguariúna-SP, CEP 13916-074"
)[0]

# Itens – Parte 1
Award.objects.create(company=rioclarense, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.475", description="ACETATO DE PREDNISOLONA 1% SUSP. OFTÁLMICA", kind="Medicamentos", unit="FR"),
    qty_awarded=100, unit_price=Decimal("16.29"), total_price=Decimal("1629.00"))

Award.objects.create(company=rioclarense, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.290", description="ÁCIDO ACETIL SALICÍLICO 100MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=200000, unit_price=Decimal("0.029"), total_price=Decimal("5800.00"))

Award.objects.create(company=rioclarense, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.044", description="BACLOFENO 10MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=6000, unit_price=Decimal("0.12"), total_price=Decimal("720.00"))

Award.objects.create(company=rioclarense, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.167", description="BROMAZEPAM 6MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=30000, unit_price=Decimal("0.13"), total_price=Decimal("3900.00"))

Award.objects.create(company=rioclarense, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.055", description="BUDESONIDA 50MCG", kind="Medicamentos", unit="FRC"),
    qty_awarded=500, unit_price=Decimal("15.90"), total_price=Decimal("7950.00"))

Award.objects.create(company=rioclarense, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.056", description="BUDESONIDA 64MCG", kind="Medicamentos", unit="FRC"),
    qty_awarded=500, unit_price=Decimal("16.40"), total_price=Decimal("8200.00"))

Award.objects.create(company=rioclarense, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.000.186", description="CEFALEXINA 500 MG", kind="Medicamentos", unit="CX"),
    qty_awarded=10000, unit_price=Decimal("0.45"), total_price=Decimal("4500.00"))

Award.objects.create(company=rioclarense, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.080", description="CETOPROFENO 100MG - I.V FRS/AMP", kind="Medicamentos", unit="F/A"),
    qty_awarded=1000, unit_price=Decimal("3.999"), total_price=Decimal("3999.00"))

Award.objects.create(company=rioclarense, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.093", description="CLORIDRATO DE AMITRIPTILINA 25MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=30000, unit_price=Decimal("0.04"), total_price=Decimal("1200.00"))

Award.objects.create(company=rioclarense, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.095", description="CLORIDRATO DE BIPERIDENO 2MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=6000, unit_price=Decimal("0.28"), total_price=Decimal("1680.00"))

Award.objects.create(company=rioclarense, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.642", description="CLORIDRATO DE CICLOBENZAPRINA 5 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("0.06"), total_price=Decimal("1200.00"))

Award.objects.create(company=rioclarense, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.098", description="CLORIDRATO DE CLONIDINA 0.100 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("0.25"), total_price=Decimal("5000.00"))

Award.objects.create(company=rioclarense, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.339", description="CLORIDRATO DE CLONIDINA 0.150 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("0.31"), total_price=Decimal("6200.00"))

Award.objects.create(company=rioclarense, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.102", description="CLORIDRATO DE FLUOXETINA 20MG", kind="Medicamentos", unit="CAP"),
    qty_awarded=30000, unit_price=Decimal("0.059"), total_price=Decimal("1770.00"))

Award.objects.create(company=rioclarense, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.112", description="CLORIDRATO DE PROMETAZINA 25MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.13"), total_price=Decimal("1300.00"))

Award.objects.create(company=rioclarense, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.113", description="CLORIDRATO DE PROMETAZINA 50MG/2ML", kind="Medicamentos", unit="AMP"),
    qty_awarded=300, unit_price=Decimal("3.25"), total_price=Decimal("975.00"))

Award.objects.create(company=rioclarense, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.995", description="CLORIDRATO DE TRAMADOL 50MG/ML", kind="Medicamentos", unit="CPR"),
    qty_awarded=600, unit_price=Decimal("1.02"), total_price=Decimal("612.00"))

Award.objects.create(company=rioclarense, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.143", description="DIMETICONA 75MG/ML FRS/10ML", kind="Medicamentos", unit="FRC"),
    qty_awarded=2000, unit_price=Decimal("1.39"), total_price=Decimal("2780.00"))

Award.objects.create(company=rioclarense, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.693", description="ESCITALOPRAM 20MG/ML GOTAS", kind="Medicamentos", unit="FR"),
    qty_awarded=50, unit_price=Decimal("10.00"), total_price=Decimal("500.00"))

Award.objects.create(company=rioclarense, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.392", description="HALOPERIDOL 1MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=5000, unit_price=Decimal("0.18"), total_price=Decimal("900.00"))

Award.objects.create(company=rioclarense, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.381", description="IMIPRAMINA 25MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("0.46"), total_price=Decimal("9200.00"))

Award.objects.create(company=rioclarense, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.665", description="LEVODOPA+BENSERAZIDA BD 100MG+25MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("1.00"), total_price=Decimal("10000.00"))

Award.objects.create(company=rioclarense, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.394", description="LEVODOPA+BENZERAZIDA 200MG/50MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=6000, unit_price=Decimal("1.50"), total_price=Decimal("9000.00"))

Award.objects.create(company=rioclarense, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.207", description="LEVOMEPROMAZINA 25MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("0.49"), total_price=Decimal("9800.00"))

Award.objects.create(company=rioclarense, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.396", description="LEVOMEPROMAZINA 40MG/ML", kind="Medicamentos", unit="FRC"),
    qty_awarded=200, unit_price=Decimal("11.00"), total_price=Decimal("2200.00"))

Award.objects.create(company=rioclarense, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.189", description="LEVOTIROXINA SÓDICA 100MCG", kind="Medicamentos", unit="CPR"),
    qty_awarded=50000, unit_price=Decimal("0.12"), total_price=Decimal("6000.00"))

Award.objects.create(company=rioclarense, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.190", description="LEVOTIROXINA SÓDICA 25MCG", kind="Medicamentos", unit="CPR"),
    qty_awarded=50000, unit_price=Decimal("0.16"), total_price=Decimal("8000.00"))

Award.objects.create(company=rioclarense, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.191", description="LEVOTIROXINA SÓDICA 50MCG", kind="Medicamentos", unit="CPR"),
    qty_awarded=50000, unit_price=Decimal("0.11"), total_price=Decimal("5500.00"))

Award.objects.create(company=rioclarense, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.193", description="LIDOCAINA GELEIA 2%", kind="Medicamentos", unit="TUB"),
    qty_awarded=600, unit_price=Decimal("5.00"), total_price=Decimal("3000.00"))

Award.objects.create(company=rioclarense, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.197", description="LOÇÃO OLEOSA À BASE DE ÁCIDOS GRAXOS ESSENCIAIS", kind="Medicamentos", unit="FRC"),
    qty_awarded=1000, unit_price=Decimal("2.76"), total_price=Decimal("2760.00"))

Award.objects.create(company=rioclarense, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.208", description="MELOXICAM 15MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=30000, unit_price=Decimal("0.119"), total_price=Decimal("3570.00"))

Award.objects.create(company=rioclarense, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.402", description="METILDOPA 250 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.32"), total_price=Decimal("3200.00"))

Award.objects.create(company=rioclarense, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.916", description="METILDOPA 500 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=3000, unit_price=Decimal("0.82"), total_price=Decimal("2460.00"))

Award.objects.create(company=rioclarense, tender=tender_med, 
    item=ItemCatalog.objects.create(code="006.001.673", description="MONTELUCASTE DE SÓDIO 4 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=3000, unit_price=Decimal("0.379"), total_price=Decimal("1137.00"))

Award.objects.create(company=rioclarense, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.966", description="OLANZAPINA 10 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=30000, unit_price=Decimal("0.359"), total_price=Decimal("10770.00"))

Award.objects.create(company=rioclarense, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.829", description="OLANZAPINA 2,5 MG", kind="Medicamentos", unit="UN"),
    qty_awarded=20000, unit_price=Decimal("0.15"), total_price=Decimal("3000.00"))

Award.objects.create(company=rioclarense, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.224", description="OMEPRAZOL 20MG", kind="Medicamentos", unit="CAP"),
    qty_awarded=200000, unit_price=Decimal("0.069"), total_price=Decimal("13800.00"))

Award.objects.create(company=rioclarense, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.532", description="QUETIAPINA 25 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=50000, unit_price=Decimal("0.12"), total_price=Decimal("6000.00"))

Award.objects.create(company=rioclarense, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.426", description="RISPERIDONA 1MG/ML SOL. ORAL", kind="Medicamentos", unit="FRC"),
    qty_awarded=500, unit_price=Decimal("9.95"), total_price=Decimal("4975.00")) 

Award.objects.create(company=rioclarense, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.491", description="ROSUVASTATINA 40 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("1.30"), total_price=Decimal("13000.00"))

Award.objects.create(company=rioclarense, tender=tender_med,
    item=ItemCatalog.objects.create(code="002.001.780", description="SULFATO DE AMICACINA 500 MG INJETÁVEL", kind="Medicamentos", unit="AMP"),
    qty_awarded=300, unit_price=Decimal("3.80"), total_price=Decimal("1140.00"))

Award.objects.create(company=rioclarense, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.275", description="VALPROATO DE SÓDIO 250MG/5ML XPE FRS/100 ML", kind="Medicamentos", unit="FRC"),
    qty_awarded=500, unit_price=Decimal("5.40"), total_price=Decimal("2700.00"))

# Garantir que o edital de medicamentos existe e buscar/criar a empresa
tender_med = Tender.objects.get_or_create(number="000016/25", kind="Medicamentos")[0]
rap = Company.objects.get_or_create(
    name="RAP APARECIDA COMERCIO DE MEDICAMENTOS LTDA",
    cnpj="06.968.107/0001-04",
    email="rap@drogaaparecida.com.br",
    phone="(14) 3811-8800",
    address="Rua Rodrigues Cesar, 174, Vila dos Lavradores, Botucatu-SP, CEP 18609-082"
)[0]

# Itens – Parte 1
Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.288", description="ACETATO DE RETINOL 5500UI/ML, COLECALCIFEROL 1000UI/ML", kind="Medicamentos", unit="FRC"),
    qty_awarded=600, unit_price=Decimal("8.86"), total_price=Decimal("5316.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.850", description="ACETILCISTEINA 20MG/ML XAROPE", kind="Medicamentos", unit="FRC"),
    qty_awarded=1000, unit_price=Decimal("3.95"), total_price=Decimal("3950.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.852", description="ACETILCISTEINA 600 MG GRANULADO", kind="Medicamentos", unit="ENV"),
    qty_awarded=100000, unit_price=Decimal("0.71"), total_price=Decimal("71000.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.293", description="ÁCIDO ASCÓRBICO 500MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("0.18"), total_price=Decimal("3600.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.853", description="ÁCIDO ASCÓRBICO GOTAS 200MG/ML", kind="Medicamentos", unit="FRC"),
    qty_awarded=300, unit_price=Decimal("1.45"), total_price=Decimal("435.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.308", description="ANLODIPINO 5MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=50000, unit_price=Decimal("0.027"), total_price=Decimal("1350.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.161", description="ATENOLOL 50MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=50000, unit_price=Decimal("0.049"), total_price=Decimal("2450.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.633", description="ATENOLOL+CLORTALIDONA 50MG/12,5MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.20"), total_price=Decimal("2000.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.275", description="AZITROMICINA 500MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=50000, unit_price=Decimal("0.72"), total_price=Decimal("36000.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.864", description="BILASTINA 20 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=3000, unit_price=Decimal("1.40"), total_price=Decimal("4200.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.236", description="BROMAZEPAM 3MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=30000, unit_price=Decimal("0.10"), total_price=Decimal("3000.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.317", description="CALCITRIOL 0,25 MCG CPS GEL", kind="Medicamentos", unit="CAP"),
    qty_awarded=10000, unit_price=Decimal("4.47"), total_price=Decimal("44700.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.637", description="CARBIDOPA+LEVODOPA 25/250 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=6000, unit_price=Decimal("0.64"), total_price=Decimal("3840.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.072", description="CARVEDILOL 3.125MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=6000, unit_price=Decimal("0.08"), total_price=Decimal("480.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.073", description="CARVEDILOL 6.25 MG", kind="Medicamentos", unit="CAP"),
    qty_awarded=20000, unit_price=Decimal("0.09"), total_price=Decimal("1800.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.871", description="CEFADROXILA 500 MG", kind="Medicamentos", unit="CAP"),
    qty_awarded=3000, unit_price=Decimal("1.77"), total_price=Decimal("5310.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.360", description="CETOPROFENO 150 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.58"), total_price=Decimal("5800.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.362", description="CIMICIFUGA 150 MG RACEMOSA", kind="Medicamentos", unit="CAP"),
    qty_awarded=1200, unit_price=Decimal("4.70"), total_price=Decimal("5640.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.326", description="CIPROFIBRATO 100 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=50000, unit_price=Decimal("0.29"), total_price=Decimal("14500.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.086", description="CLOBAZAM 20MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=5000, unit_price=Decimal("1.59"), total_price=Decimal("7950.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.492", description="CLONAZEPAM 0,5 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.052"), total_price=Decimal("520.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.364", description="CLOR.DE SÓDIO 0,9% GOTAS INFANTIL", kind="Medicamentos", unit="FR"),
    qty_awarded=1000, unit_price=Decimal("0.913"), total_price=Decimal("913.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.641", description="CLORIDRATO DE BROMEXINA 4MG/5 ML XAROPE", kind="Medicamentos", unit="FRC"),
    qty_awarded=500, unit_price=Decimal("7.80"), total_price=Decimal("3900.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.104", description="CLORIDRATO DE METFORMINA 500MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=60000, unit_price=Decimal("0.11"), total_price=Decimal("6600.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.877", description="CLORIDRATO DE NEBIVOLOL 5 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=6000, unit_price=Decimal("0.43"), total_price=Decimal("2580.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.111", description="CLORIDRATO DE PAROXETINA 20MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("0.19"), total_price=Decimal("3800.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.345", description="CODEINA 30 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=2000, unit_price=Decimal("0.85"), total_price=Decimal("1700.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.997", description="DAPAGLIFLOZINA 10 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=50000, unit_price=Decimal("5.60"), total_price=Decimal("280000.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.500", description="DESVENLAFAXINA 100 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("1.00"), total_price=Decimal("20000.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.506", description="DEXCLORFENIRAMINA 0,4MG/ML", kind="Medicamentos", unit="FRC"),
    qty_awarded=3000, unit_price=Decimal("1.78"), total_price=Decimal("5340.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.884", description="DEXPANTENOL GEL 50MG/G BISNAGAS 10G", kind="Medicamentos", unit="BG"),
    qty_awarded=100, unit_price=Decimal("48.00"), total_price=Decimal("4800.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.370", description="DOXICICLINA 100 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.51"), total_price=Decimal("5100.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.467", description="EMPAGLIFLOZINA 25 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("8.20"), total_price=Decimal("164000.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.153", description="ENALAPRIL 10MG, MALEATO DE", kind="Medicamentos", unit="CPR"),
    qty_awarded=30000, unit_price=Decimal("0.035"), total_price=Decimal("1050.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.154", description="ENALAPRIL 20MG, MALEATO DE", kind="Medicamentos", unit="CPR"),
    qty_awarded=50000, unit_price=Decimal("0.05"), total_price=Decimal("2500.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.254", description="ESCITALOPRAM 10MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=50000, unit_price=Decimal("0.12"), total_price=Decimal("6000.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.649", description="ESCITALOPRAM 15 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("0.22"), total_price=Decimal("4400.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.178", description="ESPIRONOLACTONA 25MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=50000, unit_price=Decimal("0.19"), total_price=Decimal("9500.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.468", description="EZETIMIBA 10 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=30000, unit_price=Decimal("0.48"), total_price=Decimal("14400.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.373", description="FENAZOPIRIDINA 200 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=6000, unit_price=Decimal("1.49"), total_price=Decimal("8940.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.374", description="FERRIPOLIMALTOSE 400 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=6000, unit_price=Decimal("1.87"), total_price=Decimal("11220.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.516", description="FEXOFENADINA SUSP. ORAL 6MG/60ML", kind="Medicamentos", unit="FRC"),
    qty_awarded=500, unit_price=Decimal("11.80"), total_price=Decimal("5900.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.376", description="FLUNARIZINA 10 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.09"), total_price=Decimal("900.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.895", description="FLUVOXAMINA 50 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=3000, unit_price=Decimal("2.09"), total_price=Decimal("6270.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.211", description="GALANTAMINA 24 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("4.80"), total_price=Decimal("48000.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.378", description="GALANTAMINA 8 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("3.40"), total_price=Decimal("34000.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.286", description="GLIMEPIRIDA 4MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=5000, unit_price=Decimal("0.17"), total_price=Decimal("850.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.520", description="HIALURONATO DE SÓDIO 0,15% 10 ML SOL. OFTÁLMICA", kind="Medicamentos", unit="FRC"),
    qty_awarded=200, unit_price=Decimal("39.00"), total_price=Decimal("7800.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.710", description="HIDROXIZINA 25MG C/30 CPR", kind="Medicamentos", unit="UN"),
    qty_awarded=2000, unit_price=Decimal("1.09"), total_price=Decimal("2180.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.387", description="IBUPROFENO 100MG/ML", kind="Medicamentos", unit="FRC"),
    qty_awarded=1000, unit_price=Decimal("1.90"), total_price=Decimal("1900.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.660", description="INDAPAMIDA 1,5 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.17"), total_price=Decimal("1700.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.391", description="INSULINA LANTUS SOLOSTAR (GLARGINA) 100UI", kind="Medicamentos", unit="CNT"),
    qty_awarded=500, unit_price=Decimal("51.00"), total_price=Decimal("25500.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.395", description="LEVODOPA+BENZERAZIDA HBS 100MG/25MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("2.90"), total_price=Decimal("29000.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.668", description="LUTEÍNA 10 MG + ZEAXANTINA 2 MG C/VITAMINAS", kind="Medicamentos", unit="CAP"),
    qty_awarded=3000, unit_price=Decimal("1.65"), total_price=Decimal("4950.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.403", description="METILFENIDATO 36 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("6.90"), total_price=Decimal("69000.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.388", description="METILFENIDATO 54 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=3000, unit_price=Decimal("6.90"), total_price=Decimal("20700.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.671", description="METILFENIDATO 10 MG LA", kind="Medicamentos", unit="CPR"),
    qty_awarded=3000, unit_price=Decimal("3.60"), total_price=Decimal("10800.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.527", description="METILFENIDATO 18 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=6000, unit_price=Decimal("5.27"), total_price=Decimal("31620.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.389", description="MONTELUCASTE DE SÓDIO 5 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=3000, unit_price=Decimal("0.439"), total_price=Decimal("1317.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.216", description="NIMESULIDA 100MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=50000, unit_price=Decimal("0.06"), total_price=Decimal("3000.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.965", description="NITRENDIPINO 10 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=3000, unit_price=Decimal("2.66"), total_price=Decimal("7980.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.409", description="NITRENDIPINO 20 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=3000, unit_price=Decimal("5.00"), total_price=Decimal("15000.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.231", description="PANTOPRAZOL SÓDICO 40MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=60000, unit_price=Decimal("0.15"), total_price=Decimal("9000.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.393", description="PASSIFLORA INCARNATA L 360 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("2.14"), total_price=Decimal("21400.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.236", description="PERMANGANATO DE POTÁSSIO 100MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=1000, unit_price=Decimal("0.50"), total_price=Decimal("500.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.238", description="POLIVITAMÍNICO DO COMPLEXO B", kind="Medicamentos", unit="CPR"),
    qty_awarded=50000, unit_price=Decimal("0.035"), total_price=Decimal("1750.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="002.001.774", description="PREGABALINA 150 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("0.36"), total_price=Decimal("7200.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="002.001.775", description="PREGABALINA 50 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.56"), total_price=Decimal("5600.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.403", description="ROSUVASTATINA 10 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=60000, unit_price=Decimal("0.17"), total_price=Decimal("10200.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.251", description="SAXAGLIPTINA 5MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("5.40"), total_price=Decimal("54000.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.794", description="SOTALOL 160 MG", kind="Medicamentos", unit="CX"),
    qty_awarded=2000, unit_price=Decimal("0.90"), total_price=Decimal("1800.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.971", description="SULFADIAZINA DE PRATA+NITRATO DE CÉRIO", kind="Medicamentos", unit="TUB"),
    qty_awarded=200, unit_price=Decimal("88.00"), total_price=Decimal("17600.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.409", description="SUPLEMENTO PARA GESTANTE", kind="Medicamentos", unit="FRC"),
    qty_awarded=500, unit_price=Decimal("9.89"), total_price=Decimal("4945.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.973", description="SULPIRIDA 50 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=6000, unit_price=Decimal("0.90"), total_price=Decimal("5400.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.539", description="TOPIRAMATO 25 MG", kind="Medicamentos", unit="CAP"),
    qty_awarded=20000, unit_price=Decimal("0.17"), total_price=Decimal("3400.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.277", description="VALSARTANA 320 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=100000, unit_price=Decimal("1.20"), total_price=Decimal("120000.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.943", description="VENLAFAXINA 37.5 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.30"), total_price=Decimal("3000.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.413", description="VILDAGLIPTINA 50MG+METFORMINA 1000 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=1200, unit_price=Decimal("1.23"), total_price=Decimal("1476.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.417", description="VITAMINA D3 2.000 UI", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.15"), total_price=Decimal("1500.00"))

Award.objects.create(company=rap, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.449", description="VITAMINAS E SAIS MINERAIS", kind="Medicamentos", unit="CPR"),
    qty_awarded=30000, unit_price=Decimal("0.06"), total_price=Decimal("1800.00"))

# Garantir que o edital de medicamentos existe e buscar/criar a empresa
tender_med = Tender.objects.get_or_create(number="000016/25", kind="Medicamentos")[0]
fragnari = Company.objects.get_or_create(
    name="FRAGNARI DISTRIBUIDORA DE MEDICAMENTOS LTDA",
    cnpj="14.271.474/0001-82",
    email="licitacoes@fragnari.com.br",
    phone="(14) 3814-0512 / (14) 3814-5572",
    address="Rua Manoel Deodoro Pinheiro Machado, 1218, Vila Santa Terezinha, Botucatu-SP, CEP 18606-710"
)[0]

# Itens – Parte 1
Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.854", description="ÁCIDO MEFENÂMICO 500 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=5000, unit_price=Decimal("0.43"), total_price=Decimal("2150.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.408", description="ALOPURINOL 100MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("0.12"), total_price=Decimal("2400.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.630", description="ALPRAZOLAM 0.5 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.06"), total_price=Decimal("600.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.483", description="BETAMETASONA+GENTAMICINA POMADA TBS/30", kind="Medicamentos", unit="TUB"),
    qty_awarded=200, unit_price=Decimal("6.199"), total_price=Decimal("1239.80"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.636", description="BROMETO DE ESCOPOLAMINA+PARACETAMOL 10 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=6000, unit_price=Decimal("1.45"), total_price=Decimal("8700.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.314", description="BUPROPIONA XL 300 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("3.03"), total_price=Decimal("30300.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.488", description="CEFTRIAXONA 500MG I.M", kind="Medicamentos", unit="FRC"),
    qty_awarded=1000, unit_price=Decimal("10.25"), total_price=Decimal("10250.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.322", description="CETOPROFENO 20MG/ML SOL. ORAL", kind="Medicamentos", unit="FRC"),
    qty_awarded=300, unit_price=Decimal("2.30"), total_price=Decimal("690.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.875", description="CIMETIDINA 200 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("0.36"), total_price=Decimal("7200.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.491", description="CLONAZEPAM 0,25 MG SL", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("0.273"), total_price=Decimal("5460.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.876", description="CLORETO DE POTÁSSIO 600 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=6000, unit_price=Decimal("0.815"), total_price=Decimal("4890.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.493", description="CLORIDRATO DE BUSPIRONA 10 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=3000, unit_price=Decimal("2.44"), total_price=Decimal("7320.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.994", description="CLORIDRATO DE PAROXETINA XR 25 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=6000, unit_price=Decimal("3.66"), total_price=Decimal("21960.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.366", description="COLÁGENO TIPO II", kind="Medicamentos", unit="FR"),
    qty_awarded=300, unit_price=Decimal("20.90"), total_price=Decimal("6270.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.496", description="CORIDRATO DE MOXIFLOXAXINO 5,45 MG/ML+ FO", kind="Medicamentos", unit="FRC"),
    qty_awarded=100, unit_price=Decimal("38.50"), total_price=Decimal("3850.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.497", description="CUMARINA+TROXERRUTINA 15/90 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=30000, unit_price=Decimal("0.32"), total_price=Decimal("9600.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.346", description="DABIGATRANA 110 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=1000, unit_price=Decimal("5.68"), total_price=Decimal("5680.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.347", description="DABIGATRANA 150 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=3000, unit_price=Decimal("5.68"), total_price=Decimal("17040.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.367", description="DAPAGLIFLOZINA+METFORMINA 10MG/1000 XR", kind="Medicamentos", unit="CPR"),
    qty_awarded=2000, unit_price=Decimal("7.68"), total_price=Decimal("15360.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.368", description="DAPAGLIFLOZINA+METFORMINA 5MG/1000 XR", kind="Medicamentos", unit="CPR"),
    qty_awarded=6000, unit_price=Decimal("3.86"), total_price=Decimal("23160.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.501", description="DESVENLAFAXINA 50 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.639"), total_price=Decimal("6390.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.369", description="DIACEREINA 50 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=2000, unit_price=Decimal("5.09"), total_price=Decimal("10180.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.356", description="DICLOFENACO DIETILAMÔNIO AEROSSOL 11,6 MG/G", kind="Medicamentos", unit="FRC"),
    qty_awarded=300, unit_price=Decimal("20.90"), total_price=Decimal("6270.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.510", description="DICLORIDRATO DE MANIDIPINO 10 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=2000, unit_price=Decimal("2.69"), total_price=Decimal("5380.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.886", description="DIMESILATO DE LISDEXANFETAMINA 70 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=2800, unit_price=Decimal("6.07"), total_price=Decimal("16996.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.465", description="DIMESILATO LISDEXANFETAMINA 50 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=2800, unit_price=Decimal("4.50"), total_price=Decimal("12600.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.144", description="DIOSMINA+HISPERIDINA 450/50 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=100000, unit_price=Decimal("0.38"), total_price=Decimal("38000.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.514", description="DIVALPROATO DE SÓDIO 500 MG ER", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.93"), total_price=Decimal("9300.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.359", description="DOXASOZINA 2MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=30000, unit_price=Decimal("0.086"), total_price=Decimal("2580.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.653", description="ESZOPICLONA 3 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=6000, unit_price=Decimal("3.37"), total_price=Decimal("20220.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.377", description="FUMARATO DE MOMETASONA 50 MCG SPRAY NASAL", kind="Medicamentos", unit="FRC"),
    qty_awarded=100, unit_price=Decimal("22.25"), total_price=Decimal("2225.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.656", description="FUROATO DE FLUTICASONA 27,5 MCG SPRAY NASAL", kind="Medicamentos", unit="FRC"),
    qty_awarded=100, unit_price=Decimal("62.00"), total_price=Decimal("6200.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.658", description="GLICINATO DE MAGNÉSIO (722,2 MG)+ CLORIDRATO DE PIRIDOXINA 1 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=6000, unit_price=Decimal("3.30"), total_price=Decimal("19800.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.659", description="HIDRALAZINA 50 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("0.578"), total_price=Decimal("11560.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.523", description="INSULINA DEGLUDECA+LIRAGLUTIDA", kind="Medicamentos", unit="CNT"),
    qty_awarded=300, unit_price=Decimal("281.30"), total_price=Decimal("84390.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.906", description="INSULINA NOVORAPID FLEXPEN", kind="Medicamentos", unit="CNT"),
    qty_awarded=100, unit_price=Decimal("57.70"), total_price=Decimal("5770.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.470", description="INSULINA SOLIQUA 10-40 SOLOSTAR", kind="Medicamentos", unit="CNT"),
    qty_awarded=100, unit_price=Decimal("210.15"), total_price=Decimal("21015.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.663", description="LEVETIRACETAM 100 MG/ML", kind="Medicamentos", unit="FRC"),
    qty_awarded=50, unit_price=Decimal("57.20"), total_price=Decimal("2860.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.664", description="LEVETIRACETAM 250 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=3000, unit_price=Decimal("0.66"), total_price=Decimal("1980.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.192", description="LEVOTIROXINA SÓDICA 75MCG", kind="Medicamentos", unit="CPR"),
    qty_awarded=50000, unit_price=Decimal("0.32"), total_price=Decimal("16000.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.524", description="LINAGLIPTINA 5 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=6000, unit_price=Decimal("3.70"), total_price=Decimal("22200.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.386", description="LINAGLIPTINA 2.5 MG+METFORMINA 1000 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=1200, unit_price=Decimal("2.05"), total_price=Decimal("2460.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.144", description="MIRTAZAPINA 15 MG", kind="Medicamentos", unit="CX"),
    qty_awarded=20000, unit_price=Decimal("0.65"), total_price=Decimal("13000.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.213", description="MONTELUCASTE DE SÓDIO 10MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=3000, unit_price=Decimal("0.375"), total_price=Decimal("1125.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.675", description="NARATRIPTANA 2,5 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("1.90"), total_price=Decimal("38000.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.676", description="NITAZOXANIDA 20MG/ML", kind="Medicamentos", unit="FRC"),
    qty_awarded=200, unit_price=Decimal("6.939"), total_price=Decimal("1387.80"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.413", description="OLMESARTANA 20 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=200000, unit_price=Decimal("0.479"), total_price=Decimal("95800.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.391", description="ORLISTAT 120 MG", kind="Medicamentos", unit="CX"),
    qty_awarded=200, unit_price=Decimal("89.00"), total_price=Decimal("17800.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.235", description="PERICIAZINA 4% FRS/20ML", kind="Medicamentos", unit="FRC"),
    qty_awarded=100, unit_price=Decimal("23.90"), total_price=Decimal("2390.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.394", description="PERINDOPRIL ARGININA 10MG+INDAPAMIDA 2,5", kind="Medicamentos", unit="CPR"),
    qty_awarded=3000, unit_price=Decimal("4.40"), total_price=Decimal("13200.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.929", description="POLICRESULENO 90 MG ÓVULOS CXS/6 ÓVULOS", kind="Medicamentos", unit="CX"),
    qty_awarded=100, unit_price=Decimal("22.69"), total_price=Decimal("2269.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.398", description="POLISSULFATO DE MUCOPOLISSACARIDEO 5MG/", kind="Medicamentos", unit="TUB"),
    qty_awarded=200, unit_price=Decimal("18.60"), total_price=Decimal("3720.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.399", description="PROGESTERONA MICRONIZADA 100 MG", kind="Medicamentos", unit="CAP"),
    qty_awarded=3000, unit_price=Decimal("2.10"), total_price=Decimal("6300.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.400", description="PROGESTERONA MICRONIZADA 200 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=3000, unit_price=Decimal("4.20"), total_price=Decimal("12600.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.424", description="QUETIAPINA XR 50 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=6000, unit_price=Decimal("2.30"), total_price=Decimal("13800.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="002.001.777", description="RAMIPRIL 5 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=6000, unit_price=Decimal("0.70"), total_price=Decimal("4200.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.935", description="ROSUVASTATINA 40 MG + EZETIMIBA 10 MG", kind="Medicamentos", unit="UN"),
    qty_awarded=3000, unit_price=Decimal("5.219"), total_price=Decimal("15657.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.248", description="SACCHAROMYCES BOULARDII 100 MG", kind="Medicamentos", unit="CAP"),
    qty_awarded=20000, unit_price=Decimal("0.86"), total_price=Decimal("17200.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.249", description="SACCHAROMYCES BOULARDII 200 MG", kind="Medicamentos", unit="SAC"),
    qty_awarded=10000, unit_price=Decimal("1.44"), total_price=Decimal("14400.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.407", description="SILIMARINA 200 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=3000, unit_price=Decimal("0.83"), total_price=Decimal("2490.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.969", description="SITAGLIPTINA + METFORMINA 50MG/1000 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=3000, unit_price=Decimal("1.71"), total_price=Decimal("5130.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.974", description="SULPIRIDA + BROMAZEPAM 25 MG / 1 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=6000, unit_price=Decimal("1.83"), total_price=Decimal("10980.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="002.001.782", description="TELMISARTANA 80 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=3000, unit_price=Decimal("1.10"), total_price=Decimal("3300.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.443", description="TELMISARTANA + ANLODIPINO 80MG/5MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=3000, unit_price=Decimal("4.79"), total_price=Decimal("14370.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.537", description="TOBRAMICINA + DEXAMETASONA 0,3% / 0,1% SOL. OFTÁLMICA", kind="Medicamentos", unit="FRC"),
    qty_awarded=600, unit_price=Decimal("34.19"), total_price=Decimal("20514.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="002.001.783", description="TRAZODONA RETARD 150 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("1.60"), total_price=Decimal("16000.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="002.001.785", description="TRIMETAZIDINA MR 35 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=30000, unit_price=Decimal("0.799"), total_price=Decimal("23970.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.944", description="VIMPOCETINA 5 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=3000, unit_price=Decimal("0.865"), total_price=Decimal("2595.00"))

Award.objects.create(company=fragnari, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.420", description="VORTIOXETINA 10 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=6000, unit_price=Decimal("2.179"), total_price=Decimal("13074.00"))

# Garantir que o edital de medicamentos existe e buscar/criar a empresa
tender_med = Tender.objects.get_or_create(number="000016/25", kind="Medicamentos")[0]
mamed = Company.objects.get_or_create(
    name="MAMED COMERCIAL LTDA - EPP",
    cnpj="21.608.296/0001-06",
    email="mamedvendas@gmail.com",
    phone="(14) 3667-3865",
    address="Rua Antartica, 850, Jardim Vitória, Marília-SP, CEP 17520-130"
)[0]

# Único item da MAMED
Award.objects.create(company=mamed, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.371", description="EMPAGLIFLOZINA 10 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=3000, unit_price=Decimal("5.75"), total_price=Decimal("17250.00"))

# Garantir que o edital de medicamentos existe e buscar/criar a empresa
tender_med = Tender.objects.get_or_create(number="000016/25", kind="Medicamentos")[0]
dimeva = Company.objects.get_or_create(
    name="DIMEVA DISTRIBUIDORA E IMPORTADORA LTDA",
    cnpj="76.386.283/0001-13",
    email="faturamento@dimeva.com.br",
    phone="(46) 3224-3767",
    address="Rua José Fraron, 155, Bairro Fraron, Pato Branco-PR, CEP 85503-320"
)[0]

# Itens – conforme PDF
Award.objects.create(company=dimeva, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.287", description="ACETATO DE CIPROTERONA 2MG, ETINILESTRADIOL 0,035MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("0.21"), total_price=Decimal("4200.00"))

Award.objects.create(company=dimeva, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.861", description="BETAISTINA 24 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("0.26"), total_price=Decimal("5200.00"))

Award.objects.create(company=dimeva, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.862", description="BETAISTINA 16 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=30000, unit_price=Decimal("0.22"), total_price=Decimal("6600.00"))

Award.objects.create(company=dimeva, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.462", description="CARBONATO DE LÍTIO CR 450 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("1.70"), total_price=Decimal("34000.00"))

Award.objects.create(company=dimeva, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.639", description="CILOSTAZOL 50 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=6000, unit_price=Decimal("0.24"), total_price=Decimal("1440.00"))

Award.objects.create(company=dimeva, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.992", description="CLORIDRATO DE MOXIFLOXACINO 400 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=3000, unit_price=Decimal("0.31"), total_price=Decimal("930.00"))

Award.objects.create(company=dimeva, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.349", description="DELTAMETRINA 0,02%", kind="Medicamentos", unit="FRC"),
    qty_awarded=600, unit_price=Decimal("4.48"), total_price=Decimal("2688.00"))

Award.objects.create(company=dimeva, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.361", description="DULOXETINA 30 MG", kind="Medicamentos", unit="CAP"),
    qty_awarded=30000, unit_price=Decimal("0.95"), total_price=Decimal("28500.00"))

Award.objects.create(company=dimeva, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.648", description="DULOXETINA 60 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=30000, unit_price=Decimal("1.42"), total_price=Decimal("42600.00"))

Award.objects.create(company=dimeva, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.890", description="FENOBARBITAL 100 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.18"), total_price=Decimal("1800.00"))

Award.objects.create(company=dimeva, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.184", description="LEVOFLOXACINO 500 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.63"), total_price=Decimal("6300.00"))

Award.objects.create(company=dimeva, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.926", description="NITROFURANTOINA 100 MG", kind="Medicamentos", unit="CAP"),
    qty_awarded=10000, unit_price=Decimal("0.25"), total_price=Decimal("2500.00"))

Award.objects.create(company=dimeva, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.266", description="SULFATO DE NEOMICINA+BACITRACINA 5MG/G+250UI/G", kind="Medicamentos", unit="TUB"),
    qty_awarded=3000, unit_price=Decimal("2.12"), total_price=Decimal("6360.00"))

Award.objects.create(company=dimeva, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.278", description="VARFARINA SÓDICA 5 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.16"), total_price=Decimal("1600.00"))

Award.objects.create(company=dimeva, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.421", description="ZOLPIDEM 10 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=30000, unit_price=Decimal("0.10"), total_price=Decimal("3000.00"))

# Garantir que o edital de medicamentos existe e buscar/criar a empresa
tender_med = Tender.objects.get_or_create(number="000016/25", kind="Medicamentos")[0]
dora = Company.objects.get_or_create(
    name="DORA MEDICAMENTOS LTDA EPP",
    cnpj="30.936.479/0001-33",
    email="licitacao@triunfal.com.br",
    phone="(14) 3413-5243",
    address="Avenida Silvio Bertonha, 533, Parque das Indústrias, Marília-SP, CEP 17519-690"
)[0]

# Itens – conforme PDF
Award.objects.create(company=dora, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.865", description="BISACODIL 5MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=5000, unit_price=Decimal("0.149"), total_price=Decimal("745.00"))

Award.objects.create(company=dora, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.489", description="CIPROFLOXACINO+HIDROCORTISONA SUSP. OTOLÓGICA", kind="Medicamentos", unit="FRC"),
    qty_awarded=300, unit_price=Decimal("18.19"), total_price=Decimal("5457.00"))

Award.objects.create(company=dora, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.666", description="LIRAGLUTIDA SOLUÇÃO INJETÁVEL 6 MG/ML CXS", kind="Medicamentos", unit="CX"),
    qty_awarded=100, unit_price=Decimal("314.99"), total_price=Decimal("31499.00"))

Award.objects.create(company=dora, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.211", description="MONONITRATO DE ISOSSORBIDA 40MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=50000, unit_price=Decimal("0.41"), total_price=Decimal("20500.00"))

Award.objects.create(company=dora, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.357", description="RISPERIDONA 3 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=6000, unit_price=Decimal("0.14"), total_price=Decimal("840.00"))

# Garantir que o edital de medicamentos existe e buscar/criar a empresa
tender_med = Tender.objects.get_or_create(number="000016/25", kind="Medicamentos")[0]
comercial_mark = Company.objects.get_or_create(
    name="COMERCIAL MARK ATACADISTA EIRELI",
    cnpj="09.315.996/0001-07",
    email="comercialmark@outlook.com,  faturamento.mark@outlook.com, licitacao.mark@outlook.com",
    phone="(44) 3528-5085",
    address="Rua Presidente Costa e Silva, 231, Centro, Assis Chateaubriand-PR, CEP 85935-000"
)[0]

# Itens – conforme PDF
Award.objects.create(company=comercial_mark, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.353", description="ACEBROFILINA 25MG/5ML", kind="Medicamentos", unit="UN"),
    qty_awarded=3000, unit_price=Decimal("4.71"), total_price=Decimal("14130.00"))

Award.objects.create(company=comercial_mark, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.289", description="ACICLOVIR 50MG/G", kind="Medicamentos", unit="TUB"),
    qty_awarded=600, unit_price=Decimal("2.36"), total_price=Decimal("1416.00"))

Award.objects.create(company=comercial_mark, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.631", description="ALPRAZOLAM 2 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("0.12"), total_price=Decimal("2400.00"))

Award.objects.create(company=comercial_mark, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.306", description="AMOX+CLAVULANATO 250MG+62,50MG/5ML", kind="Medicamentos", unit="FRC"),
    qty_awarded=3000, unit_price=Decimal("15.65"), total_price=Decimal("46950.00"))

Award.objects.create(company=comercial_mark, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.041", description="AMPICILINA 500MG", kind="Medicamentos", unit="CAP"),
    qty_awarded=2000, unit_price=Decimal("0.48"), total_price=Decimal("960.00"))

Award.objects.create(company=comercial_mark, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.859", description="ATORVASTATINA CÁLCICA 20 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=30000, unit_price=Decimal("0.16"), total_price=Decimal("4800.00"))

Award.objects.create(company=comercial_mark, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.860", description="ATORVASTATINA CÁLCICA 40 MG", kind="Medicamentos", unit="CAP"),
    qty_awarded=30000, unit_price=Decimal("0.43"), total_price=Decimal("12900.00"))

Award.objects.create(company=comercial_mark, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.634", description="BISOPROLOL 1,25 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=3000, unit_price=Decimal("0.25"), total_price=Decimal("750.00"))

Award.objects.create(company=comercial_mark, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.635", description="BISOPROLOL 2,5 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=6000, unit_price=Decimal("0.28"), total_price=Decimal("1680.00"))

Award.objects.create(company=comercial_mark, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.054", description="BUDESONIDA 32MCG", kind="Medicamentos", unit="FRC"),
    qty_awarded=500, unit_price=Decimal("13.20"), total_price=Decimal("6600.00"))

Award.objects.create(company=comercial_mark, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.071", description="CARVEDILOL 12,5 MG", kind="Medicamentos", unit="CAP"),
    qty_awarded=20000, unit_price=Decimal("0.08"), total_price=Decimal("1600.00"))

Award.objects.create(company=comercial_mark, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.874", description="CILOSTAZOL 100 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.42"), total_price=Decimal("4200.00"))

Award.objects.create(company=comercial_mark, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.363", description="CLARITROMICINA 250 MG/5ML SUSP.", kind="Medicamentos", unit="FR"),
    qty_awarded=200, unit_price=Decimal("56.64"), total_price=Decimal("11328.00"))

Award.objects.create(company=comercial_mark, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.428", description="CLARITROMICINA 500MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=3000, unit_price=Decimal("1.70"), total_price=Decimal("5100.00"))

Award.objects.create(company=comercial_mark, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.878", description="CLORIDRATO DE ONDANSETRONA 4 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.25"), total_price=Decimal("2500.00"))

Award.objects.create(company=comercial_mark, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.110", description="CLORIDRATO DE ONDANSETRONA 8MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.29"), total_price=Decimal("2900.00"))

Award.objects.create(company=comercial_mark, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.998", description="DESLORATADINA 0,5 MG/ML", kind="Medicamentos", unit="FRC"),
    qty_awarded=1000, unit_price=Decimal("6.85"), total_price=Decimal("6850.00"))

Award.objects.create(company=comercial_mark, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.503", description="DEXAMETASONA 4,0 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=1000, unit_price=Decimal("0.18"), total_price=Decimal("180.00"))

Award.objects.create(company=comercial_mark, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.147", description="DIVALPROATO DE SÓDIO 250MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("0.63"), total_price=Decimal("12600.00"))

Award.objects.create(company=comercial_mark, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.888", description="ESCITALOPRAM 20 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("0.18"), total_price=Decimal("3600.00"))

Award.objects.create(company=comercial_mark, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.365", description="ESPIRONOLACTONA 50 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.31"), total_price=Decimal("3100.00"))

Award.objects.create(company=comercial_mark, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.375", description="FINASTERIDA 5 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=3000, unit_price=Decimal("0.24"), total_price=Decimal("720.00"))

Award.objects.create(company=comercial_mark, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.380", description="GINKO BILOBA 80 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.28"), total_price=Decimal("2800.00"))

Award.objects.create(company=comercial_mark, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.079", description="HIDROCLOROTIAZIDA 25 MG 20 COMP.", kind="Medicamentos", unit="CPR"),
    qty_awarded=100000, unit_price=Decimal("0.02"), total_price=Decimal("2000.00"))

Award.objects.create(company=comercial_mark, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.181", description="IVERMECTINA 6 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.30"), total_price=Decimal("3000.00"))

Award.objects.create(company=comercial_mark, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.382", description="LAMOTRIGINA 100 MG CPR", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.18"), total_price=Decimal("1800.00"))

Award.objects.create(company=comercial_mark, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.915", description="MEMANTINA 10 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.18"), total_price=Decimal("1800.00"))

Award.objects.create(company=comercial_mark, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.210", description="MONONITRATO DE ISOSSORBIDA 20MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=50000, unit_price=Decimal("0.19"), total_price=Decimal("9500.00"))

Award.objects.create(company=comercial_mark, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.827", description="OLANZAPINA 5 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=30000, unit_price=Decimal("0.27"), total_price=Decimal("8100.00"))

Award.objects.create(company=comercial_mark, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.232", description="PARACETAMOL SOL. ORAL 200MG/ML FRS/15 ML", kind="Medicamentos", unit="FRC"),
    qty_awarded=5000, unit_price=Decimal("1.30"), total_price=Decimal("6500.00"))

Award.objects.create(company=comercial_mark, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.968", description="PIOGLITAZONA 30 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=6000, unit_price=Decimal("0.81"), total_price=Decimal("4860.00"))

Award.objects.create(company=comercial_mark, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.418", description="POLIVITAMINICO DO COMPLEXO B GTS", kind="Medicamentos", unit="FRC"),
    qty_awarded=200, unit_price=Decimal("2.18"), total_price=Decimal("436.00"))

Award.objects.create(company=comercial_mark, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.423", description="QUETIAPINA 100 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("0.41"), total_price=Decimal("8200.00"))

Award.objects.create(company=comercial_mark, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.401", description="QUETIAPINA 200 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("0.79"), total_price=Decimal("15800.00"))

Award.objects.create(company=comercial_mark, tender=tender_med,
    item=ItemCatalog.objects.create(code="002.001.778", description="RIVAROXABANA 10 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("0.19"), total_price=Decimal("3800.00"))

Award.objects.create(company=comercial_mark, tender=tender_med,
    item=ItemCatalog.objects.create(code="002.001.779", description="RIVAROXABANA 15 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.23"), total_price=Decimal("2300.00"))

Award.objects.create(company=comercial_mark, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.254", description="SINVASTATINA 40 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("0.14"), total_price=Decimal("2800.00"))

Award.objects.create(company=comercial_mark, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.408", description="SULFAMETOXAZOL 200 MG+TRIMETROPIMA 40MG", kind="Medicamentos", unit="FRC"),
    qty_awarded=500, unit_price=Decimal("3.38"), total_price=Decimal("1690.00"))

Award.objects.create(company=comercial_mark, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.442", description="TANSULOSINA 0,4 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("0.65"), total_price=Decimal("13000.00"))

Award.objects.create(company=comercial_mark, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.410", description="TIABENDAZOL 50MG/G", kind="Medicamentos", unit="TUB"),
    qty_awarded=300, unit_price=Decimal("7.49"), total_price=Decimal("2247.00"))

Award.objects.create(company=comercial_mark, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.538", description="TOPIRAMATO 100 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("0.34"), total_price=Decimal("6800.00"))

Award.objects.create(company=comercial_mark, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.540", description="TOPIRAMATO 50 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("0.21"), total_price=Decimal("4200.00"))

Award.objects.create(company=comercial_mark, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.279", description="VENLAFAXINA 150 MG", kind="Medicamentos", unit="CAP"),
    qty_awarded=20000, unit_price=Decimal("0.76"), total_price=Decimal("15200.00"))

# Garantir que o edital de medicamentos existe e buscar/criar a empresa
tender_med = Tender.objects.get_or_create(number="000016/25", kind="Medicamentos")[0]
interlab = Company.objects.get_or_create(
    name="INTERLAB FARMACEUTICA LTDA",
    cnpj="43.295.831/0001-40",
    email="elcio@interlab.com.br",
    phone="(11) 2997-9177 / (11) 2204-5996",
    address="Av. Água Fria, 981/985, São Paulo-SP, CEP 02333-001"
)[0]

# Itens – 006.001.458 até 006.003.418
Award.objects.create(company=interlab, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.458", description="ÁCIDO TIÓCTICO 600 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=1000, unit_price=Decimal("5.47"), total_price=Decimal("5470.00"))

Award.objects.create(company=interlab, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.484", description="CARBAMAZEPINA CR 400 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=6000, unit_price=Decimal("2.84"), total_price=Decimal("17040.00"))

Award.objects.create(company=interlab, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.495", description="CLORIDRATO DE LURASIDONA 20 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=6000, unit_price=Decimal("4.65"), total_price=Decimal("27900.00"))

Award.objects.create(company=interlab, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.392", description="INSULINA LISPRO HUMALOG KWIK PEN", kind="Medicamentos", unit="CNT"),
    qty_awarded=200, unit_price=Decimal("36.05"), total_price=Decimal("7210.00"))

Award.objects.create(company=interlab, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.404", description="SACUBITRIL VALSARTANA 100 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("4.22"), total_price=Decimal("84400.00"))

Award.objects.create(company=interlab, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.405", description="SACUBITRIL VALSARTANA 50 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("4.22"), total_price=Decimal("84400.00"))

Award.objects.create(company=interlab, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.406", description="SACUBITRIL VALSARTANA 200 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("4.22"), total_price=Decimal("42200.00"))

Award.objects.create(company=interlab, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.415", description="VITAMINA D3 1.000 UI", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.23"), total_price=Decimal("2300.00"))

Award.objects.create(company=interlab, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.416", description="VITAMINA D3 10.000 UI", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.42"), total_price=Decimal("4200.00"))

Award.objects.create(company=interlab, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.418", description="VITAMINA D3 5.000 UI", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.24"), total_price=Decimal("2400.00"))

# Garantir que o edital de medicamentos existe e buscar/criar a empresa
tender_med = Tender.objects.get_or_create(number="000016/25", kind="Medicamentos")[0]
classmed = Company.objects.get_or_create(
    name="CLASSMED PRODUTOS HOSPITALARES LTDA",
    cnpj="01.328.535/0001-59",
    email="classmed@outlook.com.br",
    phone="(43) 3275-3105",
    address="Rua Pica Pau, 1211, Centro, Arapongas-PR, CEP 86700-100"
)[0]

# Itens – conforme edital
Award.objects.create(company=classmed, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.297", description="ÁCIDO TRANEXÂMICO 250MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=3000, unit_price=Decimal("1.41"), total_price=Decimal("4230.00"))

Award.objects.create(company=classmed, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.477", description="ÁGUA DESTILADA 300 FRS/1000 ML", kind="Medicamentos", unit="FRC"),
    qty_awarded=300, unit_price=Decimal("8.09"), total_price=Decimal("2427.00"))

Award.objects.create(company=classmed, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.036", description="ALPRAZOLAM 1MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("0.079"), total_price=Decimal("1580.00"))

Award.objects.create(company=classmed, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.863", description="BETAMETASONA POMADA 1MG/G", kind="Medicamentos", unit="TUB"),
    qty_awarded=100, unit_price=Decimal("8.69"), total_price=Decimal("869.00"))

Award.objects.create(company=classmed, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.461", description="BISOPROLOL 5 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.299"), total_price=Decimal("2990.00"))

Award.objects.create(company=classmed, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.320", description="CARVEDILOL 25MG", kind="Medicamentos", unit="CAP"),
    qty_awarded=30000, unit_price=Decimal("0.149"), total_price=Decimal("4470.00"))

Award.objects.create(company=classmed, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.359", description="CEFTRIAXONA 1G I.M", kind="Medicamentos", unit="FR"),
    qty_awarded=600, unit_price=Decimal("6.50"), total_price=Decimal("3900.00"))

Award.objects.create(company=classmed, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.082", description="CETOPROFENO 50MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("0.249"), total_price=Decimal("4980.00"))

Award.objects.create(company=classmed, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.088", description="CLORETO DE POTÁSSIO 19,1% AMP/10ML", kind="Medicamentos", unit="AMP"),
    qty_awarded=100, unit_price=Decimal("0.46"), total_price=Decimal("46.00"))

Award.objects.create(company=classmed, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.091", description="CLORIDRATO DE AMBROXOL 30 MG/5 ML", kind="Medicamentos", unit="FRC"),
    qty_awarded=3000, unit_price=Decimal("2.599"), total_price=Decimal("7797.00"))

Award.objects.create(company=classmed, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.097", description="CLORIDRATO DE CLOMIPRAMINA 25MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("1.099"), total_price=Decimal("21980.00"))

Award.objects.create(company=classmed, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.100", description="CLORIDRATO DE CLORPROMAZINA 25MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.38"), total_price=Decimal("3800.00"))

Award.objects.create(company=classmed, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.365", description="CLORIDRATO DE CLORPROMAZINA 40MG SOLUÇÃO/FR", kind="Medicamentos", unit="FR"),
    qty_awarded=100, unit_price=Decimal("9.358"), total_price=Decimal("935.80"))

Award.objects.create(company=classmed, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.889", description="FENITOINA SÓDICA 50MG/ML IV/IM", kind="Medicamentos", unit="AMP"),
    qty_awarded=50, unit_price=Decimal("2.86"), total_price=Decimal("143.00"))

Award.objects.create(company=classmed, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.367", description="FENOBARBITAL 40 MG/ML GOTAS", kind="Medicamentos", unit="FRC"),
    qty_awarded=200, unit_price=Decimal("4.439"), total_price=Decimal("887.80"))

Award.objects.create(company=classmed, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.380", description="GLICOSE 25% SOLUÇÃO INJETÁVEL AMP/10ML", kind="Medicamentos", unit="AMP"),
    qty_awarded=200, unit_price=Decimal("0.62"), total_price=Decimal("124.00"))

Award.objects.create(company=classmed, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.381", description="GLICOSE 50% SOLUÇÃO INJETÁVEL AMP/10ML", kind="Medicamentos", unit="AMP"),
    qty_awarded=200, unit_price=Decimal("0.68"), total_price=Decimal("136.00"))

Award.objects.create(company=classmed, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.171", description="HALOPERIDOL 2MG/ML SOL. ORAL FRS/20ML", kind="Medicamentos", unit="FRC"),
    qty_awarded=300, unit_price=Decimal("3.739"), total_price=Decimal("1121.70"))

Award.objects.create(company=classmed, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.382", description="HALOPERIDOL DECANOATO 70,52MG/ML SOL. INJETÁVEL", kind="Medicamentos", unit="AMP"),
    qty_awarded=200, unit_price=Decimal("6.399"), total_price=Decimal("1279.80"))

Award.objects.create(company=classmed, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.386", description="HIDRÓXIDO DE ALUMÍNIO 60 MG/ML SUSP. FRS/100ML", kind="Medicamentos", unit="FRC"),
    qty_awarded=600, unit_price=Decimal("2.479"), total_price=Decimal("1487.40"))

Award.objects.create(company=classmed, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.200", description="LORAZEPAM 2MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.139"), total_price=Decimal("1390.00"))

Award.objects.create(company=classmed, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.670", description="METILFENIDATO 10 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("0.33"), total_price=Decimal("6600.00"))

Award.objects.create(company=classmed, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.917", description="MIRTAZAPINA 30 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.65"), total_price=Decimal("6500.00"))

Award.objects.create(company=classmed, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.212", description="MONONITRATO DE ISOSSORBIDA 5MG SL", kind="Medicamentos", unit="CPR"),
    qty_awarded=3000, unit_price=Decimal("0.35"), total_price=Decimal("1050.00"))

Award.objects.create(company=classmed, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.921", description="NALTREXONA 50 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("4.03"), total_price=Decimal("80600.00"))

Award.objects.create(company=classmed, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.925", description="NITRATO DE MICONAZOL CREME VAGINAL", kind="Medicamentos", unit="TUB"),
    qty_awarded=300, unit_price=Decimal("9.499"), total_price=Decimal("2849.70"))

Award.objects.create(company=classmed, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.412", description="OLEO MINERAL 100 ML", kind="Medicamentos", unit="FRC"),
    qty_awarded=600, unit_price=Decimal("3.129"), total_price=Decimal("1877.40"))

Award.objects.create(company=classmed, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.234", description="PENTOXIFILINA 400MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("1.899"), total_price=Decimal("18990.00"))

Award.objects.create(company=classmed, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.246", description="RIVAROXABANA 20 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("0.279"), total_price=Decimal("5580.00"))

Award.objects.create(company=classmed, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.402", description="ROSUVASTATINA 20 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=60000, unit_price=Decimal("0.24"), total_price=Decimal("14400.00"))

Award.objects.create(company=classmed, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.434", description="SOL. GLICOSADA 5% S.F - I.V FRS/500 ML", kind="Medicamentos", unit="FRC"),
    qty_awarded=200, unit_price=Decimal("5.107"), total_price=Decimal("1021.40"))

Award.objects.create(company=classmed, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.262", description="SOLUÇÃO RINGER SEM LACTATO FRS/500 ML", kind="Medicamentos", unit="FRC"),
    qty_awarded=200, unit_price=Decimal("4.899"), total_price=Decimal("979.80"))

Award.objects.create(company=classmed, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.263", description="SUCCINATO DE METOPROLOL 25 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=30000, unit_price=Decimal("0.249"), total_price=Decimal("7470.00"))

Award.objects.create(company=classmed, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.264", description="SUCCINATO DE METOPROLOL 50 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=50000, unit_price=Decimal("0.41"), total_price=Decimal("20500.00"))

Award.objects.create(company=classmed, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.938", description="SULFATO DE MORFINA 10 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=3000, unit_price=Decimal("0.84"), total_price=Decimal("2520.00"))

Award.objects.create(company=classmed, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.411", description="TIAMAZOL 10 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=5000, unit_price=Decimal("0.489"), total_price=Decimal("2445.00"))

Award.objects.create(company=classmed, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.412", description="TIAMAZOL 5 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=3000, unit_price=Decimal("0.26"), total_price=Decimal("780.00"))                                    

# Garantir que o edital de medicamentos existe e buscar/criar a empresa
tender_med = Tender.objects.get_or_create(number="000016/25", kind="Medicamentos")[0]
soma_sp = Company.objects.get_or_create(
    name="SOMA/SP PRODUTOS HOSPITALARES LTDA",
    cnpj="05.847.630/0001-10",
    email="soma.sp@somahospitalar.com.br",
    phone="(11) 4122-9800",
    address="Estrada Samuel Aizemberg, 100, Bairro Alves Dias, São Bernardo do Campo-SP, CEP 09851-550"
)[0]

# Itens – conforme edital
Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.291", description="ÁCIDO ASCÓRBICO 100MG/ML", kind="Medicamentos", unit="AMP"),
    qty_awarded=2000, unit_price=Decimal("0.74"), total_price=Decimal("1480.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.295", description="ÁCIDO FÓLICO 5MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=5000, unit_price=Decimal("0.03"), total_price=Decimal("150.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.298", description="ÁCIDO TRANEXÂMICO 250MG SOLUÇÃO INJETÁVEL", kind="Medicamentos", unit="AMP"),
    qty_awarded=1000, unit_price=Decimal("3.90"), total_price=Decimal("3900.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.459", description="ÁGUA P/INJEÇÃO", kind="Medicamentos", unit="FRC"),
    qty_awarded=5000, unit_price=Decimal("0.195"), total_price=Decimal("975.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.031", description="ALBENDAZOL 400MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=3000, unit_price=Decimal("0.439"), total_price=Decimal("1317.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.032", description="ALBENDAZOL 40MG/ML FRS/10ML", kind="Medicamentos", unit="FRC"),
    qty_awarded=3000, unit_price=Decimal("1.11"), total_price=Decimal("3330.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.011", description="ALOPURINOL 300MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=30000, unit_price=Decimal("0.23"), total_price=Decimal("6900.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.857", description="AMOXICILINA 500 MG", kind="Medicamentos", unit="CAP"),
    qty_awarded=20000, unit_price=Decimal("0.20"), total_price=Decimal("4000.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.481", description="ARIPIPRAZOL 10 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.395"), total_price=Decimal("3950.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.632", description="ARIPIPRAZOL 15 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=60000, unit_price=Decimal("0.40"), total_price=Decimal("24000.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.048", description="BROMETO DE IPRATROPIO 0,250MG/ML FRS/20 ML", kind="Medicamentos", unit="FRC"),
    qty_awarded=500, unit_price=Decimal("1.00"), total_price=Decimal("500.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.053", description="BROMOPRIDA 4MG/ML FRS/20ML", kind="Medicamentos", unit="FRC"),
    qty_awarded=2000, unit_price=Decimal("2.00"), total_price=Decimal("4000.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.313", description="BROMOPRIDA 5MG/ML SOLUÇÃO INJETÁVEL", kind="Medicamentos", unit="AMP"),
    qty_awarded=2000, unit_price=Decimal("1.15"), total_price=Decimal("2300.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.315", description="BUTIL BROMETO DE ESCOPOLAMINA 6,67MG/ML", kind="Medicamentos", unit="FRC"),
    qty_awarded=500, unit_price=Decimal("5.50"), total_price=Decimal("2750.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.060", description="BUTILBROMETO DE ESCOPOLAMINA 20MG/ML", kind="Medicamentos", unit="AMP"),
    qty_awarded=1000, unit_price=Decimal("1.00"), total_price=Decimal("1000.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.316", description="BUTILBROMETO DE ESCOPOLAMINA + DIPIRONA", kind="Medicamentos", unit="AMP"),
    qty_awarded=1000, unit_price=Decimal("1.42"), total_price=Decimal("1420.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.165", description="CARBAMAZEPINA 200 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("0.16"), total_price=Decimal("3200.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.064", description="CARBAMAZEPINA 20MG/ML SUSP.ORAL FRS/100ML", kind="Medicamentos", unit="FRC"),
    qty_awarded=500, unit_price=Decimal("7.00"), total_price=Decimal("3500.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.358", description="CARBOCISTEÍNA 20 MG/ML XPE", kind="Medicamentos", unit="FR"),
    qty_awarded=1000, unit_price=Decimal("3.30"), total_price=Decimal("3300.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.357", description="CARBOCISTEÍNA 50 MG/ML XPE", kind="Medicamentos", unit="FR"),
    qty_awarded=1000, unit_price=Decimal("4.55"), total_price=Decimal("4550.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.070", description="CARBONATO DE CÁLCIO 600MG; COLECALCIFEROL 400MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("0.05"), total_price=Decimal("1000.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.336", description="CARBONATO DE LÍTIO 300MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=6000, unit_price=Decimal("0.21"), total_price=Decimal("1260.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.638", description="CARMELOSE SÓDICA 5MG/ML SOL. OFT.", kind="Medicamentos", unit="FRC"),
    qty_awarded=300, unit_price=Decimal("6.95"), total_price=Decimal("2085.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.486", description="CEFALEXINA 250 MG SUSP.", kind="Medicamentos", unit="FRC"),
    qty_awarded=600, unit_price=Decimal("10.00"), total_price=Decimal("6000.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.487", description="CEFTRIAXONA 1G I.V", kind="Medicamentos", unit="FRC"),
    qty_awarded=600, unit_price=Decimal("4.40"), total_price=Decimal("2640.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.321", description="CETOCONAZOL CREME 20MG/G", kind="Medicamentos", unit="TUB"),
    qty_awarded=1000, unit_price=Decimal("2.80"), total_price=Decimal("2800.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.323", description="CETOPROFENO 50MG/ML - I.M SOLUÇÃO INJETÁVEL", kind="Medicamentos", unit="AMP"),
    qty_awarded=5000, unit_price=Decimal("1.18"), total_price=Decimal("5900.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.361", description="CIANOCOBALAMINA 2500 MCG/ML", kind="Medicamentos", unit="AMP"),
    qty_awarded=3000, unit_price=Decimal("6.80"), total_price=Decimal("20400.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.330", description="CLONAZEPAM 2.5 MG/ML GOTAS", kind="Medicamentos", unit="FRC"),
    qty_awarded=200, unit_price=Decimal("2.12"), total_price=Decimal("424.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.096", description="CLORIDRATO DE CIPROFLOXACINO 500MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("0.16"), total_price=Decimal("3200.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.103", description="CLORIDRATO DE LIDOCAÍNA S/V 2% FRS/20ML", kind="Medicamentos", unit="FRC"),
    qty_awarded=200, unit_price=Decimal("3.83"), total_price=Decimal("766.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.991", description="CLORIDRATO DE METFORMINA 500 MG XR", kind="Medicamentos", unit="CPR"),
    qty_awarded=100000, unit_price=Decimal("0.15"), total_price=Decimal("15000.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.106", description="CLORIDRATO DE METFORMINA 850 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=100000, unit_price=Decimal("0.109"), total_price=Decimal("10900.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.117", description="CLORIDRATO DE SERTRALINA 50MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=30000, unit_price=Decimal("0.10"), total_price=Decimal("3000.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.119", description="CLORIDRATO DE TIAMINA 300MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=30000, unit_price=Decimal("0.24"), total_price=Decimal("7200.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.120", description="CLORIDRATO DE TRAMADOL 50 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=30000, unit_price=Decimal("0.12"), total_price=Decimal("3600.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.122", description="CLORIDRATO DE PROPAFENONA 300MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=6000, unit_price=Decimal("0.559"), total_price=Decimal("3354.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.883", description="DEXAMETASONA 1MG/G CREME", kind="Medicamentos", unit="TUB"),
    qty_awarded=1000, unit_price=Decimal("1.65"), total_price=Decimal("1650.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.130", description="DEXAMETASONA 2MG/ML, FOSFATO DISSÓDICO", kind="Medicamentos", unit="AMP"),
    qty_awarded=5000, unit_price=Decimal("0.70"), total_price=Decimal("3500.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.133", description="DIAZEPAM 5MG/ML AMP/2ML", kind="Medicamentos", unit="AMP"),
    qty_awarded=200, unit_price=Decimal("0.78"), total_price=Decimal("156.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.134", description="DICLOFENACO SÓDICO 50 MG", kind="Medicamentos", unit="CAP"),
    qty_awarded=30000, unit_price=Decimal("0.05"), total_price=Decimal("1500.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.145", description="DIPIRONA SÓDICA 500MG/ML FRS/10 ML", kind="Medicamentos", unit="FRC"),
    qty_awarded=10000, unit_price=Decimal("1.17"), total_price=Decimal("11700.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.357", description="DIPIRONA SÓDICA 500MG/ML SOLUÇÃO INJETÁVEL", kind="Medicamentos", unit="AMP"),
    qty_awarded=5000, unit_price=Decimal("0.65"), total_price=Decimal("3250.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.372", description="ENOXAPARINA SÓDICA 40 MG/0,4 ML", kind="Medicamentos", unit="UN"),
    qty_awarded=600, unit_price=Decimal("13.90"), total_price=Decimal("8340.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.363", description="EPINEFRINA 1MG/ML", kind="Medicamentos", unit="AMP"),
    qty_awarded=300, unit_price=Decimal("1.00"), total_price=Decimal("300.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.190", description="FLUCONAZOL 150MG", kind="Medicamentos", unit="CAP"),
    qty_awarded=10000, unit_price=Decimal("0.43"), total_price=Decimal("4300.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.374", description="FOSFATO SÓDICO DE PREDNISOLONA 3 MG/ML", kind="Medicamentos", unit="FRC"),
    qty_awarded=5000, unit_price=Decimal("4.00"), total_price=Decimal("20000.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.375", description="FUROSEMIDA 10 MG/ML", kind="Medicamentos", unit="AMP"),
    qty_awarded=1000, unit_price=Decimal("0.64"), total_price=Decimal("640.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.379", description="GENTAMICINA 40 MG/ML", kind="Medicamentos", unit="AMP"),
    qty_awarded=200, unit_price=Decimal("1.00"), total_price=Decimal("200.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.383", description="HIDROCORTISONA 500 MG I.M/I.V", kind="Medicamentos", unit="FRC"),
    qty_awarded=600, unit_price=Decimal("4.50"), total_price=Decimal("2700.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.194", description="IBUPROFENO 600 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=100000, unit_price=Decimal("0.13"), total_price=Decimal("13000.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.383", description="LAMOTRIGINA 25 MG CP", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.129"), total_price=Decimal("1290.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.384", description="LAMOTRIGINA 50 MG CPR", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.169"), total_price=Decimal("1690.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.387", description="LORATADINA 1 MG/ML XAROPE", kind="Medicamentos", unit="FRC"),
    qty_awarded=6000, unit_price=Decimal("2.82"), total_price=Decimal("16920.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.672", description="MIRTAZAPINA 45 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.889"), total_price=Decimal("8890.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.219", description="NISTATINA CR. VG 25.000 UI/G TBS 60G", kind="Medicamentos", unit="TUB"),
    qty_awarded=1000, unit_price=Decimal("6.24"), total_price=Decimal("6240.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.220", description="NISTATINA SUSP. ORAL 100.000 UI/ML FRS/50 ML", kind="Medicamentos", unit="FRC"),
    qty_awarded=300, unit_price=Decimal("4.95"), total_price=Decimal("1485.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.206", description="NORFLOXACINO 400 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.309"), total_price=Decimal("3090.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.390", description="OMEPRAZOL SÓDICO 40 MG C/ DILUENTE DE 20 MG", kind="Medicamentos", unit="FRC"),
    qty_awarded=500, unit_price=Decimal("8.70"), total_price=Decimal("4350.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.417", description="PARACETAMOL 500 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=30000, unit_price=Decimal("0.06"), total_price=Decimal("1800.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.239", description="POLIVITAMINICO DO COMPLEXO B AMP/2ML", kind="Medicamentos", unit="AMP"),
    qty_awarded=5000, unit_price=Decimal("0.98"), total_price=Decimal("4900.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.192", description="PREDNISONA 20 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=30000, unit_price=Decimal("0.15"), total_price=Decimal("4500.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.421", description="PREGABALINA 75 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=30000, unit_price=Decimal("0.209"), total_price=Decimal("6270.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.208", description="RISPERIDONA 1 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=30000, unit_price=Decimal("0.09"), total_price=Decimal("2700.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.209", description="RISPERIDONA 2 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=30000, unit_price=Decimal("0.10"), total_price=Decimal("3000.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.428", description="SACARATO DE HIDRÓXIDO FÉRRICO 20 MG/ML I.V", kind="Medicamentos", unit="AMP"),
    qty_awarded=1000, unit_price=Decimal("10.20"), total_price=Decimal("10200.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.432", description="SOL. CLORETO DE SÓDIO 0,9% S.F - I.V FRS/100 ML", kind="Medicamentos", unit="FRC"),
    qty_awarded=5000, unit_price=Decimal("3.20"), total_price=Decimal("16000.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.260", description="SOL. CLORETO DE SÓDIO 0,9% FRS/10 ML", kind="Medicamentos", unit="FRC"),
    qty_awarded=2000, unit_price=Decimal("0.20"), total_price=Decimal("400.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.972", description="SULFATO DE SALBUTAMOL 100 MCG/DOSE AEROSOL", kind="Medicamentos", unit="FRC"),
    qty_awarded=300, unit_price=Decimal("10.99"), total_price=Decimal("3297.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.977", description="TOBRAMICINA 3 MG/ML SOL. OFTÁLMICA", kind="Medicamentos", unit="FRC"),
    qty_awarded=300, unit_price=Decimal("4.50"), total_price=Decimal("1350.00"))

Award.objects.create(company=soma_sp, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.419", description="VITAMINA D3 7.000 UI", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.18"), total_price=Decimal("1800.00"))

# Garantir que o edital de medicamentos existe e criar/buscar a empresa
tender_med = Tender.objects.get_or_create(number="000016/25", kind="Medicamentos")[0]
dimaster = Company.objects.get_or_create(
    name="DIMASTER - COMERCIO DE PRODUTOS HOSPITALARES LTDA",
    cnpj="02.520.829/0004-93",
    email="pregao@dimaster.com.br, licitacao2@dimaster.com.br, faturamento@dimaster.com.br",
    phone="(054) 3523-2600",
    address="Av. Cumbica, nº 429, Bairro Cidade Industrial de São Paulo, Guarulhos-SP, CEP 07223-300"
)[0]

Award.objects.create(company=dimaster, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.851", description="ACETILCISTEINA 40MG/ML XAROPE", kind="Medicamentos", unit="FRC"),
    qty_awarded=1000, unit_price=Decimal("4.37"), total_price=Decimal("4370.00"))

Award.objects.create(company=dimaster, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.213", description="ACICLOVIR 200MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.169"), total_price=Decimal("1690.00"))

Award.objects.create(company=dimaster, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.027", description="ÁCIDO URSODESOXICÓLICO 300 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=2000, unit_price=Decimal("1.60"), total_price=Decimal("3200.00"))

Award.objects.create(company=dimaster, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.215", description="AMIODARONA 200MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("0.35"), total_price=Decimal("7000.00"))

Award.objects.create(company=dimaster, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.040", description="AMOX+CLAVULANATO POTÁSSIO 500 MG+125 MG", kind="Medicamentos", unit="CAP"),
    qty_awarded=30000, unit_price=Decimal("1.00"), total_price=Decimal("30000.00"))

Award.objects.create(company=dimaster, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.855", description="AMOXICILINA + CLAVULANATO 872 MG+125 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=50000, unit_price=Decimal("1.80"), total_price=Decimal("90000.00"))

Award.objects.create(company=dimaster, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.856", description="AMOXICILINA 250MG/5ML SUSP.", kind="Medicamentos", unit="FRC"),
    qty_awarded=1000, unit_price=Decimal("5.40"), total_price=Decimal("5400.00"))

Award.objects.create(company=dimaster, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.355", description="AXETILCEFUROXIMA 250 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=3000, unit_price=Decimal("2.59"), total_price=Decimal("7770.00"))

Award.objects.create(company=dimaster, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.003.356", description="AXETILCEFUROXIMA 500 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=3000, unit_price=Decimal("3.54"), total_price=Decimal("10620.00"))

Award.objects.create(company=dimaster, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.043", description="AZITROMICINA 200MG/5ML SUSP. FRS/15ML", kind="Medicamentos", unit="FRC"),
    qty_awarded=3000, unit_price=Decimal("7.07"), total_price=Decimal("21210.00"))

Award.objects.create(company=dimaster, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.047", description="BISSULFATO DE CLOPIDOGREL 75 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("0.24"), total_price=Decimal("4800.00"))

Award.objects.create(company=dimaster, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.050", description="BROMIDRATO DE CITALOPRAM 20MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("0.099"), total_price=Decimal("1980.00"))

Award.objects.create(company=dimaster, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.057", description="BUPROPIONA LIBERAÇÃO PROLONGADA 150 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=30000, unit_price=Decimal("0.36"), total_price=Decimal("10800.00"))

Award.objects.create(company=dimaster, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.059", description="BUTILBROMETO DE ESCOPALAMINA 10 MG, DIPIRONA 250 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=30000, unit_price=Decimal("0.25"), total_price=Decimal("7500.00"))

Award.objects.create(company=dimaster, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.085", description="CINARIZINA 75 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.32"), total_price=Decimal("3200.00"))

Award.objects.create(company=dimaster, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.087", description="CLONAZEPAM 2MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=60000, unit_price=Decimal("0.049"), total_price=Decimal("2940.00"))

Award.objects.create(company=dimaster, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.000.902", description="DIPIRONA 500 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=200000, unit_price=Decimal("0.11"), total_price=Decimal("22000.00"))

Award.objects.create(company=dimaster, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.649", description="DONEPEZILA 10 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=3000, unit_price=Decimal("0.35"), total_price=Decimal("1050.00"))

Award.objects.create(company=dimaster, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.887", description="DONEPEZILA 5 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=2000, unit_price=Decimal("0.30"), total_price=Decimal("600.00"))

Award.objects.create(company=dimaster, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.364", description="ESOMEPRAZOL MAGNÉSICO 40 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=6000, unit_price=Decimal("1.00"), total_price=Decimal("6000.00"))

Award.objects.create(company=dimaster, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.169", description="GLICLAZIDA 30MG LIBERAÇÃO PROLONGADA", kind="Medicamentos", unit="CPR"),
    qty_awarded=200000, unit_price=Decimal("0.12"), total_price=Decimal("24000.00"))

Award.objects.create(company=dimaster, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.393", description="LACTULOSE 667MG/ML", kind="Medicamentos", unit="FRC"),
    qty_awarded=1000, unit_price=Decimal("3.69"), total_price=Decimal("3690.00"))

Award.objects.create(company=dimaster, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.002.277", description="LEVOMEPROMAZINA 100MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("0.62"), total_price=Decimal("12400.00"))

Award.objects.create(company=dimaster, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.215", description="NIFEDIPINO 20MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=20000, unit_price=Decimal("0.09"), total_price=Decimal("1800.00"))

Award.objects.create(company=dimaster, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.226", description="OXCARBAZEPINA 300MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=10000, unit_price=Decimal("0.67"), total_price=Decimal("6700.00"))

Award.objects.create(company=dimaster, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.233", description="PARACETAMOL+FOSFATO DE CODEINA 500/30MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=50000, unit_price=Decimal("0.34"), total_price=Decimal("17000.00"))

Award.objects.create(company=dimaster, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.425", description="RIFAMICINA SPRAY", kind="Medicamentos", unit="FRC"),
    qty_awarded=1000, unit_price=Decimal("4.14"), total_price=Decimal("4140.00"))

Award.objects.create(company=dimaster, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.430", description="SOL. CLORETO DE SÓDIO 0,9% S.F - I.V FRS/250 ML", kind="Medicamentos", unit="FRC"),
    qty_awarded=5000, unit_price=Decimal("3.80"), total_price=Decimal("19000.00"))

Award.objects.create(company=dimaster, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.431", description="SOL. CLORETO DE SÓDIO 0,9% S.F - I.V FRS/500 ML", kind="Medicamentos", unit="FRC"),
    qty_awarded=5000, unit_price=Decimal("4.37"), total_price=Decimal("21850.00"))

Award.objects.create(company=dimaster, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.265", description="SULFADIAZINA DE PRATA CREME 10 MG/G TBS 50 G", kind="Medicamentos", unit="TUB"),
    qty_awarded=1000, unit_price=Decimal("6.48"), total_price=Decimal("6840.00"))

Award.objects.create(company=dimaster, tender=tender_med,
    item=ItemCatalog.objects.create(code="006.001.280", description="VENLAFAXINA 75 MG", kind="Medicamentos", unit="CPR"),
    qty_awarded=30000, unit_price=Decimal("0.339"), total_price=Decimal("10170.00"))

