from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from pathlib import Path
from django.utils import timezone
import os

from app_principal.models import MovimentoEstoque, ItemLicitado, Fornecedor
from app_principal.storage.mega_cmd import enviar_para_mega

# Bibliotecas do Google Drive (pydrive2)
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive


def enviar_para_google_drive(caminho_arquivo, nome_arquivo, pasta_id=None):
    """
    Envia um arquivo para o Google Drive usando conta de serviço.
    Retorna o link público do arquivo.
    """
    gauth = GoogleAuth()
    # Carrega credenciais da conta de serviço (JSON baixado do Google Cloud)
    gauth.LoadServiceConfigFile("credenciais_drive.json")
    drive = GoogleDrive(gauth)

    # Cria o arquivo no Drive
    arquivo = drive.CreateFile(
        {"title": nome_arquivo, "parents": [{"id": pasta_id}] if pasta_id else []}
    )
    arquivo.SetContentFile(caminho_arquivo)
    arquivo.Upload()

    # Torna o arquivo público para leitura
    arquivo.InsertPermission({"type": "anyone", "value": "anyone", "role": "reader"})

    return f"https://drive.google.com/file/d/{arquivo['id']}/view"

    def handle(self, *args, **options):
        """
        Método principal do comando.
        """
        caminho_arquivo = options.get("arquivo")

        # 1️⃣ Valida se o arquivo foi informado e existe
        if not caminho_arquivo or not os.path.exists(caminho_arquivo):
            self.stdout.write(self.style.ERROR("Arquivo não encontrado."))
            return

        # 2️⃣ Aqui você faria o parsing real do XML/PDF para extrair dados
        # Por enquanto, vamos simular com dados fictícios:
        item = ItemLicitado.objects.first()
        fornecedor = Fornecedor.objects.first()
        quantidade = 10
        numero_documento = "NF-TESTE-001"
        data_movimento = timezone.now()

        # 3️⃣ Cria o registro no banco
        movimento = MovimentoEstoque.objects.create(
            item=item,
            tipo="ENTRADA",
            quantidade=quantidade,
            fornecedor=fornecedor,
            documento=numero_documento,
            data_movimento=data_movimento,
        )

        # 4️⃣ Salva o arquivo localmente no FileField
        nome_arquivo = Path(caminho_arquivo).name
        with open(caminho_arquivo, "rb") as f:
            movimento.arquivo_nf.save(nome_arquivo, ContentFile(f.read()), save=True)

        # 5️⃣ Envia para o MEGA
        try:
            link_mega = enviar_para_mega(movimento.arquivo_nf.path, pasta_destino="/NF")
            if link_mega:
                movimento.arquivo_nf_url = link_mega
                movimento.save(update_fields=["arquivo_nf_url"])
                self.stdout.write(
                    self.style.SUCCESS(f"NF-e enviada para o MEGA: {link_mega}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        "NF-e salva localmente, mas não foi possível gerar link no MEGA."
                    )
                )
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Erro ao enviar para o MEGA: {e}"))

        # 6️⃣ Envia para o Google Drive
        try:
            link_drive = enviar_para_google_drive(
                movimento.arquivo_nf.path,
                nome_arquivo,
                pasta_id=None,  # Coloque o ID da pasta se quiser organizar
            )
            movimento.arquivo_nf_url_drive = link_drive
            movimento.save(update_fields=["arquivo_nf_url_drive"])
            self.stdout.write(
                self.style.SUCCESS(f"NF-e enviada para o Google Drive: {link_drive}")
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f"Erro ao enviar para o Google Drive: {e}")
            )
