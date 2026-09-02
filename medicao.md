# Medição — economia de contexto do subagente (seção 5.5)

**Pergunta das duas rodadas:** "Investigue o pacote `mcp` instalado em `.venv` e me
diga, em um parágrafo, quais transportes ele suporta e em quais arquivos cada um
está implementado."

**Adaptação:** a aula mede no OpenCode com `/details` (contagem de chamadas) e
`opencode stats --days 1` (tokens). Aqui o agente é o Claude Code; usei a contagem
de chamadas do transcript e o campo `subagent_tokens` que o próprio Claude Code
reporta ao encerrar a tarefa delegada (equivalente ao `Input` do `opencode stats`).

## Rodada A — sem subagente

A investigação aconteceu na **minha janela**. Chamadas para responder:

| # | Ferramenta | Resultado |
|---|-----------|-----------|
| 1 | Glob `**/mcp/**/*.py` | vazio (o `.gitignore` esconde `.venv/` das buscas) |
| 2 | Glob `**/*transport*.py` | 3 arquivos |
| 3 | Glob `**/mcp/server/*.py` | vazio (mesmo motivo) |
| 4 | Bash `ls server/ client/` + grep `Literal["stdio"` | listagem + 3 hits |
| 5 | Read `server/mcpserver/server.py` (70 linhas) | o `match transport` |
| 6 | Bash grep `run_*_async` + `cat __init__.py` + `head` de 3 transportes | cabeçalhos |

- **6 chamadas** (3 Glob, 1 Read, 2 Bash); 2 delas infrutíferas.
- **~3.000 tokens** de listagens, trechos e cabeçalhos entraram na janela principal
  **e ficam lá** pelo resto da sessão.
- Resposta obtida: 3 transportes (`stdio`, `sse`, `streamable-http`, os aceitos por
  `MCPServer.run`). **Não** cheguei ao transporte in-memory de teste nem ao lado
  cliente — a investigação parou raso.

## Rodada B — com subagente

Deleguei a mesma pergunta ao subagente de exploração (`@explore` na aula).

- **1 chamada** na minha janela (a de delegação).
- O que voltou para a minha janela: **1 parágrafo, ~155 palavras (~260 tokens)**.
- O que o subagente gastou, na **janela dele**: **43.157 tokens** e **18 chamadas
  de ferramenta**, em ~67 s (números reportados pelo Claude Code ao fim da tarefa).
- Resposta obtida: mais completa que a da Rodada A — os 4 transportes
  (`stdio` em `server/stdio.py` + `client/stdio.py`; `sse`, legado, em `server/sse.py`
  + `client/sse.py`; `streamable-http` em `server/streamable_http.py`,
  `streamable_http_manager.py` e `_streamable_http_modern.py` + `client/streamable_http.py`;
  in-memory de teste em `shared/memory.py` + `client/_memory.py`), com a observação
  de que WebSocket foi removido.

## Números lado a lado

| | Rodada A (sem) | Rodada B (com) |
|---|---|---|
| Chamadas na minha janela | 6 | 1 |
| Tokens de investigação na minha janela | ~3.000 (permanentes) | ~260 (o parágrafo) |
| Tokens gastos na investigação | ~3.000 | ~43.157 (na janela do subagente) |
| Profundidade da resposta | 3 transportes, sem o lado cliente | 4 transportes, servidor + cliente |

## Conclusão

O subagente **gastou ~14× mais tokens** para responder (43 k contra 3 k) e mesmo
assim **foi o mais barato para o que importa**: custou 1 chamada e ~260 tokens da
minha janela, contra 6 chamadas e ~3.000 tokens que a Rodada A deixou entulhados
lá até o fim da sessão. Janela e tokens são recursos diferentes (seção 5.1), e a
janela — que é finita e não se recupera — é o gargalo. Delegar troca um recurso
abundante (tokens) por um escasso (espaço de contexto), e ainda entregou uma
resposta mais completa porque as 18 leituras couberam todas na janela do orientando.
