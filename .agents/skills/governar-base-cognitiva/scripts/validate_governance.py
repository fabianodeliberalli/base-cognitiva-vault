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
COURSE = ROOT / "70 - Produções/Cursos/Curso - Nome Provisório"
ENTRY = COURSE / "LEIA PRIMEIRO - Estado Atual e Continuidade do Curso.md"
DOSSIER = COURSE / "00 - Dossiê de Contexto e Arquitetura Mestre.md"
M1_STATE = COURSE / "Materiais/Módulo 1/00 - Estado e Continuidade da Produção M1.md"
MASTERCLASS_STATE = COURSE / "Guia-de-Conducao-Masterclass - Estado e Continuidade.md"
IDENTITY_INDEX = COURSE / "20 - Identidade Visual/00 - Índice da Identidade Visual.md"
ENTRY_SNAPSHOT = COURSE / "Registros de Continuidade/2026-08-23 - Snapshot da antiga porta de entrada do curso.md"
DOSSIER_SNAPSHOT = COURSE / "Registros de Continuidade/2026-08-22 - Snapshot do Dossiê de Contexto e Arquitetura Mestre.md"
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

    required_files = (COMMON, TSH, LEARNING, ENTRY, DOSSIER, M1_STATE, MASTERCLASS_STATE, IDENTITY_INDEX, ENTRY_SNAPSHOT, DOSSIER_SNAPSHOT, README, SKILL, CLAUDE_SKILL, *ADAPTERS)
    for path in required_files:
        if not path.is_file():
            errors.append(f"arquivo obrigatório ausente: {path.relative_to(ROOT)}")

    if errors:
        print(json.dumps({"ok": False, "errors": errors, "warnings": warnings}, ensure_ascii=False, indent=2))
        return 1

    common_text = COMMON.read_text(encoding="utf-8")
    tsh_text = TSH.read_text(encoding="utf-8")
    learning_text = LEARNING.read_text(encoding="utf-8")
    entry_text = ENTRY.read_text(encoding="utf-8")
    dossier_text = DOSSIER.read_text(encoding="utf-8")
    m1_text = M1_STATE.read_text(encoding="utf-8")
    masterclass_text = MASTERCLASS_STATE.read_text(encoding="utf-8")
    identity_text = IDENTITY_INDEX.read_text(encoding="utf-8")
    snapshot_text = ENTRY_SNAPSHOT.read_text(encoding="utf-8")
    dossier_snapshot_text = DOSSIER_SNAPSHOT.read_text(encoding="utf-8")
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
        entry_text,
        (
            "9 módulos e 54 aulas",
            "sem funcionar como segunda arquitetura",
            "Nenhum chat possui autoridade exclusiva",
            "Não existe lista fixa de documentos para toda retomada",
            "Snapshot da antiga porta de entrada do curso",
        ),
        "porta de entrada do TSH",
        errors,
    )
    require_phrases(
        dossier_text,
        (
            "status: referencia-atual-revisavel",
            "9 módulos e 54 aulas",
            "não funciona como arquitetura paralela",
            "Doze semanas",
            "não uma autoridade independente",
            "Snapshot do Dossiê de Contexto e Arquitetura Mestre",
        ),
        "dossiê ativo do TSH",
        errors,
    )
    require_phrases(
        m1_text,
        (
            "status: referencia-atual-revisavel",
            "Nenhum chat possui competência exclusiva",
            "reabrindo-a quando a construção atual pedir revisão",
        ),
        "estado da produção M1",
        errors,
    )
    require_phrases(
        masterclass_text,
        (
            "status: referencia-atual-revisavel",
            "referência atual e revisável para a condução da masterclass",
            "fonte histórica consultável",
        ),
        "estado da masterclass",
        errors,
    )
    require_phrases(
        identity_text,
        (
            "status: referencia-atual-revisavel",
            "ponto de partida para trabalhos de identidade visual",
            "aberta a revisão autoral",
        ),
        "índice da identidade visual",
        errors,
    )
    require_phrases(
        snapshot_text,
        (
            "status: snapshot-historico-preservado",
            "Suas instruções não orientam o trabalho atual",
            "A arquitetura 7/14 continua governando",
        ),
        "snapshot da antiga porta de entrada",
        errors,
    )

    require_phrases(
        dossier_snapshot_text,
        (
            "status: snapshot-historico-preservado",
            "Suas instruções de arquitetura e continuidade não orientam automaticamente o trabalho atual",
            "A estrutura de 14 unidades curriculares permanece vigente",
        ),
        "snapshot do dossiê mestre",
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
        ENTRY: (
            "A arquitetura 7/14 continua governando",
            "arquitetura de desenvolvimento, integração e rastreabilidade do conteúdo:** 7 módulos",
            "patrimônio canônico",
            "não reabrir a Unidade 0.1",
        ),
        DOSSIER: (
            "Os 7 módulos e 14 unidades curriculares permanecem como arquitetura interna",
            "A estrutura de 14 unidades curriculares permanece vigente",
            "este Dossiê governa a arquitetura geral",
            "sem reabrir a Unidade 0.1",
        ),
        M1_STATE: (
            "patrimônio canônico",
            "chat competente",
            "- não reabrir a UC 0.1;",
        ),
        MASTERCLASS_STATE: (
            "Estatuto:** canônico",
            "Rastreabilidade do conteúdo:** arquitetura 7/14",
        ),
        IDENTITY_INDEX: (
            "porta de entrada obrigatória",
            "direção conceitual: congelada",
        ),
        README: (
            "Ao final, gera um pacote de registro",
        ),
    }
    for path, phrases in forbidden_active_phrases.items():
        text = path.read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase in text:
                errors.append(f"rigidez antiga ainda ativa em {path.relative_to(ROOT)}: {phrase}")

    if ENTRY.stat().st_size > 12000:
        errors.append(f"porta de entrada do TSH excede 12000 bytes: {ENTRY.stat().st_size}")
    if DOSSIER.stat().st_size > 12000:
        errors.append(f"dossiê ativo do TSH excede 12000 bytes: {DOSSIER.stat().st_size}")

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
