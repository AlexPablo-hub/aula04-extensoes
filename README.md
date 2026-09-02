# aula04-extensoes

Laboratório da **Aula 04 — Criando seus próprios MCPs, Skills e Subagentes**
(Tópicos Especiais em Programação). Três extensões de agente sobre o diário de
notas de uma turma:

| Extensão | Arquivo | O que resolve |
| --- | --- | --- |
| Servidor MCP `diario` | `servidor.py` | lê/grava notas em CSV, calcula média ponderada, classifica situação |
| Skill `relatorio-de-atividade` | `.opencode/skills/relatorio-de-atividade/SKILL.md` | padroniza o relatório de fechamento de entrega |
| Subagente `auditor-de-contexto` | `.opencode/agents/auditor-de-contexto.md` | audita o `AGENTS.md` contra os seis defeitos de configuração |

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
```

O servidor em si é iniciado pelo host (OpenCode) a partir do bloco `mcp` do
`opencode.json`. O campo `cwd` ali é um caminho absoluto — **cada máquina precisa
ajustá-lo** para o caminho local do repositório.

## Entregas

- **Entrega 1** — este repositório (lab feito em sala).
- **Entrega 2** — `relatorio.md`, gerado pela Skill e revisado à mão, mais as duas
  versões do `SKILL.md` com a nota do que mudou.

Medição da economia de contexto do subagente: `medicao.md` (seção 5.5 da aula).
