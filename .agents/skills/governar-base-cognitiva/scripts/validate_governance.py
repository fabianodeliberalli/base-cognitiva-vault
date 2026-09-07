#!/usr/bin/env python3
"""Valida preservação, autoria e liberdade criativa na governança do vault."""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path.cwd()
COMMON = ROOT / "90 - Sistema/Governança de IA/10 - Contrato Comum de Contexto para Assistentes de IA.md"
TSH = ROOT / "90 - Sistema/Governança de IA/11 - Contexto Mínimo - Traduzindo o Ser Humano.md"
LEARNING = ROOT / "90 - Sistema/Governança de IA/12 - Aprendizado Operacional e Melhoria Contínua.md"
POSITIONING = ROOT / "70 - Produções/Projetos/Posicionamento Profissional e Autoridade"
POSITIONING_ENTRY = POSITIONING / "00 - LEIA PRIMEIRO - Estado Atual e Continuidade.md"
POSITIONING_PROMPT = POSITIONING / "11 - Prompt de Abertura do Projeto Estratégico.md"
POSITIONING_SNAPSHOTS = POSITIONING / "Registros de Continuidade"
POSITIONING_ENTRY_SNAPSHOT = POSITIONING_SNAPSHOTS / "2026-09-07 - Snapshot da antiga porta de entrada.md"
POSITIONING_PROMPT_SNAPSHOT = POSITIONING_SNAPSHOTS / "2026-09-07 - Snapshot do antigo prompt de abertura.md"
COURSE = ROOT / "70 - Produções/Cursos/Curso - Nome Provisório"
ENTRY = COURSE / "LEIA PRIMEIRO - Estado Atual e Continuidade do Curso.md"
DOSSIER = COURSE / "00 - Dossiê de Contexto e Arquitetura Mestre.md"
M1_STATE = COURSE / "Materiais/Módulo 1/00 - Estado e Continuidade da Produção M1.md"
MASTERCLASS_STATE = COURSE / "Guia-de-Conducao-Masterclass - Estado e Continuidade.md"
IDENTITY_INDEX = COURSE / "20 - Identidade Visual/00 - Índice da Identidade Visual.md"
KNOWLEDGE = COURSE / "10 - Governança do Conhecimento"
KNOWLEDGE_INDEX = KNOWLEDGE / "00 - Índice da Governança do Conhecimento.md"
OLD_RECONCILIATION = KNOWLEDGE / "01 - Reconciliação da Governança do Conhecimento e Disponibilidade do Acervo.md"
INVENTORY = KNOWLEDGE / "02 - Inventário Mestre de Conteúdos Disponíveis.md"
OLD_FOUNDATIONS = KNOWLEDGE / "03 - Reconciliação Documental dos Fundamentos Transversais e Revisão Curricular.md"
PLURALISM = KNOWLEDGE / "04 - Deliberação Transversal - Pluralismo Epistemológico Não Redutivo e Integração Autoral.md"
BRIDGE = KNOWLEDGE / "05 - Nota-Ponte - Desenvolvimento do Conteúdo 7-14 e Entrega 9-54.md"
OLD_MATRIX = KNOWLEDGE / "06 - Matriz Mestre de Incorporação do Conteúdo à Estrutura 9-54.md"
OLD_POSITIONING = KNOWLEDGE / "07 - Deliberação Transversal - Posicionamento, Linguagem e Arquitetura Dupla - 2026-08-23.md"
FORMULATIONS = COURSE / "Registro Mestre de Formulações Estruturantes.md"
OLD_PROTOCOL = COURSE / "01 - Protocolo de Continuidade Integral e Abertura de Novos Chats.md"
ENTRY_SNAPSHOT = COURSE / "Registros de Continuidade/2026-08-23 - Snapshot da antiga porta de entrada do curso.md"
DOSSIER_SNAPSHOT = COURSE / "Registros de Continuidade/2026-08-22 - Snapshot do Dossiê de Contexto e Arquitetura Mestre.md"
README = ROOT / "README.md"
SKILL = ROOT / ".agents/skills/governar-base-cognitiva/SKILL.md"
CLAUDE_SKILL = ROOT / ".claude/skills/governar-base-cognitiva/SKILL.md"
ADAPTERS = (ROOT / "AGENTS.md", ROOT / "CLAUDE.md")
REQUIRED_POINTERS = (
    str(COMMON.relative_to(ROOT)),
    str(TSH.relative_to(ROOT)),
    str(POSITIONING_ENTRY.relative_to(ROOT)),
)

HISTORICAL_STATUS_MARKERS = (
    "histor",
    "snapshot",
    "substitu",
    "arquiv",
    "acervo",
    "memoria",
)
ACTIVE_STATUS_MARKERS = (
    "vigente",
    "ativo",
    "referencia-atual",
    "oficial",
    "canon",
    "definitiv",
    "consolidado",
)
GOVERNANCE_NAME_MARKERS = (
    "leia primeiro",
    "estado e continuidade",
    "dossiê",
    "dossie",
    "governança",
    "governanca",
    "protocolo",
    "matriz mestre",
    "registro mestre",
)
HIGH_CONFIDENCE_RIGIDITY = (
    ("fonte exclusiva", re.compile(r"\bfonte\s+(?:única|exclusiva|canônica|canonica|oficial)\b", re.I)),
    ("entrada obrigatória", re.compile(r"\b(?:porta|leitura|entrada)\s+(?:única|obrigatória|obrigatorio|obrigatória|obrigatório)\b", re.I)),
    ("chat exclusivo", re.compile(r"\b(?:único\s+chat|somente\s+(?:neste|nesse)\s+chat|apenas\s+(?:neste|nesse)\s+chat|chat\s+competente)\b", re.I)),
    (
        "bloqueio de revisão",
        re.compile(
            r"\b(?:não\s+reabrir|nao\s+reabrir|proibid[ao]\s+(?:a\s+)?revisão|"
            r"(?:é|será|sera|permanece|fica)\s+(?:imutável|imutavel|congelad[oa]))\b",
            re.I,
        ),
    ),
    ("cânone imposto", re.compile(r"\b(?:patrimônio|patrimonio|implementação|implementacao|formulação|formulacao|copy|texto)\s+canônic[oa]\b", re.I)),
    ("decisão governante", re.compile(r"\bdecisão\s+governante\b", re.I)),
    (
        "estrutura 7/14 governante",
        re.compile(
            r"(?:7\s*(?:módulos)?\s*(?:/|e)\s*14\s*(?:aulas|unidades)?[^\n.]{0,140}\bgoverna|"
            r"\bgoverna[^\n.]{0,140}7\s*(?:módulos)?\s*(?:/|e)\s*14\s*(?:aulas|unidades)?)",
            re.I,
        ),
    ),
)


def frontmatter(text: str) -> dict[str, str]:
    """Lê apenas propriedades YAML simples; suficiente para classificação documental."""
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    properties: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line or line.startswith((" ", "\t", "-")):
            continue
        key, value = line.split(":", 1)
        properties[key.strip().lower()] = value.strip().strip('"\'').lower()
    return properties


def is_historical(properties: dict[str, str]) -> bool:
    status = properties.get("status", "")
    current_use = properties.get("uso_atual", "")
    return any(marker in status for marker in HISTORICAL_STATUS_MARKERS) or current_use in {
        "consulta-historica",
        "consulta-histórica",
        "acervo-consultivo",
    }


def is_active_governance(path: Path, properties: dict[str, str]) -> bool:
    if is_historical(properties):
        return False
    status = properties.get("status", "")
    kind = properties.get("tipo", "")
    name = path.name.lower()
    return (
        any(marker in status for marker in ACTIVE_STATUS_MARKERS)
        or any(marker in name for marker in GOVERNANCE_NAME_MARKERS)
        or any(marker in kind for marker in ("govern", "protocolo", "contexto", "continuidade"))
    )


def visible_text(text: str) -> str:
    """Evita tratar nomes técnicos ocultos por alias como instrução ao leitor."""
    text = re.sub(r"\[\[[^\]|]+\|([^\]]+)\]\]", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)
    return text


def git_lines(*args: str) -> set[str]:
    try:
        process = subprocess.run(
            ("git", "-c", "core.quotepath=false", *args),
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
    except OSError:
        return set()
    if process.returncode != 0:
        return set()
    return {line for line in process.stdout.splitlines() if line}


def changed_markdown_files() -> list[Path]:
    """Descobre alterações locais e, em branches, tudo que diverge da main."""
    names = set()
    names |= git_lines("diff", "--name-only", "--diff-filter=AM")
    names |= git_lines("diff", "--cached", "--name-only", "--diff-filter=AM")
    names |= git_lines("ls-files", "--others", "--exclude-standard")

    base_ref = os.environ.get("GOVERNANCE_BASE_REF")
    if not base_ref and os.environ.get("GITHUB_BASE_REF"):
        base_ref = f"origin/{os.environ['GITHUB_BASE_REF']}"
    if not base_ref and git_lines("rev-parse", "--verify", "origin/main"):
        base_ref = "origin/main"
    if base_ref:
        merge_bases = git_lines("merge-base", "HEAD", base_ref)
        if merge_bases:
            merge_base = next(iter(merge_bases))
            names |= git_lines("diff", "--name-only", "--diff-filter=AM", f"{merge_base}...HEAD")

    paths: list[Path] = []
    for name in sorted(names):
        path = ROOT / name
        if path.suffix.lower() == ".md" and path.is_file():
            paths.append(path)
    return paths


def validate_changed_documents(errors: list[str]) -> None:
    """Impede que um arquivo novo ou alterado recrie autoridade rígida."""
    for path in changed_markdown_files():
        text = path.read_text(encoding="utf-8")
        properties = frontmatter(text)
        if not is_active_governance(path, properties):
            continue
        relative = path.relative_to(ROOT)
        text_for_review = visible_text(text)
        for label, pattern in HIGH_CONFIDENCE_RIGIDITY:
            match = pattern.search(text_for_review)
            if match:
                excerpt = " ".join(match.group(0).split())[:160]
                errors.append(
                    f"nova rigidez em referência ativa ({label}) — {relative}: {excerpt}. "
                    "Reformular como referência revisável ou classificar como histórico consultivo."
                )

        is_entrypoint = any(
            marker in path.name.lower()
            for marker in ("leia primeiro", "estado e continuidade", "prompt de abertura")
        )
        if is_entrypoint and path.stat().st_size > 12000:
            errors.append(
                f"nova porta de contexto excede 12000 bytes: {relative} ({path.stat().st_size})"
            )


def require_phrases(text: str, phrases: tuple[str, ...], label: str, errors: list[str]) -> None:
    for phrase in phrases:
        if phrase not in text:
            errors.append(f"orientação ausente em {label}: {phrase}")


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    required_files = (
        COMMON, TSH, LEARNING, POSITIONING_ENTRY, POSITIONING_PROMPT,
        POSITIONING_ENTRY_SNAPSHOT, POSITIONING_PROMPT_SNAPSHOT,
        ENTRY, DOSSIER, M1_STATE, MASTERCLASS_STATE,
        IDENTITY_INDEX, KNOWLEDGE_INDEX, OLD_RECONCILIATION, INVENTORY,
        OLD_FOUNDATIONS, PLURALISM, BRIDGE, OLD_MATRIX, OLD_POSITIONING,
        FORMULATIONS, OLD_PROTOCOL, ENTRY_SNAPSHOT, DOSSIER_SNAPSHOT, README,
        SKILL, CLAUDE_SKILL, *ADAPTERS,
    )
    for path in required_files:
        if not path.is_file():
            errors.append(f"arquivo obrigatório ausente: {path.relative_to(ROOT)}")

    if errors:
        print(json.dumps({"ok": False, "errors": errors, "warnings": warnings}, ensure_ascii=False, indent=2))
        return 1

    common_text = COMMON.read_text(encoding="utf-8")
    tsh_text = TSH.read_text(encoding="utf-8")
    learning_text = LEARNING.read_text(encoding="utf-8")
    positioning_entry_text = POSITIONING_ENTRY.read_text(encoding="utf-8")
    positioning_prompt_text = POSITIONING_PROMPT.read_text(encoding="utf-8")
    positioning_entry_snapshot_text = POSITIONING_ENTRY_SNAPSHOT.read_text(encoding="utf-8")
    positioning_prompt_snapshot_text = POSITIONING_PROMPT_SNAPSHOT.read_text(encoding="utf-8")
    entry_text = ENTRY.read_text(encoding="utf-8")
    dossier_text = DOSSIER.read_text(encoding="utf-8")
    m1_text = M1_STATE.read_text(encoding="utf-8")
    masterclass_text = MASTERCLASS_STATE.read_text(encoding="utf-8")
    identity_text = IDENTITY_INDEX.read_text(encoding="utf-8")
    knowledge_index_text = KNOWLEDGE_INDEX.read_text(encoding="utf-8")
    old_reconciliation_text = OLD_RECONCILIATION.read_text(encoding="utf-8")
    inventory_text = INVENTORY.read_text(encoding="utf-8")
    old_foundations_text = OLD_FOUNDATIONS.read_text(encoding="utf-8")
    pluralism_text = PLURALISM.read_text(encoding="utf-8")
    bridge_text = BRIDGE.read_text(encoding="utf-8")
    old_matrix_text = OLD_MATRIX.read_text(encoding="utf-8")
    old_positioning_text = OLD_POSITIONING.read_text(encoding="utf-8")
    formulations_text = FORMULATIONS.read_text(encoding="utf-8")
    old_protocol_text = OLD_PROTOCOL.read_text(encoding="utf-8")
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
            "Continuidade em sessões longas",
            "Ativação entre ferramentas",
            "não descobrir seus arquivos automaticamente",
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
            "usar o Registro Mestre como acervo histórico consultivo",
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
            "o verificador protegia arquivos conhecidos",
            "sessões longas podem acumular decisões",
        ),
        "aprendizado operacional",
        errors,
    )
    require_phrases(
        positioning_entry_text,
        (
            "status: referencia-atual-revisavel",
            "Consultar somente os materiais relacionados à tarefa",
            "Nenhuma formulação, bio, currículo ou estratégia se torna imutável",
            "Não formam uma cadeia obrigatória",
            "mais de 30 anos de trajetória no cuidado terapêutico, desde as práticas corporais e integrativas até a Psicologia Clínica",
            "carga de duas mil horas de estágio no Shiozawa, confirmada anteriormente por Fabiano",
        ),
        "porta de entrada de Posicionamento Profissional e Autoridade",
        errors,
    )
    require_phrases(
        positioning_prompt_text,
        (
            "status: referencia-atual-revisavel",
            "consulte apenas as fontes necessárias à tarefa atual",
            "Este apontador substitui a antiga abertura que exigia a leitura integral de treze documentos",
        ),
        "apontador de Posicionamento Profissional e Autoridade",
        errors,
    )
    require_phrases(
        positioning_entry_snapshot_text,
        (
            "status: snapshot-historico-preservado",
            "conteúdo da antiga porta de entrada, preservado integralmente",
            "Suas instruções não orientam automaticamente o trabalho atual",
        ),
        "snapshot da antiga porta de Posicionamento Profissional e Autoridade",
        errors,
    )
    require_phrases(
        positioning_prompt_snapshot_text,
        (
            "status: snapshot-historico-preservado",
            "conteúdo do antigo prompt de abertura, preservado integralmente",
            "A lista de treze leituras não orienta automaticamente novos chats",
        ),
        "snapshot do antigo prompt de Posicionamento Profissional e Autoridade",
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
    for text, label, phrases in (
        (knowledge_index_text, "índice da governança do conhecimento", ("status: referencia-atual-revisavel", "Mapa atual de uso", "não como correspondências obrigatórias")),
        (old_reconciliation_text, "reconciliação antiga", ("status: acervo-historico-consultivo", "Registro de uma etapa anterior")),
        (inventory_text, "inventário de conteúdos", ("status: referencia-de-busca-revisavel", "fotografias das etapas")),
        (old_foundations_text, "reconciliação curricular antiga", ("status: acervo-historico-consultivo", "Registro histórico consultivo")),
        (pluralism_text, "referência autoral de pluralismo", ("status: referencia-atual-revisavel", "permanece uma formulação autoral revisável")),
        (bridge_text, "nota-ponte histórica", ("status: acervo-historico-consultivo", "Registro histórico da decisão à época")),
        (old_matrix_text, "matriz histórica", ("status: acervo-historico-consultivo", "não define correspondências obrigatórias", "nenhum chat possui exclusividade")),
        (old_positioning_text, "deliberação antiga de posicionamento", ("status: acervo-historico-consultivo", "Registro misto de uma etapa anterior")),
        (formulations_text, "registro de formulações", ("status: acervo-historico-consultivo", "não cria portões para as aulas", "Aprovada na etapa registrada")),
        (old_protocol_text, "protocolo histórico", ("status: historico-consultivo-substituido", "Documento histórico consultivo", "nenhuma conversa possui autoridade exclusiva")),
    ):
        require_phrases(text, phrases, label, errors)
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
            "Uso em diferentes assistentes",
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
            "Continuidade proporcional",
            "documentos novos ou alterados em relação à `main`",
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
        POSITIONING_ENTRY: (
            "Formulação pública canônica",
            "Fonte curricular de consulta obrigatória",
            "A fonte única para reconstrução",
        ),
        POSITIONING_PROMPT: (
            "Antes de propor estratégia ou redação, leia integralmente",
            "Formulação pública canônica",
            "Não reabra como pendências",
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
    if POSITIONING_ENTRY.stat().st_size > 8000:
        errors.append(
            "porta de entrada de Posicionamento Profissional e Autoridade "
            f"excede 8000 bytes: {POSITIONING_ENTRY.stat().st_size}"
        )
    if POSITIONING_PROMPT.stat().st_size > 2500:
        errors.append(
            "apontador de Posicionamento Profissional e Autoridade "
            f"excede 2500 bytes: {POSITIONING_PROMPT.stat().st_size}"
        )

    for adapter in ADAPTERS:
        text = adapter.read_text(encoding="utf-8")
        if adapter.stat().st_size > 2500:
            errors.append(f"adaptador excede 2500 bytes: {adapter.name}")
        for pointer in REQUIRED_POINTERS:
            if pointer not in text:
                errors.append(f"{adapter.name} não aponta para {pointer}")

    if OLD_PROTOCOL.is_file():
        for number, line in enumerate(old_protocol_text.splitlines(), start=1):
            if "emitir Relatório de Retomada e aguardar deliberação autoral" in line and "~~" not in line:
                errors.append(f"ritual ultrapassado ainda ativo: {OLD_PROTOCOL}:{number}")
    else:
        warnings.append("protocolo histórico do TSH não encontrado no caminho esperado")

    validate_changed_documents(errors)

    result = {"ok": not errors, "errors": errors, "warnings": warnings}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
