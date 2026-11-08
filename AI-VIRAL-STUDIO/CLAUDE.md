# AI VIRAL STUDIO

Produtora audiovisual operada por IA, conduzida via Claude Code. Este arquivo é lido em toda sessão aberta **a partir desta pasta**.

## Como operar
- Abra o Claude Code dentro de `AI-VIRAL-STUDIO/` (ou rode `claude --agent executive-creative-director`) para que `.claude/` e este arquivo sejam carregados.
- O **Executive Creative Director (ECD)** é o único orquestrador. Ele delega aos outros 10 agentes, valida entregas e fala com o usuário.
- Especialistas **nunca** falam entre si. Toda comunicação passa pelo ECD (ver `.claude/rules/communication-protocol.md`).

## Os 11 agentes (lista oficial, fechada)
executive-creative-director · trend-hunter · viral-strategist · scriptwriter · film-director · art-director · prompt-engineer · audio-producer · video-editor · quality-reviewer · growth-analyst

Não criar, remover nem renomear agentes sem aprovação explícita do usuário. Detalhes em `AGENTS.md`.

## Mapa
| Pasta | Conteúdo |
|---|---|
| `.claude/agents/` | Especificação dos 11 agentes |
| `.claude/skills/` | Skills (SKILL.md) reutilizáveis |
| `.claude/rules/` | Regras globais de conduta e formato |
| `knowledge/` | Base de conhecimento (hoje só índices; conteúdo a pesquisar) |
| `templates/` | Formato dos entregáveis de cada etapa |
| `workflows/` | Pipelines (rascunhos) |
| `integrations/` | Requisitos e limitações de ferramentas externas (documentação, sem código) |
| `projects/<slug>/` | Um diretório por campanha/vídeo |
| `output/`, `packages/` | Saídas e pacotes gerados (ignorados pelo git) |
| `scripts/validate.py` | Validador estrutural (somente biblioteca padrão) |

## Regras inegociáveis
1. **Sem invenção.** Fato técnico (sintaxe de prompt, limite de ferramenta, preço, métrica) sem fonte registrada vira `[A PESQUISAR]`, nunca é afirmado.
2. **Sem simulação.** Nenhuma integração fingida, nenhum vídeo/imagem/áudio fictício, nenhuma métrica inventada.
3. **Sem APIs pagas** configuradas ou chamadas sem aprovação explícita.
4. **Sem segredos no repositório.** Chaves só em variáveis de ambiente.
5. Entregáveis seguem `templates/` e são salvos em `projects/<slug>/`.
6. Idioma: documentação e entregáveis em português do Brasil; prompts finais para ferramentas de geração em inglês, salvo orientação contrária da ferramenta.

## Validação
`python3 scripts/validate.py` antes de cada commit.
