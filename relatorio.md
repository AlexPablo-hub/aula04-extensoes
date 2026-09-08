# Relatório — Aula 04: MCPs, Skills e Subagentes

## O que foi pedido

Criar minhas próprias extensões de agente — um servidor MCP, uma Skill e um subagente — sobre o diário de notas da turma das Aulas 02/03. A Entrega 2 pede ainda o `relatorio.md` gerado pela Skill e as duas versões do `SKILL.md`.

## O que foi feito

- Servidor MCP `diario` (`servidor.py`): ferramentas `listar_alunos`, `boletim`, `lancar_nota`, `resumo_turma` e recurso `diario://regras`, com média ponderada 3-3-4 e situação calculadas no servidor.
- Tratei uso previsível como `ToolError` (nota fora de 0–10, matrícula inexistente); rodei `pytest` e passam os 15 testes, com o CSV isolado em `tmp`.
- Configurei o `.mcp.json` com caminhos relativos; `claude mcp list` mostra `diario`.
- Entreguei a Skill `relatorio-de-atividade` em duas versões, com `HISTORICO.md` registrando o diff.
- Entreguei o subagente `auditor-de-contexto` sem `Edit`/`Write`/`Bash` e o `medicao.md` com o experimento de economia de contexto (1 chamada contra 6).

## O que falhou

Não houve falha de execução: nenhum traceback nem revert no `git log`. O histórico mostra três ajustes:

- Registrei o servidor com `cwd` em caminho absoluto (commit `03b1c4d`) — cada integrante teria de editar o arquivo ao clonar.
- O `AGENTS.md` inicial (commit `ea71da5`) nasceu com 67 linhas e os seis defeitos de configuração de Santos et al.
- A v1 da Skill gerou um relatório de 678 palavras e em voz impessoal, fora do formato pedido.

## Como foi resolvido

- Troquei o `cwd` absoluto por caminhos relativos resolvidos a partir da raiz do projeto (commit `391b337`); verifiquei com `claude -p` chamando `mcp__diario__listar_alunos`.
- Rodei o subagente `auditor-de-contexto`, apliquei as correções e enxuguei o arquivo para 39 linhas (commit `f7cd870`).
- Reescrevi o `SKILL.md` (v2): teto de 400 palavras, limites por seção e "primeira pessoa do singular" como regra nº 1.

## Ferramentas de IA

- Claude Code (Sonnet 5) — implementei `servidor.py`, os testes, o `.mcp.json` e a Skill, e escrevi os commits.
- Subagente `auditor-de-contexto` (Sonnet 5; tools Read/Grep/Glob) — auditou o `CLAUDE.md` no passo 10.
- Subagente de exploração `Explore` (Sonnet 5) — rodada B da medição da seção 5.5.
- Skill `relatorio-de-atividade` (Claude Code, Sonnet 5) — gerou este `relatorio.md`.

## O que faltou?

- A aula é escrita para OpenCode e usei Claude Code na correspondência aprovada pelo professor — isso vale na correção da Entrega 1?
- O `.mcp.json` assume o layout Windows (`.venv/Scripts/python.exe`); preciso de fallback para `.venv/bin/python`?
- A medição usou o `subagent_tokens` do Claude Code no lugar de `opencode stats` — a equivalência é aceita?
- Ainda falta commitar e dar push neste `relatorio.md`.
