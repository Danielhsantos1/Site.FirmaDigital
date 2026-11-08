---
name: campaign-orchestration
description: Planeja e conduz o pipeline entre os 10 especialistas: ordem, delegação, gates do Quality Reviewer, retrabalho e consolidação. Use depois que o brief estiver aprovado.
---

# campaign-orchestration

**Agente responsável:** `executive-creative-director` · **Status:** esqueleto inicial (procedimento de processo; conhecimento técnico ainda não documentado)

## Quando usar
Brief aprovado; antes e durante a produção.

## Entradas
`00-brief.md` aprovado e `STATUS.md`.

## Procedimento
1. Escolher o workflow em `workflows/` adequado ao tipo de entrega.
2. Para cada etapa: montar a delegação (slug, caminhos de entrada, template de saída, critérios de aceite) e acionar o agente dono.
3. Exigir `Relatório ao Diretor` no retorno e checar a autoavaliação.
4. Acionar `quality-reviewer` nos gates definidos no workflow; tratar reprovação com no máximo 2 ciclos.
5. Atualizar `STATUS.md` a cada etapa concluída.
6. Consolidar resumo final ao usuário: arquivos, decisões, pendências `[A PESQUISAR]`, próximos passos.

## Saída
`STATUS.md` atualizado e resumo final.

## Referências
- `WORKFLOWS.md`
- `workflows/`
- `AGENTS.md`
- `.claude/rules/communication-protocol.md`

## Conhecimento a pesquisar e documentar
- [A PESQUISAR] Validar em execução real se o agente principal consegue delegar com `Agent(...)` restrito (ver IMPLEMENTATION-ROADMAP).
- [A PESQUISAR] Definir política de paralelismo após primeiros testes.

## Regras
Segue `.claude/rules/no-fabrication.md`. Fato técnico sem fonte em `knowledge/` não é afirmado.
