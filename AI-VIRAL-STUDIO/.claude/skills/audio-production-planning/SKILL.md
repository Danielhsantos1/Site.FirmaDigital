---
name: audio-production-planning
description: Planeja narração, vozes, efeitos e trilha e produz 07-audio-plan.md. Use após roteiro e direção.
---

# audio-production-planning

**Agente responsável:** `audio-producer` · **Status:** esqueleto inicial (procedimento de processo; conhecimento técnico ainda não documentado)

## Quando usar
Após `04-direction.md`.

## Entradas
`03-script.md`, `04-direction.md`, `02-strategy.md`.

## Procedimento
1. Extrair texto de locução limpo do roteiro.
2. Definir direção de voz por trecho.
3. Mapear efeitos por plano.
4. Definir diretrizes de trilha e prioridades de mixagem.
5. Montar checklist de direitos e autorização de voz.
6. Preencher `templates/audio-plan.md`.

## Saída
`projects/<slug>/07-audio-plan.md`.

## Referências
- `templates/audio-plan.md`
- `knowledge/audio/README.md`
- `integrations/elevenlabs.md`

## Conhecimento a pesquisar e documentar
- [A PESQUISAR] Fontes de música/efeitos e licenças aplicáveis.
- [A PESQUISAR] Capacidades e termos de uso de voz sintética da ferramenta escolhida.

## Regras
Segue `.claude/rules/no-fabrication.md`. Fato técnico sem fonte em `knowledge/` não é afirmado.
