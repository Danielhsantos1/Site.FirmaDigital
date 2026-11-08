# Agentes

Lista oficial e fechada: 11 agentes. Não criar, remover nem renomear sem aprovação do usuário. Especificação completa de cada um em `.claude/agents/<nome>.md` (identidade, objetivo, entradas, saídas, critérios de qualidade, limites, comunicação com o diretor).

| # | Agente | Responsabilidade | Entrega | Skill |
|---|---|---|---|---|
| 1 | `executive-creative-director` | Orquestra os outros 10; único contato com o usuário | `00-brief`, `STATUS` | project-intake, campaign-orchestration |
| 2 | `trend-hunter` | Tendências e referências com fonte e data | `01-trends` | trend-research |
| 3 | `viral-strategist` | Viralização e retenção como hipóteses testáveis | `02-strategy` | viral-retention-strategy |
| 4 | `scriptwriter` | Roteiro e storytelling | `03-script` | script-writing |
| 5 | `film-director` | Decupagem, câmera, luz, continuidade | `04-direction` | shot-direction |
| 6 | `art-director` | Identidade visual, personagens, cenários | `05-art-bible` | visual-identity-consistency |
| 7 | `prompt-engineer` | Prompts de imagem e vídeo por plano/ferramenta | `06-prompts` | media-prompt-engineering |
| 8 | `audio-producer` | Locução, voz, SFX, trilha, direitos | `07-audio-plan` | audio-production-planning |
| 9 | `video-editor` | Montagem, ritmo, legendas, exportação | `08-edit-plan` | edit-planning |
| 10 | `quality-reviewer` | Revisão independente e veredito | `09-qa-report` | quality-review |
| 11 | `growth-analyst` | Análise de métricas reais e otimização | `10-performance` | performance-analysis |

## Fronteiras (anti-sobreposição)
| Tema | Quem decide | Quem NÃO decide |
|---|---|---|
| Estratégia, gancho, CTA | viral-strategist | scriptwriter (executa), film-director |
| Texto falado e em tela | scriptwriter | film-director, video-editor |
| Plano, câmera, luz | film-director | art-director, prompt-engineer |
| Visual global, personagem, cenário | art-director | film-director |
| Texto do prompt de ferramenta | prompt-engineer | film-director, art-director |
| Som | audio-producer | video-editor (apenas posiciona) |
| Montagem e exportação | video-editor | film-director |
| Aprovação | quality-reviewer | quem produziu |
| Medição | growth-analyst | viral-strategist (propõe hipóteses) |

## Pontos de atenção
- **Quality Reviewer não escreve** entregáveis alheios; só avalia.
- **Prompt Engineer depende de `knowledge/`**: enquanto as ferramentas não estiverem documentadas, só produz prompts genéricos rotulados.
- **Growth Analyst sem dados reais** não analisa; só planeja a medição.
- **Tools por agente** seguem o menor privilégio; só `trend-hunter` tem acesso à web e só o ECD tem `Agent` e `Bash`.
