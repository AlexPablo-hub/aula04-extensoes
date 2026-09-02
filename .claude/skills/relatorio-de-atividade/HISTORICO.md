# Histórico do SKILL.md — Entrega 2

A Entrega 2 pede as duas versões da Skill e duas linhas do que mudou. O teste de
fogo: rodar a Skill e ver se o `relatorio.md` sai no formato especificado.

## O que mudou da v1 para a v2

- **Limite de tamanho virou número.** "Máximo de uma página" → "no máximo 400
  palavras" + tetos por seção (2 frases em "O que foi pedido", 5 bullets em "O que
  foi feito"). A v1 produziu um relatório de 678 palavras.
- **"Primeira pessoa do singular" virou regra nº 1, com exemplo** de certo
  ("implementei", "rodei") e errado ("foi implementado"). A v1 saiu quase toda
  impessoal.

## SKILL.md v1 (original, commit `ced6111`)

```markdown
---
name: relatorio-de-atividade
description: Escreve o relatório técnico de uma atividade prática da disciplina, no formato exigido pela avaliação. Use quando eu pedir relatório, documentação da atividade, ou quando eu disser que vou fechar a entrega.
---

# Relatório de atividade

1. Rode `git log --oneline` e leia os commits desta atividade.
2. Rode `git diff --stat` contra o primeiro commit, para saber o tamanho do que mudou.
3. Escreva `relatorio.md` com estas seções, nesta ordem:
   - **O que foi pedido** — o enunciado, em duas frases
   - **O que foi feito** — o que existe e funciona ao final
   - **O que falhou** — os erros que apareceram no caminho, com a mensagem exata
   - **Como foi resolvido** — o que corrigiu cada um
   - **Ferramentas de IA** — qual agente, qual modelo, e em que etapa de cada
4. Termine perguntando o que faltou, em vez de preencher lacuna com suposição.

Regras:
- Nunca invente um erro que não aconteceu. Se o histórico não mostra falha, escreva que não houve.
- Máximo de uma página. Relatório longo não é lido.
- Português do Brasil, primeira pessoa do singular.
```
