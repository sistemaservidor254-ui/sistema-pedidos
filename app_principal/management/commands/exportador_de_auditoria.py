# save as: export_awards.py (exemplo de snippet para Django shell)
import csv
from pathlib import Path
from app_principal.models import Award

OUT = Path("audit_awards_export.csv")
with OUT.open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow([
        "tender_number","tender_kind",
        "company_name","cnpj","email","phone","address",
        "code","description","unit",
        "qty_awarded","unit_price","total_price"
    ])
    for a in Award.objects.select_related("tender","company","item").all():
        w.writerow([
            a.tender.number, a.tender.kind,
            a.company.name, getattr(a.company, "cnpj", ""), a.company.email, a.company.phone, getattr(a.company, "address", ""),
            a.item.code, a.item.description, a.item.unit,
            a.qty_awarded, f"{a.unit_price}", f"{a.total_price}",
        ])