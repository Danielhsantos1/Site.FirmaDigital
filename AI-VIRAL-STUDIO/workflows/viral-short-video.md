# Workflow: vídeo curto viral (pipeline principal)

**Status:** rascunho · **Gatilho:** pedido de vídeo curto/anúncio/Reel a partir de uma ideia ou produto.

## Etapas
| # | Agente | Entradas | Saída | Gate QA |
|---|---|---|---|---|
| 0 | executive-creative-director | pedido | `00-brief.md`, `STATUS.md` | confirmação do usuário |
| 1 | trend-hunter | 00 | `01-trends.md` | |
| 2 | viral-strategist | 00, 01 | `02-strategy.md` | ✔ |
| 3 | scriptwriter | 00, 01, 02 | `03-script.md` | ✔ |
| 4 | film-director | 00, 02, 03 | `04-direction.md` | ✔ |
| 5 | art-director | 00, 02, 03, 04 | `05-art-bible.md` | ✔ |
| 6 | prompt-engineer | 04, 05 | `06-prompts.md` | ✔ |
| 7 | audio-producer | 02, 03, 04 | `07-audio-plan.md` | ✔ |
| 8 | video-editor | 02, 03, 04, 07 | `08-edit-plan.md` | ✔ |
| 9 | quality-reviewer | todos | `09-qa-report.md` (revisão final) | final |
| 10 | growth-analyst | métricas reais | `10-performance.md` | opcional |

## Paralelismo possível (a validar)
Etapas 6 e 7 dependem de 4 e 5 / 4, respectivamente, e não entre si.

## Condições de parada
Reprovação após 2 ciclos de retrabalho; `NEEDS_INFO` sem resposta do usuário; item bloqueante `[A PESQUISAR]`.

## Pendências
Definir variantes (demo de software, storytelling, sequência de posts) após validar este pipeline.
