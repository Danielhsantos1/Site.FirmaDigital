---
projeto: forma-digital
versão: 2.0
autor-agente: scriptwriter
data: 2026-11-08
entradas-usadas: [03-script.md, 09-qa-report.md (Revisão 1: RO-01 a RO-09), _sources/site-extract.md, 00-brief.v2.md, 02-strategy.md, templates/script.md, .claude/skills/script-writing/SKILL.md, .claude/rules/*.md]
substitui: 03-script.md
status: rascunho   # 3 propostas, NÃO aprovadas; condicionais a D1 a D6 (brief v2: nenhum roteiro pode ser aprovado antes das decisões)
---

# Roteiro v2: 3 propostas de vídeo curto vertical (Instagram Reels / TikTok)

Status de todas as propostas: **rascunho / proposta, não aprovada.** O `03-script.md` (v1) permanece intacto.

## Resumo das mudanças vs. v1
| ID | Como foi resolvido | Onde (linha deste arquivo) |
|---|---|---|
| RO-01 (bloq.) | Falas reescritas/encurtadas e durações revistas. Tabela completa palavras × duração (23 linhas: 6 ganchos, 12 cenas, 5 CTAs; variantes D/I separadas), com regra de pausa declarada como premissa. Todas as folgas >= +0,2 s. Fonte do ritmo: `[A PESQUISAR]`, tratado como hipótese. Autoavaliação refeita com a conta. | L_TAB |
| RO-02 | Reconciliação fala × tela caso a caso (tabela própria); duas perdas aceitas por escrito; CTA institucional com tela própria. | L_RO02 |
| RO-03 | Ganchos de P1 e P2 (e variações) reescritos: o objeto "site" aparece na tela desde o quadro 0 e na fala até 1,2 s. Recomendação justificada por critério de retenção (hipótese sem fonte) e troca de risco declarada. | L_GANCHO |
| RO-04 | Omissão da landing page (Ang-3) registrada como decisão pendente do ECD (D-ECD-01). Não decidi. | L_COBERTURA |
| RO-05 | CTA por proposta (site: P1/P2; sistema/painel: P3). Textos marcados provisórios até D4/D6. Nenhuma fala imperativa para destino indefinido; destino na tela como `[DESTINO-D4]`. Ramo reconhecimento sem "salve/envie". | L_CTA |
| RO-06 | Sobreposição de P3 com o caso "Controle de solicitações de serviço" registrada como risco ligado a D5. Exemplo trocado por estoque pequeno (Item, Quantidade, Local), genérico, fictício, rotulado. | L_RISCO |
| RO-07 | Regra única de atribuição (RA) aplicada a todas as peças: selo "Declarado pelo negócio" na tela de toda cena de declaração. | L_RA |
| RO-08 | "antes de seguir" removido; "tudo em um só lugar" removido (painel agora "para organizar o processo", extrato l.53); "escopo ... por escrito" separado em duas frases fiéis (l.44 e l.82). Condensações restantes listadas em Hipóteses. | L_RASTRO |
| RO-09 | Nota sobre H1 corrigida: P1 × P2 diferem em ângulo e em família de gancho e não formam par de H1. | L_GANCHO |

## Como ler este documento
- Marcação de voz: **[Variante D2=Daniel]** (1ª pessoa) e **[Variante D2=institucional]** (narrador, sem equipe). Este roteiro não escolhe entre elas. Quando só há uma fala, ela vale para as duas.
- D1: nenhum nome em fala ou tela. Onde um nome seria necessário: `[NOME-D1]`.
- D3: nenhum avatar, imagem ou voz sintética de Daniel. A entrega da variante Daniel é decisão de D3 e da direção.
- D4: nenhum @, nenhum "link na bio". O destino do CTA é o marcador `[DESTINO-D4]`.
- D5: nenhuma prova de caso, cliente, tela ou dado real. Elementos visuais são ilustrativos e rotulados.
- D6: dois ramos de CTA (contatos / reconhecimento) mantidos; nenhum escolhido.
- Sem hashtags, músicas, áudios ou formatos "em alta". Áudio de fundo: `[A PESQUISAR]` (inclui licença comercial).
- Intenções de retenção são hipóteses, não validadas.

### Convenções de contagem e tempo (RO-01)
- **Palavra** = sequência separada por espaço. "e-mail" e "ajustezinho" contam 1. Numeral conta 1 ("4" = "quatro"). Os sinais "·" e "/" não contam. Contei cada fala palavra a palavra (seção "Contagem palavra a palavra").
- **Ritmo de fala: 2,5 palavras/s = 0,4 s por palavra.** Fonte: nenhuma. `knowledge/short-form-video/README.md` foi reportado como vazio no v1 e a skill `script-writing` lista o ritmo como `[A PESQUISAR]`. **É hipótese**, usada só para estimar. Só se mede com locução real.
- **Regra de pausa (PREMISSA minha, sem fonte):** 0,3 s por fronteira entre frases (cada ponto final, de interrogação ou de exclamação separa frases; vírgula e dois-pontos não contam) + 0,4 s de respiro por cena (0,2 s no início e 0,2 s no fim).
- **Tempo necessário** = 0,4 × palavras + 0,3 × (frases − 1) + 0,4. **Folga** = duração da cena − tempo necessário. Critério adotado: folga >= 0 em toda linha.
- **Leitura da tela** (hipótese, sem fonte, `[A PESQUISAR]`): 0,3 s por palavra de tela, incluindo selos, rótulos e marcadores. Critério: leitura <= duração da cena.
- **"Primeiro segundo"** (RO-03), definição de trabalho: o texto de tela está visível desde o quadro 0 (hipótese) e a palavra "site" é dita até 1,2 s.
- Duração-alvo por plataforma: **`[A PESQUISAR]`**. A conta fecha só internamente, contra a duração que este roteiro atribui a cada cena.

### Regras de redação aplicadas a todas as peças
- **RA, atribuição (RO-07):** toda cena que afirma modelo, processo, diferencial ou serviço do negócio exibe, na tela, o selo fixo **"Declarado pelo negócio"** durante a cena inteira. A fala usa verbo descritivo no presente, sem "garante", "sempre", "nunca", "sem erros". Quando D1 sair, a área de assinatura pode substituir o selo (pendência). Cenas puramente ilustrativas (situação, exemplo fictício) não levam o selo; levam o rótulo de ilustrativo.
- **RI, rótulo ilustrativo:** "Situação ilustrativa" em P1-C1 e P1-C2; "Exemplo fictício, ilustrativo" em P3-C1 a P3-C4 e no fechamento de P3. Mesmo texto, mesma posição, em toda a sequência.
- **RF, fidelidade:** frase do negócio só entra na fala com lastro no extrato; condensações e extensões estão em Hipóteses.

## Logline
- **P1, o "ajustezinho":** um site quase pronto recebe um pedido pequeno que se repete e o projeto não fecha; o modelo declarado do negócio é combinar o escopo antes de começar, trabalhar em pacotes fechados e ter aprovação em cada etapa.
- **P2, quatro etapas:** quem quer um site vê o caminho em quatro etapas (Escopo, Protótipo, Construção, Publicação), com aprovação em cada uma, como o negócio descreve.
- **P3, da planilha ao painel:** um processo manual genérico e fictício (um estoque pequeno em planilha) vira um formulário para registrar e um painel de controle para organizar o processo.

## Estrutura narrativa
Todas seguem a estrutura da estratégia (gancho, promessa, desenvolvimento de um ponto só, virada visual, fechamento com CTA). Um ângulo por peça (hipótese H4).
| Proposta | Ângulo (02-strategy) | Família de gancho | Oferta | Público (hipótese) |
|---|---|---|---|---|
| P1 | Ang-2 Problema do retrabalho | G1 dor reconhecível | Site (serviço 01) | A, C |
| P2 | Ang-1 Processo visível | G4 processo em uma linha | Site (serviço 01) | A, B, C |
| P3 | Ang-4 Do processo manual ao painel | G1/G2 (situação, depois resultado ilustrativo) | Sistema ou painel simples (serviço 03) | B |

### Cobertura e omissão registrada (RO-04)
O brief v2 (linha 34) e a estratégia (Ang-3, G3) priorizam **landing page**, depois site local, depois sistema/painel. Nenhuma das três propostas cobre a landing page (Ang-3), e o público A (principal) só é tocado de modo genérico por P1 e P2. A omissão veio do escopo pedido na v1 (3 propostas) e não de uma decisão de prioridade.
**Decisão pendente do ECD (D-ECD-01), que não tomei:** (a) pedir uma proposta P4 de landing page (Ang-3) ao scriptwriter, ou (b) aceitar por escrito que o piloto de roteiro começa pela prioridade 2 e 3. Se (a), a P4 entra numa v3 e o 04, 06, 07 e 08 passam a ter uma peça a mais.

## Variações de gancho (recomendada marcada)
Os ganchos não usam nome de marca. Janela de gancho em segundos: `[A PESQUISAR]`. Contagens na seção de tabela.
| Proposta | Gancho principal (fala) | Tela | Variação de gancho (fala) | Quadro 0 / "site" na fala |
|---|---|---|---|---|
| P1 | "Site quase pronto. Só um ajustezinho." | "Site quase pronto." / "Só um ajustezinho..." + "Situação ilustrativa" | "Site: quantos 'ajustezinhos' cabem num projeto?" | "site" é a 1ª palavra (0,0 a 0,4 s) nas duas |
| P2 | "Quer um site? Quatro etapas, aprovação em cada uma." | "Quer um site?" / "4 etapas · aprovação em cada uma" + selo | "Pediu um site? O que vem depois?" | "site" dito em 0,8 a 1,2 s |
| P3 | "Tem processo que mora numa planilha." | idem + "Exemplo fictício, ilustrativo" | "Quantas abas tem a sua planilha?" | objeto = "planilha"/"processo", em 0,8 a 2,4 s |

### Recomendação (decisão é do ECD)
**Recomendada: P2 com o gancho principal.** Justificativa por critério de retenção, **tudo hipótese sem fonte**, a validar no piloto:
- c1, objeto e situação cedo: P1 e P2 atendem (v1 não atendia).
- c2, tempo até a primeira informação nova após o gancho (soma das durações das cenas anteriores): P2 entrega a etapa 1 aos **4,5 s**; P1 entrega a virada (modelo declarado) aos **9,0 s** (C1 3,5 s + C2 5,5 s). Hipótese: quanto mais cedo a informação nova, menor o risco de abandono.
- c3, motivo para continuar: P2 tem sequência numerada que se completa (1 a 4); P1 tem situação reconhecível (dor), possivelmente mais forte na identificação, mas sem expectativa de conclusão explícita.
**Troca de risco declarada:** ao recomendar P2, aceito um gancho possivelmente menos emocional que o de P1 (perda possível de identificação, hipótese) em troca de (i) virada mais cedo (c2) e (ii) menor exposição a dramatização, pois cada frase de P2 tem lastro direto no extrato (l.79 a 91). P1 mantém o gancho de dor com mais risco de leitura como crítica a terceiros e mais dependência de tratamento visual cuidadoso.
Observação (hipótese): em P1 com CTA de contatos, o gancho (3,5 s) e o CTA (8,0 s) somam 11,5 s de 35,0 s (33%); se a direção os fizer como cartões só de texto, esse peso é um risco de retenção (já anotado como DI-07 no QA).

### Nota sobre H1 (RO-09, corrigida)
A H1 (02, linha 159) compara gancho de dor (G1) com gancho de processo (G4) **no mesmo ângulo**. P1 (Ang-2, G1) e P2 (Ang-1, G4) diferem em ângulo **e** em família de gancho; portanto **não formam par de H1** (a comparação ficaria confundida). A comparação P1 × P2 só se aproxima de H5 (Ang-1 × Ang-2, se D6 = contatos), ainda com gancho diferente. Um par válido de H1 exigiria o mesmo ângulo com os dois ganchos (por exemplo, P1 com gancho G4, ou P2 com gancho G1); **isso não foi escrito** e depende de pedido do ECD. As variações de gancho acima (pergunta) também não são G1 × G4.

---

## Roteiro por cena
Notas: "Conta" remete à linha da tabela de contagem. Durações e textos são estimativas sob as hipóteses acima.

### P1. O "ajustezinho" que vira retrabalho (rascunho / proposta, não aprovada)

**Cena 1. Gancho** (3,5 s)
- Intenção: identificar o objeto (site) e a situação (quase pronto, pedido pequeno) no primeiro segundo.
- Fala (as duas variantes): "Site quase pronto. Só um ajustezinho." (variação: "Site: quantos 'ajustezinhos' cabem num projeto?")
- Texto em tela: "Site quase pronto." / "Só um ajustezinho..." + "Situação ilustrativa". (variação: "Site: quantos ajustezinhos cabem num projeto?" + rótulo)
- Conta: G-P1, G-P1v.

**Cena 2. A repetição** (5,5 s)
- Intenção: mostrar o pedido que se repete, sem cliente nem caso real.
- Fala (as duas variantes): "Mais um. E mais outro. E o projeto não fecha."
- Texto em tela: "Mais um. E mais outro. E o projeto não fecha." + "Situação ilustrativa".
- Conta: P1-C2.

**Cena 3. O modelo declarado** (6,0 s)
- Intenção: virada. Apresentar o modelo como declaração do negócio.
- [Variante D2=Daniel]: "No meu modelo, o escopo é combinado antes de começar."
- [Variante D2=institucional]: "No modelo de trabalho, o escopo é combinado antes de começar."
- Texto em tela: "Escopo combinado antes de começar" + selo "Declarado pelo negócio".
- Conta: P1-C3.

**Cena 4. Pacote fechado** (6,0 s)
- Intenção: segundo ponto de apoio no mesmo tema (retrabalho). Sem valor, sem prazo numérico.
- [Variante D2=Daniel]: "Trabalho com pacotes fechados, sem cobrança por hora perdida em ajustes."
- [Variante D2=institucional]: "O trabalho é em pacotes fechados, sem cobrança por hora perdida em ajustes."
- Texto em tela: "Pacotes fechados" / "Sem cobrança por hora perdida em ajustes" + selo.
- Conta: P1-C4.

**Cena 5. Aprovação a cada etapa** (6,0 s)
- Intenção: ligar o problema ao processo, sem prometer resultado.
- [Variante D2=Daniel]: "O processo tem quatro etapas, e você aprova cada uma."
- [Variante D2=institucional]: "O processo tem quatro etapas, e o cliente aprova cada uma."
- Texto em tela: "4 etapas · aprovação em cada uma" + selo.
- Conta: P1-C5.

**Cena 6. CTA** (8,0 s no ramo contatos / 4,0 s no ramo reconhecimento). Ver seção CTA.

**Duração total estimada P1:** 35,0 s (D6=contatos) / 31,0 s (D6=reconhecimento).

---

### P2. Quatro etapas com aprovação (rascunho / proposta, não aprovada)

**Cena 1. Gancho** (4,5 s; 4,0 s na variação)
- Intenção: objeto e processo em uma linha (G4), com a situação de quem quer um site.
- Fala (as duas variantes): "Quer um site? Quatro etapas, aprovação em cada uma." (variação: "Pediu um site? O que vem depois?")
- Texto em tela: "Quer um site?" / "4 etapas · aprovação em cada uma" + selo. (variação: "Pediu um site? O que vem depois?", sem selo por não conter declaração)
- Conta: G-P2, G-P2v.

**Cena 2. Escopo** (6,0 s)
- Intenção: etapa 1 como fato do processo.
- [Variante D2=Daniel]: "Escopo: o que o site precisa ter, prazo e valor, tudo por escrito."
- [Variante D2=institucional]: "Escopo: o que o site precisa ter, prazo e valor, registrados por escrito."
- Texto em tela: "1 · Escopo" / "O que o site precisa ter · prazo · valor" / "Por escrito" + selo.
- Conta: P2-C2.

**Cena 3. Protótipo** (6,0 s)
- Intenção: etapa 2; virada visual (da lista para uma estrutura de página ilustrativa).
- [Variante D2=Daniel]: "Protótipo: você aprova estrutura e visual antes de qualquer conteúdo final."
- [Variante D2=institucional]: "Protótipo: o cliente aprova estrutura e visual antes de qualquer conteúdo final."
- Texto em tela: "2 · Protótipo" / "Estrutura e visual aprovados antes de qualquer conteúdo final" + selo.
- Conta: P2-C3.

**Cena 4. Construção** (6,0 s)
- Intenção: etapa 3; há ambiente de teste antes do ar.
- Fala (as duas variantes): "Construção: código versionado no GitHub e publicação em ambiente de teste."
- Texto em tela: "3 · Construção" / "Código versionado · ambiente de teste" + selo. ("GitHub" só na fala.)
- Conta: P2-C4.

**Cena 5. Publicação** (6,0 s)
- Intenção: etapa 4; fechar o caminho.
- Fala (as duas variantes): "Publicação: domínio conectado, HTTPS ativo e revisão final antes da entrega oficial."
- Texto em tela: "4 · Publicação" / "Domínio · HTTPS" / "Revisão final antes da entrega oficial" + selo.
- Conta: P2-C5.

**Cena 6. CTA** (8,0 s no ramo contatos / 5,0 s no ramo reconhecimento). Ver seção CTA.

**Duração total estimada P2:** 36,5 s (contatos) / 33,5 s (reconhecimento). Com a variação de gancho (4,0 s): 36,0 s / 33,0 s.

---

### P3. Da planilha ao painel (rascunho / proposta, não aprovada)

Todo o processo mostrado é **genérico e fictício** (um estoque pequeno em planilha), criado para ilustrar. Nenhum cliente, caso real, tela real ou o SaaS de contratos. Rótulo "Exemplo fictício, ilustrativo" em P3-C1 a C4 e no fechamento.

**Cena 1. Gancho** (3,0 s)
- Intenção: identificação (público B, hipótese).
- Fala (as duas variantes): "Tem processo que mora numa planilha." (variação: "Quantas abas tem a sua planilha?")
- Texto em tela: "Tem processo que mora numa planilha." + rótulo. (variação: "Quantas abas tem a sua planilha?" + rótulo)
- Conta: G-P3, G-P3v.

**Cena 2. O processo manual** (6,0 s)
- Intenção: mostrar a dispersão num exemplo fictício, sem exagero nem estatística.
- Fala (as duas variantes): "Itens numa aba, quantidades noutra, locais em outra."
- Texto em tela: "Item · Quantidade · Local" / "em abas separadas" + rótulo.
- Conta: P3-C2.

**Cena 3. O formulário** (6,0 s)
- Intenção: virada visual (da planilha para um formulário). Primeira metade da solução.
- [Variante D2=Daniel]: "Eu posso construir um formulário para registrar cada item."
- [Variante D2=institucional]: "Um formulário pode registrar cada item."
- Texto em tela: "Formulário para registrar" + rótulo.
- Conta: P3-C3.

**Cena 4. O painel** (6,0 s)
- Intenção: segunda metade da solução (resultado visual ilustrativo, G2). Sem prometer ganho.
- [Variante D2=Daniel]: "E um painel de controle para organizar o processo."
- [Variante D2=institucional]: "E um painel de controle pode organizar o processo."
- Texto em tela: "Painel de controle para organizar o processo" + rótulo.
- Conta: P3-C4.

**Cena 5. Enquadramento da oferta** (5,5 s)
- Intenção: ligar o exemplo ao serviço real descrito no site, sem prova de caso.
- [Variante D2=Daniel]: "Sistema ou painel simples, sob medida, para um processo do seu negócio."
- [Variante D2=institucional]: "Sistema ou painel simples, sob medida, para um processo do negócio."
- Texto em tela: "Sistema ou painel simples, sob medida" + selo.
- Conta: P3-C5.

**Cena 6. CTA** (8,5 s no ramo contatos / 3,5 s no ramo reconhecimento). Ver seção CTA.

**Duração total estimada P3:** 35,0 s (contatos) / 30,0 s (reconhecimento).

---

## CTA (RO-05): por proposta, PROVISÓRIO até D4 e D6
- Canais que existem no site (extrato l.99 a 105): WhatsApp, e-mail e formulário "Solicitar orçamento" (que abre o e-mail). "Redes sociais: Em breve" (l.106 a 107).
- **Nenhuma fala manda agir em canal que o espectador não consegue localizar.** A fala é pergunta + frase do site. O destino aparece na tela como `[DESTINO-D4]`; só quando D4 definir o destino ele é preenchido com os canais acima. Como o espectador chega ao site (endereço, link) está fora do extrato: **NEEDS_INFO**. Link por plataforma: `[A PESQUISAR]`.
- O ramo reconhecimento **não usa "salve/envie"** (v1): a ação não leva ao negócio sem nome e sem perfil (QA RO-05c). Foi trocado por um fechamento que retoma o conteúdo da peça, sem imperativo, com `[NOME-D1]` e `[DESTINO-D4]` na tela. O ECD pode reintroduzir salvar/compartilhar se quiser; isso não foi decidido aqui. Reconhecimento de nome fica limitado enquanto D1 não sair (apontado na estratégia como ES-02).

### CTA para P1 e P2 (oferta: site) [PROVISÓRIO até D4/D6]
**[se D6=contatos]** (8,0 s) Conta: CTA-S-C.
- [Variante D2=Daniel]: "Quer conversar sobre o seu site? A primeira conversa é para entender seu objetivo, não para vender."
  - Tela [Daniel]: "Quer conversar sobre o seu site?" / "A primeira conversa é para entender seu objetivo, não para vender." / `[DESTINO-D4]` + selo.
- [Variante D2=institucional]: "Quer conversar sobre o seu site? A primeira conversa é para entender o objetivo, não para vender."
  - Tela [institucional], **própria**: "Quer conversar sobre o seu site?" / "A primeira conversa é para entender o objetivo, não para vender." / `[DESTINO-D4]` + selo.
- Nota: "não para vender" é frase do site (l.94), mantida como declaração do negócio (selo). H6 (CTA "conversa" × "orçamento") pode trocar a segunda frase por "Solicitar orçamento" quando houver destino; não escrito aqui.

**[se D6=reconhecimento]** (sem destino de ação; fala por peça)
- P1 (4,0 s), Conta: CTA-P1-R. Fala (as duas variantes): "Site com escopo combinado antes de começar." Tela: "Escopo combinado antes de começar" + selo + `[NOME-D1]` + `[DESTINO-D4]`.
- P2 (5,0 s), Conta: CTA-P2-R. Fala (as duas variantes): "Site em quatro etapas, com aprovação em cada uma." Tela: "4 etapas · aprovação em cada uma" + selo + `[NOME-D1]` + `[DESTINO-D4]`.

### CTA para P3 (oferta: sistema ou painel simples) [PROVISÓRIO até D4/D6]
**[se D6=contatos]** (8,5 s) Conta: CTA-P3-C.
- [Variante D2=Daniel]: "Quer organizar um processo do seu negócio? A primeira conversa é para entender seu objetivo, não para vender."
  - Tela [Daniel]: "Quer organizar um processo do seu negócio?" / "A primeira conversa é para entender seu objetivo, não para vender." / `[DESTINO-D4]` + selo.
- [Variante D2=institucional]: "Quer organizar um processo do seu negócio? A primeira conversa é para entender o objetivo, não para vender."
  - Tela [institucional], **própria**: "Quer organizar um processo do seu negócio?" / "A primeira conversa é para entender o objetivo, não para vender." / `[DESTINO-D4]` + selo.
- Nota: a frase de contato do site (l.93 a 94) é escrita para site; aplicá-la ao serviço 03 é extensão minha (ver Hipóteses).

**[se D6=reconhecimento]** (3,5 s) Conta: CTA-P3-R. Fala (as duas variantes): "Da planilha ao painel." Tela: "Da planilha ao painel" + rótulo "Exemplo fictício, ilustrativo" + `[NOME-D1]` + `[DESTINO-D4]`.

**[se D6=ambos / sem resposta]:** NEEDS_INFO. Não escolho o ramo.

## Duração total estimada
Estimativas sob o ritmo hipotético e a regra de pausa acima. Duração-alvo por plataforma: `[A PESQUISAR]`.
| Proposta | D6=contatos | D6=reconhecimento | v1 (contatos / reconhecimento) |
|---|---|---|---|
| P1 | 35,0 s | 31,0 s | 36 s / 32 s |
| P2 | 36,5 s (36,0 s com a variação de gancho) | 33,5 s (33,0 s) | 37 s / 33 s |
| P3 | 35,0 s | 30,0 s | 36 s / 32 s |

Soma conferida: P1 = 3,5 + 5,5 + 6,0 + 6,0 + 6,0 = 27,0, + 8,0 = 35,0 e + 4,0 = 31,0. P2 = 4,5 + 6,0 × 4 = 28,5, + 8,0 = 36,5 e + 5,0 = 33,5. P3 = 3,0 + 6,0 × 3 + 5,5 = 26,5, + 8,5 = 35,0 e + 3,5 = 30,0.
Se a duração-alvo pesquisada for menor, candidatas a corte (avaliação do ECD): P1-C4, P2-C3 e C4, P3-C3.

## Tabela de contagem: palavras × duração (RO-01)
Fórmulas: fala = 0,4 × P; necessário = fala + pausas + respiro (0,4 s); pausas = 0,3 × (frases − 1); folga = duração − necessário. D = Daniel, I = institucional; valor único = igual nas duas. Tela: palavras incluindo selo/rótulo/marcadores; leitura = 0,3 × palavras (hipótese). Tudo em segundos.
| ID | Trecho | Pal. D / I | Frases | Fala | Pausas | Respiro | Necessário D / I | Duração | Folga D / I | Tela (pal.) | Leitura da tela |
|---|---|---|---|---|---|---|---|---|---|---|---|
| G-P1 | gancho P1 | 6 | 2 | 2,4 | 0,3 | 0,4 | 3,1 | 3,5 | +0,4 | 8 | 2,4 |
| G-P1v | variação P1 | 6 | 1 | 2,4 | 0 | 0,4 | 2,8 | 3,5 | +0,7 | 8 | 2,4 |
| G-P2 | gancho P2 | 9 | 2 | 3,6 | 0,3 | 0,4 | 4,3 | 4,5 | +0,2 | 12 | 3,6 |
| G-P2v | variação P2 | 7 | 2 | 2,8 | 0,3 | 0,4 | 3,5 | 4,0 | +0,5 | 7 | 2,1 |
| G-P3 | gancho P3 | 6 | 1 | 2,4 | 0 | 0,4 | 2,8 | 3,0 | +0,2 | 9 | 2,7 |
| G-P3v | variação P3 | 6 | 1 | 2,4 | 0 | 0,4 | 2,8 | 3,0 | +0,2 | 9 | 2,7 |
| P1-C2 | repetição | 10 | 3 | 4,0 | 0,6 | 0,4 | 5,0 | 5,5 | +0,5 | 12 | 3,6 |
| P1-C3 | modelo | 10 / 11 | 1 | 4,0 / 4,4 | 0 | 0,4 | 4,4 / 4,8 | 6,0 | +1,6 / +1,2 | 8 | 2,4 |
| P1-C4 | pacote | 11 / 13 | 1 | 4,4 / 5,2 | 0 | 0,4 | 4,8 / 5,6 | 6,0 | +1,2 / +0,4 | 12 | 3,6 |
| P1-C5 | aprovação | 10 / 11 | 1 | 4,0 / 4,4 | 0 | 0,4 | 4,4 / 4,8 | 6,0 | +1,6 / +1,2 | 9 | 2,7 |
| P2-C2 | escopo | 13 / 13 | 1 | 5,2 | 0 | 0,4 | 5,6 | 6,0 | +0,4 | 15 | 4,5 |
| P2-C3 | protótipo | 11 / 12 | 1 | 4,4 / 4,8 | 0 | 0,4 | 4,8 / 5,2 | 6,0 | +1,2 / +0,8 | 14 | 4,2 |
| P2-C4 | construção | 11 | 1 | 4,4 | 0 | 0,4 | 4,8 | 6,0 | +1,2 | 10 | 3,0 |
| P2-C5 | publicação | 12 | 1 | 4,8 | 0 | 0,4 | 5,2 | 6,0 | +0,8 | 13 | 3,9 |
| P3-C2 | processo manual | 8 | 1 | 3,2 | 0 | 0,4 | 3,6 | 6,0 | +2,4 | 9 | 2,7 |
| P3-C3 | formulário | 9 / 6 | 1 | 3,6 / 2,4 | 0 | 0,4 | 4,0 / 2,8 | 6,0 | +2,0 / +3,2 | 6 | 1,8 |
| P3-C4 | painel | 9 / 9 | 1 | 3,6 | 0 | 0,4 | 4,0 | 6,0 | +2,0 | 10 | 3,0 |
| P3-C5 | oferta | 12 / 11 | 1 | 4,8 / 4,4 | 0 | 0,4 | 5,2 / 4,8 | 5,5 | +0,3 / +0,7 | 9 | 2,7 |
| CTA-S-C | CTA site, contatos (P1, P2) | 17 / 17 | 2 | 6,8 | 0,3 | 0,4 | 7,5 | 8,0 | +0,5 | 21 / 21 | 6,3 |
| CTA-P3-C | CTA P3, contatos | 18 / 18 | 2 | 7,2 | 0,3 | 0,4 | 7,9 | 8,5 | +0,6 | 22 / 22 | 6,6 |
| CTA-P1-R | CTA P1, reconhecimento | 7 | 1 | 2,8 | 0 | 0,4 | 3,2 | 4,0 | +0,8 | 10 | 3,0 |
| CTA-P2-R | CTA P2, reconhecimento | 9 | 1 | 3,6 | 0 | 0,4 | 4,0 | 5,0 | +1,0 | 11 | 3,3 |
| CTA-P3-R | CTA P3, reconhecimento | 4 | 1 | 1,6 | 0 | 0,4 | 2,0 | 3,5 | +1,5 | 9 | 2,7 |

**Resultado da conta:** 23 linhas (35 falas contando as variantes D/I distintas); **nenhuma folga negativa**; **folga mínima +0,2 s** (G-P2, G-P3, G-P3v); leitura de tela <= duração em todas (maior razão: G-P3 e G-P3v, 2,7 de 3,0 s; CTA-S-C, 6,3 de 8,0 s). Isto vale **somente sob** o ritmo de 2,5 pal/s e a regra de pausa acima, ambos hipóteses. Folgas de +0,2 s não toleram locução mais lenta; só locução real ou teste de leitura decide. Comparação com o QA: as 5 falas que excediam (P2-C2 institucional, P2-C3, P3-C5, CTA contatos, CTA reconhecimento) e as 2 com +0,2 s (P1-C2, P2-C1) foram refeitas; as variações de gancho de P2 (12 palavras) e P3 (8 palavras) também.

### Contagem palavra a palavra (recontada por mim)
- G-P1: Site(1) quase(2) pronto(3). Só(4) um(5) ajustezinho(6) = 6
- G-P1v: Site(1) quantos(2) ajustezinhos(3) cabem(4) num(5) projeto(6) = 6
- G-P2: Quer(1) um(2) site(3)? Quatro(4) etapas(5), aprovação(6) em(7) cada(8) uma(9) = 9
- G-P2v: Pediu(1) um(2) site(3)? O(4) que(5) vem(6) depois(7) = 7
- G-P3: Tem(1) processo(2) que(3) mora(4) numa(5) planilha(6) = 6
- G-P3v: Quantas(1) abas(2) tem(3) a(4) sua(5) planilha(6) = 6
- P1-C2: Mais(1) um(2). E(3) mais(4) outro(5). E(6) o(7) projeto(8) não(9) fecha(10) = 10
- P1-C3 D: No(1) meu(2) modelo(3), o(4) escopo(5) é(6) combinado(7) antes(8) de(9) começar(10) = 10
- P1-C3 I: No(1) modelo(2) de(3) trabalho(4), o(5) escopo(6) é(7) combinado(8) antes(9) de(10) começar(11) = 11
- P1-C4 D: Trabalho(1) com(2) pacotes(3) fechados(4), sem(5) cobrança(6) por(7) hora(8) perdida(9) em(10) ajustes(11) = 11
- P1-C4 I: O(1) trabalho(2) é(3) em(4) pacotes(5) fechados(6), sem(7) cobrança(8) por(9) hora(10) perdida(11) em(12) ajustes(13) = 13
- P1-C5 D: O(1) processo(2) tem(3) quatro(4) etapas(5), e(6) você(7) aprova(8) cada(9) uma(10) = 10
- P1-C5 I: O(1) processo(2) tem(3) quatro(4) etapas(5), e(6) o(7) cliente(8) aprova(9) cada(10) uma(11) = 11
- P2-C2 D: Escopo(1): o(2) que(3) o(4) site(5) precisa(6) ter(7), prazo(8) e(9) valor(10), tudo(11) por(12) escrito(13) = 13
- P2-C2 I: Escopo(1): o(2) que(3) o(4) site(5) precisa(6) ter(7), prazo(8) e(9) valor(10), registrados(11) por(12) escrito(13) = 13
- P2-C3 D: Protótipo(1): você(2) aprova(3) estrutura(4) e(5) visual(6) antes(7) de(8) qualquer(9) conteúdo(10) final(11) = 11
- P2-C3 I: Protótipo(1): o(2) cliente(3) aprova(4) estrutura(5) e(6) visual(7) antes(8) de(9) qualquer(10) conteúdo(11) final(12) = 12
- P2-C4: Construção(1): código(2) versionado(3) no(4) GitHub(5) e(6) publicação(7) em(8) ambiente(9) de(10) teste(11) = 11
- P2-C5: Publicação(1): domínio(2) conectado(3), HTTPS(4) ativo(5) e(6) revisão(7) final(8) antes(9) da(10) entrega(11) oficial(12) = 12
- P3-C2: Itens(1) numa(2) aba(3), quantidades(4) noutra(5), locais(6) em(7) outra(8) = 8
- P3-C3 D: Eu(1) posso(2) construir(3) um(4) formulário(5) para(6) registrar(7) cada(8) item(9) = 9
- P3-C3 I: Um(1) formulário(2) pode(3) registrar(4) cada(5) item(6) = 6
- P3-C4 D: E(1) um(2) painel(3) de(4) controle(5) para(6) organizar(7) o(8) processo(9) = 9
- P3-C4 I: E(1) um(2) painel(3) de(4) controle(5) pode(6) organizar(7) o(8) processo(9) = 9
- P3-C5 D: Sistema(1) ou(2) painel(3) simples(4), sob(5) medida(6), para(7) um(8) processo(9) do(10) seu(11) negócio(12) = 12
- P3-C5 I: Sistema(1) ou(2) painel(3) simples(4), sob(5) medida(6), para(7) um(8) processo(9) do(10) negócio(11) = 11
- CTA-S-C D: Quer(1) conversar(2) sobre(3) o(4) seu(5) site(6)? A(7) primeira(8) conversa(9) é(10) para(11) entender(12) seu(13) objetivo(14), não(15) para(16) vender(17) = 17
- CTA-S-C I: igual, com "o(13) objetivo(14)" no lugar de "seu(13) objetivo(14)" = 17
- CTA-P3-C D: Quer(1) organizar(2) um(3) processo(4) do(5) seu(6) negócio(7)? A(8) primeira(9) conversa(10) é(11) para(12) entender(13) seu(14) objetivo(15), não(16) para(17) vender(18) = 18
- CTA-P3-C I: igual, com "o(14) objetivo(15)" = 18
- CTA-P1-R: Site(1) com(2) escopo(3) combinado(4) antes(5) de(6) começar(7) = 7
- CTA-P2-R: Site(1) em(2) quatro(3) etapas(4), com(5) aprovação(6) em(7) cada(8) uma(9) = 9
- CTA-P3-R: Da(1) planilha(2) ao(3) painel(4) = 4

## Reconciliação fala × texto em tela (RO-02)
A premissa da v1 ("tela neutra vale para as duas variantes") foi mantida, com a atribuição passando para o selo (RA). Caso a caso:
| Caso | Divergência na v1 | Resolução na v2 |
|---|---|---|
| P1-C2 | fala "E o projeto continua aberto" sem tela | **Reconciliado:** a tela repete a fala ("E o projeto não fecha") |
| P1-C3 | fala atribuída ("No meu modelo" / "No modelo de trabalho"), tela sem atribuição | **Reconciliado:** selo "Declarado pelo negócio" na tela. **Perda aceita:** a pessoa gramatical (meu / de trabalho) não aparece na tela. Justificativa: a tela é neutra por premissa e o selo cobre as duas variantes |
| P1-C5 | fala "antes de seguir", tela sem | **Reconciliado:** "antes de seguir" removido da fala (também RO-08) |
| P2-C2 | fala "prazo e valor", tela só "Tudo registrado por escrito" | **Reconciliado:** a tela lista "O que o site precisa ter · prazo · valor" e "Por escrito" |
| P3-C2 | fala sobre abas, tela só campos | **Reconciliado:** a tela traz "em abas separadas" |
| CTA contatos | fala institucional "o objetivo" × tela única "seu objetivo" | **Reconciliado:** tela própria por variante (Daniel "seu", institucional "o") |
| CTA reconhecimento | fala longa × tela "Salvar · Compartilhar" | **Reconciliado:** nova fala curta por proposta; a tela repete a ideia da fala |
| Pessoa gramatical em P1-C5, P2-C3 ("você" / "o cliente") | fala varia por variante, tela neutra | **Perda aceita:** tela diz "aprovação em cada uma" / "aprovados"; justificativa: tela neutra por premissa, sentido preservado |
Diferenças restantes por variante são só de pessoa gramatical (Daniel / institucional), nunca de conteúdo.

## Risco registrado: P3 × caso "Controle de solicitações de serviço" (RO-06, ligado a D5)
- O extrato (l.63 a 69) lista o caso "Controle de solicitações de serviço" ("Rastreio de prazos e status de solicitações de serviço e material", "Uso interno"). A v1 de P3 usava Pedido, Status e Prazo, que **replicam** esse caso. O `00-inconsistencies-report.md` (I6/D5) trata a citação desse caso como pendência.
- **Risco:** mesmo sem nomear o caso, um exemplo com solicitação, status e prazo pode ser lido como o caso real. Depende de D5 (não resolvida aqui).
- **Mitigação nesta v2:** exemplo trocado por estoque pequeno com campos "Item · Quantidade · Local", que não reproduz solicitações, status ou prazos, nem treinamento (check-in, importação), nem contratos. É genérico, fictício e rotulado. Resta o risco de que o próprio tema "planilha para painel" evoque o caso; aguardar D5 se o ECD quiser eliminar.
- **Impacto a jusante:** `04-direction.md` (linhas 129 a 142) e `06-prompts.md` ainda descrevem "Pedido · Status · Prazo" e precisam ser refeitos para P3.

## Notas ao ECD (fora do roteiro falado)
- A etapa 1 do site usa "Definimos juntos" (l.82), 1ª pessoa do plural, em tensão com a regra "sem equipe". Não foi reutilizada; a frase foi reescrita sem sujeito coletivo.
- A variante institucional usa "o cliente" e "o negócio". A distância em relação ao site (1ª pessoa) é risco de coerência já apontado na estratégia.
- Em P3 (Daniel), "Eu posso construir" é capacidade declarada pelo site (serviço 03 e "Sistemas que projetei e construí", l.55), sem referência a caso.
- "valor" aparece como item do escopo registrado por escrito (l.82), sem número. Confirmar com o responsável se pode ser mencionado em peça.
- Durações mudaram em várias cenas (ver tabela). Isso invalida os tempos de planos do 04, os âncoras do 07 e a matriz do 08.

## Rastreabilidade
Fontes: `_sources/site-extract.md` (2026-11-08, única fonte de fatos do cliente); `03-script.md` (v1); `09-qa-report.md` (Revisão 1, RO-01 a RO-09); `00-brief.v2.md`; `02-strategy.md`; `templates/script.md`; `.claude/skills/script-writing/SKILL.md`; `.claude/rules/*.md` (recebidas no contexto).
Fatos confirmados: (extrato do site) escopo definido, prazo combinado e nada de "ajustezinho" que vira retrabalho, como declaração do negócio (l.31); pacotes fechados, sem cobrança por hora perdida em ajustes, escopo combinado antes de começar (l.44); sistema ou painel simples, "Formulários, cadastros ou painéis de controle para organizar um processo específico do seu negócio" (l.52 a 53); "Sistemas que projetei e construí" (l.55); quatro etapas com aprovação em cada uma (l.79); Escopo: o que o site precisa ter, prazo e valor, tudo registrado por escrito (l.82); Protótipo: aprovação de estrutura e visual antes de qualquer conteúdo final entrar no ar (l.85); Construção: código versionado no GitHub e ambiente de teste (l.88); Publicação: domínio conectado, HTTPS ativo, revisão final antes da entrega oficial (l.91); "A primeira conversa é para entender seu objetivo, não para vender" (l.94); botão "Solicitar orçamento" que abre o e-mail (l.99 a 100); canais WhatsApp e e-mail (l.102 a 105); "Redes sociais: Em breve" (l.106 a 107); contagens de palavras e somas de duração deste arquivo (conferência aritmética sobre o texto, sob as hipóteses abaixo).
Hipóteses: ritmo de 2,5 palavras/s (sem fonte, `[A PESQUISAR]`); regra de pausa (0,3 s por fronteira de frase + 0,4 s de respiro por cena); piso de leitura de tela de 0,3 s/palavra; definição de "primeiro segundo"; todas as durações; critérios de retenção c1 a c3 e a recomendação de P2; intenções de retenção e identificação; público A/B/C; "uma peça, um ponto" (H4); texto em tela legível sem som (H9); dramatização de P1-C1/C2 e o estoque fictício de P3 como representativos; condensações do extrato: "estrutura e visual antes de qualquer conteúdo final" (l.85, sem "entrar no ar"), "para um processo do seu negócio" (l.53, sem "específico"), "aprova cada uma" (l.79 e 85 combinados), "o projeto não fecha" (dramatização, sem lastro no extrato), "você aprova" aplicado a todas as etapas (l.79); extensão da frase "A primeira conversa..." (l.94, escrita para site) ao serviço 03 em P3; "Quer/Pediu um site?" como situação do espectador; selo "Declarado pelo negócio" como forma de atribuição suficiente; "Site quase pronto" como situação ilustrativa.
Pendências: D1 a D6 (roteiro não aprovável antes delas); D2 (variantes mantidas); D3; D4 (destino do CTA, `[DESTINO-D4]`; como o espectador chega ao site); D5 (inclui o risco de P3 × caso "Controle de solicitações"); D6 (dois ramos); D-ECD-01 (landing page, Ang-3: incluir P4 ou aceitar a omissão); decisão do ECD sobre reintroduzir "salvar/compartilhar" no ramo reconhecimento; par válido de H1 (exigiria gancho extra, não escrito); ritmo de fala, duração-alvo por plataforma, janela de gancho, piso de leitura de tela, áudio e licença, regras de rotulagem de IA e regras publicitárias: `[A PESQUISAR]`; confirmar se "valor" e "Definimos juntos" podem aparecer/ser ajustados; medir a locução real; **reconfirmação obrigatória após esta v2: `04-direction.md` (planos e durações por cena, ganchos, P3 com novo exemplo, rótulo), `07-audio-plan.md` (falas, sincronia, CTA), `08-edit-plan.md` (contagem de palavras, matriz de exportações, CTA por proposta) e `06-prompts.md` (decupagem de P3 e dos ganchos)**; `STATUS.md` deve indicar a versão vigente; `scripts/validate.py` não foi executado (sem shell).
Responsável: scriptwriter

## Relatório ao Diretor
- **agente:** scriptwriter
- **tarefa recebida:** gravar `03-script.v2.md` corrigindo o `03-script.md` após a Revisão 1 do Quality Reviewer (RO-01 a RO-09), sem alterar o original nem outros arquivos, mantendo D1 a D6 como NEEDS_INFO e as variantes D2.
- **arquivos consultados:** `projects/forma-digital/03-script.md`; `09-qa-report.md`; `_sources/site-extract.md`; `00-brief.v2.md`; `02-strategy.md`; `templates/script.md`. Regras e `CLAUDE.md` vieram no contexto. Não reabri `knowledge/*` (o v1 e a skill registram o ritmo de fala como `[A PESQUISAR]`).
- **trabalho realizado:** tabela de 23 linhas palavras × duração com regra de pausa, todas as folgas >= +0,2 s, contagem palavra a palavra; falas e durações revistas; ganchos de P1 e P2 reescritos; CTA por proposta, provisório e sem imperativo para destino indefinido; reconciliação fala × tela; regra única de atribuição (selo); exemplo de P3 trocado e risco de D5 registrado; omissão da landing page registrada para o ECD; fala ajustada ao extrato; nota de H1 corrigida.
- **skills aplicadas:** `script-writing`, passos 2 a 6 reexecutados (gancho e variações; cenas com intenção, fala e tela; estimativa de duração com conta e conferência com o formato; CTA coerente; template). Passo 1 mantido da v1.
- **status:** NEEDS_INFO (parcial). As 3 propostas estão revisadas como rascunho; aprovação e produção dependem de D1 a D6, D-ECD-01 e reconfirmação de 04, 06, 07 e 08.
- **entregáveis:** `/home/user/Site.FirmaDigital/AI-VIRAL-STUDIO/projects/forma-digital/03-script.v2.md`
- **premissas:** (1) ritmo de 2,5 pal/s e regra de pausa (0,3 s por fronteira de frase + 0,4 s por cena) são hipóteses minhas sem fonte; (2) piso de leitura de tela de 0,3 s/palavra, hipótese; (3) selo "Declarado pelo negócio" resolve a atribuição (RA), a validar com D1; (4) recomendação de P2 por critério de retenção hipotético, decisão é do ECD; (5) o ramo reconhecimento perdeu "salve/envie" por RO-05c; (6) elementos visuais citados são ilustrativos, sem câmera, luz ou enquadramento; (7) nenhum prompt foi escrito.
- **pendências:** ver linha "Pendências" da Rastreabilidade. Em resumo: D1 a D6; D-ECD-01 (landing page); destino do CTA (D4); ritmo de fala, duração-alvo e demais itens `[A PESQUISAR]`; reconfirmar 04, 06, 07, 08 contra esta v2; `validate.py` não executado.
- **autoavaliação:**
  - ✔ Gancho nos primeiros instantes conforme a estratégia: P1 e P2 identificam o objeto e a situação (tela no quadro 0; "site" na fala até 1,2 s); janela em segundos segue `[A PESQUISAR]`.
  - ✔ Cada cena tem intenção clara: campo "Intenção" nas 18 cenas.
  - ✔ Duração compatível, **apenas internamente**: 23 linhas, nenhuma folga negativa (mínima +0,2 s) com 0,4 s/palavra, pausas de 0,3 s por fronteira de frase e 0,4 s de respiro por cena (conta na tabela). Ritmo e pausas são hipóteses; compatibilidade com o limite de cada plataforma não verificada (`[A PESQUISAR]`).
  - ✔ Tom de voz consistente com o brief: direto, sem superlativo, hype, urgência ou promessa; sem sujeito coletivo ou equipe.
  - ✔ Sem alegações factuais não suportadas: cada fato com linha do extrato; extensões e condensações listadas em Hipóteses; nada de cliente, SaaS, "03 sistemas", preço, número ou depoimento.
  - ✘ Aprovabilidade: o roteiro não pode ser aprovado por bloqueio de D1 a D6 e D-ECD-01 (limitação externa, não falha do texto).
