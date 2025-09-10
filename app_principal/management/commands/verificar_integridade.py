from django.core.management.base import BaseCommand
from django.db.models import Count
from django.db import transaction
from app_principal.models import Edital, Fornecedor, ItemLicitado
from datetime import datetime
import os


class Command(BaseCommand):
    help = "Verifica integridade dos dados, corrige duplicatas e gera log detalhado."

    def handle(self, *args, **options):
        # Criar pasta de logs se não existir
        logs_dir = os.path.join(os.getcwd(), "logs_integridade")
        os.makedirs(logs_dir, exist_ok=True)

        # Nome do arquivo de log com data/hora
        log_file = os.path.join(
            logs_dir, f"log_integridade_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        )

        with open(log_file, "w", encoding="utf-8") as log:
            log.write(f"=== VERIFICAÇÃO DE INTEGRIDADE ===\n")
            log.write(f"Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n")

            self.stdout.write(
                self.style.MIGRATE_HEADING("🔍 Verificando integridade dos dados...\n")
            )
            log.write("🔍 Verificando integridade dos dados...\n\n")

            log.write(f"📄 Editais: {Edital.objects.count()}\n")
            log.write(f"🏢 Fornecedores: {Fornecedor.objects.count()}\n")
            log.write(f"📦 Itens licitados: {ItemLicitado.objects.count()}\n\n")

            self.corrigir_editais(log)
            self.corrigir_fornecedores(log)
            self.corrigir_itens(log)

            self.stdout.write(
                self.style.MIGRATE_HEADING("\n✔️ Verificação e correção concluídas.")
            )
            log.write("\n✔️ Verificação e correção concluídas.\n")

        self.stdout.write(self.style.SUCCESS(f"📁 Log salvo em: {log_file}"))

    @transaction.atomic
    def corrigir_editais(self, log):
        dups = Edital.objects.values("numero").annotate(n=Count("id")).filter(n__gt=1)
        if not dups:
            self.stdout.write(self.style.SUCCESS("✅ Nenhum edital duplicado."))
            log.write("✅ Nenhum edital duplicado.\n")
            return

        self.stdout.write(self.style.ERROR("⚠️ Corrigindo editais duplicados..."))
        log.write("⚠️ Corrigindo editais duplicados...\n")
        for dup in dups:
            numero = dup["numero"]
            registros = list(Edital.objects.filter(numero=numero).order_by("id"))
            manter = registros[0]
            remover = registros[1:]
            self.stdout.write(
                f"   - Número: {numero} | Mantendo ID {manter.id}, removendo {[r.id for r in remover]}"
            )
            log.write(
                f"   - Número: {numero} | Mantendo ID {manter.id}, removendo {[r.id for r in remover]}\n"
            )
            ItemLicitado.objects.filter(edital__in=remover).update(edital=manter)
            for r in remover:
                r.delete()
        self.stdout.write(self.style.SUCCESS("✅ Editais duplicados corrigidos."))
        log.write("✅ Editais duplicados corrigidos.\n")

    @transaction.atomic
    def corrigir_fornecedores(self, log):
        dups = Fornecedor.objects.values("cnpj").annotate(n=Count("id")).filter(n__gt=1)
        if not dups:
            self.stdout.write(self.style.SUCCESS("✅ Nenhum fornecedor duplicado."))
            log.write("✅ Nenhum fornecedor duplicado.\n")
            return

        self.stdout.write(self.style.ERROR("⚠️ Corrigindo fornecedores duplicados..."))
        log.write("⚠️ Corrigindo fornecedores duplicados...\n")
        for dup in dups:
            cnpj = dup["cnpj"]
            registros = list(Fornecedor.objects.filter(cnpj=cnpj).order_by("id"))
            manter = registros[0]
            remover = registros[1:]
            self.stdout.write(
                f"   - CNPJ: {cnpj} | Mantendo ID {manter.id}, removendo {[r.id for r in remover]}"
            )
            log.write(
                f"   - CNPJ: {cnpj} | Mantendo ID {manter.id}, removendo {[r.id for r in remover]}\n"
            )
            ItemLicitado.objects.filter(fornecedor__in=remover).update(
                fornecedor=manter
            )
            for r in remover:
                r.delete()
        self.stdout.write(self.style.SUCCESS("✅ Fornecedores duplicados corrigidos."))
        log.write("✅ Fornecedores duplicados corrigidos.\n")

    @transaction.atomic
    def corrigir_itens(self, log):
        dups = (
            ItemLicitado.objects.values("edital_id", "codigo")
            .annotate(n=Count("id"))
            .filter(n__gt=1)
        )
        if not dups:
            self.stdout.write(self.style.SUCCESS("✅ Nenhum item duplicado."))
            log.write("✅ Nenhum item duplicado.\n")
            return

        self.stdout.write(self.style.ERROR("⚠️ Corrigindo itens duplicados..."))
        log.write("⚠️ Corrigindo itens duplicados...\n")
        for dup in dups:
            edital_id = dup["edital_id"]
            codigo = dup["codigo"]
            registros = list(
                ItemLicitado.objects.filter(
                    edital_id=edital_id, codigo=codigo
                ).order_by("id")
            )
            manter = registros[0]
            remover = registros[1:]
            self.stdout.write(
                f"   - Edital ID: {edital_id} | Código: {codigo} | Mantendo ID {manter.id}, removendo {[r.id for r in remover]}"
            )
            log.write(
                f"   - Edital ID: {edital_id} | Código: {codigo} | Mantendo ID {manter.id}, removendo {[r.id for r in remover]}\n"
            )
            for r in remover:
                r.delete()
        self.stdout.write(self.style.SUCCESS("✅ Itens duplicados corrigidos."))
        log.write("✅ Itens duplicados corrigidos.\n")
