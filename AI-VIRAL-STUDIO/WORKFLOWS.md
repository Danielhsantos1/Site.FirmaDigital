# Workflows

Status: **um rascunho** (`workflows/viral-short-video.md`), não validado em projeto real.

## Pipeline principal
Brief → Tendências → Estratégia → Roteiro → Direção → Art bible → (Prompts ‖ Áudio) → Edição → QA final → (pós-publicação) Desempenho.

## Gates de qualidade
O ECD aciona o `quality-reviewer` após: estratégia, roteiro, direção, art bible, prompts, áudio e edição, e uma vez ao final. Reprovação volta ao autor via ECD; máximo 2 ciclos antes de escalar ao usuário. Gates intermediários podem ser relaxados pelo usuário para ganhar velocidade (trade-off: custo de retrabalho tardio).

## Regras de execução
- Etapa só inicia com entradas aprovadas.
- Paralelismo apenas entre etapas sem dependência mútua (6 e 7); ainda a validar.
- Estados de retorno: `DONE`, `NEEDS_INFO`, `BLOCKED`.
- Nenhuma etapa gera mídia ou chama API; produzem especificações.

## Variantes planejadas (não criadas)
Demo de software · Anúncio comercial · Storytelling · Sequência de posts · Somente prompts por cena · Somente storyboard. Devem nascer como variações do pipeline principal depois de validá-lo, para evitar duplicação.
