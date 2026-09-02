---
name: relatorio-de-atividade
description: Escreve o relatório técnico de uma atividade prática da disciplina, no formato exigido pela avaliação. Use quando eu pedir relatório, documentação da atividade, ou quando eu disser que vou fechar a entrega.
---

# Relatório de atividade

1. Rode `git log --oneline` e leia os commits desta atividade.
2. Rode `git diff --stat` contra o primeiro commit, para saber o tamanho do que mudou.
3. Escreva `relatorio.md` com estas seções, nesta ordem e com estes limites:
   - **O que foi pedido** — o enunciado, em no máximo 2 frases.
   - **O que foi feito** — o que existe e funciona ao final, em no máximo 5 bullets de uma linha.
   - **O que falhou** — os erros que apareceram no caminho, com a mensagem exata. Se não houve, uma frase dizendo isso.
   - **Como foi resolvido** — o que corrigiu cada erro da seção anterior, um por linha.
   - **Ferramentas de IA** — qual agente, qual modelo, em que etapa. Um bullet por ferramenta.
4. Termine com a seção **O que faltou?** perguntando o que ficou em aberto, em vez de preencher lacuna com suposição.

Regras (confira cada uma antes de fechar o arquivo):
- **Primeira pessoa do singular.** Escreva "implementei", "rodei os testes", "corrigi o cwd". Nunca "foi implementado", "os testes foram rodados", "o cwd foi corrigido".
- **No máximo 400 palavras** no arquivo todo, títulos à parte. Conte antes de fechar — relatório longo não é lido.
- **Não invente erro.** Se o `git log` não mostra revert nem commit de correção, escreva que não houve falha de execução.
- Português do Brasil.
