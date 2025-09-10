import re
from pathlib import Path
import shutil

# Caminho do arquivo a ajustar
arquivo = Path("app_principal/management/commands/migrar_dados_antigos.py")
backup = arquivo.with_name(arquivo.stem + "_backup_itemlicitado.py")

# Backup antes de mexer
shutil.copy2(arquivo, backup)
print(f"✅ Backup criado: {backup.name}")

conteudo = arquivo.read_text(encoding="utf-8")

# Regex para encontrar blocos de update_or_create de ItemLicitado
padrao = re.compile(
    r"ItemLicitado\.objects\.update_or_create\s*\(\s*edital\s*=\s*([^\n,]+)\s*,\s*fornecedor\s*=\s*([^\n,]+)\s*,\s*codigo\s*=\s*([^\n,]+)\s*,\s*defaults\s*=\s*\{([\s\S]*?)\}\s*\)",
    re.MULTILINE,
)


def reorganizar(match):
    edital = match.group(1).strip()
    fornecedor = match.group(2).strip()
    codigo = match.group(3).strip()
    corpo = match.group(4).strip()

    return (
        f"ItemLicitado.objects.update_or_create(\n"
        f"    edital={edital},\n"
        f"    codigo={codigo},\n"
        f"    defaults={{\n"
        f'        "fornecedor": {fornecedor},\n'
        f"{corpo}\n"
        f"    }}\n"
        f")"
    )


# Aplicar substituições
novo_conteudo = padrao.sub(reorganizar, conteudo)

# Salvar novo arquivo
arquivo.write_text(novo_conteudo, encoding="utf-8")
print("✅ Blocos de ItemLicitado reorganizados com sucesso.")
print("🔍 Abra o arquivo no VS Code e revise antes de rodar.")
