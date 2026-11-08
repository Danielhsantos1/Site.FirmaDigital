# Plano de teste de orquestração

**Pergunta:** o ECD, rodando como agente principal, consegue delegar aos 10 especialistas e receber o retorno, sem simulação?

## Níveis
| Nível | O que prova | Custo | Status |
|---|---|---|---|
| 1. Ping de delegação (`run.sh`) | Delegação real ECD → 10 agentes e retorno | Tokens do Claude Code, baixo; teto `BUDGET_USD` | **Executado em 2026-11-08, aprovado** (ver abaixo) |
| 2. Controle negativo (`run.sh --control`) | O ECD como subagente não recebe `Agent` | Baixo | **Executado, confirmado** |
| 3. Carregamento de skills | Agente recebe o corpo da própria skill | Baixo | **Executado**, ver abaixo |
| 4. Pipeline curto real (00→03) no projeto `forma-digital` | Templates e handoff reais, gates de QA | Médio | **Não executado; depende de aprovação do brief** |
| 5. Pipeline completo 00→09 sem mídia | Fluxo inteiro | Médio/alto | Não executado |

## Resultados do nível 1 (evidência)
- 10 chamadas `Agent`, todas da thread principal (`parent_tool_use_id` nulo), uma para cada especialista; 0 chamadas aninhadas.
- Retornos coletados e consolidados pelo ECD; 9 de 10 incluíram o bloco `Relatório ao Diretor` (o `viral-strategist` respondeu só a linha pedida). Em produção isso seria devolução por incompletude.
- Custo medido da execução: cerca de US$ 0,32.

## Controle negativo
O ECD invocado como subagente relatou `BLOCKED`: "a ferramenta Agent não existe no meu conjunto de ferramentas". Não simulou a delegação. **Limitação confirmada:** subagentes não delegam; o ECD precisa ser a sessão principal (`claude --agent executive-creative-director`).

## Carregamento de skills (achado e correção)
- **Antes:** o `scriptwriter` respondeu `NAO CARREGADO` para o conteúdo da própria skill, e a thread principal do ECD não tinha a ferramenta `Skill`. O vínculo agente→skill era só documental.
- **Correção mínima:** campo `skills:` no frontmatter dos 11 agentes; `Skill` adicionada às ferramentas do ECD.
- **Depois:** o `scriptwriter` citou corretamente o passo 3 da `script-writing`; o ECD invocou `project-intake` pela ferramenta `Skill` e citou o passo 1, ambos conferem com os arquivos.

## Limites do que foi provado
- Provado: delegação, retorno, carregamento de skills em 2 agentes (scriptwriter e ECD).
- **Não provado:** skills dos outros 9 agentes carregam (mesmo mecanismo, mas só 1 especialista foi testado); escrita de entregáveis em `projects/`; gates de QA; retrabalho; acesso à web do `trend-hunter`; paralelismo; `Glob`/`Grep` (a thread principal do ECD expôs só `Task, Read, Write, Edit, Bash, Skill`, ou seja, não expôs `Glob`/`Grep` nesta versão).
