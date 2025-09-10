import csv
import re
from decimal import Decimal, InvalidOperation
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from app_principal.models import Tender, Company, ItemCatalog, Award


REQUIRED_HEADERS = [
    "code", "description", "unit", "qty", "unit_price",
    "company_name", "cnpj", "email", "phone", "address"
]


def to_decimal(value) -> Decimal:
    """Converte valores para Decimal, tratando formatos brasileiros."""
    if value is None:
        return Decimal("0")
    if isinstance(value, (int, float, Decimal)):
        return Decimal(str(value))
    s = (
        str(value)
        .strip()
        .replace("R$", "")
        .replace(" ", "")
        .replace(".", "")    # remove milhar
        .replace(",", ".")   # vírgula -> ponto
    )
    try:
        return Decimal(s)
    except InvalidOperation:
        raise CommandError(f"Valor decimal inválido: {value!r}")


def normalize_cnpj(cnpj: str) -> str:
    """Remove caracteres não numéricos do CNPJ."""
    return re.sub(r"\D", "", cnpj or "")


class Command(BaseCommand):
    help = (
        "Migra dados dos editais (Medicamentos 000016/25, Enfermagem 000027/25) a partir de arquivos CSV.\n"
        "Cabeçalhos: code, description, unit, qty, unit_price, company_name, cnpj, email, phone, address, "
        "[tender_number], [tender_kind]. "
        "Se tender_number/kind não vierem, o comando tenta inferir pelo nome do arquivo."
    )

    def add_arguments(self, parser):
        parser.add_argument("--data-dir", default="data", help="Diretório com os CSVs (default: ./data)")
        parser.add_argument("--dry-run", action="store_true", help="Valida sem gravar no banco")
        parser.add_argument("--default-tender-number", default=None, help="Ex: 000016/25")
        parser.add_argument("--default-tender-kind", default=None, help="Ex: Medicamentos")

    def handle(self, *args, **opts):
        data_dir = Path(opts["data_dir"])
        if not data_dir.exists():
            raise CommandError(f"Diretório não encontrado: {data_dir}")

        csv_files = list(data_dir.glob("*.csv"))
        if not csv_files:
            raise CommandError(f"Nenhum CSV encontrado em {data_dir}")

        total_rows = 0
        created_awards = 0
        updated_awards = 0

        for csv_path in csv_files:
            self.stdout.write(self.style.NOTICE(f"Lendo: {csv_path.name}"))
            inferred_number, inferred_kind = self._infer_tender_from_filename(csv_path.name)

            with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
                reader = csv.DictReader(f)
                headers = [h.strip() for h in (reader.fieldnames or [])]

                missing = [h for h in REQUIRED_HEADERS if h not in headers]
                if missing:
                    raise CommandError(f"{csv_path.name}: faltam colunas obrigatórias: {', '.join(missing)}")

                for i, row in enumerate(reader, start=2):
                    total_rows += 1

                    code = (row.get("code") or "").strip()
                    description = (row.get("description") or "").strip()
                    unit = (row.get("unit") or "").strip()

                    try:
                        qty = int(Decimal(str(row.get("qty") or "0")).to_integral_value())
                    except InvalidOperation:
                        raise CommandError(f"{csv_path.name} linha {i}: quantidade inválida: {row.get('qty')}")

                    unit_price = to_decimal(row.get("unit_price"))
                    total_price = unit_price * Decimal(qty)

                    company_name = (row.get("company_name") or "").strip()
                    cnpj = normalize_cnpj(row.get("cnpj"))
                    email = (row.get("email") or "").strip()
                    phone = (row.get("phone") or "").strip()
                    address = (row.get("address") or "").strip()

                    tender_number = (
                        (row.get("tender_number") or "").strip()
                        or (opts.get("default_tender_number") or "")
                        or (inferred_number or "")
                    )
                    tender_kind = (
                        (row.get("tender_kind") or "").strip()
                        or (opts.get("default_tender_kind") or "")
                        or (inferred_kind or "")
                    )
                    if not tender_number or not tender_kind:
                        raise CommandError(f"{csv_path.name} linha {i}: tender_number/kind ausentes e não inferidos.")

                    if opts["dry_run"]:
                        self.stdout.write(
                            f"  [DRY-RUN] {tender_number} - {company_name} - {code} - {qty} x {unit_price}"
                        )
                        continue

                    # Tender
                    tender, _ = Tender.objects.get_or_create(number=tender_number, kind=tender_kind)

                    # Company
                    company, _ = Company.objects.get_or_create(
                        cnpj=cnpj,
                        defaults={"name": company_name, "email": email, "phone": phone, "address": address}
                    )
                    updates = {}
                    if company.name != company_name and company_name:
                        updates["name"] = company_name
                    if company.email != email:
                        updates["email"] = email
                    if company.phone != phone:
                        updates["phone"] = phone
                    if getattr(company, "address", "") != address:
                        updates["address"] = address
                    if updates:
                        for k, v in updates.items():
                            setattr(company, k, v)
                        company.save(update_fields=list(updates.keys()))

                    # ItemCatalog
                    item, _ = ItemCatalog.objects.get_or_create(
                        code=code, kind=tender.kind,
                        defaults={"description": description, "unit": unit},
                    )
                    item_updates = {}
                    if item.description != description and description:
                        item_updates["description"] = description
                    if item.unit != unit and unit:
                        item_updates["unit"] = unit
                    if item_updates:
                        for k, v in item_updates.items():
                            setattr(item, k, v)
                        item.save(update_fields=list(item_updates.keys()))

                    # Award
                    award, created = Award.objects.get_or_create(
                        tender=tender, company=company, item=item,
                        defaults={"qty_awarded": qty, "unit_price": unit_price, "total_price": total_price}
                    )
                    if created:
                        created_awards += 1
                    else:
                        changed = False
                        if award.qty_awarded != qty:
                            award.qty_awarded = qty
                            changed = True
                        if award.unit_price != unit_price:
                            award.unit_price = unit_price
                            changed = True
                        # Recalcula total_price sempre que qty ou unit_price mudarem
                        new_total = award.unit_price * Decimal(award.qty_awarded)
                        if award.total_price != new_total:
                            award.total_price = new_total
                            changed = True
                        if changed:
                            award.save(update_fields=["qty_awarded", "unit_price", "total_price"])
                            updated_awards += 1

            self.stdout.write(self.style.SUCCESS(f"Concluído: {csv_path.name}"))

        self.stdout.write(self.style.SUCCESS(
            f"Linhas lidas: {total_rows} | Awards criados: {created_awards} | Awards atualizados: {updated_awards}"
        ))

    def _infer_tender_from_filename(self, filename: str):
        name = filename.lower()
        number = None
        kind = None
        if "000016" in name or "16_25" in name or "016_25" in name:
            number = "000016/25"
            kind = "Medicamentos"
        elif "000027" in name or "27_25" in name or "027_25" in name:
            number = "000027/25"
            kind = "Itens de Enfermagem"
        return number, kind