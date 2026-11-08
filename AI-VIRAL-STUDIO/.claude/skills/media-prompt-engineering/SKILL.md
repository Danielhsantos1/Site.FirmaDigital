---
name: media-prompt-engineering
description: Gera prompts de imagem e vídeo por plano e ferramenta e produz 06-prompts.md. Use somente com direção e art bible aprovados.
---

# media-prompt-engineering

**Agente responsável:** `prompt-engineer` · **Status:** esqueleto inicial (procedimento de processo; conhecimento técnico ainda não documentado)

## Quando usar
Após `04-direction.md` e `05-art-bible.md` aprovados.

## Entradas
`04-direction.md`, `05-art-bible.md`, ferramentas-alvo, documentação em `knowledge/` e `integrations/`.

## Procedimento
1. Listar planos e ferramentas-alvo.
2. Para cada ferramenta, conferir documentação em `knowledge/prompts-*`; sem documentação, marcar `[A PESQUISAR]` e usar formato genérico rotulado.
3. Compor um prompt por plano reutilizando descrições fixas do art bible.
4. Registrar parâmetros, ordem de geração e riscos.
5. Preencher `templates/prompt-sheet.md` mantendo rastreio plano → prompt.

## Saída
`projects/<slug>/06-prompts.md`.

## Referências
- `templates/prompt-sheet.md`
- `knowledge/prompts-image/README.md`
- `knowledge/prompts-video/README.md`
- `knowledge/consistency/README.md`
- `integrations/README.md`

## Conhecimento a pesquisar e documentar
- [A PESQUISAR] Guias oficiais de prompt de cada ferramenta (Veo, Kling, Runway e geradores de imagem escolhidos).
- [A PESQUISAR] Parâmetros e limites por ferramenta com data de verificação.

## Regras
Segue `.claude/rules/no-fabrication.md`. Fato técnico sem fonte em `knowledge/` não é afirmado.
