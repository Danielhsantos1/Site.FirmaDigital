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
| R1 | ~~Confirmar delegação do ECD~~ **Resolvido (Missão 02)**: ping real aprovado; skills corrigidas via `skills:` e `Skill` |
| R2 | `.claude/` só carrega ao abrir o Claude Code nesta pasta; decidir se vira repositório próprio |
| R3 | Instalação duplicada: **explicada** em `docs/ENVIRONMENT-AUDIT.md` (pacote npm órfão no contêiner, sem conflito); falta checar a máquina local do usuário |
| R4 | `knowledge/` vazio: nenhum guia de ferramenta documentado |
| R5 | Integrações 100% pendentes de pesquisa oficial |
| R6 | `projects/` ignorado pelo git: decidir se projetos de cliente serão versionados |
| R7 | Definir ferramenta(s) de imagem (nenhuma foi nomeada no planejamento) |
| R8 | Variantes de workflow ainda não criadas |
| R9 | Migração para `Danielhsantos1/AI-Viral-Studio`: plano pronto em `docs/MIGRATION-PLAN.md`, aguarda autorização e criação do repositório |
| R10 | Brief da Forma Digital com 12 perguntas ao cliente, incluindo o nome da marca (Forma ou Firma), em `projects/forma-digital/00-brief.md` |
| R11 | Skills de 9 dos 10 especialistas e a escrita real de entregáveis ainda não testadas em execução |
| R12 | `Glob`/`Grep` listadas nos agentes não foram expostas ao ECD nesta versão do Claude Code; revisar a lista de ferramentas |
