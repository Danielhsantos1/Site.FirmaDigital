---
projeto: forma-digital
versão: 0.1
autor-agente: quality-reviewer
data: 2026-11-08
entradas-usadas: [_sources/site-extract.md, 00-client-audit.md, 00-brief.md, 00-brief.v2.md, 00-inconsistencies-report.md, 01-trends.md, 02-strategy.md, 03-script.md, 04-direction.md, 05-art-bible.md, 06-prompts.md, 07-audio-plan.md, 08-edit-plan.md, 10-performance.md, STATUS.md, _qa-test/03-script.SEEDED-DEFECTS.md, templates/qa-report.md, templates/brief.md, templates/trend-report.md, templates/viral-strategy.md, templates/script.md, templates/direction.md, templates/art-bible.md, templates/prompt-sheet.md, templates/audio-plan.md, templates/edit-plan.md, templates/performance-report.md, scripts/validate.py (só busca textual)]
status: em revisão   # gate de qualidade executado; correções voltam ao agente dono somente via ECD
---

# Relatório de qualidade

## Revisão 1 · 2026-11-08 · gate de qualidade dos rascunhos do piloto forma-digital (12 itens)

### Escopo e método
- Escopo: os 11 arquivos de `projects/forma-digital/` pedidos pelo ECD mais o roteiro de teste `_qa-test/03-script.SEEDED-DEFECTS.md` (não é entregável; revisado como qualquer outro, sem presumir o que foi plantado).
- Fonte de fatos do cliente: somente `_sources/site-extract.md`. Fato do cliente fora do extrato é tratado como achado.
- Método: leitura integral; conferência de citações e números de linha do extrato; **contagem manual de palavras de todas as falas** (hipótese de ritmo do próprio roteiro: 2,5 palavras/s = 0,4 s por palavra, sem fonte, sem pausas); conferência aritmética de somas de duração; busca textual para confirmar ausências (ex.: "carrossel").
- Critério de veredito (definido por este revisor): **REPROVADO** = pelo menos 1 achado bloqueante. **APROVADO COM RESSALVAS** = sem bloqueante; há achado importante e/ou pendência interna do arquivo que impede uso sem nova versão. **APROVADO** = sem bloqueante, sem importante e sem pendência impeditiva. Nenhum arquivo atingiu APROVADO, pois todos dependem de D1 a D6 e de itens `[A PESQUISAR]`.
- Veredito de QA **não** substitui D1 a D6 e **não** promove nenhum arquivo: o `status` de cada um segue `rascunho` até decisão do ECD.
- Severidades: **bloqueante** = impede avanço ou viola regra inegociável; **importante** = corrigir na próxima versão, afeta qualidade, consistência ou risco; **menor** = ajuste de forma ou rastreio.

### Leituras (de fato) e não leituras
- **Lidos com a ferramenta de leitura:** `_sources/site-extract.md`; `00-client-audit.md`; `00-brief.md` (v1); `00-brief.v2.md`; `00-inconsistencies-report.md`; `01-trends.md`; `02-strategy.md`; `03-script.md`; `04-direction.md`; `05-art-bible.md`; `06-prompts.md` (integral, em 2 páginas); `07-audio-plan.md`; `08-edit-plan.md` (integral, em 2 páginas); `10-performance.md`; `STATUS.md`; `_qa-test/03-script.SEEDED-DEFECTS.md`; templates `qa-report`, `brief`, `trend-report`, `viral-strategy`, `script`, `direction`, `art-bible`, `prompt-sheet`, `audio-plan`, `edit-plan`, `performance-report`.
- **Recebidos no contexto da sessão, não reabertos como arquivo:** `CLAUDE.md` e as 5 regras de `.claude/rules/` (existência confirmada por Glob).
- **Verificados só por busca textual (não lidos):** `scripts/validate.py` (linhas que tratam de Rastreabilidade e cabeçalho); marcadores "VAZIO"/"NÃO PESQUISADO" em `knowledge/*/README.md` e `integrations/*.md` (16 ocorrências em 16 arquivos).
- **Não lidos:** `templates/project-status.md`, `templates/README.md`, `_execution/*` (prompt-run1-3, evidence-run1-2), `AGENTS.md`, `WORKFLOWS.md`, `workflows/`, demais `.claude/skills/*`.
- **Não executado:** `python3 scripts/validate.py` (este agente não tem shell).

## Veredito

### Tabela de vereditos
| # | Arquivo | Dono | Veredito | Bloq. | Imp. | Men. |
|---|---|---|---|---|---|---|
| 1 | 00-brief.v2.md | executive-creative-director | APROVADO COM RESSALVAS | 0 | 2 | 1 |
| 2 | 00-inconsistencies-report.md | executive-creative-director | APROVADO COM RESSALVAS | 0 | 1 | 2 |
| 3 | 01-trends.md | trend-hunter | APROVADO COM RESSALVAS | 0 | 1 | 3 |
| 4 | 02-strategy.md | viral-strategist | APROVADO COM RESSALVAS | 0 | 1 | 3 |
| 5 | 03-script.md | scriptwriter | **REPROVADO** | 1 | 6 | 2 |
| 6 | 04-direction.md | film-director | APROVADO COM RESSALVAS | 0 | 2 | 5 |
| 7 | 05-art-bible.md | art-director | APROVADO COM RESSALVAS | 0 | 0 | 1 |
| 8 | 06-prompts.md | prompt-engineer | APROVADO COM RESSALVAS | 0 | 0 | 3 |
| 9 | 07-audio-plan.md | audio-producer | APROVADO COM RESSALVAS | 0 | 0 | 1 |
| 10 | 08-edit-plan.md | video-editor | APROVADO COM RESSALVAS | 0 | 0 | 2 |
| 11 | 10-performance.md | growth-analyst | APROVADO COM RESSALVAS | 0 | 0 | 2 |
| 12 | _qa-test/03-script.SEEDED-DEFECTS.md (teste, não entregável) | harness | **REPROVADO** | 9 | 5 | 1 |
| transversal | GL-01 (regra × template) | executive-creative-director | n/a | 0 | 0 | 1 |

Totais nos 11 entregáveis reais: **1 bloqueante, 13 importantes, 26 menores** (o menor transversal GL-01 está incluído). No arquivo de teste: 9 bloqueantes, 5 importantes, 1 menor.

Justificativas curtas:
- **03 REPROVADO** por RO-01 (falas não cabem nas cenas pela hipótese do próprio roteiro; o roteiro afirma compatibilidade). Todo o resto do roteiro está dentro das proibições do projeto (nenhum SaaS, "03 sistemas", cliente, tela real, avatar, voz sintética, preço, depoimento ou "nós" em fala ou tela, conferido por leitura e busca).
- **04, 06, 07, 08, 10** não têm bloqueante próprio; o veredito vale para o conteúdo atual e **deve ser reconfirmado** quando o roteiro v2 mudar falas, durações ou CTA (04, 07 e 08 consomem a duração e o texto do 03; 06 consome a decupagem).
- **01** aprovado só quanto a honestidade, rastro e aderência ao template; **a verdade das fontes externas não foi verificada** (sem acesso web).

## Achados

### Bloqueantes

**RO-01 · bloqueante · 03-script.md · dono: scriptwriter** · Fala × duração da cena
- Trecho: linha 21 ("fala em cerca de 2,5 palavras por segundo"); cenas com duração estimada nas linhas 52 a 163; linha 213 (premissa: "durações calculadas com 2,5 palavras/s"); linha 217 (autoavaliação ✔ "Duração compatível").
- Regra/critério: coerência roteiro × duração; verificação de consistência entre durações (skill quality-review, passo 3). O roteiro adota a hipótese 2,5 pal/s e depois viola a própria hipótese.
- A conta (contagem manual; 0,4 s por palavra; **sem pausas**, logo o excesso real é maior). Verifiquei também as 5 contagens do 07 e todas as 17 do 08: coincidem.

| Cena | Palavras D / I | Fala D / I (×0,4 s) | Cena | Folga D / I |
|---|---|---|---|---|
| P1-C1 | 3 / 3 | 1,2 / 1,2 | 3,0 | +1,8 / +1,8 |
| P1-C2 | 12 / 12 | 4,8 / 4,8 | 5,0 | +0,2 / +0,2 (3 frases = 2 pausas) |
| P1-C3 | 12 / 12 | 4,8 / 4,8 | 6,0 | +1,2 / +1,2 |
| P1-C4 | 11 / 13 | 4,4 / 5,2 | 6,0 | +1,6 / +0,8 |
| P1-C5 | 13 / 14 | 5,2 / 5,6 | 6,0 | +0,8 / +0,4 |
| P2-C1 | 7 / 7 | 2,8 / 2,8 | 3,0 | +0,2 / +0,2 (2 frases) |
| P2-C2 | 13 / 16 | 5,2 / 6,4 | 6,0 | +0,8 / **−0,4** |
| P2-C3 | 16 / 17 | 6,4 / 6,8 | 6,0 | **−0,4 / −0,8** |
| P2-C4 | 11 / 11 | 4,4 / 4,4 | 6,0 | +1,6 / +1,6 |
| P2-C5 | 12 / 12 | 4,8 / 4,8 | 6,0 | +1,2 / +1,2 |
| P3-C1 | 6 / 6 | 2,4 / 2,4 | 3,0 | +0,6 / +0,6 |
| P3-C2 | 9 / 9 | 3,6 / 3,6 | 6,0 | +2,4 / +2,4 |
| P3-C3 | 9 / 6 | 3,6 / 2,4 | 6,0 | +2,4 / +3,6 |
| P3-C4 | 13 / 13 | 5,2 / 5,2 | 6,0 | +0,8 / +0,8 |
| P3-C5 | 14 / 13 | 5,6 / 5,2 | 5,0 | **−0,6 / −0,2** |
| CTA contatos | 29 / 27 | 11,6 / 10,8 | 10,0 | **−1,6 / −0,8** |
| CTA reconhecimento | 16 / 16 | 6,4 / 6,4 | 6,0 | **−0,4 / −0,4** |

  Exemplo de contagem (CTA contatos, D2=Daniel): "Quer conversar sobre o seu site?" (6) + "Chame no WhatsApp, mande um e-mail ou use o formulário Solicitar orçamento." (12) + "A primeira conversa é para entender seu objetivo, não para vender." (11) = 29 palavras × 0,4 = 11,6 s contra ~10 s.
  Variações de gancho (linhas 42 a 44), cena de ~3 s: P1 "Quantos 'ajustezinhos' cabem em um projeto?" 6 pal = 2,4 s (cabe); P3 "Quantas abas tem a planilha do seu processo?" 8 pal = 3,2 s (−0,2 s); **P2 "O que acontece entre pedir um site e ele ir ao ar?" 12 pal = 4,8 s (−1,8 s)**.
  Resultado: 5 cenas faladas excedem a duração (P2-C2 institucional, P2-C3, P3-C5, CTA contatos, CTA reconhecimento) e 2 têm folga de 0,2 s (P1-C2, P2-C1), que desaparece com uma única pausa.
- Correção pedida: refazer a relação fala × duração (reduzir texto ou rever durações, decisão do scriptwriter via ECD), mostrar a contagem por cena no próprio roteiro, retirar o ✔ "Duração compatível" até a conta fechar, registrar a fonte do ritmo de fala (`[A PESQUISAR]` se não houver) e propagar a mudança a 04, 07 e 08 (nova versão, ver "Ordem de correção").
- Por que bloqueante: 04, 07 e 08 foram construídos sobre essas durações (as somas 36/32, 37/33, 36/32 s fecham aritmeticamente, mas sobre falas que não cabem). O ECD já tem a pendência (STATUS linha 50), porém a autoavaliação do roteiro a contradiz.

**Bloqueantes do arquivo de teste (item 12):** ver SD-01 a SD-08 e SD-11 abaixo.

### Importantes

**B2-01 · 00-brief.v2.md · dono: executive-creative-director** · Template do brief
- Trecho: cabeçalhos "Regra de bloqueio", "Fatos confirmados", "Hipóteses", "NEEDS_INFO", "Restrições", "Critério de sucesso", "Rastreabilidade" (linhas 15 a 64).
- Regra: CLAUDE.md regra 5 (entregáveis seguem `templates/`); `templates/brief.md` exige Objetivo, Público, Plataforma(s), Formato e duração, Tom e voz, Marca e ativos disponíveis, Restrições, Critério de sucesso, **Premissas confirmadas pelo usuário**, Perguntas em aberto. Faltam como seção: Objetivo, Público, Plataforma(s), Formato e duração, Tom e voz, Marca e ativos, **Premissas confirmadas pelo usuário** e Perguntas em aberto (o conteúdo existe, diluído em "Hipóteses" e "NEEDS_INFO").
- Correção: nova versão com os cabeçalhos do template, mantendo a marcação fato/hipótese/NEEDS_INFO dentro de cada seção, e com "Premissas confirmadas pelo usuário: nenhuma" explícito.

**B2-03 · 00-brief.v2.md · dono: ECD** · Mensagem central com forma de promessa absoluta
- Trecho: linha 30 ("Mensagem: 'Escopo definido. Prazo combinado. Sem retrabalho.' (palavras do site; tratar como declaração, não prova)") e linha 31 ("sem hype, superlativos, urgência artificial ou promessa de resultado").
- Regra/critério: promessa sem comprovação; coerência com o tom do próprio brief. O site (linhas 20 e 31 do extrato) usa "sem retrabalho" como texto do próprio negócio, mas a frase imperativa e absoluta lida em peça soa como garantia; nada no projeto define **como** a atribuição ao negócio aparece na peça. A regra de "declaração, não prova" existe só como intenção.
- Correção: definir regra de redação para a mensagem central (forma atribuída ao modelo de trabalho, ou uso restrito a texto interno), registrar a pendência de regras publicitárias `[A PESQUISAR]` já aberta e alinhar 02 (ES-01).

**IR-01 · 00-inconsistencies-report.md · dono: ECD** · Público classificado como fato
- Trecho: linha 21, ponto 3: "**CONFIRMADO** (A) / **HIPÓTESE** (B, C, D)", base "oferta 'pronto para clientes encontrarem você' e 'negócio local'".
- Regra/critério: handoff-format ("fato sem fonte vai para Hipóteses"); consistência entre arquivos. O extrato não nomeia público: "negócio local" é nome de oferta, e "dono(a)" e "pequeno" não constam. O próprio 00-brief.v2 (linha 29) e o 02 (linhas 22 a 25: "hipótese, não nomeado pelo site") tratam A como hipótese. O `00-client-audit.md` §8 marca A, B e C como ✅, também em desacordo.
- Correção: reclassificar A como HIPÓTESE (base: oferta 01) e alinhar o `00-client-audit.md` na mesma rodada.

**TR-01 · 01-trends.md · dono: trend-hunter** · Tendência sem data de publicação nem leitura da fonte
- Trecho: T1 a T3 (linhas 32 a 49) com "pub.: não verificada"; critério da própria seção (linha 27): "padrão recorrente" só com "2 ou mais fontes independentes e datadas"; T1 marcado "média-baixa" com 2 blogs sem data; T2 com 2 fontes do mesmo autor (linha 42).
- Regra: no-fabrication ("Tendência só entra com fonte e data"). A data de consulta existe; a de publicação não. Esses itens alimentam o 02 (Ang-1 "liga-se a T1", linha 64; princípio de gancho, linha 88) e o 03.
- Correção: rebaixar T1 a T3 a "sinal isolado/hipótese" (nomenclatura do próprio relatório) enquanto não houver data e leitura, e fazer a legenda de confiança obedecer ao critério declarado na linha 27.
- Nota: a honestidade das limitações (linhas 12 a 17) é adequada e foi considerada. Não verifiquei nenhuma URL (ver "Itens não verificados").

**ES-02 · 02-strategy.md · dono: viral-strategist** · Objetivo de reconhecimento inalcançável com as próprias regras
- Trecho: linha 37 ("Se D6 = reconhecimento | Alcance e lembrança do nome"); linha 59 ("'Forma Digital' não é fixado em peça final"); linha 76 ("nenhuma peça final com nome"). O 03 também não põe nome em fala ou tela (linha 16).
- Regra/critério: coerência objetivo × peça; métrica que não mede o objetivo. Sem nome na peça, "lembrança do nome" não é produzível nem mensurável. (O 10-performance, F7, chega à mesma conclusão; a falha está no 02.)
- Correção: redefinir o ramo "reconhecimento" (por exemplo, exposição/alcance sem a promessa de lembrança) ou condicioná-lo à resolução de D1 e ao uso do nome; sem escolher D6.

**RO-02 · 03-script.md · dono: scriptwriter** · Fala × texto em tela
- Trecho: linha 15 ("O texto em tela é neutro e vale para as duas [variantes]"). Divergências encontradas:
  - P1-C2: fala "E o projeto continua aberto." sem equivalente na tela (linhas 61 e 63).
  - P1-C3: fala traz "No meu modelo"/"O modelo de trabalho prevê"; tela "Escopo combinado por escrito, antes de começar." perde a atribuição (linhas 66 a 68).
  - P1-C5: fala "antes de seguir"; tela "4 etapas · aprovação em cada uma" (linhas 78 a 80).
  - P2-C2: fala "prazo e valor"; tela "Tudo registrado por escrito" (linhas 98 a 100).
  - P3-C2: fala "anotados aqui... em outra aba"; tela "Pedido · Status · Prazo" (linhas 137 a 139).
  - CTA contatos: fala institucional "entender **o** objetivo" (linha 171); tela única para as duas variantes "entender **seu** objetivo" (linha 172), contra a própria premissa de tela neutra.
  - CTA reconhecimento: fala longa; tela "Salvar · Compartilhar" (linhas 177 e 178).
- Regra/critério: consistência fala × texto em tela (critério obrigatório); H9 depende de a tela sustentar o sentido sem som. O 07 e o 08 mapearam parte disso e deixaram sem correção, corretamente.
- Correção: reconciliar caso a caso (ou aceitar a perda por escrito, com justificativa) e dar texto de tela próprio à variante institucional do CTA.

**RO-03 · 03-script.md · dono: scriptwriter** · Ganchos e clareza
- Trecho: P2 gancho "Quatro etapas. Uma aprovação em cada uma." (linha 93; peça recomendada na linha 46); P1 "Só um ajustezinho." (linha 56); variação de P2 de 12 palavras (RO-01).
- Regra/critério: gancho fraco; clareza; aderência à estratégia, que manda "entregar logo a situação ou a dor do público" (`02-strategy.md` linha 88). O gancho de P2 não diz de quê são as quatro etapas (a palavra "site" só aparece na cena 2), nem para quem, nem qual dor; o de P1 não tem sujeito nem contexto (quem fala? sobre o quê?) e ocupa 3 s num cartão de texto sobre fundo liso, e a virada ("No meu modelo") só chega em ~8 s. A justificativa da recomendação de P2 ("menos arrisca virar promessa", linha 46) é de risco, não de retenção, e isso não está dito como troca.
- Observação do revisor (hipótese, sem fonte de plataforma): no P1 com CTA de contatos, 13 s de 36 s (3 s do gancho + 10 s de CTA) são cartões só de texto (36%).
- Correção: reescrever os ganchos para identificar o objeto (site) e a situação já no primeiro segundo; ajustar ou justificar a recomendação com critério de retenção explícito; tornar P1 compreensível sem depender da cena 3.

**RO-04 · 03-script.md · dono: scriptwriter** · Aderência ao brief e à estratégia (cobertura)
- Trecho: tabela de propostas, linhas 32 a 36. Brief v2 (linha 34) e 02 (linha 31, Ang-3 na linha 66) priorizam landing page, depois site local, depois sistema/painel; as propostas são P1 (site, dor), P2 (site, processo) e P3 (sistema/painel, prioridade 3). Nenhuma cobre landing page (Ang-3 / G3), e o público A (principal) só é tocado de modo genérico em P1/P2.
- Regra/critério: aderência ao brief/estratégia; o roteiro não registra a omissão.
- Correção: incluir proposta de landing page (Ang-3) ou registrar por escrito por que a prioridade 1 ficou fora (decisão do ECD).

**RO-05 · 03-script.md · dono: scriptwriter** · CTA inadequado como entregável de fala
- Trecho: linhas 170 e 171 ("Chame no WhatsApp, mande um e-mail ou use o formulário Solicitar orçamento"); linha 177 ("envie a quem está pensando em fazer um site"); CTA "comum às três propostas" (linha 167).
- Regra/critério: CTA adequado. (a) O CTA manda agir em canais que o espectador não consegue localizar: sem perfil, sem link, sem site, sem número; o roteiro marca isso como NEEDS_INFO (linha 167, correto), mas ainda assim fixa a fala imperativa. (b) Em P3, cuja oferta é "sistema ou painel", o CTA comum fala em "seu site" (e o de reconhecimento em "fazer um site"): incoerência oferta × CTA. (c) No ramo reconhecimento não há nome nem perfil, então a ação (salvar, enviar) não leva ao negócio.
- Correção: CTA por proposta quando a oferta diferir; marcar o texto de CTA como provisório até D4/D6; nenhuma fala imperativa sem destino definido. Não exijo escolher D4 ou D6.

**RO-06 · 03-script.md (e 04, 06) · dono: scriptwriter** · P3 espelha um caso cuja citação está em aberto
- Trecho: P3 usa "Pedido · Status · Prazo", formulário que registra pedidos e painel de status (03 linhas 129 a 151; 04 linhas 129 a 142). Extrato linhas 63 a 69: caso "Controle de solicitações de serviço", "Rastreio de prazos e status de solicitações de serviço e material", "Uso interno". O 00-inconsistencies-report (I6, D5) e o `00-client-audit.md` (§7.6) tratam a citação desse caso como pendência (contexto profissional possivelmente distinto).
- Regra/critério: restrição do projeto de não expor casos/telas sem autorização; o 03 afirma "genérico e fictício" (linha 129) e a regra 7 do art bible (`05` linha 119) proíbe formas que lembrem os casos do site. A sobreposição temática (solicitação, status, prazo) não é registrada como risco.
- Correção: registrar a sobreposição como risco ligado a D5 e trocar campos/entidades do exemplo por outros que não repliquem o caso, ou aguardar D5. Não estou resolvendo D5.

**RO-07 · 03-script.md · dono: scriptwriter** · Declaração × prova sem mecanismo na peça
- Trecho: só P1-C4 traz a marca "Modelo declarado pelo negócio" (linha 74). As demais afirmações aparecem como fato seco na tela: "Escopo combinado por escrito, antes de começar." (linha 68), "Tudo registrado por escrito" (linha 100), "Código versionado" (linha 112), "Domínio · HTTPS" (linha 118). P2 não atribui o processo a ninguém, nem na fala nem na tela (sem nome por D1).
- Regra/critério: promessas sem comprovação; brief v2 (linha 30) e 02 (linha 13): diferenciais são "declaração do negócio, não prova" (`00-client-audit.md` §6: todos ⚠️ sem evidência).
- Correção: definir uma regra única de atribuição (rótulo ou enquadramento na fala) aplicada a todas as peças, ou documentar que a atribuição será dada pela área de assinatura quando D1 sair.

**DI-01 · 04-direction.md · dono: film-director** · Continuidade do rótulo "ilustrativo"
- Trecho: regra de continuidade (linha 182: rótulo "na mesma posição ... em todos os planos onde o elemento ilustrativo aparece, sem sumir no meio de uma cena"; também `05` linha 107). Tabelas: P2-C2-S1 tem rótulo (linha 93) e P2-C2-S2, com a mesma lista, não (linha 94); P2-C3-S1 sim (linha 99), S2 não (linha 100); P2-C5-S1 sim (linha 111), S2 não (linha 112); P1 só em C1; P3-C1 sem rótulo. A divergência 1 (linha 219) diz "Neste rascunho propus rótulo nesses planos", mas as tabelas não o fazem.
- Regra/critério: continuidade visual; consistência interna.
- Correção: alinhar as tabelas à regra (ou declarar que a regra só vale após E1/ED-4). 06 e 08 já estendem o rótulo como proposta; o 04 é a fonte inconsistente.

**DI-02 · 04-direction.md · dono: film-director** · Alegação de sincronia fala × plano não verificada
- Trecho: linha 260 ("a duração de cada plano foi pensada para a fala do roteiro") e linha 263 ("cada troca de plano deve cair no início da frase"); a "Checagem de continuidade" (linhas 192 a 214) só confere somas de duração, não palavras.
- Regra/critério: inconsistência roteiro × direção (falas × duração). O 08 (linhas 222 a 229) mostra desvios entre −1,4 s e +2,6 s (P1-C2, P1-C4, P1-C5, P2-C2, P3-C4, CTA) e os excessos de RO-01; refiz as contas e confirmo.
- Correção: após o 03 v2, recalcular os planos por cena em função das palavras, ou retirar a alegação e incluir tabela fala × plano.

**SD-09, SD-10, SD-12, SD-13, SD-14** (importantes do arquivo de teste): ver seção do item 12.

### Menores
| ID | Arquivo (dono) | Trecho | Regra violada | Correção pedida |
|---|---|---|---|---|
| GL-01 | 03, 04, 05, 06, 07, 08, 10 (ECD decide a regra) | `## Rastreabilidade` vem antes de `## Relatório ao Diretor` (03 l.198/205; 04 l.280/287; 05 l.260/267; 06 l.493/500; 07 l.276/283; 08 l.484/491; 10 l.270/277) | handoff-format: "termina com a seção ## Rastreabilidade" × templates terminam em Relatório; `validate.py` só exige a seção e os 5 rótulos depois do cabeçalho (l.123 a 125) | ECD decide qual vale (regra ou template) e atualiza o texto; não penalizei os autores. Este relatório segue a ordem dos templates |
| B2-02 | 00-brief.v2 (ECD) | linha 45 remete às "perguntas 7 a 12" do v1; v1 perguntas 5 ("uso interno") e 6 ("experiência em contratos no posicionamento") não constam; v1 linha 7 pedia validação do usuário antes de delegar | consistência com v1; rastro de pendências | Reincluir as perguntas 5 e 6 (D5 cobre só em parte); registrar se houve validação do brief pelo usuário (não verificável por mim) |
| IR-02 | 00-inconsistencies-report (ECD) | linha 39, I6: "origem profissional possivelmente distinta" (também audit §7.6 "provavelmente") | a legenda exige CONFIRMADO/HIPÓTESE/NEEDS_INFO; a tabela (b) não tem coluna de classificação; a conjectura não vem do extrato | Rotular I6 como HIPÓTESE/NEEDS_INFO |
| IR-03 | 00-inconsistencies-report (ECD) | I4 (linha 37) cita "comigo", "Atuo", "Construí"; o extrato linha 82 traz "Definimos juntos" (1ª pessoa do plural), tensão com "sem nós", levantada só pelo 03 (linhas 194, 202) | cobertura da auditoria de inconsistências | Acrescentar a tensão como inconsistência do site |
| TR-02 | 01-trends (trend-hunter) | linhas 59 a 62: 134 mi, 113 mi, 60%, 90 mi, 111 mi, "80% nanocriadores" | no-fabrication (dado de mercado só com fonte); estão marcados "não adotados", mas seguem no entregável | Remover ou manter com marca explícita "não verificado" e sem número |
| TR-03 | 01-trends (trend-hunter) | linhas 75 a 80: duas pessoas nomeadas (Bru Santos, Bruno Roberto) como "referências", sem verificação de relevância; "o que funciona" não preenchido | template ("Referências reais (link, o que funciona)"); dados de terceiros sem finalidade | Manter como "candidatos não verificados" ou retirar os nomes |
| TR-04 / ES-04 | 01-trends, 02-strategy (trend-hunter, viral-strategist) | seção "Relatório ao Diretor" é remissão ("Ver bloco ... na resposta final do agente"; 01 l.111 a 112; 02 l.216 a 217) | template inclui a seção; o conteúdo não está no arquivo | Incluir o bloco no arquivo, como fizeram 03 a 08 e 10 |
| ES-01 | 02-strategy (viral-strategist) | linha 52 adota "Sem retrabalho" como mensagem central; linha 185 proíbe "garantimos" e "sem erros" | coerência interna; ver B2-03 | Alinhar à regra de redação definida pelo ECD |
| ES-03 | 02-strategy (viral-strategist) | linha 186 propõe H1, H3 e H6 como prioridade; H3 exige carrossel, que não existe em 03 a 08 (0 ocorrências de "carrossel"/"Stories" por busca); H6 depende de mecanismo de chegada inexistente | executabilidade do desenho de testes (ver `10-performance.md` F3) | Rever a priorização com base no 10; decisão do ECD |
| RO-08 | 03-script (scriptwriter) | fala vai além do extrato: "antes de seguir" (l.78), "tudo em um só lugar" (l.149), "escopo ... por escrito" (l.66, junta extrato l.44 e l.82) | Rastreabilidade ("fato sem fonte vai para Hipóteses") | Listar em Hipóteses ou ajustar o texto ao extrato |
| RO-09 | 03-script (scriptwriter) | linha 46 apresenta P1 × P2 como par de H1 ("H1 compara G1 e G4"), mas H1 exige o mesmo ângulo (02 l.159) e P1/P2 diferem (Ang-2 × Ang-1, linhas 34 e 35) | consistência com 02 | Corrigir a nota |
| DI-03 | 04-direction (film-director) | linhas 37, 154 e 224: "O roteiro cita 'GitHub' em fala e texto"; o 03 só cita GitHub na fala (linhas 110 e 111); a tela traz "Código versionado · ambiente de teste". A pendência se propaga (05 E10; 06 lacuna 6; 08 ED-9) | consistência 04 × 03 | Corrigir: "GitHub" é só fala |
| DI-04 | 04-direction (film-director) | linha 83 ("etapa corrente em destaque, as anteriores com marca") × P2-C1 termina com 4 nós aprovados (linha 88) e P2-C2 expande o nó 1 (linha 93) | continuidade visual (estado dos nós) | Definir o estado dos nós na passagem C1 para C2 |
| DI-05 | 04, 08 (film-director, video-editor) | 04 l.277 e 08 l.433: checagem "nenhum número" × tela com "4 etapas", "1 ·" a "4 ·"; a exceção está só no 05 (regra 5, l.95) | consistência entre checklists | Copiar a exceção para as duas checagens |
| DI-06 | 04-direction (film-director) | P3-C2-S1 (linha 129): cabeçalhos "Pedido/Status/Prazo" na grade **e** texto em tela "Pedido · Status · Prazo" | regra "um bloco de texto por plano" (linha 184) | Esclarecer se os cabeçalhos são o texto |
| DI-07 | 04-direction (film-director) | P1-C1-S1 (linha 50): cartão de texto sobre fundo liso, sem gráfico, como gancho; ver RO-03 | adequação à plataforma (hipótese de retenção sem fonte) | Registrar o risco ou prever elemento visual no gancho |
| AB-01 | 05-art-bible (art-director) | regra de composição 9 (linha 88: quadro final do CTA "sem elemento além do texto") × E11 (linha 257) e 04 (linhas 79, 115, 169: elemento da peça ao fundo, opcional) | consistência interna | Alinhar a regra 9 à decisão E11 |
| PR-01 | 06-prompts (prompt-engineer) | prompts trazem os tokens de macro `EL-NOS`, `EL-CARTAO`, `EL-FOLHA`, `EL-GRADE`, `EL-VISTO` dentro do "Prompt (EN)" (ex.: linhas 125, 191, 202, 324); "Como usar" (linha 34) só manda colar os BLK | prompt final enviado sem expandir seria ruído para a ferramenta | Instruir a expansão dos EL-* ou expandi-los no texto |
| PR-02 | 06-prompts (prompt-engineer) | linha 53: "Papéis de cada cor = PROPOSTA ... (sem base no site)"; o extrato (linha 7) dá fundo, superfície e texto; só os papéis dos acentos faltam | exatidão da fonte | Restringir a ressalva aos acentos |
| PR-03 | 06-prompts (prompt-engineer) | BLK-QUADRO (linha 57: faixa inferior vazia, margens iguais) × P3-C1-S1 (linha 324: "filling most of the frame") | consistência prompt × bloco comum | Reconciliar |
| AU-01 | 07-audio-plan (audio-producer) | tabelas de sincronia (linhas 79 a 104) ancoram frases a planos (ex.: P1-C2 "E mais outro." em S2) sem checar a posição da frase; pelo 08 a frase começa a 1,6 s e S2 a 2,5 s | coerência 07 × 04/08 | Marcar as âncoras como aproximadas ou rever após o 03 v2 |
| EP-01 | 08-edit-plan (video-editor) | linha 218 diz "sem desvio relevante (≤ 0,2 s): P2-C3"; para a variante institucional são 9 palavras antes de "antes" = 3,6 s contra S2 em 3,0 s (+0,6 s); só a Daniel dá +0,2 s | exatidão da conta (único erro aritmético que achei no 08) | Corrigir a linha |
| EP-02 | 08-edit-plan (video-editor) | Rastreabilidade (linha 485) declara o extrato "linhas 1 a 70"; o extrato tem 110 linhas e a seção de contato (92 a 108) não foi lida, embora o plano trate do CTA | Fontes devem refletir o lido | Corrigir a Fonte (os fatos de CTA vêm via 03) |
| PF-01 | 10-performance (growth-analyst) | linhas 70 e 272 tratam "formulário sem campo de origem" como fato confirmado; o extrato é "texto visível apenas" (linha 4) e a premissa 5 do próprio 10 admite que analytics e campos ocultos são desconhecidos | Rastreabilidade (fato sem fonte vai para Hipóteses) | Qualificar como "no texto visível" ou mover para Hipóteses |
| PF-02 | 10-performance (growth-analyst) | linha 48 (H8): "D3 não autorizado" | consistência com STATUS (linha 43): D3 é NEEDS_INFO, não negada | Escrever "sem resposta" |

### Arquivo de teste (item 12): defeitos que detectei em `_qa-test/03-script.SEEDED-DEFECTS.md`
Veredito: **REPROVADO** (não é entregável; não afeta STATUS). Lista do que encontrei, sem presumir o que foi plantado:

| ID | Sev. | Trecho (linha) | Regra/critério | Correção pedida |
|---|---|---|---|---|
| SD-01 | bloqueante | C2: "Já temos 3 sistemas em produção" (l.17) | Indicador "03 sistemas em produção" proibido (brief v2; I2: só 1 caso "Em produção"); "temos" sugere equipe | Remover |
| SD-02 | bloqueante | C2: "dezenas de clientes satisfeitos" (l.17) | no-fabrication: número de clientes e satisfação inexistentes no extrato | Remover |
| SD-03 | bloqueante | C2: "A Ana, da Padaria Central, disse: 'dobrei minhas vendas em 30 dias...'" (l.17) | Depoimento, cliente nomeado e resultado inventados (no-fabrication; extrato l.77: nomes não divulgados; brief: sem depoimentos) | Remover |
| SD-04 | bloqueante | C3: "Nosso SaaS de contratos já está disponível e analisa tudo com inteligência artificial" (l.18) | SaaS como oferta é proibido e falso (extrato: "Em desenvolvimento"); "tudo" excede "análise automatizada de conflitos entre termo de referência, proposta técnica e proposta comercial" | Remover |
| SD-05 | bloqueante | C3: "Garantimos resultado ou seu dinheiro de volta" (l.18) | Garantia e reembolso inventados; promessa de resultado (tom do brief); "Garantimos" sugere equipe; regras de consumo `[A PESQUISAR]` | Remover |
| SD-06 | bloqueante | C4: imagem "tela real do sistema de treinamentos do cliente Empresa-Exemplo S.A." (l.19) | Tela real e nome de cliente proibidos (extrato l.77; brief v2 restrições); o rótulo "nome fictício de teste" não muda o padrão | Substituir por demo ilustrativa rotulada |
| SD-07 | bloqueante | C5: "Somos a maior agência de sites da região" (l.20) | Superlativo sem comprovação; "agência"/"somos" contradiz negócio de uma pessoa; "região" não definida (só Votorantim consta) | Remover |
| SD-08 | bloqueante | C1: "Olá, somos a Forma Digital, uma empresa de tecnologia." (l.16) | "somos" (equipe); "empresa de tecnologia" não consta (extrato: desenvolvimento web, 1 pessoa); nome em fala antes de D1 (o site diz "Firma Digital"); gancho que abre pela marca contraria 02 l.88 | Remover |
| SD-09 | importante | Título "em 30s" (l.12) × "Reel de 90 segundos" (l.14); as 68 falas somam 68 palavras = 27,2 s a 2,5 pal/s, compatíveis com nenhum dos dois; sem duração por cena | Inconsistência interna de duração; template `script.md` exige duração por cena | Definir uma duração e fechar a conta por cena |
| SD-10 | importante | "Reel de 90 segundos para TikTok" (l.14) | Adequação à plataforma: "Reels" é formato de Instagram (brief v2 l.32 separa Instagram/Reels de TikTok); duração de 90 s sem fonte (`[A PESQUISAR]`) | Corrigir formato e marcar a duração como `[A PESQUISAR]` |
| SD-11 | bloqueante | "(Sem chamada para ação.)" (l.22) | Ausência de CTA; template exige seção CTA; objetivo do brief é gerar conversas | Incluir CTA pelos canais do extrato |
| SD-12 | importante | Arquivo sem logline, estrutura, variações de gancho, intenção, texto em tela, duração por cena, CTA, Rastreabilidade, Relatório; cabeçalho sem entradas | `templates/script.md`; handoff-format | Seguir o template |
| SD-13 | importante | "Já temos 3 sistemas" (l.17) e "dezenas de clientes" na mesma fala; C4 "Veja como controlamos tudo" (l.19), "controlamos"/"tudo" sem referente | Clareza e coerência interna; "controlamos" atribui ao negócio a operação do sistema do cliente | Reescrever com arco problema, solução e prova admissível |
| SD-14 | importante | C1 abre com autoapresentação ("Olá, somos...") em vez de dor ou situação (l.16) | Gancho fraco; 02 manda nunca abrir pelo nome | Reescrever o gancho |
| SD-15 | n/v | Avatar ou voz sintética de Daniel: o arquivo não os menciona nem especifica a voz | Uso proibido: não há como afirmar conformidade nem violação | Especificar a voz ao reescrever |
| SD-16 | menor | Tom de superlativo e hype ("dobrei", "maior", "garantimos") | Tom do brief: sem hype, superlativos, promessa | Neutralizar |

## Avaliação por critério obrigatório (síntese)
| Critério | Resultado nos 11 entregáveis reais |
|---|---|
| Inconsistências comerciais | Falas do 03 conferidas contra o extrato (linhas 31, 44, 53, 79 a 94 citadas corretamente). Achados: RO-04 (prioridade de oferta), RO-05(b) (CTA "site" em P3), RO-06 (P3 × caso em aberto) |
| Promessas sem comprovação | B2-03, ES-01, RO-07, RO-08. O 03 evita preço, prazo numérico, depoimento e resultado |
| Posicionamento | B2-03, RO-07, ES-02 |
| Clareza e ganchos | RO-03, DI-07 |
| Continuidade visual | DI-01, DI-04, AB-01, PR-03 (só em texto: não existe mídia) |
| Roteiro × direção (falas × duração; fala × tela) | RO-01 (bloqueante), RO-02, DI-02, DI-03, AU-01, EP-01. Somas de duração de 04 e 08 conferem (36/32, 37/33, 36/32 s; 29 planos; 29 prompts) |
| CTA | RO-05 |
| Plataforma | Limites, proporção e duração-alvo corretamente `[A PESQUISAR]`; DI-07, ES-03 |
| Não invenção | Nenhuma invenção de cliente, número ou métrica nos reais; RO-08, PF-01, TR-01 e TR-02 são desvios de rastro. Mídia: nenhum arquivo descreve mídia como existente (06 todos "NÃO EXECUTADO") |
| Usos proibidos (SaaS como oferta, "03 sistemas", nomes/telas de clientes, avatar/voz de Daniel) | **Nenhuma ocorrência nos 11 entregáveis** (leitura integral e buscas). Aparecem só como proibição. O arquivo de teste os viola (SD-01, SD-04, SD-06, SD-08) |
| Rastreabilidade e cabeçalhos | Cabeçalho do template presente em todos; os 5 rótulos presentes em todos; GL-01, B2-01, TR-04/ES-04 |

## Tratamento de D1 a D6 (NEEDS_INFO; não resolvidas por este revisor)
| Decisão | Como os arquivos tratam | Avaliação |
|---|---|---|
| D1 nome | `[NOME-D1]`, nenhum nome em fala ou tela, "Forma Digital (provisório)" só em títulos e notas | Correto. O teste (SD-08) viola |
| D2 voz | Variantes Daniel/institucional mantidas em 03, 07, 08 | Correto, com ressalva RO-02 (tela do CTA institucional) |
| D3 imagem/voz por IA | Nenhum avatar, rosto ou voz sintética de Daniel em 04 a 08; 07 com caminhos (a), (b), (c) | Correto. PF-02 corrige a redação em 10 |
| D4 perfis | Publicação bloqueada, sem @, sem "link na bio" | Correto no bloqueio; o CTA falado ainda manda agir sem destino (RO-05) |
| D5 sistemas | Nenhum caso, número ou tela | Correto, exceto a sobreposição de P3 com o caso "Uso interno" (RO-06) |
| D6 objetivo | CTA em dois ramos; 02 em dois ramos | Correto no CTA; ramo reconhecimento sem nome na peça (ES-02) |

## Dono do arquivo para correção (via ECD; no máximo 2 ciclos, communication-protocol item 6)
| Arquivo | Motivo | Agente dono | Achados |
|---|---|---|---|
| 03-script.md | REPROVADO | scriptwriter | RO-01 (bloqueante); RO-02 a RO-07 (importantes); RO-08, RO-09 |
| 04-direction.md | importantes | film-director | DI-01, DI-02 (+ menores DI-03 a DI-07; reconfirmar após 03 v2) |
| 00-brief.v2.md | importantes | executive-creative-director | B2-01, B2-03 |
| 00-inconsistencies-report.md | importante | executive-creative-director | IR-01 (+ IR-02, IR-03) |
| 01-trends.md | importante | trend-hunter | TR-01 (+ TR-02 a TR-04) |
| 02-strategy.md | importante | viral-strategist | ES-02 (+ ES-01, ES-03, ES-04) |
| 05, 06, 07, 08, 10 | só menores | art-director, prompt-engineer, audio-producer, video-editor, growth-analyst | AB-01; PR-01 a PR-03; AU-01; EP-01, EP-02; PF-01, PF-02. 06, 07, 08 devem ser reconfirmados se o 03 v2 mudar falas, durações ou CTA |

Versionamento (handoff-format): a correção sai como `<nome>.v2.md` com `substitui:` e resumo das mudanças; o original não é sobrescrito.

## Observações ao ECD (fora dos achados)
1. **Ordem de correção sugerida:** 03 v2 primeiro (RO-01 a RO-07). Só depois reconformar 04, 07 e 08 (e 06 se a decupagem mudar). Em paralelo e sem dependência do roteiro: B2-01/B2-03, IR-01, TR-01, ES-02.
2. **Decisão ineficiente a apontar:** 04 a 08 e 10 foram produzidos sobre um 03 que não passou pelo gate; o defeito de tempo (RO-01) propaga retrabalho a quatro arquivos. Rodar o QA logo após cada etapa-chave evita isso.
3. **02 × 10:** o 10 (F1, F3, F9) recomenda H1 como único teste controlado e adiar H3 e H6; o 02 propõe H1, H3 e H6. As bases factuais do 10 que conferi se sustentam (0 ocorrências de "carrossel" em 03 a 08; matriz de 36 e 9 exportações em 08 l.351; P1/P2 com ângulos diferentes). Decisão do ECD.
4. **Matriz de versões do 08 (até 36 exportações):** ineficiente enquanto D2 e D6 estiverem abertas (08 ED-7 e 10 F9 já apontam). Alternativa: montar só a timeline mestra e o texto em tela.
5. **Cobertura de estilos:** o pipeline cobre só gráfico/motion; o brief v2 lista mais estilos para o piloto. Está sinalizado em 04 (divergência 14), 05 (E9) e 06 (lacuna 10); decisão do ECD, não é defeito dos agentes.
6. **STATUS.md** (dono: ECD) precisa registrar este gate; hoje diz "09-qa-report.md ... não criado" e "nenhum gate executado".
7. **00-client-audit.md** (fora do escopo de veredito) marca públicos B e C como ✅ (§8), em desacordo com o relatório de inconsistências e o brief v2 (hipótese).

## Itens não verificados
1. **Todas as URLs e afirmações externas do `01-trends.md`** (blogs, TikTok Shop, rotulagem de IA de TikTok e Meta, marketplaces): este agente não tem acesso web; aprovei só a honestidade, o rastro e o template, não a verdade.
2. **`python3 scripts/validate.py`**: não executado (sem shell). O STATUS diz que retornou OK após a correção de rótulo no 03; não confirmei.
3. **Ritmo de 2,5 palavras/s:** hipótese do 03 sem fonte; usei-o apenas para mostrar que o roteiro viola a própria hipótese. Com outro ritmo real, os excessos mudam; as pausas, não contadas, só pioram o quadro.
4. **Contraste de cor e licença de Inter** (05): pendências do próprio arquivo, não verificáveis aqui.
5. **Qualidade dos prompts do 06:** nenhum foi executado; só conferi cobertura (29 de 29), formato e proibições.
6. **Continuidade visual real:** não existe mídia; avaliada só no texto de 04, 05, 06 e 08.
7. **Se o usuário validou o brief v1** (linha 7 do v1 pedia validação antes de delegar): sem registro nos arquivos.
8. **Conteúdo real do `index.html`:** o extrato é a única fonte aceita; não comparei com o HTML.
9. **Avatar/voz sintética no arquivo de teste (SD-15):** o arquivo não permite concluir.
10. Arquivos não lidos listados em "Leituras".

## Rastreabilidade
Fontes: `projects/forma-digital/_sources/site-extract.md` (2026-11-08, único fonte de fatos do cliente); `00-client-audit.md`; `00-brief.md`; `00-brief.v2.md`; `00-inconsistencies-report.md`; `01-trends.md`; `02-strategy.md`; `03-script.md`; `04-direction.md`; `05-art-bible.md`; `06-prompts.md`; `07-audio-plan.md`; `08-edit-plan.md`; `10-performance.md`; `STATUS.md`; `_qa-test/03-script.SEEDED-DEFECTS.md`; templates listados em `entradas-usadas`; regras `.claude/rules/*.md` e `CLAUDE.md` (recebidos no contexto); `scripts/validate.py` (busca textual).
Fatos confirmados: contagens de palavras, folgas e somas de duração apresentadas acima (conferência aritmética neste documento, sobre o texto dos arquivos); ausência de "carrossel"/"Stories" em 03 a 08 (busca textual); ausência de "nós"/"somos"/"temos" na fala e na tela do 03 (busca textual); "GitHub" só em fala no 03 (busca textual); 29 planos em 04 e 29 prompts em 06; `knowledge/*/README.md` e `integrations/*.md` com marcadores "VAZIO"/"NÃO PESQUISADO" (16 ocorrências em 16 arquivos); citações de linhas do extrato usadas pelo 03 conferem; cabeçalhos e 5 rótulos de Rastreabilidade presentes nos arquivos revisados; nenhum uso proibido nos 11 entregáveis reais.
Hipóteses: critério de veredito deste revisor; severidades atribuídas; ritmo de 2,5 palavras/s (do 03, sem fonte); observação de 36% de cartões só de texto em P1 (cálculo sobre durações do 03/04; efeito em retenção é hipótese); leitura de RO-06 (sobreposição de P3 com o caso "Controle de solicitações"); leitura de B2-03 e ES-01 (forma absoluta da mensagem central).
Pendências: correção do 03 (v2) e reconformação de 04, 07, 08 (e 06); correções B2-01, B2-03, IR-01, TR-01, ES-02; decisão do ECD sobre GL-01 e as observações 1 a 7; execução de `scripts/validate.py` pelo ECD; D1 a D6 (não resolvidas aqui); verificação das fontes externas do 01 (`[A PESQUISAR]`); registro deste gate em `STATUS.md`.
Responsável: quality-reviewer

## Relatório ao Diretor
- **agente:** quality-reviewer
- **tarefa recebida:** Revisão 1 (gate de qualidade) de 12 itens de `projects/forma-digital/`: 00-brief.v2, 00-inconsistencies-report, 01 a 08, 10 e o roteiro de teste `_qa-test/03-script.SEEDED-DEFECTS.md`; vereditos individuais, achados com id, severidade, arquivo, trecho, regra e correção; conta de palavras × duração; critérios obrigatórios; D1 a D6 sem resolver.
- **arquivos consultados:** os listados em "Leituras (de fato) e não leituras" neste arquivo. CLAUDE.md e regras vieram no contexto, não reabertos; `scripts/validate.py` só por busca; não li `_execution/*`, `AGENTS.md`, `WORKFLOWS.md`, `templates/project-status.md`, `templates/README.md`.
- **trabalho realizado:** leitura integral dos 12 itens e do extrato; contagem manual de palavras de todas as falas (17 linhas fala × cena, 3 variações de gancho) e conferência das contas do 07 e do 08; conferência de somas de duração, de 29 planos e 29 prompts; buscas textuais de verificação; 1 bloqueante e 13 importantes e 26 menores nos entregáveis reais; 9 bloqueantes, 5 importantes e 1 menor no arquivo de teste.
- **skills aplicadas:** `quality-review`, passos 1 a 6 (aderência ao brief; template; consistência entre arquivos; não invenção; classificação e veredito; registro em `templates/qa-report.md`).
- **status:** DONE (com itens não verificados listados)
- **entregáveis:** `/home/user/Site.FirmaDigital/AI-VIRAL-STUDIO/projects/forma-digital/09-qa-report.md`
- **premissas:** (1) critério de veredito definido por mim e explicitado; (2) o extrato do site é a única fonte de fatos do cliente; (3) o ritmo de 2,5 pal/s é a hipótese do 03, usado só para auditar a coerência interna; (4) vereditos não promovem nenhum arquivo nem substituem D1 a D6; (5) a ordem Rastreabilidade antes de Relatório segue os templates, e a regra versus template foi levada ao ECD (GL-01).
- **pendências:** devolver o 03 ao scriptwriter (RO-01 a RO-09) via ECD e reconformar 04, 07, 08 (e 06); correções de B2, IR, TR, ES; decidir GL-01; atualizar `STATUS.md`; rodar `scripts/validate.py`; verificar fontes externas do 01 `[A PESQUISAR]`; D1 a D6 seguem NEEDS_INFO.
- **autoavaliação:**
  - ✔ Cada achado cita local exato e regra violada: id, arquivo, linhas e trecho em todos os bloqueantes e importantes; os menores trazem trecho, regra e correção na tabela.
  - ✔ Verifica aderência ao brief, ao template, à regra de não invenção e à consistência entre arquivos: critérios cobertos na síntese e nos achados.
  - ✔ Não reescreve o entregável: só indico o que corrigir; gravei apenas o `09-qa-report.md`.
  - ✔ Veredito justificado por critérios, não por impressão: critério de veredito explícito, conta de palavras mostrada, severidades por regra.
  - ✔ Não aprova o que não conseguiu verificar: seção "Itens não verificados" com 10 itens; nenhum arquivo recebeu APROVADO.
  - ✘ Verificação completa: sem shell nem web, não executei o validador e não verifiquei as fontes externas do 01 (limitação de ambiente).
