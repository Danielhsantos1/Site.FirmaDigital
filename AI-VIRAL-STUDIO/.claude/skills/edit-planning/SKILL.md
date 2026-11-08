---
name: edit-planning
description: Planeja montagem, cortes, ritmo, transições, legendas e exportação e produz 08-edit-plan.md. Use após direção, áudio e prompts.
---

# edit-planning

**Agente responsável:** `video-editor` · **Status:** esqueleto inicial (procedimento de processo; conhecimento técnico ainda não documentado)

## Quando usar
Após `07-audio-plan.md`.

## Entradas
`03-script.md`, `04-direction.md`, `07-audio-plan.md`, `02-strategy.md`, material real se existir.

## Procedimento
1. Montar timeline por tempo fechando com a duração-alvo.
2. Posicionar pontos de retenção da estratégia.
3. Definir cortes, transições e ritmo.
4. Escrever legendas com temporização.
5. Mapear camadas de áudio.
6. Definir especificações de exportação (do brief ou `knowledge/platforms/`).
7. Preencher `templates/edit-plan.md`.

## Saída
`projects/<slug>/08-edit-plan.md`.

## Referências
- `templates/edit-plan.md`
- `knowledge/short-form-video/README.md`
- `knowledge/platforms/README.md`
- `integrations/capcut.md`

## Conhecimento a pesquisar e documentar
- [A PESQUISAR] Especificações de exportação por plataforma com fonte.
- [A PESQUISAR] Viabilidade de integração com CapCut (hoje desconhecida).

## Regras
Segue `.claude/rules/no-fabrication.md`. Fato técnico sem fonte em `knowledge/` não é afirmado.
