#!/usr/bin/env python3
"""Valida invariantes mínimas da governança de IA do vault."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path.cwd()
COMMON = ROOT / "90 - Sistema/Governança de IA/10 - Contrato Comum de Contexto para Assistentes de IA.md"
TSH = ROOT / "90 - Sistema/Governança de IA/11 - Contexto Mínimo - Traduzindo o Ser Humano.md"
ADAPTERS = (ROOT / "AGENTS.md", ROOT / "CLAUDE.md")
REQUIRED_POINTERS = (str(COMMON.relative_to(ROOT)), str(TSH.relative_to(ROOT)))


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    for path in (COMMON, TSH, *ADAPTERS):
        if not path.is_file():
            errors.append(f"arquivo obrigatório ausente: {path.relative_to(ROOT)}")

    if errors:
        print(json.dumps({"ok": False, "errors": errors, "warnings": warnings}, ensure_ascii=False, indent=2))
        return 1

    common_text = COMMON.read_text(encoding="utf-8")
    required_phrases = (
        "Fabiano é o decisor final",
        "Não carregar o vault inteiro",
        "Não integrar à `main` sem homologação de Fabiano",
    )
    for phrase in required_phrases:
        if phrase not in common_text:
            errors.append(f"invariante ausente no contrato comum: {phrase}")

    for adapter in ADAPTERS:
        text = adapter.read_text(encoding="utf-8")
        if adapter.stat().st_size > 2500:
            errors.append(f"adaptador excede 2500 bytes: {adapter.name}")
        for pointer in REQUIRED_POINTERS:
            if pointer not in text:
                errors.append(f"{adapter.name} não aponta para {pointer}")

    old_protocol = ROOT / (
        "70 - Produções/Cursos/Curso - Nome Provisório/"
        "01 - Protocolo de Continuidade Integral e Abertura de Novos Chats.md"
    )
    if old_protocol.is_file():
        for number, line in enumerate(old_protocol.read_text(encoding="utf-8").splitlines(), start=1):
            if "emitir Relatório de Retomada e aguardar deliberação autoral" in line and "~~" not in line:
                errors.append(f"ritual ultrapassado ainda ativo: {old_protocol}:{number}")
    else:
        warnings.append("protocolo histórico do TSH não encontrado no caminho esperado")

    result = {"ok": not errors, "errors": errors, "warnings": warnings}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
