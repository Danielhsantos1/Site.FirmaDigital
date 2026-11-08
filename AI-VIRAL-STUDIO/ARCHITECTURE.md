# Arquitetura

## Princípios
1. **Estrela com um orquestrador.** O ECD é o único que delega e fala com o usuário.
2. **Arquivos como contrato.** Agentes se comunicam por arquivos com template fixo em `projects/<slug>/`, não por conversa solta. Isso permite validação, revisão e retomada.
3. **Conhecimento separado de processo.** Skills dizem *como trabalhar*; `knowledge/` guarda *o que se sabe*, sempre com fonte e data. Hoje o conhecimento está vazio de propósito.
4. **Integrações desacopladas.** Agentes geram especificações; adaptadores futuros as executam (`integrations/adapter-contract.md`).
5. **Sem invenção e sem simulação** (`.claude/rules/no-fabrication.md`).

## Camadas
| Camada | Local | Função |
|---|---|---|
| Regras | `.claude/rules/` | Conduta, protocolo, formato |
| Agentes | `.claude/agents/` | Papéis, entradas/saídas, limites |
| Skills | `.claude/skills/` | Procedimentos reutilizáveis por papel |
| Conhecimento | `knowledge/` | Referência pesquisada e datada |
| Contratos | `templates/` | Formato dos entregáveis |
| Fluxos | `workflows/` | Ordem, dependências e gates |
| Integrações | `integrations/` | Documentação de ferramentas externas |
| Dados de trabalho | `projects/`, `output/`, `packages/` | Instâncias e saídas |
| Verificação | `scripts/validate.py` | Consistência estrutural |

## Fluxo de dados
```
usuário → ECD → 00-brief
ECD → Trend Hunter → 01 → Viral Strategist → 02 → Scriptwriter → 03
03 → Film Director → 04 → Art Director → 05
04+05 → Prompt Engineer → 06        03+04 → Audio Producer → 07
02+03+04+07 → Video Editor → 08
tudo → Quality Reviewer (gates) → 09        métricas reais → Growth Analyst → 10 → ECD
```

## Decisões e trade-offs
- **Subagentes não geram subagentes.** Para o ECD delegar, ele precisa rodar como agente principal (`claude --agent ...`), não como subagente de outro. Por isso `CLAUDE.md` e o README instruem esse modo. A restrição `Agent(...)` na lista de ferramentas do ECD limita quem ele pode acionar. **Confirmado em teste real (Missão 02):** o ECD como agente principal delegou aos 10 especialistas; como subagente, não recebe `Agent`. Skills chegam aos agentes pelo campo `skills:` do frontmatter (especialistas) e pela ferramenta `Skill` (ECD); sem isso o vínculo era só documental.
- **Pasta autocontida.** `.claude/` e `CLAUDE.md` só carregam quando o Claude Code é aberto nesta pasta. Dentro do repositório do site, abrir na raiz do repositório **não** os carrega.
- **Sem código de aplicação.** Só `scripts/validate.py`, sem dependências.
- **Sem interface web** nesta fase, por decisão do usuário.
