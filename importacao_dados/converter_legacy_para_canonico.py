import csv
import sys
from pathlib import Path

def load_map(path, key):
    with Path(path).open("r", encoding="utf-8-sig", newline="") as f:
        r = csv.DictReader(f)
        return {row[key].strip().lower(): row for row in r}

def main(input_csv, companies_csv, tenders_csv, output_csv):
    companies = load_map(companies_csv, "alias")
    tenders = load_map(tenders_csv, "alias")

    with Path(input_csv).open("r", encoding="utf-8-sig", newline="") as fin, \
         Path(output_csv).open("w", encoding="utf-8", newline="") as fout:

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
            if alias not in companies:
                raise ValueError(f"{input_csv} linha {i}: empresa '{alias}' não mapeada em companies.csv")
            if tender_alias not in tenders:
                raise ValueError(f"{input_csv} linha {i}: tender '{tender_alias}' não mapeado em tenders.csv")

            comp = companies[alias]
            tend = tenders[tender_alias]

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

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Uso: python converter_legacy_para_canonico.py <entrada.csv> <companies.csv> <tenders.csv> <saida.csv>")
        sys.exit(1)
    main(*sys.argv[1:])