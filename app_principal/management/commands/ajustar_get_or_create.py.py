import re
from pathlib import Path
import shutil

# Caminho do arquivo a ajustar
arquivo = Path("app_principal/management/commands/migrar_dados_antigos.py")
backup = arquivo.with_name(arquivo.stem + "_backup.py")

# Backup antes de mexer
shutil.copy2(arquivo, backup)
print(f"Backup criado: {backup}")

conteudo = arquivo.read_text(encoding="utf-8")

# Remove [0] e troca por , _ =
conteudo = re.sub(
    r"^(\s*)([A-Za-z_]\w*)\s*=\s*([A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*\.objects\.get_or_create\([\s\S]*?\))\s*\[\s*0\s*\]",
    r"\1\2, _ = \3",
    conteudo,
    flags=re.MULTILINE,
)

# Ajusta Fornecedor
conteudo = re.sub(
    r"Fornecedor\.objects\.get_or_create\s*\(\s*([^\n,]+)\s*,\s*([\s\S]*?)\)",
    r"Fornecedor.objects.get_or_create(\n    cnpj=\1,\n    defaults={\2}\n)",
    conteudo,
)

# Ajusta Edital
conteudo = re.sub(
    r"Edital\.objects\.get_or_create\s*\(\s*([^\n,]+)\s*,\s*([\s\S]*?)\)",
    r"Edital.objects.get_or_create(\n    numero=\1,\n    defaults={\2}\n)",
    conteudo,
)

arquivo.write_text(conteudo, encoding="utf-8")
print("Arquivo ajustado com sucesso. Confira no VS Code antes de rodar.")
