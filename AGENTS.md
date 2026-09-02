# AGENTS.md

Este projeto foi inicializado para desenvolvimento colaborativo. Siga as melhores
práticas de engenharia de software, escreva código limpo e legível, e mantenha a
cobertura de testes alta. Este arquivo orienta agentes de código que trabalham
neste repositório.

## Visão geral

Laboratório da Aula 04 (MCPs, Skills e Subagentes) da disciplina Tópicos Especiais
em Programação. O projeto constrói três extensões de agente sobre o domínio das
Aulas 02 e 03 — o diário de notas de uma turma.

## Contexto: o Model Context Protocol

O Model Context Protocol (MCP) foi anunciado pela Anthropic em novembro de 2024
como um padrão aberto para conectar assistentes de LLM a fontes de dados e
ferramentas. Ele define uma arquitetura host / cliente / servidor que fala
JSON-RPC, geralmente sobre stdio para servidores locais ou sobre HTTP para
serviços em rede. O protocolo expõe três primitivas: ferramentas (controladas
pelo modelo), recursos (controlados pela aplicação) e prompts (controlados pelo
usuário). O SDK Python passou por uma mudança de versão principal na qual a classe
`FastMCP` foi renomeada para `MCPServer`. Um servidor MCP é portável: o mesmo
código serve OpenCode, Claude Code, Codex, Cursor e outros agentes.

## Estrutura

- `servidor.py` — servidor MCP `diario`.
- `dados/turma.csv` — notas da turma (dados fictícios).
- `opencode.json` — registro do servidor MCP.
- `.opencode/skills/relatorio-de-atividade/SKILL.md`
- `.opencode/agents/auditor-de-contexto.md`
- `medicao.md` — consulte também este arquivo.

## Estilo de código

- Siga a PEP 8: indentação de 4 espaços, linhas de no máximo 79 colunas.
- Use aspas duplas para strings.
- Funções auxiliares privadas começam com `_`.
- Ordene os imports: biblioteca padrão, depois terceiros, depois locais.

## Ambiente

- Python 3.12 em `.venv`. Ative antes de qualquer comando.
- Dependência única: `mcp[cli]`.

## Como rodar

- Testar o servidor sem agente: `mcp dev servidor.py` e abrir o MCP Inspector.
- Rodar os testes: `python -m pytest -q`.
- Para depurar, rode `python servidor.py` diretamente e observe a saída.
- Nunca rode o servidor manualmente — quem o executa é o host, pela config em `opencode.json`.

## Fechamento de entrega

Ao fechar a entrega, rode `git log --oneline` e leia os commits, rode
`git diff --stat` contra o primeiro commit, e escreva `relatorio.md` com as
seções: o que foi pedido, o que foi feito, o que falhou (com a mensagem exata de
cada erro), como foi resolvido, e quais ferramentas de IA foram usadas em cada
etapa. Máximo de uma página, português do Brasil, primeira pessoa. Termine
perguntando o que faltou.

## Convenções do domínio

- Toda regra de cálculo e validação de nota vive em `servidor.py`, não no prompt.
- Erro de uso previsível é `ToolError`; erro de programação sobe como exceção comum.
- Dados de aluno real não entram neste repositório.
