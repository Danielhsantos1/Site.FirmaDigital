---
name: trend-research
description: Pesquisa tendências, formatos e referências com fonte e data e produz 01-trends.md. Use na fase de descoberta de um projeto.
---

# trend-research

**Agente responsável:** `trend-hunter` · **Status:** esqueleto inicial (procedimento de processo; conhecimento técnico ainda não documentado)

## Quando usar
Após o brief; antes da estratégia.

## Entradas
`00-brief.md`.

## Procedimento
1. Definir perguntas de pesquisa a partir do brief (nicho, plataforma, público).
2. Pesquisar em fontes abertas; registrar URL, data de consulta e confiança para cada achado.
3. Separar evidência observada de interpretação.
4. Listar referências reais (links) e o que as torna eficazes, sem copiar.
5. Registrar lacunas que não foi possível confirmar.
6. Preencher `templates/trend-report.md`.

## Saída
`projects/<slug>/01-trends.md`.

## Referências
- `templates/trend-report.md`
- `knowledge/trends/README.md`
- `knowledge/platforms/README.md`
- `.claude/rules/no-fabrication.md`

## Conhecimento a pesquisar e documentar
- [A PESQUISAR] Fontes confiáveis por plataforma e método de coleta.
- [A PESQUISAR] Critério para distinguir tendência de moda passageira.

## Regras
Segue `.claude/rules/no-fabrication.md`. Fato técnico sem fonte em `knowledge/` não é afirmado.
