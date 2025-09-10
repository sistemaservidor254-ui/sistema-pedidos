import csv
from pathlib import Path

# Mapeie aqui todos os apelidos de empresa -> dados completos
COMPANIES = {
    "lumar": {
        "company_name": "LUMAR COMÉRCIO DE PRODUTOS FARMACÊUTICOS LTDA",
        "cnpj": "49.228.695/0001-52",
        "email": "licitacoes@lumarfranca.com.br",
        "phone": "(16) 3721-1102",
        "address": "Av. Wilson Bego, 745, Distrito Industrial Antônio Della Torres, Franca-SP, CEP 14406-091",
    },
    # adicione aqui as demais empresas...
}

# Mapeie apelidos de edital -> número e tipo
TENDERS = {
    "tender_enf": {"tender_number": "000027/25", "tender_kind": "Itens de Enfermagem"},
    "tender_med": {"tender_number": "000016/25", "tender_kind": "Medicamentos"},
}

INPUT = Path("entrada_legacy.csv")
OUTPUT = Path("saida_canonico.csv")

with INPUT.open("r", encoding="utf-8-sig", newline="") as fin, \
     OUTPUT.open("w", encoding="utf-8", newline="") as fout:

    reader = csv.DictReader(fin)
    fieldnames = [
        "code","description","unit","qty","unit_price",
        "company_name","cnpj","email","phone","address",
        "tender_number","tender_kind"
    ]
    writer = csv.DictWriter(fout, fieldnames=fieldnames)
    writer.writeheader()

    for i, row in enumerate(reader, start=2):
        alias = (row.get("company") or "").strip().lower()
        tender_alias = (row.get("tender") or "").strip().lower()

        if alias not in COMPANIES:
            raise ValueError(f"Linha {i}: empresa '{alias}' sem mapeamento em COMPANIES")
        if tender_alias not in TENDERS:
            raise ValueError(f"Linha {i}: tender '{tender_alias}' sem mapeamento em TENDERS")

        comp = COMPANIES[alias]
        tend = TENDERS[tender_alias]

        writer.writerow({
            "code": (row.get("code") or "").strip(),
            "description": (row.get("description") or "").strip(),
            "unit": (row.get("unit") or "").strip(),
            "qty": (row.get("qty_awarded") or "").strip(),
            "unit_price": (row.get("unit_price") or "").strip(),
            "company_name": comp["company_name"],
            "cnpj": comp["cnpj"],
            "email": comp["email"],
            "phone": comp["phone"],
            "address": comp["address"],
            "tender_number": tend["tender_number"],
            "tender_kind": tend["tender_kind"],
        })