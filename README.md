# aula04-extensoes

Laboratório da **Aula 04 — Criando seus próprios MCPs, Skills e Subagentes**
(Tópicos Especiais em Programação). Três extensões de agente sobre o diário de
notas de uma turma:

| Extensão | Arquivo | O que resolve |
| --- | --- | --- |
| Servidor MCP `diario` | `servidor.py` | lê/grava notas em CSV, calcula média ponderada, classifica situação |
| Skill `relatorio-de-atividade` | `.claude/skills/relatorio-de-atividade/SKILL.md` | padroniza o relatório de fechamento de entrega |
| Subagente `auditor-de-contexto` | `.claude/agents/auditor-de-contexto.md` | audita o `CLAUDE.md` contra os seis defeitos de configuração |

## Agente: Claude Code

A aula é escrita para o OpenCode; o professor liberou os equivalentes do Claude
Code, que é o agente do grupo. A correspondência:

| Aula (OpenCode) | Aqui (Claude Code) |
| --- | --- |
| `opencode.json` → bloco `mcp` | `.mcp.json` → `mcpServers` |
| `.opencode/skills/<nome>/SKILL.md` | `.claude/skills/<nome>/SKILL.md` (formato idêntico) |
| `.opencode/agents/<nome>.md` + bloco `permission:` | `.claude/agents/<nome>.md` + `tools:` (allowlist) |
| `AGENTS.md` (do `/init`) | `CLAUDE.md` (do `/init`) |
| `opencode mcp list` / `opencode agent list` | `claude mcp list` / subagentes em `/agents` |

## Ambiente

```
python -m venv .venv
.venv\Scripts\Activate.ps1        # Windows;  ou:  source .venv/bin/activate
pip install "mcp[cli]" pytest
```

SDK: `mcp` 2.x — a classe é `MCPServer` (`from mcp.server import MCPServer`), não `FastMCP`.

## Rodar

```
mcp dev servidor.py     # testa o servidor no MCP Inspector, sem agente
python -m pytest -q      # 15 testes das regras e das ferramentas
claude mcp list         # deve mostrar "diario" (aprovar o .mcp.json na 1a vez)
```

O servidor é iniciado pelo Claude Code a partir do `.mcp.json`, com caminhos
relativos resolvidos a partir da raiz do projeto — nenhum integrante precisa
editar o arquivo. (O `.venv` é o do layout Windows: `.venv/Scripts/python.exe`.)

## Entregas

- **Entrega 1** — este repositório (lab feito em sala).
- **Entrega 2** — `relatorio.md`, gerado pela Skill e revisado à mão, mais as duas
  versões do `SKILL.md` com a nota do que mudou.

Medição da economia de contexto do subagente: `medicao.md` (seção 5.5 da aula).
