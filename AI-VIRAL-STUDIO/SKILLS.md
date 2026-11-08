# Skills

Estado: **12 esqueletos** em `.claude/skills/<nome>/SKILL.md`, com frontmatter (`name`, `description`), quando usar, entradas, procedimento, saída, referências e conhecimento a pesquisar. Os procedimentos descrevem processo; **nenhum conhecimento técnico de ferramenta foi escrito**.

| Skill | Agente | Saída |
|---|---|---|
| project-intake | executive-creative-director | 00-brief, STATUS |
| campaign-orchestration | executive-creative-director | STATUS, resumo final |
| trend-research | trend-hunter | 01-trends |
| viral-retention-strategy | viral-strategist | 02-strategy |
| script-writing | scriptwriter | 03-script |
| shot-direction | film-director | 04-direction |
| visual-identity-consistency | art-director | 05-art-bible |
| media-prompt-engineering | prompt-engineer | 06-prompts |
| audio-production-planning | audio-producer | 07-audio-plan |
| edit-planning | video-editor | 08-edit-plan |
| quality-review | quality-reviewer | 09-qa-report |
| performance-analysis | growth-analyst | 10-performance |

## Convenções
- `name` = nome da pasta; minúsculas e hífens. `description` diz o que faz **e quando usar**.
- Skill referencia `templates/` e `knowledge/` por caminho; `validate.py` confere que existem.
- Todo ponto sem base documentada aparece em "Conhecimento a pesquisar" como `[A PESQUISAR]`.

## Conhecimento ainda a pesquisar (consolidado)
| Área | Pendência | Skills afetadas |
|---|---|---|
| Cinematografia | Definições verificadas de planos, movimentos e iluminação | shot-direction |
| Ferramentas de vídeo | Guias oficiais de prompt, limites e parâmetros (Veo, Kling, Runway) | media-prompt-engineering, shot-direction |
| Geração de imagem | Ferramenta(s) a adotar e seus guias | media-prompt-engineering, visual-identity-consistency |
| Consistência | Técnicas por ferramenta, validadas por teste | visual-identity-consistency, media-prompt-engineering |
| Retenção/Reels | Estruturas documentadas com fonte | viral-retention-strategy, edit-planning |
| Copy e storytelling | Estruturas e fórmulas com fonte | script-writing |
| Plataformas | Especificações de exportação e práticas, datadas | edit-planning, viral-retention-strategy, performance-analysis |
| Áudio | Licenças, termos de voz sintética, fontes de trilha | audio-production-planning |
| Tendências | Fontes e método de coleta | trend-research |
| Métricas | Métricas por plataforma e exportação | performance-analysis |

## Compatibilidade
O formato (diretório + `SKILL.md` com frontmatter YAML) segue o padrão de Skills do Claude Code. Campos opcionais (ex.: restrição de ferramentas) não foram usados de propósito.
