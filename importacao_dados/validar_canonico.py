import csv, sys
from decimal import Decimal, InvalidOperation
from pathlib import Path

REQUIRED = ["code","description","unit","qty","unit_price",
            "company_name","cnpj","email","phone","address",
            "tender_number","tender_kind"]

def to_dec(s):
    s = (s or "").strip().replace("R$","").replace(" ","").replace(".","").replace(",",".")
    return Decimal(s or "0")

def main(path):
    with Path(path).open("r", encoding="utf-8-sig", newline="") as f:
        r = csv.DictReader(f)
        miss = [h for h in REQUIRED if h not in (r.fieldnames or [])]
        if miss: raise SystemExit(f"Faltam colunas: {', '.join(miss)}")
        seen = set()
        for i, row in enumerate(r, start=2):
            key = (row["tender_number"], row["tender_kind"], row["company_name"], row["code"])
            if key in seen:
                print(f"Aviso linha {i}: duplicata para {key}")
            seen.add(key)
            try:
                q = int(Decimal(row["qty"]).to_integral_value())
                p = to_dec(row["unit_price"])
                _ = q * p
            except (InvalidOperation, ValueError) as e:
                raise SystemExit(f"Linha {i}: erro em qty/unit_price: {e}")
        print("Validação OK.")

if __name__ == "__main__":
    main(sys.argv[1])