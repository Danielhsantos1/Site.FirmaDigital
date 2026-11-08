# Protocolo de comunicação ECD ↔ especialistas

1. **Topologia em estrela.** Só o `executive-creative-director` delega. Especialistas não chamam nem citam instruções para outros especialistas; se precisam de algo, pedem ao ECD.
2. **Delegação.** O ECD entrega a cada especialista: slug do projeto, caminho do brief, caminhos das entradas necessárias, entregável esperado (template) e critérios de aceite.
3. **Retorno.** Todo especialista termina com um bloco `## Relatório ao Diretor` contendo:
   - `agente`: nome do agente
   - `tarefa recebida`: resumo do que o ECD pediu
   - `arquivos consultados`: caminhos lidos de fato
   - `trabalho realizado`: o que foi feito
   - `skills aplicadas`: skill e passos usados
   - `status`: `DONE` | `NEEDS_INFO` | `BLOCKED`
   - `entregáveis`: caminhos dos arquivos criados (ou "nenhum")
   - `premissas`: o que foi assumido
   - `pendências`: perguntas abertas e itens `[A PESQUISAR]`
   - `autoavaliação`: cada critério de qualidade do agente como ✔ / ✘ com uma linha de justificativa
4. **Ambiguidade.** Se o brief for insuficiente, retornar `NEEDS_INFO` com perguntas objetivas. Não preencher lacunas por suposição silenciosa.
5. **Escopo.** Trabalho fora das responsabilidades do agente é devolvido ao ECD, não executado.
6. **Revisão.** O ECD aciona o `quality-reviewer` nos gates definidos em `WORKFLOWS.md`. Reprovação volta ao agente de origem via ECD, com no máximo 2 ciclos antes de escalar ao usuário.
7. **Usuário.** Apenas o ECD fala com o usuário.
