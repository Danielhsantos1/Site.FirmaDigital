#!/usr/bin/env bash
# Teste de orquestração (ping): o ECD, como agente principal, delega aos 10 especialistas.
# Não lê/escreve arquivos de projeto, não usa web, não gera mídia. Consome tokens do Claude Code (teto abaixo).
# Uso: bash tests/orchestration/run.sh [--control]
#   --control  também roda o controle negativo (ECD como subagente deve falhar em delegar).
# Requer: claude, jq. Variável opcional: BUDGET_USD (padrão 1.5).
set -u
cd "$(dirname "$0")/../.." || exit 2
command -v claude >/dev/null && command -v jq >/dev/null || { echo "requer claude e jq"; exit 2; }
BUDGET="${BUDGET_USD:-1.5}"; OUT="$(mktemp -d)"; FAIL=0
EXPECTED="art-director audio-producer film-director growth-analyst prompt-engineer quality-reviewer scriptwriter trend-hunter video-editor viral-strategist"

claude -p "TESTE DE ORQUESTRAÇÃO (ping, sem produção). Delegue, usando a ferramenta Agent, uma tarefa a CADA um dos 10 especialistas (trend-hunter, viral-strategist, scriptwriter, film-director, art-director, prompt-engineer, audio-producer, video-editor, quality-reviewer, growth-analyst). Instrução a cada um: 'Teste de ping. Não leia nem escreva arquivos, não use web. Responda em uma única linha: seu nome de agente e a primeira Saída obrigatória da sua especificação.' Colete as 10 respostas e apresente uma tabela agente | resposta. Não faça mais nada." \
  --agent executive-creative-director --output-format stream-json --verbose \
  --max-budget-usd "$BUDGET" < /dev/null > "$OUT/main.jsonl" 2> "$OUT/main.err"

EV="$(python3 -I tests/orchestration/evidence.py "$OUT/main.jsonl" "teste de orquestração")"
GOT=$(jq -r 'select(.type=="system" and .subtype=="task_started" and .spawn_depth==1) | .subagent_type' "$OUT/main.jsonl" | sort | tr '\n' ' ' | sed 's/ $//')
DONEN=$(jq -r 'select(.type=="system" and .subtype=="task_notification" and .status=="completed") | .task_id' "$OUT/main.jsonl" | wc -l)
NESTED=$(echo "$EV" | grep -c 'sim (' )
STATUS=$(jq -r 'select(.type=="result") | .subtype' "$OUT/main.jsonl" | tail -1)
COST=$(jq -r 'select(.type=="result") | .total_cost_usd' "$OUT/main.jsonl" | tail -1)

[ "$GOT" = "$EXPECTED" ] && echo "PASS delegou exatamente aos 10 especialistas pela thread principal" || { echo "FAIL delegações: [$GOT]"; FAIL=1; }
[ "$DONEN" -eq 10 ] && echo "PASS 10 retornos (task_notification) com status completed" || { echo "FAIL retornos completos: $DONEN"; FAIL=1; }
[ "$NESTED" -eq 0 ] && echo "PASS nenhum subagente tentou delegar (transcrições inspecionadas)" || { echo "FAIL subagentes chamaram Agent: $NESTED"; FAIL=1; }
[ "$STATUS" = "success" ] && echo "PASS execução terminou com sucesso (custo US\$ $COST)" || { echo "FAIL resultado: $STATUS"; FAIL=1; }

if [ "${1:-}" = "--control" ]; then
  R=$(claude -p "Use a ferramenta Agent com subagent_type=executive-creative-director e peça: 'Tente delegar via Agent um ping ao trend-hunter e relate exatamente se conseguiu. Não simule.' Relate a resposta literal." --max-budget-usd 0.6 < /dev/null 2>/dev/null)
  echo "$R" | grep -qiE "BLOCKED|não consegui|nao consegui" && echo "PASS controle: ECD como subagente não delega (comportamento esperado)" || { echo "FAIL controle inesperado"; FAIL=1; }
fi
echo "$EV" > "$OUT/evidencia.md"; echo "logs brutos e evidencia.md: $OUT"; exit $FAIL
