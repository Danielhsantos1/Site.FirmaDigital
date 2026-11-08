# Formato de handoff e arquivos de projeto

Cada projeto vive em `projects/<slug>/` (slug em minúsculas, hífens). Arquivos por etapa:

| Arquivo | Dono | Template |
|---|---|---|
| `00-brief.md` | executive-creative-director | `templates/brief.md` |
| `01-trends.md` | trend-hunter | `templates/trend-report.md` |
| `02-strategy.md` | viral-strategist | `templates/viral-strategy.md` |
| `03-script.md` | scriptwriter | `templates/script.md` |
| `04-direction.md` | film-director | `templates/direction.md` |
| `05-art-bible.md` | art-director | `templates/art-bible.md` |
| `06-prompts.md` | prompt-engineer | `templates/prompt-sheet.md` |
| `07-audio-plan.md` | audio-producer | `templates/audio-plan.md` |
| `08-edit-plan.md` | video-editor | `templates/edit-plan.md` |
| `09-qa-report.md` | quality-reviewer | `templates/qa-report.md` |
| `10-performance.md` | growth-analyst | `templates/performance-report.md` |
| `STATUS.md` | executive-creative-director | `templates/project-status.md` |

Cada arquivo começa com o cabeçalho do template (projeto, versão, autor-agente, data, entradas usadas, status). Só o dono edita seu arquivo; mudanças pedidas por outros passam pelo ECD.

## Rastreabilidade obrigatória (a partir da Missão 03)
Todo entregável numerado termina com a seção `## Rastreabilidade`, contendo exatamente estas linhas: `Fontes:`, `Fatos confirmados:`, `Hipóteses:`, `Pendências:` e `Responsável:`. Fato sem fonte vai para Hipóteses ou Pendências, nunca para Fatos confirmados.

## Versões e revisões
O arquivo original (v1) não é sobrescrito após revisão do Quality Reviewer. A correção é gravada como `<nome>.v2.md` (depois `.v3.md`), com cabeçalho `substitui: <arquivo anterior>` e resumo das mudanças. O `STATUS.md` indica a versão vigente. Arquivos em pastas iniciadas por `_` (`_sources`, `_qa-test`, `_execution`) não são entregáveis.
