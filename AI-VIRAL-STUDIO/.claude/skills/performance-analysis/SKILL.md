---
name: performance-analysis
description: Analisa métricas reais fornecidas pelo usuário e propõe otimizações e testes em 10-performance.md. Use após publicação. Sem dados reais, apenas planeja a medição.
---

# performance-analysis

**Agente responsável:** `growth-analyst` · **Status:** esqueleto inicial (procedimento de processo; conhecimento técnico ainda não documentado)

## Quando usar
Após publicação, com métricas reais.

## Entradas
Métricas reais, `02-strategy.md`, `00-brief.md`.

## Procedimento
1. Registrar origem, período e plataforma de cada dado.
2. Comparar com as hipóteses da estratégia.
3. Diagnosticar com limites de amostra explícitos.
4. Priorizar recomendações e definir testes.
5. Indicar quais agentes reacionar.
6. Preencher `templates/performance-report.md`. Sem dados, entregar só o plano de medição e `NEEDS_INFO`.

## Saída
`projects/<slug>/10-performance.md`.

## Referências
- `templates/performance-report.md`
- `knowledge/platforms/README.md`

## Conhecimento a pesquisar e documentar
- [A PESQUISAR] Métricas relevantes por plataforma e como exportá-las.
- [A PESQUISAR] Método de comparação e teste adequado ao volume típico de dados.

## Regras
Segue `.claude/rules/no-fabrication.md`. Fato técnico sem fonte em `knowledge/` não é afirmado.
