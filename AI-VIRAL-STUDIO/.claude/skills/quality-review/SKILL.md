---
name: quality-review
description: Revisa entregáveis contra brief, templates e regras e emite veredito em 09-qa-report.md. Use nos gates do workflow.
---

# quality-review

**Agente responsável:** `quality-reviewer` · **Status:** esqueleto inicial (procedimento de processo; conhecimento técnico ainda não documentado)

## Quando usar
Nos gates definidos em `WORKFLOWS.md`.

## Entradas
Entregável(is) sob revisão e arquivos de referência.

## Procedimento
1. Verificar aderência ao brief.
2. Verificar conformidade com o template do entregável.
3. Verificar consistência com arquivos anteriores (nomes, durações, personagens).
4. Verificar a regra de não invenção: fatos sem fonte, métricas, mídia fictícia.
5. Classificar achados e emitir veredito.
6. Registrar em `templates/qa-report.md`.

## Saída
Nova seção em `projects/<slug>/09-qa-report.md`.

## Referências
- `templates/qa-report.md`
- `.claude/rules/no-fabrication.md`
- `.claude/rules/handoff-format.md`

## Conhecimento a pesquisar e documentar
- [A PESQUISAR] Checklists específicos por tipo de entregável após as primeiras execuções reais.

## Regras
Segue `.claude/rules/no-fabrication.md`. Fato técnico sem fonte em `knowledge/` não é afirmado.
