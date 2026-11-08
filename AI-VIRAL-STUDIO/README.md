# AI VIRAL STUDIO

Produtora audiovisual baseada em IA, operada por Claude Code: 11 agentes especializados, Skills, workflows e uma base de conhecimento, com integrações externas planejadas para o futuro.

> **Estado atual: Missão 02 — preparação e piloto.** Existem a estrutura, os 11 agentes, as 12 Skills, a documentação, o teste de orquestração e o brief preliminar do primeiro cliente (`projects/forma-digital/`). **Não existem** integrações funcionais, vídeos gerados, base de conhecimento preenchida nem interface web.

## Começando
```bash
cd AI-VIRAL-STUDIO
claude --agent executive-creative-director   # ECD como agente principal (ver ressalva abaixo)
python3 scripts/validate.py                  # valida a estrutura
```
O ECD **só delega se for a sessão principal** (`--agent`); como subagente ele não recebe a ferramenta `Agent`. Verificado em teste real: `bash tests/orchestration/run.sh --control` (ver `tests/orchestration/PLAN.md`). Abrir o Claude Code fora desta pasta não carrega nada do estúdio (`docs/ENVIRONMENT-AUDIT.md`).

## Documentação
| Arquivo | Assunto |
|---|---|
| `CLAUDE.md` | Instruções carregadas pelo Claude Code |
| `ARCHITECTURE.md` | Visão geral, camadas e decisões |
| `AGENTS.md` | Os 11 agentes e suas fronteiras |
| `SKILLS.md` | Skills e pendências de conhecimento |
| `WORKFLOWS.md` | Pipelines e gates de qualidade |
| `INTEGRATIONS.md` | Ferramentas externas: requisitos e limitações |
| `IMPLEMENTATION-ROADMAP.md` | Próximas fases, riscos e pendências |
| `docs/` | Auditoria do ambiente e plano de migração |
| `tests/orchestration/` | Plano e script do teste de orquestração |

## Requisitos
Claude Code, Git e Python 3 (somente biblioteca padrão). Node.js não é necessário nesta fase.

## Local deste projeto
Esta pasta está dentro do repositório do site da Firma Digital apenas por conveniência da sessão. É autocontida e pode ser movida para um repositório próprio sem alterações.
