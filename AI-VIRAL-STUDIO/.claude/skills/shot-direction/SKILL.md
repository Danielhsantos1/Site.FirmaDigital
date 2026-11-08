---
name: shot-direction
description: Decupa o roteiro em cenas e planos com enquadramento, movimento, luz e continuidade e produz 04-direction.md. Use após o roteiro.
---

# shot-direction

**Agente responsável:** `film-director` · **Status:** esqueleto inicial (procedimento de processo; conhecimento técnico ainda não documentado)

## Quando usar
Após `03-script.md`.

## Entradas
`03-script.md`, `02-strategy.md`, `00-brief.md`.

## Procedimento
1. Dividir o roteiro em cenas e planos numerados.
2. Para cada plano: descrição visual, enquadramento, movimento, iluminação, duração, transição prevista.
3. Declarar continuidade (personagem, cenário, eixo).
4. Sinalizar planos de risco para geração por IA.
5. Registrar requisitos para áudio e edição.
6. Preencher `templates/direction.md`.

## Saída
`projects/<slug>/04-direction.md`.

## Referências
- `templates/direction.md`
- `knowledge/cinematography/README.md`
- `knowledge/camera-and-lighting/README.md`

## Conhecimento a pesquisar e documentar
- [A PESQUISAR] Catálogo de movimentos de câmera, enquadramentos e iluminação com definições verificadas.
- [A PESQUISAR] Quais técnicas são reproduzíveis por cada gerador de vídeo (depende de pesquisa por ferramenta).

## Regras
Segue `.claude/rules/no-fabrication.md`. Fato técnico sem fonte em `knowledge/` não é afirmado.
