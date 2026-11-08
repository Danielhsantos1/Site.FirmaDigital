# AI VIRAL STUDIO

Produtora audiovisual baseada em IA, operada por Claude Code: 11 agentes especializados, Skills, workflows e uma base de conhecimento, com integrações externas planejadas para o futuro.

> **Estado atual: Missão 01 — fundação.** Existem a estrutura, as especificações dos agentes, as Skills iniciais e a documentação. **Não existem** integrações funcionais, vídeos gerados, base de conhecimento preenchida nem interface web.

## Começando
```bash
cd AI-VIRAL-STUDIO
claude --agent executive-creative-director   # ECD como agente principal (ver ressalva abaixo)
python3 scripts/validate.py                  # valida a estrutura
```
Ressalva: delegação do ECD aos especialistas depende de recurso do Claude Code ainda **não testado nesta fundação** (ver `IMPLEMENTATION-ROADMAP.md`, item R1). Alternativa: abrir `claude` normalmente nesta pasta e pedir ao Claude que atue como ECD conforme `.claude/agents/executive-creative-director.md`.

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

## Requisitos
Claude Code, Git e Python 3 (somente biblioteca padrão). Node.js não é necessário nesta fase.

## Local deste projeto
Esta pasta está dentro do repositório do site da Firma Digital apenas por conveniência da sessão. É autocontida e pode ser movida para um repositório próprio sem alterações.
