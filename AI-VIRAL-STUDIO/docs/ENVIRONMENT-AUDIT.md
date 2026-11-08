# Auditoria do ambiente: Claude Code

Data: 2026-11-08 · Escopo: o **contêiner da sessão em nuvem**. Nada foi desinstalado ou alterado.

## Fatos medidos
| Item | Valor |
|---|---|
| Comando `claude` no PATH | `/opt/node22/bin/claude`, que é um link simbólico para `/opt/claude-code/bin/claude` |
| Versão executada | **2.1.319** |
| Pacote npm global `@anthropic-ai/claude-code` | **2.1.42**, em `/opt/node22/lib/node_modules/@anthropic-ai/claude-code`, binário `cli.js` |
| Processo da sessão atual (PID 88) | `/opt/node22/bin/claude`, ou seja, a **2.1.319** |
| Outras instalações encontradas | nenhuma (`which -a claude` retorna uma só entrada) |

## Diagnóstico
A diferença de versão tem uma causa: o link `claude` no PATH foi apontado para a build em `/opt/claude-code` (2.1.319), enquanto o pacote do npm ficou **órfão**, instalado mas nunca executado pelo PATH. Não há conflito ativo: a sessão e todos os testes usaram a 2.1.319. O processo de upgrade do ambiente (`--upgrade-claude-code`) parece manter essa build; isso é inferência, não verificado.
**Este achado é do contêiner.** Não sei o que existe na sua máquina local.

## Como corrigir (não executado)
No contêiner: nada a fazer; o pacote npm órfão é inofensivo.
Na sua máquina, para checar duplicidade:
```bash
which -a claude          # quantas entradas?
claude --version
npm ls -g @anthropic-ai/claude-code
claude doctor            # se disponível na sua versão
```
Se houver duas, mantenha a que `claude doctor` indicar como a oficial/atualizável e remova a outra, por exemplo `npm uninstall -g @anthropic-ai/claude-code` se você usa o instalador nativo. **Só com autorização e depois de conferir o resultado do `which -a`.**

## Carregamento do projeto (testado de verdade)
| Teste | Resultado |
|---|---|
| Iniciar dentro de `AI-VIRAL-STUDIO/` | 11 agentes e 12 skills do estúdio carregados |
| `CLAUDE.md` e `.claude/rules/` | carregados (citados corretamente sem ler arquivos) |
| Iniciar na raiz do repositório do site | **0** agentes e **0** skills do estúdio |
| Agente principal com `--agent executive-creative-director` | funciona; delega via `Agent` (ver `tests/orchestration/PLAN.md`) |

Conclusão: o estúdio só funciona com o Claude Code aberto **dentro** da pasta. Isso reforça migrar para repositório próprio.
