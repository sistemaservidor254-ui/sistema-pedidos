import subprocess
import os


def enviar_para_mega(caminho_arquivo, pasta_destino="/NF"):
    """
    Envia arquivo para o MEGA e retorna link público.
    """
    # Envia o arquivo
    subprocess.run(["mega-put", caminho_arquivo, pasta_destino], check=True)

    # Nome do arquivo no MEGA
    nome_arquivo = os.path.basename(caminho_arquivo)

    # Gera link público
    resultado = subprocess.run(
        ["mega-export", f"{pasta_destino}/{nome_arquivo}"],
        capture_output=True,
        text=True,
        check=True,
    )

    # Procura link na saída
    for linha in resultado.stdout.splitlines():
        if "https://" in linha:
            return linha.strip()

    return None
