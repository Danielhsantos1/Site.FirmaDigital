---
name: visual-identity-consistency
description: Cria o art bible (identidade visual, fichas de personagem e cenário, regras de consistência) e produz 05-art-bible.md. Use após a direção.
---

# visual-identity-consistency

**Agente responsável:** `art-director` · **Status:** esqueleto inicial (procedimento de processo; conhecimento técnico ainda não documentado)

## Quando usar
Após ou junto de `04-direction.md`.

## Entradas
`00-brief.md`, `02-strategy.md`, `03-script.md`, `04-direction.md`, ativos de marca.

## Procedimento
1. Definir conceito visual, paleta e estilo a partir do brief e da marca.
2. Criar ficha para cada personagem e cenário com atributos fixos.
3. Listar referências visuais reais com origem.
4. Escrever regras de consistência verificáveis e lista do que evitar.
5. Preencher `templates/art-bible.md`.

## Saída
`projects/<slug>/05-art-bible.md`.

## Referências
- `templates/art-bible.md`
- `knowledge/consistency/README.md`
- `knowledge/prompts-image/README.md`

## Conhecimento a pesquisar e documentar
- [A PESQUISAR] Técnicas de consistência de personagem e cenário por ferramenta (pesquisa e testes necessários).

## Regras
Segue `.claude/rules/no-fabrication.md`. Fato técnico sem fonte em `knowledge/` não é afirmado.
