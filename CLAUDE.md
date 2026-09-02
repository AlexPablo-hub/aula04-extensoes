# CLAUDE.md

Laboratório da Aula 04 (MCPs, Skills e Subagentes) da disciplina Tópicos Especiais
em Programação. Três extensões de agente sobre o diário de notas de uma turma — o
mesmo domínio das Aulas 02 e 03.

## Estrutura

- `servidor.py` — servidor MCP `diario`: as ferramentas `listar_alunos`,
  `boletim`, `lancar_nota`, `resumo_turma` e o recurso `diario://regras`.
- `dados/turma.csv` — notas da turma (dados fictícios). N1 e N2 peso 3, N3 peso 4.
- `.mcp.json` — registro do servidor. Caminhos relativos (`.venv/Scripts/...`,
  `servidor.py`), resolvidos a partir da raiz do projeto — funciona em qualquer
  clone sem editar nada. Assume `.venv` no layout Windows.
- `.claude/skills/relatorio-de-atividade/` — Skill que fecha a entrega. Acione-a
  ("escreve o relatório desta atividade") em vez de reescrever o procedimento.
- `.claude/agents/auditor-de-contexto.md` — subagente que audita este arquivo.
- `medicao.md` — resultado do experimento da seção 5.5 (economia de contexto do
  subagente). Abra só se for refazer ou citar a medição.

## Ambiente

- Python 3.12 em `.venv`, ativado. Dependências: `mcp[cli]` e `pytest`.
- SDK `mcp` 2.x: a classe é `MCPServer` (`from mcp.server import MCPServer`).

## Como rodar

- `mcp dev servidor.py` — testa o servidor no MCP Inspector, sem agente.
- `python -m pytest -q` — a suíte de testes.
- Em uso normal, quem inicia o servidor é o Claude Code, pela config do `.mcp.json`
  (`claude mcp list` mostra `diario`). Para depurar, rode `python servidor.py` à
  mão e leia o traceback (ele fica parado à espera de stdin — isso é o esperado).

## Convenções do domínio

- Toda regra de cálculo e validação de nota vive em `servidor.py`, não no prompt.
- Erro de uso previsível (nota fora da faixa, matrícula inexistente) é `ToolError`;
  erro não previsto sobe como exceção comum e vai para o log.
- Dado de aluno real não entra neste repositório.
