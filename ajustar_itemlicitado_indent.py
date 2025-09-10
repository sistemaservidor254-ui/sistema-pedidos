import re
from pathlib import Path
import shutil
from datetime import datetime

ARQUIVO = Path("app_principal/management/commands/migrar_dados_antigos.py")
BACKUP = ARQUIVO.with_name(
    ARQUIVO.stem + f"_backup_itemlicitado_{datetime.now().strftime('%Y%m%d_%H%M%S')}.py"
)


def split_top_level_commas(s: str):
    # Divide s por vírgulas apenas no nível 0 (fora de (), {}, [])
    parts = []
    buf = []
    depth_par = depth_brace = depth_brack = 0
    i = 0
    while i < len(s):
        ch = s[i]
        if ch == "(":
            depth_par += 1
        elif ch == ")":
            depth_par -= 1
        elif ch == "{":
            depth_brace += 1
        elif ch == "}":
            depth_brace -= 1
        elif ch == "[":
            depth_brack += 1
        elif ch == "]":
            depth_brack -= 1
        if ch == "," and depth_par == 0 and depth_brace == 0 and depth_brack == 0:
            parts.append("".join(buf))
            buf = []
        else:
            buf.append(ch)
        i += 1
    if buf:
        parts.append("".join(buf))
    return parts


def extract_defaults_content(token: str):
    # token é algo como: defaults={ ... }  (com possíveis espaços)
    # Retorna o conteúdo interno das chaves e o token “limpo”
    m = re.search(r"defaults\s*=\s*\{", token)
    if not m:
        return None
    start = m.end()  # posição após a abertura da chave
    depth = 1
    i = start
    while i < len(token):
        ch = token[i]
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                inner = token[start:i]
                return inner
        i += 1
    return None  # não conseguiu fechar corretamente


def reindent_block(text: str, indent: str):
    # Remove espaços comuns à esquerda e reidenta cada linha com indent
    # Mantém quebras de linha existentes.
    lines = text.splitlines()
    # Detecta indentação mínima comum
    min_lead = None
    for ln in lines:
        if ln.strip() == "":
            continue
        lead = len(ln) - len(ln.lstrip())
        if min_lead is None or lead < min_lead:
            min_lead = lead
    if min_lead is None:
        min_lead = 0
    out = []
    for ln in lines:
        if ln.strip() == "":
            out.append("")
        else:
            out.append(indent + ln[min_lead:])
    return "\n".join(out)


def find_matching_paren(s: str, start_idx: int):
    # s[start_idx] deve ser '('; retorna índice da ')' correspondente
    depth = 0
    for i in range(start_idx, len(s)):
        if s[i] == "(":
            depth += 1
        elif s[i] == ")":
            depth -= 1
            if depth == 0:
                return i
    return -1


def process_file(text: str):
    out = []
    i = 0
    changed = 0
    pattern = re.compile(
        r"(?P<indent>[ \t]*)ItemLicitado\.objects\.update_or_create\s*\(", re.MULTILINE
    )

    while True:
        m = pattern.search(text, i)
        if not m:
            out.append(text[i:])
            break

        # Copia o texto até antes da chamada
        out.append(text[i : m.start()])

        indent = m.group("indent")
        open_paren_idx = m.end() - 1  # posição do '('
        close_paren_idx = find_matching_paren(text, open_paren_idx)
        if close_paren_idx == -1:
            # Não conseguiu fechar: copia bruto e segue
            out.append(text[m.start() :])
            break

        call_block = text[m.start() : close_paren_idx + 1]
        inside = text[open_paren_idx + 1 : close_paren_idx]  # conteúdo entre parênteses

        # Parse dos argumentos top-level
        tokens = split_top_level_commas(inside)
        # Mapa de argumentos por chave top-level
        args = {}
        other_tokens = []
        defaults_inner = None

        for tok in tokens:
            tok_stripped = tok.strip()
            if not tok_stripped:
                continue
            # Só considera key=value no nível superior
            eq_idx = tok_stripped.find("=")
            if eq_idx == -1:
                other_tokens.append(tok)
                continue
            key = tok_stripped[:eq_idx].strip()
            val = tok_stripped[eq_idx + 1 :].strip()
            if key == "defaults":
                inner = extract_defaults_content(tok_stripped)
                if inner is not None:
                    defaults_inner = inner
                else:
                    # defaults malformado; vamos manter o bloco original
                    args[key] = val
            elif key in ("edital", "codigo", "fornecedor"):
                args[key] = val
            else:
                # outros argumentos; vamos empurrar para defaults depois
                other_tokens.append(tok)

        # Precisamos no mínimo de edital e codigo para reescrever
        if "edital" not in args or "codigo" not in args:
            # Não altera este bloco
            out.append(call_block)
            i = close_paren_idx + 1
            continue

        # Preparar defaults: construímos um corpo com reindentação
        inner_indent = indent + " " * 4
        defaults_indent = inner_indent + " " * 4

        # Verifica se defaults já contém fornecedor no nível superior
        fornecedor_in_defaults = False
        if defaults_inner is not None:
            if re.search(r'(^|\n)\s*"fornecedor"\s*:', defaults_inner):
                fornecedor_in_defaults = True

        # Se não houver defaults original, começamos com vazio
        defaults_pieces = []

        # Adiciona fornecedor no início do defaults se não existir
        if "fornecedor" in args and not fornecedor_in_defaults:
            defaults_pieces.append(
                f'{defaults_indent}"fornecedor": {args["fornecedor"]},'
            )

        # Inclui quaisquer tokens “outros” (que não eram defaults/edital/codigo/fornecedor) dentro de defaults
        # Isso cobre casos onde havia argumentos extras fora de defaults.
        for tok in other_tokens:
            t = tok.strip()
            if not t:
                continue
            # Transformar key=value simples em "key": value,
            eq_idx = t.find("=")
            if eq_idx != -1:
                k = t[:eq_idx].strip()
                v = t[eq_idx + 1 :].strip()
                defaults_pieces.append(f'{defaults_indent}"{k}": {v},')
            else:
                # caso estranho; apenas comenta e evita perder o conteúdo
                defaults_pieces.append(
                    f"{defaults_indent}# AVISO: argumento não reconhecido mantido: {t},"
                )

        # Mantém o conteúdo original de defaults (se existir), reindentado
        if defaults_inner is not None and defaults_inner.strip():
            reindented = reindent_block(defaults_inner, defaults_indent)
            # Evita chave/fecha a mais: defaults_inner já não inclui { }
            # Garante quebra de linha ao final
            if not reindented.endswith("\n"):
                reindented += "\n"
            defaults_pieces.append(reindented.rstrip("\n"))

        # Monta o novo bloco
        new_block_lines = []
        new_block_lines.append(f"{indent}ItemLicitado.objects.update_or_create(")
        new_block_lines.append(f"{inner_indent}edital={args['edital']},")
        new_block_lines.append(f"{inner_indent}codigo={args['codigo']},")
        new_block_lines.append(f"{inner_indent}defaults={{")

        # Se não houver nada, ainda assim deixamos um bloco vazio formatado
        if defaults_pieces:
            # Junta preservando linhas
            # Remover possíveis vírgulas duplas ao final não é crítico para Python/dict,
            # mas podemos normalizar em um passo simples:
            # Se a última linha termina com ',', mantemos; senão, deixamos como está.
            new_block_lines.extend(defaults_pieces)
        # Fecha defaults e chamada
        new_block_lines.append(f"{inner_indent}}}")
        new_block_lines.append(f"{indent})")

        new_block = "\n".join(new_block_lines)

        out.append(new_block)
        changed += 1
        i = close_paren_idx + 1

    return "".join(out), changed


def main():
    if not ARQUIVO.exists():
        raise SystemExit(f"Arquivo não encontrado: {ARQUIVO}")

    shutil.copy2(ARQUIVO, BACKUP)
    print(f"✅ Backup criado: {BACKUP.name}")

    texto = ARQUIVO.read_text(encoding="utf-8")
    novo_texto, total = process_file(texto)

    if total == 0:
        print(
            "ℹ️ Nenhum bloco de ItemLicitado.update_or_create elegível foi encontrado/alterado."
        )
    else:
        ARQUIVO.write_text(novo_texto, encoding="utf-8")
        print(f"✅ {total} bloco(s) reorganizado(s) com sucesso.")
        print(
            "🔍 Revise as mudanças no VS Code antes de executar o comando de migração."
        )


if __name__ == "__main__":
    main()
