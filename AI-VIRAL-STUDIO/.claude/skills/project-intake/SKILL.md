---
name: project-intake
description: Recebe um pedido e produz o brief do projeto (00-brief.md) e a pasta projects/<slug>/. Use ao iniciar qualquer campanha ou vídeo, antes de delegar a qualquer especialista.
---

# project-intake

**Agente responsável:** `executive-creative-director` · **Status:** esqueleto inicial (procedimento de processo; conhecimento técnico ainda não documentado)

## Quando usar
Início de projeto, ou quando o brief estiver incompleto.

## Entradas
Pedido livre do usuário.

## Procedimento
1. Criar o slug (minúsculas, hífens) e a pasta `projects/<slug>/`.
2. Copiar `templates/brief.md` para `00-brief.md`.
3. Preencher o que o pedido já informa; para cada campo vazio, formular pergunta objetiva ao usuário (objetivo, público, plataforma, formato/duração, tom, marca/ativos, restrições, prazo, critério de sucesso).
4. Perguntar antes de presumir; registrar respostas e premissas confirmadas.
5. Criar `STATUS.md` a partir de `templates/project-status.md`.
6. Obter confirmação do usuário sobre o brief antes de delegar.

## Saída
`projects/<slug>/00-brief.md` e `STATUS.md`.

## Referências
- `templates/brief.md`
- `templates/project-status.md`
- `.claude/rules/handoff-format.md`

## Conhecimento a pesquisar e documentar
- [A PESQUISAR] Lista mínima de campos do brief por tipo de entrega (anúncio, demo de software, storytelling) a validar com uso real.

## Regras
Segue `.claude/rules/no-fabrication.md`. Fato técnico sem fonte em `knowledge/` não é afirmado.
