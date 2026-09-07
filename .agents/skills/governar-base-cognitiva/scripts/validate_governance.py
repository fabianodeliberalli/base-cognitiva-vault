#!/usr/bin/env python3
"""Valida preservação, autoria e liberdade criativa na governança do vault."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path.cwd()
COMMON = ROOT / "90 - Sistema/Governança de IA/10 - Contrato Comum de Contexto para Assistentes de IA.md"
TSH = ROOT / "90 - Sistema/Governança de IA/11 - Contexto Mínimo - Traduzindo o Ser Humano.md"
LEARNING = ROOT / "90 - Sistema/Governança de IA/12 - Aprendizado Operacional e Melhoria Contínua.md"
README = ROOT / "README.md"
SKILL = ROOT / ".agents/skills/governar-base-cognitiva/SKILL.md"
CLAUDE_SKILL = ROOT / ".claude/skills/governar-base-cognitiva/SKILL.md"
ADAPTERS = (ROOT / "AGENTS.md", ROOT / "CLAUDE.md")
REQUIRED_POINTERS = (str(COMMON.relative_to(ROOT)), str(TSH.relative_to(ROOT)))


def require_phrases(text: str, phrases: tuple[str, ...], label: str, errors: list[str]) -> None:
    for phrase in phrases:
        if phrase not in text:
            errors.append(f"orientação ausente em {label}: {phrase}")


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    required_files = (COMMON, TSH, LEARNING, README, SKILL, CLAUDE_SKILL, *ADAPTERS)
    for path in required_files:
        if not path.is_file():
            errors.append(f"arquivo obrigatório ausente: {path.relative_to(ROOT)}")

    if errors:
        print(json.dumps({"ok": False, "errors": errors, "warnings": warnings}, ensure_ascii=False, indent=2))
        return 1

    common_text = COMMON.read_text(encoding="utf-8")
    tsh_text = TSH.read_text(encoding="utf-8")
    learning_text = LEARNING.read_text(encoding="utf-8")
    readme_text = README.read_text(encoding="utf-8")
    skill_text = SKILL.read_text(encoding="utf-8")
    claude_skill_text = CLAUDE_SKILL.read_text(encoding="utf-8")

    require_phrases(
        common_text,
        (
            "Fabiano é o decisor final",
            "Não carregar o vault inteiro",
            "Nenhuma formulação criada por IA",
            "Não integrar à `main` sem homologação de Fabiano",
            "Não transformar refinamentos rotineiros",
            "Não carregar essa nota em tarefas comuns",
            "Não exigir plugin, painel, modelo ou configuração específica",
        ),
        "guia comum",
        errors,
    )
    require_phrases(
        tsh_text,
        (
            "Referências atuais de trabalho",
            "Doze semanas",
            "estimativa provisória",
            "Nenhuma inteligência artificial pode declarar uma proposta própria",
        ),
        "contexto mínimo do TSH",
        errors,
    )
    require_phrases(
        learning_text,
        (
            "Não consultar por padrão em tarefas comuns",
            "Ideias isoladas, explorações criativas e preferências momentâneas não viram regra",
            "não exigir plugin, painel, modelo ou configuração do Obsidian",
            "Não criar revisão periódica obrigatória",
        ),
        "aprendizado operacional",
        errors,
    )
    require_phrases(
        readme_text,
        (
            "Fluxo leve",
            "Uso com o Obsidian",
            "não há plugin, painel, modelo ou configuração obrigatória",
        ),
        "README",
        errors,
    )
    require_phrases(
        skill_text,
        (
            "A governança existe para reduzir carga",
            "Nenhum texto gerado por IA pode ser declarado",
            "Pare e consulte somente",
            "Questões reversíveis e criativas podem avançar",
            "Aprendizado longitudinal",
            "Não leia essa memória em tarefas comuns",
        ),
        "skill principal",
        errors,
    )

    forbidden_active_phrases = {
        TSH: (
            "Formulação canônica",
            "proteção canônica",
            "Produção curricular oficial deve ocorrer",
        ),
        CLAUDE_SKILL: ("implementação canônica",),
        SKILL: (
            "fonte normativa comum",
            "decisões consolidadas",
        ),
    }
        README: (
            "Ao final, gera um pacote de registro",
        ),
    }
    for path, phrases in forbidden_active_phrases.items():
        text = path.read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase in text:
                errors.append(f"rigidez antiga ainda ativa em {path.relative_to(ROOT)}: {phrase}")

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
