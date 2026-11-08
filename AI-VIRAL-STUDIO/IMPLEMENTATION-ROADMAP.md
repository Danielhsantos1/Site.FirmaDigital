# Roadmap de implementação

## Fase 0 — Fundação (Missão 01) ✔
Estrutura, 11 agentes, 12 skills, 12 templates, regras, documentação, validador.

## Fase 1 — Validar o núcleo (próxima)
1. **R1 – Orquestração:** testar `claude --agent executive-creative-director` delegando aos especialistas com `Agent(...)` restrito; confirmar que `.claude/rules/` e skills carregam; ajustar `tools` se necessário.
2. **Piloto de ponta a ponta com 1 brief real** (sem geração de mídia): percorrer 00→09, medir retrabalho, corrigir templates e skills.
3. Ajustar gates do QA conforme o piloto.

## Fase 2 — Conhecimento (pesquisa com fonte)
Ordem sugerida, por impacto no piloto: plataformas e vídeo curto → cinematografia e câmera/luz → storytelling e copy → prompts de vídeo (por ferramenta escolhida) → consistência → áudio → tendências (método).

## Fase 3 — Workflows e variantes
Derivar demo de software, anúncio, storytelling, sequência de posts, somente-prompts e somente-storyboard do pipeline validado.

## Fase 4 — Integrações (uma por vez, com aprovação)
Escolher a primeira ferramenta, preencher seu arquivo em `integrations/`, decidir linguagem do adaptador, implementar `validate`/`submit`/`status`/`fetch` com custo controlado.

## Fase 5 — Empacotamento
Script de ZIP compartilhável (fora da Missão 01) e interface somente se o uso real justificar.

## Pendências identificadas na Missão 01
| ID | Pendência |
|---|---|
| R1 | Confirmar delegação do ECD como agente principal |
| R2 | `.claude/` só carrega ao abrir o Claude Code nesta pasta; decidir se vira repositório próprio |
| R3 | Duas instalações do Claude Code no ambiente (2.1.319 no PATH e 2.1.42 global no npm); confirmar qual o usuário usa |
| R4 | `knowledge/` vazio: nenhum guia de ferramenta documentado |
| R5 | Integrações 100% pendentes de pesquisa oficial |
| R6 | `projects/` ignorado pelo git: decidir se projetos de cliente serão versionados |
| R7 | Definir ferramenta(s) de imagem (nenhuma foi nomeada no planejamento) |
| R8 | Variantes de workflow ainda não criadas |
