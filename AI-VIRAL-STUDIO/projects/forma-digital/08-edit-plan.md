---
projeto: forma-digital
versão: 0.1
autor-agente: video-editor
data: 2026-11-08
entradas-usadas: [03-script.md, 04-direction.md, 05-art-bible.md, 06-prompts.md, 07-audio-plan.md, 02-strategy.md, 00-brief.v2.md, 00-inconsistencies-report.md, _sources/site-extract.md, templates/edit-plan.md, .claude/rules/*.md, .claude/skills/edit-planning/SKILL.md, knowledge/README.md, knowledge/platforms/README.md, knowledge/short-form-video/README.md, integrations/README.md, integrations/capcut.md]
status: rascunho   # plano de edição das 3 propostas NÃO aprovadas; condicional a D1 a D6; roteiro, direção, art bible, prompts e plano de áudio também são rascunho; nenhuma mídia existe
---

# Plano de edição: P1, P2 e P3 (vertical curto, Instagram Reels / TikTok)

Tudo neste documento é **plano**. Nenhum vídeo, imagem, áudio, legenda ou arquivo de projeto de edição foi produzido. Os 29 prompts de `06-prompts.md` têm status `NÃO EXECUTADO`; portanto não há material para montar hoje. Nenhuma ferramenta de edição foi escolhida e nenhuma foi chamada.

## Como ler este documento
- **Tempos**: todos **ESTIMADOS**. Vêm das durações do roteiro/decupagem (hipótese do roteirista de ~2,5 palavras por segundo, sem fonte). Eu **não medi nada**: não existe áudio real. Cada tempo é um ponto de partida a ser refeito sobre a locução real.
- **Numeração**: cenas e planos iguais a `03-script.md` e `04-direction.md` (`P1-C2-S1` = proposta, cena, plano). Os mesmos ids são usados em `06-prompts.md` (estados do quadro) e `07-audio-plan.md` (SFX e âncoras).
- **Falas e textos**: não foram reescritos. Onde há texto de fala (legendas, Camada B) ele é cópia literal de `03-script.md`/`07-audio-plan.md`. Problemas encontrados vão para "Conflitos e divergências", não são corrigidos aqui.
- **Variantes**: [Variante D2=Daniel] e [Variante D2=institucional]; ramos [D6=contatos] e [D6=reconhecimento]. **Nenhuma é escolhida.** O ramo "D6=ambos / sem resposta" é NEEDS_INFO.
- **Base técnica**: `knowledge/platforms/` e `knowledge/short-form-video/` estão **VAZIOS**; `integrations/capcut.md` está "NÃO PESQUISADO" (todos os campos `[A PESQUISAR]`). Portanto **não afirmo** resolução, proporção, fps, codec, bitrate, limites, zonas seguras, loudness, nem qualquer recurso ou preço de software de edição. O que seria técnica ou especificação vira `[A PESQUISAR]`.
- **Duração-alvo**: o brief v2 não define duração-alvo ("duração e frequência a definir após pesquisa"). A timeline abaixo fecha com as **durações estimadas do roteiro** (36/32 s, 37/33 s, 36/32 s), não com uma meta de plataforma.
- **Marca e canais**: nenhum nome de marca (D1: `[NOME-D1]`, só em material interno), nenhum identificador de perfil, nenhuma hashtag, nenhum mecanismo de link (D4). Sem avatar, imagem ou voz de Daniel (D3).
- **Legenda dos rótulos de ilustração** usada nas tabelas: **R-D** = rótulo previsto no roteiro/decupagem; **R-E1** = extensão proposta no art bible (E1), com texto proposto pelo prompt-engineer, **decisão do ECD pendente**; "—" = sem rótulo.

## Premissas de edição e estrutura do projeto

**Timeline mestra + slots variáveis (hipótese de organização).** A decupagem diz que a variante D2 altera só o áudio (e a legenda da fala, se existir) e que D6 altera só a Cena 6. Logo, por proposta, proponho uma timeline mestra (C1 a C5, texto em tela, rótulos, gráficos) e três slots:

| Slot | Conteúdo | Muda com | Observação |
|---|---|---|---|
| S-A1 | Locução | D2 | Arquivo de locução **inexistente**; origem depende de D2/D3 (07, caminhos a/b/c). Este plano não prevê voz sintética de Daniel |
| S-C6 | Cena 6 (CTA) | D6 | `Px-C6a` (contatos, 2 planos) ou `Px-C6b` (reconhecimento, 1 plano) |
| S-LB | Legenda da fala (Camada B) | D2 e decisão ED-1 | Texto difere entre variantes; só existe se o ECD aprovar |

**Pontos de corte dependem da variante D2.** As frases das duas variantes têm tamanhos diferentes (ex.: P2-C2, P3-C3, CTA). Portanto os cortes ancorados na fala podem divergir entre variantes; ver "Mapa de sincronia".

**Pilha de camadas sugerida** (descrição por função, sem nomear trilhas de nenhum software):

| Camada | Conteúdo | Regra |
|---|---|---|
| V1 | Fundo liso `#161826` (CEN-01) | Contínuo do primeiro ao último quadro, nunca muda de tom (05, composição 8) |
| V2 | Gráfico por plano (estado(s) do prompt, 06) | Montado por camadas e estados; morph e acúmulo como corte entre estados ou composição (R10, R11 da direção) |
| V3 | Texto em tela (Inter, `#e9e9ed`) | **Camada composta, não gerada** (R1, RC5). Um bloco por plano (04) |
| V4 | Rótulo "ilustrativo" | **Camada fixa**, mesma posição e aparência, atravessa os cortes dentro de uma cena, nunca some no meio dela (R5, RC10) |
| V5 | Legenda da fala (Camada B) | **Condicional** (ED-1). Sem zona livre garantida; ver "Legendas" |
| A1 | Locução | Prioridade máxima de mixagem (07) |
| A2 | SFX funcionais | Abaixo da voz; mesmo tipo de som para o mesmo tipo de evento em todas as peças (07) |
| A3 | Trilha (opcional) | Duas versões a comparar: sem trilha e com trilha (07; H9) |

**Inventário de ativos necessários (nenhum existe hoje).**

| Ativo | Origem prevista | Status |
|---|---|---|
| Fundo liso, visto único, 4 nós, folha/cartão (âncoras) | 06, ordem 0 | NÃO EXISTE |
| Estados de quadro dos 29 planos | 06 (`NÃO EXECUTADO`) | NÃO EXISTE; ferramenta de geração não definida |
| Fonte Inter | Site (Google Fonts); licença em vídeo comercial `[A PESQUISAR]`; substituta se indisponível: NEEDS_INFO (E5) | Não verificado |
| Locução D2=Daniel / D2=institucional | 07 (caminhos a, b, c) | NEEDS_INFO (D2, D3); não existe |
| SFX | 07; origem e licença `[A PESQUISAR]` | NÃO EXISTE |
| Trilha (se houver) | 07; origem e licença `[A PESQUISAR]` | NÃO EXISTE |
| Arquivo de legenda | Texto-fonte neste documento; formato de arquivo `[A PESQUISAR]` | Não gerado |

## Timeline por proposta (tempo, plano, corte/transição, áudio, texto)

Convenções: tempos em segundos, estimados, pela duração dos planos de `04-direction.md` (sem reajuste à fala; ver conflitos). Transição entre planos = **corte seco**, como descrição da direção (efeito: `[A PESQUISAR]`). Dentro do plano, o movimento é animação de elementos por camada, não de câmera (curva e duração da animação: `[A PESQUISAR]`). Locução: só a âncora; texto integral em `07-audio-plan.md`, "Texto de locução". SFX: tipo, conforme 07.

### P1. O "ajustezinho" que vira retrabalho (rascunho / proposta, não aprovada)

| Plano | In–Out | Dur | V2 gráfico (estado) | V3 texto em tela | V4 | A1 âncora | A2 SFX | Transição |
|---|---|---|---|---|---|---|---|---|
| P1-C1-S1 | 0,0–3,0 | 3,0 | Fundo liso, sem forma | "Só um ajustezinho..." (reticências por último) | R-D "Situação ilustrativa" | "Só um ajustezinho." no início do plano | Aparição de texto; silêncio breve nas reticências | Corte seco |
| P1-C2-S1 | 3,0–5,5 | 2,5 | Bloco-base; cartão entra pela lateral e encaixa | "Mais um." | R-E1 | "Aí vem mais um." | Encaixe suave e seco | Corte seco |
| P1-C2-S2 | 5,5–8,0 | 2,5 | Cartões se acumulam; anel aberto que não fecha | "E mais outro." | R-E1 | "E mais outro."; "E o projeto continua aberto." sobre o fim | Encaixes repetidos, mais próximos entre si; textura contínua sem resolução | Corte seco |
| P1-C3-S1 | 8,0–11,0 | 3,0 | Cartões se alinham em folha (**virada: bagunça para ordem**) | sem texto | R-E1 | Início da frase na reorganização | Organização suave | Corte seco |
| P1-C3-S2 | 11,0–14,0 | 3,0 | Detalhe do topo da folha | "Escopo combinado por escrito, antes de começar." | R-E1 | Continuação da frase | Aparição de texto (igual ao gancho) | Corte seco |
| P1-C4-S1 | 14,0–17,0 | 3,0 | Contorno fechado em acento ao redor da folha | "Pacotes fechados" | R-E1 | "pacotes fechados" | Fechamento suave | Corte seco |
| P1-C4-S2 | 17,0–20,0 | 3,0 | Relógio genérico + traço riscado | "Sem cobrança por hora perdida em ajustes" + "Modelo declarado pelo negócio" | R-D "Modelo declarado pelo negócio"; R-E1 se aprovado (**duas legendas na mesma posição, ver C-7**) | "sem cobrança por hora perdida em ajustes" | Risco breve e discreto | Corte seco |
| P1-C5-S1 | 20,0–22,0 | 2,0 | 4 nós vazios, em sequência | sem texto | R-E1 | "O processo tem quatro etapas" | 4 toques leves, um por nó | Corte seco |
| P1-C5-S2 | 22,0–26,0 | 4,0 | Vistos nos 4 nós, um a um | "4 etapas · aprovação em cada uma" | R-E1 | "aprova cada uma antes de seguir" | Confirmação curta, padrão | Corte seco |
| P1-C6a-S1 | 26,0–31,0 | 5,0 | Fundo liso; três rótulos de texto entram um a um (CEN-07) | "WhatsApp" / "E-mail" / "Solicitar orçamento" | — | Abertura e canais (ver C-2) | Mesmo som de aparição ou sem efeito | Corte seco |
| P1-C6a-S2 | 31,0–36,0 | 5,0 | Lista sobe; frase em área limpa; quadro final estático | "A primeira conversa é para entender seu objetivo." | — | "A primeira conversa é para entender..." | Sem efeito | Fim (fade ou corte: `[A PESQUISAR]`) |
| P1-C6b-S1 | 26,0–32,0 | 6,0 | Fundo liso; texto; quadro final estático | "Salvar · Compartilhar" | — | Fala do ramo reconhecimento | Sem efeito | Fim |

**Total P1:** 36,0 s (D6=contatos) = 26,0 + C6a 10,0; 32,0 s (D6=reconhecimento) = 26,0 + C6b 6,0. Confere com `03-script.md` e `04-direction.md`.

### P2. Quatro etapas com aprovação (rascunho / proposta, não aprovada)

| Plano | In–Out | Dur | V2 gráfico (estado) | V3 texto em tela | V4 | A1 âncora | A2 SFX | Transição |
|---|---|---|---|---|---|---|---|---|
| P2-C1-S1 | 0,0–3,0 | 3,0 | 4 nós acendem em sequência, cada um seguido do visto | "4 etapas. Aprovação em cada uma." | R-E1 "Ilustrativo" | "Quatro etapas. Uma aprovação em cada uma." | Toque leve por nó + confirmação padrão | Corte seco |
| P2-C2-S1 | 3,0–6,0 | 3,0 | Nó 1 se amplia em lista (**virada: nó para lista**) | "1 · Escopo" | R-D "Ilustrativo" | "Escopo: o que o site precisa ter" | Expansão suave | Corte seco |
| P2-C2-S2 | 6,0–9,0 | 3,0 | Selo de "registrado" no canto da lista | "Tudo registrado por escrito" | R-E1 | "por escrito" (ver C-3) | Registro breve e discreto | Corte seco |
| P2-C3-S1 | 9,0–12,0 | 3,0 | Lista vira wireframe de blocos vazios (**virada: lista para página**) | "2 · Protótipo" | R-D "Ilustrativo" | "Protótipo" na virada | Reorganização suave | Corte seco |
| P2-C3-S2 | 12,0–15,0 | 3,0 | Wireframe ganha visto; blocos continuam vazios | "Estrutura e visual aprovados antes do conteúdo final" | R-E1 | "aprova... antes de qualquer conteúdo final" | Confirmação padrão | Corte seco |
| P2-C4-S1 | 15,0–18,0 | 3,0 | Wireframe recua; bloco de linhas abstratas entra (sem caracteres) | "3 · Construção" / "Código versionado" | R-E1 | "código versionado no GitHub" | Entrada suave | Corte seco |
| P2-C4-S2 | 18,0–21,0 | 3,0 | Cópia do wireframe desliza para a área de teste | "Ambiente de teste" | R-E1 | "ambiente de teste" | Deslize suave | Corte seco |
| P2-C5-S1 | 21,0–24,0 | 3,0 | Wireframe + barra de endereço vazia + cadeado genérico | "4 · Publicação" / "Domínio · HTTPS" | R-D "Ilustrativo" | "domínio conectado, HTTPS ativo" | Trava breve e discreta | Corte seco |
| P2-C5-S2 | 24,0–27,0 | 3,0 | 4 vistos na linha de nós (mesma composição de P2-C1) | "Revisão final" | R-E1 | "revisão final" | Confirmação padrão, mais resolvida | Corte seco |
| P2-C6a-S1 | 27,0–32,0 | 5,0 | Igual a P1-C6a-S1 | "WhatsApp" / "E-mail" / "Solicitar orçamento" | — | Ver C-2 | Idem P1 | Corte seco |
| P2-C6a-S2 | 32,0–37,0 | 5,0 | Igual a P1-C6a-S2; (opcional, decisão de edição) linha de 4 nós reduzida em canto | "A primeira conversa é para entender seu objetivo." | — | "A primeira conversa..." | Sem efeito | Fim (`[A PESQUISAR]`) |
| P2-C6b-S1 | 27,0–33,0 | 6,0 | Igual a P1-C6b-S1 | "Salvar · Compartilhar" | — | Fala do ramo reconhecimento | Sem efeito | Fim |

**Total P2:** 37,0 s (contatos) = 27,0 + 10,0; 33,0 s (reconhecimento) = 27,0 + 6,0. Confere.

### P3. Da planilha ao painel (rascunho / proposta, não aprovada)

Todo o conteúdo mostrado é genérico e fictício. Rótulo obrigatório no roteiro em C2 a C4: "Exemplo fictício, ilustrativo".

| Plano | In–Out | Dur | V2 gráfico (estado) | V3 texto em tela | V4 | A1 âncora | A2 SFX | Transição |
|---|---|---|---|---|---|---|---|---|
| P3-C1-S1 | 0,0–3,0 | 3,0 | Grade genérica preenche o quadro (barras abstratas) | "Tem processo que mora numa planilha." | R-E1 | Fala e texto coincidem | Textura de formação discreta | Corte seco |
| P3-C2-S1 | 3,0–6,0 | 3,0 | Grade com 3 cabeçalhos que acendem um a um | "Pedido · Status · Prazo" | R-D | "Pedidos... status... prazo" | 3 toques leves | Corte seco |
| P3-C2-S2 | 6,0–9,0 | 3,0 | Abas em cascata atrás da grade | sem texto | R-D (mantido) | "em outra aba" | Toques curtos em sequência | Corte seco |
| P3-C3-S1 | 9,0–11,0 | 2,0 | Grade se dissolve em 3 campos (**virada: planilha para formulário**) | sem texto | R-D | Fala inicia na transformação | Transformação suave | Corte seco |
| P3-C3-S2 | 11,0–15,0 | 4,0 | Campos se preenchem; botão; registro novo | "Formulário para registrar" | R-D | Fala segue no preenchimento | Preenchimento, clique suave, confirmação curta | Corte seco |
| P3-C4-S1 | 15,0–18,0 | 3,0 | Registro desliza da esquerda para a coluna (exceção horizontal, só neste plano) | sem texto | R-E1 | "um painel" (ver C-3) | Deslize suave | Corte seco |
| P3-C4-S2 | 18,0–21,0 | 3,0 | Painel de 3 colunas com cartões abstratos | "Painel para acompanhar" | R-D | "acompanhar o status de tudo em um só lugar" | Toques discretos e ordenados | Corte seco |
| P3-C5-S1 | 21,0–26,0 | 5,0 | Painel recua e esmaece para fundo neutro (ver "Cor e acabamento") | "Sistema ou painel simples, sob medida" | R-D, **só se o painel permanecer visível** | Fala sobre o esmaecer | Recuo suave; aparição de texto | Corte seco |
| P3-C6a-S1 | 26,0–31,0 | 5,0 | Igual a P1-C6a-S1 (o painel não volta) | "WhatsApp" / "E-mail" / "Solicitar orçamento" | — | Ver C-2 | Idem P1 | Corte seco |
| P3-C6a-S2 | 31,0–36,0 | 5,0 | Igual a P1-C6a-S2 (sem elemento da peça ao fundo) | "A primeira conversa é para entender seu objetivo." | — | "A primeira conversa..." | Sem efeito | Fim (`[A PESQUISAR]`) |
| P3-C6b-S1 | 26,0–32,0 | 6,0 | Igual a P1-C6b-S1 | "Salvar · Compartilhar" | — | Fala do ramo reconhecimento | Sem efeito | Fim |

**Total P3:** 36,0 s (contatos) = 26,0 + 10,0; 32,0 s (reconhecimento) = 26,0 + 6,0. Confere.

Contagem de planos (04): P1 = 9 + CTA; P2 = 9 + CTA; P3 = 8 + CTA; CTA = 2 (contatos) ou 1 (reconhecimento). Total 29 planos distintos, igual à decupagem e a `06-prompts.md`.

### Ritmo (virada visual por cena, H4)

Aritmética sobre as durações acima (não é avaliação de eficácia; ritmo ideal e janela de gancho: `[A PESQUISAR]`).

| Peça / ramo | Planos | Duração est. | Média por plano | Menor plano | Maior plano |
|---|---|---|---|---|---|
| P1 contatos | 11 | 36,0 s | ~3,3 s | 2,0 s (C5-S1) | 5,0 s (C6a) |
| P1 reconhecimento | 10 | 32,0 s | 3,2 s | 2,0 s | 6,0 s (C6b) |
| P2 contatos | 11 | 37,0 s | ~3,4 s | 3,0 s | 5,0 s (C6a) |
| P2 reconhecimento | 10 | 33,0 s | 3,3 s | 3,0 s | 6,0 s (C6b) |
| P3 contatos | 10 | 36,0 s | 3,6 s | 2,0 s (C3-S1) | 5,0 s (C5-S1, C6a) |
| P3 reconhecimento | 9 | 32,0 s | ~3,6 s | 2,0 s | 6,0 s (C6b) |

Diretrizes de ritmo:
1. **Uma virada visual por cena** (H4, hipótese): cada cena de C2 a C5 tem pelo menos um evento de imagem marcado em negrito ou na descrição de V2. C1 de P1 e as cenas de CTA são cartões de texto: a mudança ali é a entrada do texto, não de imagem (observação ao ECD, não defeito).
2. **A troca de plano cai no início da frase ou do trecho correspondente** (requisito de 04). As exceções detectadas estão no "Mapa de sincronia".
3. **Não acelerar a fala** para caber (07). Se a fala não cabe, é conflito de tempo, tratado como opção do ECD, não resolvido apertando a voz.
4. **Silêncio entre frases é intencional** (07, mixagem 4); a folga de cada cena precisa absorvê-lo. Duração da pausa: desconhecida (`[A PESQUISAR]`; medir no áudio real).
5. **Cenas com plano único longo**: P3-C5-S1 (5,0 s) e o CTA. Nesses, o ritmo depende de animação interna (esmaecer, entrada de rótulos), não de corte.

## Pontos de retenção (02-strategy) na timeline

Estrutura da estratégia: gancho, promessa, desenvolvimento de um ponto só, virada visual, fechamento com CTA. Janela de gancho em segundos: `[A PESQUISAR]` (não existe fonte); "gancho" abaixo significa só a Cena 1.

| Bloco (02) | P1 (Ang-2, G1) | P2 (Ang-1, G4) | P3 (Ang-4, G1/G2) |
|---|---|---|---|
| 1. Gancho | C1, 0,0–3,0: "Só um ajustezinho." | C1, 0,0–3,0: "Quatro etapas. Uma aprovação em cada uma." | C1, 0,0–3,0: "Tem processo que mora numa planilha." |
| 2. Promessa (frase da mensagem central, atribuída ao negócio) | C3, 8,0–14,0 (declaração do modelo) | Sem cena separada: o gancho já entrega o processo (lacuna registrada, não corrigida) | Sem frase de promessa; C5, 21,0–26,0, liga o exemplo ao serviço |
| 3. Desenvolvimento (um ponto só: H4) | C2 a C5, 3,0–26,0 (retrabalho) | C2 a C5, 3,0–27,0 (as 4 etapas) | C2 a C5, 3,0–26,0 (planilha, formulário, painel) |
| 4. Virada visual (H4) | 3,0 (cartão encaixa); 5,5 (acúmulo); **8,0 (bagunça para ordem)**; 14,0 (contorno); 17,0 (relógio riscado); 20,0 e 22,0 (nós e vistos) | 3,0 (nó para lista); **9,0 (lista para wireframe)**; 15,0; 18,0; 21,0; 24,0 (4 vistos) | 3,0 (cabeçalhos); 6,0 (abas); **9,0 (grade para campos)**; 11,0; 15,0; 18,0 (painel); 21,0 (painel esmaece) |
| 5. Fechamento (retomar o gancho e apontar o CTA) | C6 em 26,0. Opcional (04): folha ordenada de P1-C3-S1 ao fundo | C6 em 27,0. Retomada do gancho: linha de 4 nós concluída reduzida em canto (opcional, decisão de edição) | C6 em 26,0. O painel não volta (evita sugerir produto real) |

Hipóteses de teste da estratégia que tocam a edição (nenhuma validada):
- **H1 / H2 / H3** pedem variações de gancho. O roteiro traz uma "variação de gancho" por proposta, **sem decupagem nem texto em tela**. Elas ficam **fora da timeline**; verificação de tempo na seção de conflitos (C-9).
- **H4**: ver diretriz 1 de ritmo.
- **H6**: a versão do CTA que troca a frase final por "Solicitar orçamento" depende de o ECD devolver o texto; este plano não reescreve. Se decidido, o slot S-C6 muda de duração.
- **H9**: versão sem áudio, ver "Versões".

## Orçamento fala × cena (estimado) e conflitos de tempo

Método: contagem manual de palavras da fala em `07-audio-plan.md` × 0,4 s por palavra (2,5 palavras/s, hipótese do roteirista, sem fonte), **sem pausas**. As contagens do audio-producer foram conferidas e coincidem nos cinco casos que ele listou. Folga = duração da cena − duração estimada da fala. Valor negativo = fala maior que a cena.

| Cena | Palavras D / I | Fala est. D / I | Cena (04) | Folga D / I |
|---|---|---|---|---|
| P1-C1 | 3 / 3 | 1,2 / 1,2 | 3,0 | +1,8 / +1,8 |
| P1-C2 | 12 / 12 | 4,8 / 4,8 | 5,0 | **+0,2** / **+0,2** |
| P1-C3 | 12 / 12 | 4,8 / 4,8 | 6,0 | +1,2 / +1,2 |
| P1-C4 | 11 / 13 | 4,4 / 5,2 | 6,0 | +1,6 / +0,8 |
| P1-C5 | 13 / 14 | 5,2 / 5,6 | 6,0 | +0,8 / +0,4 |
| P2-C1 | 7 / 7 | 2,8 / 2,8 | 3,0 | **+0,2** / **+0,2** |
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

Leitura:
- **Excesso (folga negativa), mesmos casos do 07**: CTA contatos, CTA reconhecimento, P2-C3, P2-C2 institucional, P3-C5.
- **Risco adicional que identifiquei (folga de 0,2 s)**: P1-C2 (3 frases, logo 2 pausas internas) e P2-C1 (2 frases, 1 pausa). Em P1-C2, duas pausas somando mais de 0,2 s já geram excesso; em P2-C1, uma pausa maior que 0,2 s já gera. Se o ECD concordar, entram na mesma lista de decisão.
- Como as pausas não foram contadas, **todo excesso real será maior** que o da tabela; e as folgas pequenas (≤ 0,8 s) podem virar excesso.

### Totais se a cena for esticada até o tamanho estimado da fala (opção O1, sem pausas, piso)

| Peça | Base (04) | D2=Daniel | D2=institucional |
|---|---|---|---|
| P1 contatos | 36,0 | 37,6 | 36,8 |
| P1 reconhecimento | 32,0 | 32,4 | 32,4 |
| P2 contatos | 37,0 | 39,0 | 39,0 |
| P2 reconhecimento | 33,0 | 33,8 | 34,6 |
| P3 contatos | 36,0 | 38,2 | 37,0 |
| P3 reconhecimento | 32,0 | 33,0 | 32,6 |

(Soma das cenas com `max(cena, fala)`; as demais ficam na duração da cena.) Se a duração-alvo pesquisada de alguma plataforma ficar abaixo desses valores, o excesso vira corte de conteúdo (ver O4).

### Opções para o ECD (nenhuma aplicada; o plano não reescreve fala)

| Opção | O que faz | Efeito | Custo / risco |
|---|---|---|---|
| **O1. Esticar a cena** | Plano(s) da cena ganham o tempo que a locução real exigir | Resolve a cena; total sobe (tabela acima) | Cena fica diferente da decupagem; alonga a peça; pode ultrapassar duração-alvo (`[A PESQUISAR]`) |
| **O2. Redistribuir folga** | Encurta cenas com folga grande (ex.: P2-C4, P2-C5, P3-C2, P3-C3) para esticar as em excesso, mantendo o total | Total preservado | Mexe em ritmo de cenas vizinhas; as folgas precisam ainda absorver pausas. Exemplo de saldo, sem pausas: P2 institucional contatos tem excesso total de 2,0 s (C2 +0,4, C3 +0,8, C6 +0,8) contra folga de 3,0 s (C1 0,2, C4 1,6, C5 1,2) |
| **O3. Tratar só a cauda** | No CTA, definir se o quadro final inclui silêncio depois da última palavra (pergunta aberta do 04) | Define o piso real do CTA | Não resolve excesso de fala, só mede o que sobra depois dela |
| **O4. Cortar conteúdo** | Remover plano/cena candidata (roteiro e 04 indicam: P1-C4, P2-C3/C4, P3-C3; no 04, o plano S2) | Reduz o total | Altera o roteiro: **só o ECD decide e devolve o texto**; este plano não corta |
| **O5. Devolver a fala para encurtar** | O ECD pede revisão do texto (ex.: CTA contatos, o maior excesso) | Resolve na origem | Mudança de roteiro, fora do meu escopo; invalida âncoras e legendas deste plano |
| **O6. Descartada** | Acelerar a voz | — | O 07 proíbe apertar a voz para caber |

### Mapa de sincronia: onde o corte planejado diverge da fala estimada

Início estimado da frase-âncora (07) dentro da cena (palavras anteriores × 0,4 s, sem pausas) comparado ao início do plano-âncora (04). Valor da coluna "Desvio" = início da frase − início do plano. Negativo: a fala chega **antes** do corte; positivo: **depois**. Sem desvio relevante (≤ 0,2 s): P2-C3 (âncora "antes de qualquer conteúdo final"), P2-C4 ("ambiente de teste").

| Cena | Âncora (07) | Início da frase (D / I) | Início do plano-âncora (04) | Desvio D / I | Opção de ajuste (candidata; fixar com áudio real) |
|---|---|---|---|---|---|
| P1-C2 | "E mais outro." em S2 | 1,6 / 1,6 | 2,5 (S2) | −0,9 / −0,9 | Antecipar o corte S1/S2 para entre 1,6 e 2,5 s conforme a pausa real |
| P1-C4 | "sem cobrança por hora perdida em ajustes" em S2 | 1,6 / 2,4 | 3,0 (S2) | −1,4 / −0,6 | Antecipar o corte para ~1,6–2,4 s (varia por variante). Efeito colateral útil: S2 ganha mais tempo para o texto, que é o mais denso da peça (ver C-8) |
| P1-C5 | "aprova cada uma antes de seguir" em S2 | 2,8 / 3,2 | 2,0 (S2) | +0,8 / +1,2 | Manter o corte; atrasar a 1ª marca de aprovação em S2 até a palavra "aprova" (animação interna) |
| P2-C2 | "por escrito" em S2 | 4,4 / 5,6 | 3,0 (S2) | +1,4 / +2,6 | Manter o corte; fazer o selo entrar na âncora (dentro de S2), não no início do plano |
| P2-C5 | "revisão final" em S2 | 2,4 / 2,4 | 3,0 (S2) | −0,6 / −0,6 | Manter; avaliar com pausa real |
| P3-C2 | "em outra aba" em S2 | 2,4 / 2,4 | 3,0 (S2) | −0,6 / −0,6 | Manter; avaliar com pausa real |
| P3-C4 | "acompanhar/mostrar o status de tudo..." em S2 | 1,6 / 1,6 | 3,0 (S2) | −1,4 / −1,4 | Antecipar o corte S1/S2 para ~2,0 s (S1 2,0 / S2 4,0, total da cena mantido) |
| CTA contatos (P1, P2, P3) | Canais em S1; "A primeira conversa..." em S2 | 7,2 / 6,4 | 5,0 (C6a-S2) | +2,2 / +1,4 | **C-2**: ver abaixo |

Regra decorrente: **como os cortes ancorados na fala mudam por variante D2, cada variante pode precisar do seu próprio ponto de corte** (P1-C4, P1-C5, P2-C2, P3-C3). Se o ECD preferir uma timeline única, o corte será um compromisso e uma das variantes ficará fora de sincronia (decisão ED-5).

## Conflitos e divergências tratados

**C-1. Excesso de fala sobre cena**: tabela e opções acima. Decisão ED-2.

**C-2. CTA contatos: canais falados depois do fim de S1.** O plano divide a cena em S1 (lista, 5,0 s) e S2 (frase final, 5,0 s). A fala, estimada, termina os canais em 7,2 s (Daniel) ou 6,4 s (institucional) e só então diz "A primeira conversa...". Com os cortes de 04 (5,0 s), a lista de canais sairia de cena antes de a locução terminar de citá-los. Opções para o ECD:
- **(a)** S1 = 7,2 s / S2 = 4,4 s (Daniel); S1 = 6,4 s / S2 = 4,4 s (institucional). Totais 11,6 s e 10,8 s, sem cauda e sem pausas.
- **(b)** Manter 5,0 s / 5,0 s e aceitar que os rótulos precedem a fala em parte do trecho (ou mantê-los visíveis na S2 como lista reduzida, o que já é o movimento previsto "a lista sobe").
- **(c)** Reduzir a fala (O5).
Em qualquer caso, cauda de silêncio no quadro final e mecanismo de chegada ao site (D4) continuam abertos: se D4 trouxer um mecanismo, falta um plano e tempo de fechamento (NEEDS_INFO).

**C-3. Texto em tela × fala divergem (07, "Alternativa sem áudio") e tratamento na edição.** Não reescrevo. Tratamento por caso, com as opções (a) manter, (b) cobrir com Camada B, (c) reforçar pelo gráfico já previsto, (d) devolver ao roteirista via ECD:

| Onde | Fala traz | Tela traz | Perde na versão sem áudio | Tratamento na edição |
|---|---|---|---|---|
| P1-C2 | "E o projeto continua aberto." | "Mais um. E mais outro." | A ideia de projeto aberto | (c) o anel que não fecha precisa ficar visível até o fim de S2 e o SFX sem resolução; (b) ou (d) se não bastar |
| P1-C3 / P1-C4 | "No meu modelo..." / "O modelo de trabalho prevê..."; "Trabalho com..." | Resumos; só C4 tem "Modelo declarado pelo negócio" | A marca de declaração do negócio em C3 | (a) ou (b); ver C-7 sobre o rótulo de C4 |
| P2-C2 | "o que o site precisa ter, prazo e valor" | "Tudo registrado por escrito" | "prazo e valor" | (a) ou (b). **"Valor" continua pendência aberta do roteiro** (pode ser citado?) |
| P3-C2 | "anotados aqui... em outra aba" | "Pedido · Status · Prazo" | A dispersão (depende da cascata de abas) | (c) cascata de P3-C2-S2 legível; (b) |
| CTA contatos | Convite, três canais, frase final | Lista de canais + "A primeira conversa é para entender seu objetivo." | O convite "Quer conversar...?" | (a) ou (b) |
| CTA reconhecimento | "Se foi útil, salve este vídeo e envie a quem está pensando em fazer um site." | "Salvar · Compartilhar" | Quem enviar e para quê | (a) ou (b); nomes dos botões por plataforma `[A PESQUISAR]` |
| **CTA contatos, D2=institucional (achado novo)** | "...entender **o** objetivo..." | "...entender **seu** objetivo." (o roteiro diz que a tela é neutra para as duas variantes) | n/a (divergência dentro da variante) | **Pergunta ao ECD**: a tela fica com "seu objetivo" na variante institucional? Não reescrevo |

**C-4. Camada B (legenda da fala) e o princípio "um bloco de texto por plano".** O 04 e o 05 pedem **um bloco de texto por plano** e **só o texto previsto no roteiro**. Se a Camada B coexistir com a Camada A, são dois blocos. Além disso, **não há zona livre garantida no quadro**: o terço superior é do texto principal (05, composição 5; bloco de quadro do 06), o centro é do diagrama e a faixa inferior é do rótulo e foi mantida vazia no 06. Zonas seguras da plataforma: `[A PESQUISAR]`. Decisão ED-1 (existe ou não; se existir, onde).

**C-5. Camada B duplica a Camada A em alguns planos.** Onde o texto em tela repete a fala (P1-C1, P3-C1; quase em P2-C1), a legenda da fala seria a mesma frase mostrada duas vezes (hipótese: competição por espaço). Opção: suprimir a Camada B nesses planos. Decisão ED-1.

**C-6. Rótulo "ilustrativo": abrangência (E1).** O roteiro exige rótulo só em P1-C1 e P3-C2 a C4; a direção e o art bible recomendam estendê-lo (R-E1). Esta timeline marca R-D e R-E1 separadamente para que a decisão do ECD altere só a camada V4. Texto do rótulo nos planos R-E1 é proposta do prompt-engineer (o rótulo da própria peça). Regra de plataforma/publicitária para o rótulo: `[A PESQUISAR]`. Decisão ED-4.

**C-7. P1-C4-S2: dois textos secundários na mesma posição.** "Modelo declarado pelo negócio" (R-D, função em dúvida: rótulo de declaração ou de ilustração, E2) e "Situação ilustrativa" (R-E1) disputam o canto inferior. Opções: (a) só o primeiro neste plano; (b) empilhar os dois com ordem fixa; (c) decisão do ECD sobre E2. Decisão ED-4.

**C-8. Densidade de texto em tela (sem piso de leitura documentado).** Tempo mínimo de leitura e tamanho mínimo: `[A PESQUISAR]`. Planos de maior carga por segundo, só como alerta de revisão:
| Plano | Texto em tela | Palavras | Plano | Observação |
|---|---|---|---|---|
| P1-C4-S2 | "Sem cobrança por hora perdida em ajustes" + "Modelo declarado pelo negócio" | 11 | 3,0 s | O mais denso; beneficia-se da antecipação do corte (S2 de ~4,0 s) |
| P2-C3-S2 | "Estrutura e visual aprovados antes do conteúdo final" | 8 | 3,0 s | Mais a marca de aprovação |
| CTA contatos S2 | "A primeira conversa é para entender seu objetivo." (+ lista subindo) | 8 | 5,0 s | Mais a lista |
| P1-C3-S2 | "Escopo combinado por escrito, antes de começar." | 6 | 3,0 s | |

**C-9. Variações de gancho do roteiro não decupadas e com tempo.** O roteiro lista uma variação por proposta, sem cena, sem texto em tela e sem plano na decupagem. Contagem de palavras da fala (hipótese 2,5 palavras/s) contra os 3,0 s da Cena 1: P1 "Quantos 'ajustezinhos' cabem em um projeto?" = 6 palavras, ~2,4 s (cabe); P3 "Quantas abas tem a planilha do seu processo?" = 8 palavras, ~3,2 s (−0,2 s); P2 "O que acontece entre pedir um site e ele ir ao ar?" = 12 palavras, ~4,8 s (**−1,8 s**). Por isso **não entram na timeline**. Para testar H1/H2/H3, o ECD precisaria pedir decupagem e arte das variações (NEEDS_INFO).

**C-10. Transformações e esmaecimentos geram tons fora da paleta.** O art bible limita as peças às cinco cores do site em quadros de repouso e evita tons intermediários. Um esmaecimento por opacidade (P3-C5-S1; fim do CTA, "fade ou corte") produz tons intermediários momentâneos. Opção de montagem: **corte entre estados** (painel reduzido em `#232532` sobre `#161826`), como já sugere o 06 (AP6). Aceitar ou não opacidade: ED-10. Efeitos de transição: `[A PESQUISAR]`.

## Legendas e temporização

### Camada A: texto em tela (do roteiro)
- **Texto**: o do roteiro (coluna V3 da timeline), exato, com acentos, na pontuação do roteiro (RC4). Texto composto na edição, nunca gerado (R1).
- **Estilo (coerente com 05)**: Inter; `#e9e9ed` por padrão; acento (`#9184d9`) só em destaque curto (numeração de etapa "1 ·", PROPOSTA do art bible); sem caixa colorida, sem sombra, sem brilho, sem contorno; sem cor fora das cinco. Pesos, tamanhos e entrelinha: `[A PESQUISAR]` (CSS completo do site). Texto longo em acento sobre `#232532`: evitar até verificar contraste.
- **Temporização**: o texto entra no início do plano (ou na âncora da fala, quando a tabela da timeline indica) e fica até o fim do plano. Duração e curva da animação de entrada: `[A PESQUISAR]`. Tempo mínimo de leitura: `[A PESQUISAR]`.
- **Posição e zona segura**: `[A PESQUISAR]`. Até lá, texto longe das bordas e fora do terço inferior reservado ao rótulo (04, 05).
- **Casos especiais**: P1-C1 (reticências por último); P1-C3 (texto só em S2); P1-C5 (texto só em S2); P2-C4 ("GitHub" não aparece em tela, só "Código versionado", conforme 04/06; aceitação do texto "GitHub": pendência E10).

### Camada B: legenda da fala (CONDICIONAL, ED-1)
Só existe se o ECD aprovar. **Texto = a fala da variante escolhida**, cópia literal de `07-audio-plan.md` (que copia `03-script.md`). Estilo proposto, coerente com o art bible: Inter, `#e9e9ed`, sem caixa e sem sombra. Posição, número de linhas, caracteres por linha, velocidade de leitura e zona segura: `[A PESQUISAR]` (ver C-4). Formato de arquivo de legenda aceito por cada plataforma: `[A PESQUISAR]` (não afirmo nenhum). Tempos abaixo = início e fim estimados (palavras × 0,4 s, sem pausas), **na timeline-base**; se a cena for reajustada (O1/O2), deslocar junto. Quando o fim ultrapassa o limite da cena, marquei com (+).

**P1** (cenas em 0,0 / 3,0 / 8,0 / 14,0 / 20,0 / 26,0)

| Cue | D2=Daniel | D2=institucional | In–Out D | In–Out I |
|---|---|---|---|---|
| 1 | "Só um ajustezinho." | igual | 0,0–1,2 | 0,0–1,2 |
| 2 | "Aí vem mais um." | igual | 3,0–4,6 | 3,0–4,6 |
| 3 | "E mais outro." | igual | 4,6–5,8 | 4,6–5,8 |
| 4 | "E o projeto continua aberto." | igual | 5,8–7,8 | 5,8–7,8 |
| 5 | "No meu modelo, o escopo é combinado por escrito antes de começar." | "O modelo de trabalho prevê escopo combinado por escrito antes de começar." | 8,0–12,8 | 8,0–12,8 |
| 6 | "Trabalho com pacotes fechados, sem cobrança por hora perdida em ajustes." | "O trabalho é em pacotes fechados, sem cobrança por hora perdida em ajustes." | 14,0–18,4 | 14,0–19,2 |
| 7 | "O processo tem quatro etapas, e você aprova cada uma antes de seguir." | "O processo tem quatro etapas, e o cliente aprova cada uma antes de seguir." | 20,0–25,2 | 20,0–25,6 |

**P2** (cenas em 0,0 / 3,0 / 9,0 / 15,0 / 21,0 / 27,0)

| Cue | D2=Daniel | D2=institucional | In–Out D | In–Out I |
|---|---|---|---|---|
| 1 | "Quatro etapas." | igual | 0,0–0,8 | 0,0–0,8 |
| 2 | "Uma aprovação em cada uma." | igual | 0,8–2,8 | 0,8–2,8 |
| 3 | "Escopo: o que o site precisa ter, prazo e valor, tudo por escrito." | "Escopo: o que o site precisa ter, o prazo e o valor ficam registrados por escrito." | 3,0–8,2 | 3,0–9,4 (+) |
| 4 | "Protótipo: você aprova a estrutura e o visual antes de qualquer conteúdo final entrar no ar." | "Protótipo: o cliente aprova a estrutura e o visual antes de qualquer conteúdo final entrar no ar." | 9,0–15,4 (+) | 9,0–15,8 (+) |
| 5 | "Construção: código versionado no GitHub e publicação em ambiente de teste." | igual | 15,0–19,4 | 15,0–19,4 |
| 6 | "Publicação: domínio conectado, HTTPS ativo e revisão final antes da entrega oficial." | igual | 21,0–25,8 | 21,0–25,8 |

**P3** (cenas em 0,0 / 3,0 / 9,0 / 15,0 / 21,0 / 26,0)

| Cue | D2=Daniel | D2=institucional | In–Out D | In–Out I |
|---|---|---|---|---|
| 1 | "Tem processo que mora numa planilha." | igual | 0,0–2,4 | 0,0–2,4 |
| 2 | "Pedidos anotados aqui, status ali, prazo em outra aba." | igual | 3,0–6,6 | 3,0–6,6 |
| 3 | "Eu posso construir um formulário para registrar cada pedido." | "Um formulário pode registrar cada pedido." | 9,0–12,6 | 9,0–11,4 |
| 4 | "E um painel para acompanhar o status de tudo em um só lugar." | "E um painel pode mostrar o status de tudo em um só lugar." | 15,0–20,2 | 15,0–20,2 |
| 5 | "Sistema ou painel simples, sob medida, para organizar um processo específico do seu negócio." | "Sistema ou painel simples, sob medida, para organizar um processo específico do negócio." | 21,0–26,6 (+) | 21,0–26,2 (+) |

**CTA (Cena 6, comum; tempos relativos ao início da Cena 6)**

| Ramo / cue | D2=Daniel | D2=institucional | In–Out D | In–Out I |
|---|---|---|---|---|
| Contatos 1 | "Quer conversar sobre o seu site?" | "Quer conversar sobre o site do seu negócio?" | 0,0–2,4 | 0,0–3,2 |
| Contatos 2 | "Chame no WhatsApp, mande um e-mail ou use o formulário Solicitar orçamento." | "Há WhatsApp, e-mail e o formulário Solicitar orçamento." | 2,4–7,2 | 3,2–6,4 |
| Contatos 3 | "A primeira conversa é para entender seu objetivo, não para vender." | "A primeira conversa é para entender o objetivo, não para vender." | 7,2–11,6 (+) | 6,4–10,8 (+) |
| Reconhecimento | "Se foi útil, salve este vídeo e envie a quem está pensando em fazer um site." | igual | 0,0–6,4 (+) | 0,0–6,4 (+) |

## Camadas de áudio

Fonte única das diretrizes: `07-audio-plan.md`. Aqui só o que cabe à edição. Todo nível numérico (dB, LUFS), taxa de amostragem e formato: `[A PESQUISAR]`.

- **A1 Locução**: arquivo **inexistente**. Entra uma variante por versão (D2). Origem condicionada a D2/D3; **nenhuma voz sintética de Daniel** (07, caminho a: somente gravação real feita por ele; b: voz institucional a definir; c: só com autorização escrita). Pronúncia de "WhatsApp", "GitHub", "HTTPS", "e-mail": pendente (07).
- **A2 SFX**: mapa por plano em 07 (e coluna A2 da timeline). Regra de edição: cada SFX cola no evento visual; **quando coincide com palavra-chave, o efeito cede**; mesmo timbre para aprovação e para aparição de texto nas três peças; sem sons que imitem notificações, interfaces ou identidade sonora de plataformas ou marcas.
- **A3 Trilha (opcional)**: versões a comparar: **(1) voz + SFX, sem trilha; (2) voz + SFX + trilha discreta**. Gancho (C1) com trilha ausente ou entrando só depois da primeira frase; desenvolvimento com cama contínua; CTA estável, quadro final estático e encerramento natural (fade ou corte: `[A PESQUISAR]`). Faixa, fonte e licença comercial para conta empresarial: `[A PESQUISAR]`.
- **Prioridades de mixagem (qualitativas, 07)**: 1) voz, 2) SFX abaixo da voz, 3) trilha como cama que recua enquanto a voz fala, 4) silêncio entre frases preservado, 5) consistência entre peças, 6) verificação em mais de um tipo de reprodução (procedimento `[A PESQUISAR]`).
- **Loudness por plataforma**: `[A PESQUISAR]`.
- **Alternativa sem áudio (H9)**: ver "Versões".

## Versões (matriz de entrega, rotuladas, sem escolha)

Eixos: **proposta** (P1, P2, P3) × **D2** (Daniel, institucional) × **D6** (contatos, reconhecimento) × **áudio** (narrada sem trilha, narrada com trilha, silenciosa).

| Eixo | Altera | Não altera |
|---|---|---|
| D2 | A1 (locução) e a Camada B, se existir; pontos de corte ancorados na fala | Texto em tela (neutro), gráficos, rótulos |
| D6 | Cena 6 (planos, duração, texto em tela, fala do CTA); total da peça | C1 a C5 |
| Trilha | A3 | Tudo o mais |
| Silenciosa (H9) | Remove A1, A2 e A3 | Timeline-base, texto em tela, rótulos, gráficos |

**Volume bruto.** Narrada: 3 propostas × 2 (D2) × 2 (D6) × 2 (com/sem trilha) = **24**; silenciosa: 3 × 2 (D6) = **6**, ou **12** se a Camada B existir (depende de D2). Total até **36** exportações, antes de multiplicar por plataforma. **Isso é ineficiente** e pouco útil como piloto: as decisões D2 e D6 colapsam a matriz. Com D2 e D6 respondidas e sem Camada B: 3 propostas × (narrada sem trilha, narrada com trilha, silenciosa) = **9**. Alternativa sem decidir D2/D6 agora: montar só a **timeline mestra e o texto em tela** (que não dependem de D2), deixando S-A1 e S-C6 prontos para encaixe. Decisão ED-7.

**Versão sem áudio (H9).**
- Peça legível só pela Camada A. Mantida a **mesma timeline-base** da versão narrada (hipótese: variar só uma coisa por teste). A versão silenciosa não sofre os conflitos de tempo da fala; fica sujeita ao tempo mínimo de leitura (`[A PESQUISAR]`) e ao alerta de densidade (C-8).
- Perdas já mapeadas em C-3. Perguntas ao ECD (herdadas do 07): aceitar as perdas? Camada B entra para recuperá-las? Se entrar, a silenciosa passa a depender de D2.
- Dispensa as pendências de direitos de voz e, se não houver trilha, de áudio em geral; mantém rotulagem e regras publicitárias.
- Métrica de comparação narrada × silenciosa: H9 em `02-strategy.md`; nome oficial da métrica `[A PESQUISAR]`.

**Nomes de arquivo (proposta, hipótese de organização):** `<proposta>_<d2>_<d6>_<audio>` (ex.: `P2_inst_con_semtrilha`). Sem nome de marca, sem data de publicação, sem identificador de perfil.

## Cor e acabamento planejados

Peças gráficas 2D chapadas. **Não há correção de cor a planejar** no sentido de gradação: não se prevê LUT, filtro, grão, vinheta, sombra, brilho, gradiente ou textura (05: "O que evitar"). O que existe é **conferência de cor**:
1. Fundo `#161826` em 100% dos quadros (RC1); só as cinco cores do site (RC2): `#161826`, `#232532`, `#e9e9ed`, `#9184d9`, `#a7a1db`.
2. **A aprovação da cor se faz sobre o quadro exportado**, não sobre o hex do site (05). Comportamento da cor após edição e compressão por plataforma (perfil de cor, fidelidade do hex): `[A PESQUISAR]`.
3. Contraste dos pares texto/fundo: não calculado; método e norma `[A PESQUISAR]`; testar em tela real de celular.
4. Texto: Inter composta, com acentos corretos, revisão quadro a quadro contra `03-script.md` (RC3, RC4). Licença de Inter em vídeo comercial `[A PESQUISAR]`; fonte substituta se indisponível: NEEDS_INFO (E5), não improvisar.
5. Transições com opacidade geram tons momentâneos fora da paleta (C-10).
6. Valores de espessura de linha, raio de canto, margem e tamanhos de fonte: `[A PESQUISAR]` (E12). Não declaro números.
7. Nenhum quadro com número, moeda, data, gráfico com valor, logotipo ou aparência de produto de terceiros, pessoa, nome de marca, identificador de perfil, URL, telefone ou e-mail (RC11 a RC14).

## Especificações de exportação por plataforma

**Nenhum valor é afirmado.** `knowledge/platforms/` está vazio e o brief v2 não traz especificação (só "vertical"; duração e frequência "a definir após pesquisa"). Campos a preencher, com fonte (URL ou documento oficial), data da consulta e confiança, conforme as regras de `knowledge/`. Pedido ao ECD: acionar a pesquisa e registrar em `knowledge/platforms/<tema>.md`.

| Campo | Instagram (Reels) | TikTok | Fonte | Data | Confiança |
|---|---|---|---|---|---|
| Proporção | `[A PESQUISAR]` | `[A PESQUISAR]` | | | |
| Resolução | `[A PESQUISAR]` | `[A PESQUISAR]` | | | |
| Taxa de quadros (fps) | `[A PESQUISAR]` | `[A PESQUISAR]` | | | |
| Contêiner/formato de arquivo | `[A PESQUISAR]` | `[A PESQUISAR]` | | | |
| Codec de vídeo | `[A PESQUISAR]` | `[A PESQUISAR]` | | | |
| Codec e taxa de amostragem de áudio | `[A PESQUISAR]` | `[A PESQUISAR]` | | | |
| Bitrate (vídeo e áudio) | `[A PESQUISAR]` | `[A PESQUISAR]` | | | |
| Perfil/espaço de cor | `[A PESQUISAR]` | `[A PESQUISAR]` | | | |
| Duração mínima e máxima | `[A PESQUISAR]` | `[A PESQUISAR]` | | | |
| Tamanho máximo de arquivo | `[A PESQUISAR]` | `[A PESQUISAR]` | | | |
| Zonas seguras (topo, base, laterais) para texto, rótulo e legenda | `[A PESQUISAR]` | `[A PESQUISAR]` | | | |
| Loudness alvo e pico | `[A PESQUISAR]` | `[A PESQUISAR]` | | | |
| Legenda embutida × arquivo de legenda, formatos aceitos | `[A PESQUISAR]` | `[A PESQUISAR]` | | | |
| Música: biblioteca da plataforma × áudio incorporado; licença comercial para conta empresarial | `[A PESQUISAR]` | `[A PESQUISAR]` | | | |
| Rotulagem de conteúdo gerado/IA: regra vigente, campo ou aviso, texto | `[A PESQUISAR]` | `[A PESQUISAR]` | | | |
| Nome dos botões Salvar/Compartilhar (para o CTA de reconhecimento) | `[A PESQUISAR]` | `[A PESQUISAR]` | | | |
| Mecanismo de link/botão de ação (D4; fora do escopo da edição, registrado por dependência do CTA) | `[A PESQUISAR]` | `[A PESQUISAR]` | | | |

**Master (arquivo de trabalho/intermediário):** parâmetros do projeto de edição `[A PESQUISAR]`; definir só depois de preencher a tabela acima. Pendência de compatibilidade: a duração-alvo pesquisada pode ficar abaixo das durações estimadas, e então valem as opções O1 a O5.

## Fluxo de trabalho: manual assistido, ferramenta não escolhida

- **Ferramenta de edição: NÃO escolhida.** `integrations/capcut.md` está "NÃO PESQUISADO" e a existência de API ou automação oficial viável está "NÃO CONFIRMADA". Pela política de integrações, o fluxo é **manual assistido** com entregáveis exportáveis. **Não afirmo recursos, formatos de projeto, atalhos ou preços de nenhum editor.** Escolha da ferramenta: decisão do ECD (ED-13); se a escolha cair no que está documentado em `integrations/`, a pesquisa precede o uso.
- **Entregáveis exportáveis deste plano (texto, independentes de ferramenta):** (1) **lista de cortes** = tabelas de timeline de P1, P2 e P3; (2) **texto-fonte de legendas** = cues da Camada B e textos da Camada A; (3) **mapa de sincronia** e **opções de reajuste**; (4) **roteiro de montagem** abaixo; (5) **checklist** abaixo. Arquivo de legenda em formato de plataforma: `[A PESQUISAR]`.

**Roteiro de montagem (para quem monta; descrição genérica, não instrução a outros agentes):**
0. **Pré-condição**: existem os estados de quadro (06 executado), a fonte Inter validada, e as decisões ED-1, ED-2, ED-4 respondidas. Hoje nada disso existe.
1. Criar o projeto com os parâmetros do master (`[A PESQUISAR]`).
2. Importar ativos e nomeá-los por id de plano e estado.
3. V1: fundo liso `#161826` do início ao fim.
4. V2: montar planos em ordem da timeline, por estados e camadas; transformações como corte entre estados ou composição.
5. Transições: **corte seco** entre planos, exceto onde o ECD decidir (ED-10).
6. V3: compor texto em Inter, um bloco por plano, textos exatos do roteiro.
7. V4: rótulos como camada contínua dentro de cada cena, mesma posição e aparência (RC10).
8. A1: inserir a locução da variante; **refazer os cortes ancorados** conforme o mapa de sincronia, com o áudio real.
9. A2: inserir SFX nos eventos visuais, abaixo da voz.
10. A3: trilha só nas versões "com trilha".
11. V5: Camada B só se ED-1 aprovar.
12. Conferir contagens e consistência (4 nós, 3 cabeçalhos/campos/colunas, visto único).
13. Exportar conforme a tabela de exportação preenchida; revisar o **arquivo exportado**, não o projeto.
14. Registrar origem e licença de cada trilha, efeito e voz (07, R9).

## Checklist de finalização e QA pré-publicação

Todos os itens estão **não iniciados**: nenhum material existe. Itens com `[A PESQUISAR]` não podem ser dados como cumpridos antes da pesquisa.

**Bloqueios e decisões**
- [ ] D1 a D6 respondidas (nenhum roteiro aprovado antes disso; brief v2).
- [ ] Roteiro, direção, art bible, prompts e plano de áudio aprovados (hoje, rascunhos).
- [ ] ED-1 a ED-13 respondidas.
- [ ] **D4: nada publicado.** Sem perfis oficiais confirmados, não há publicação; este plano não publica, não agenda e não configura nada.
- [ ] D3: nenhum avatar, imagem, voz ou semelhança de Daniel em nenhum quadro ou áudio sem autorização escrita.

**Conteúdo**
- [ ] Texto em tela idêntico ao roteiro, com acentos, quadro a quadro (RC4); legenda (se houver) idêntica à fala da variante.
- [ ] Nenhum número, preço, prazo, estatística, moeda, data, depoimento, cliente, "03 sistemas", SaaS de contratos ou tela real.
- [ ] Diferenciais ("escopo definido, prazo combinado, sem retrabalho"; pacotes fechados) apresentados como **declaração do negócio**, não como prova ou resultado.
- [ ] Nenhum nome de marca (D1), nenhum identificador de perfil, nenhuma hashtag, nenhum "link na bio", nenhuma URL, telefone ou e-mail.
- [ ] Nenhum logotipo, ícone ou aparência de WhatsApp, GitHub, navegador, planilha, rede social.
- [ ] Rótulo "ilustrativo" presente conforme a decisão ED-4, mesma posição, sem sumir no meio da cena.
- [ ] Sem "nós"/equipe na variante institucional; "valor" e "GitHub" em fala/tela só conforme decisão do ECD (pendências).

**Imagem**
- [ ] RC1 a RC16 do art bible verificados no quadro exportado.
- [ ] Contagem: 4 nós em P1-C5, P2-C1 e P2-C5, sobreponíveis; 3 cabeçalhos/campos/colunas em P3.
- [ ] Contraste e legibilidade testados em tela real de celular (método `[A PESQUISAR]`).
- [ ] Texto e rótulo fora das zonas cobertas pela interface da plataforma (zonas `[A PESQUISAR]`).

**Áudio**
- [ ] Locução inteligível acima de todo o resto; SFX cedem a palavras-chave; trilha recua sob a voz.
- [ ] Loudness conforme especificação da plataforma (`[A PESQUISAR]`).
- [ ] Voz com origem e autorização registradas (07, R3 a R5); trilha e SFX com licença comercial registrada (07, R1, R2, R9).
- [ ] Verificação em mais de um tipo de reprodução (procedimento `[A PESQUISAR]`).

**Sincronia e tempo**
- [ ] Conflitos de tempo resolvidos pela opção escolhida (ED-2); cortes ancorados refeitos com áudio real.
- [ ] CTA: cauda do quadro final e mecanismo de chegada ao site definidos (ED-3, D4).
- [ ] Duração final dentro do limite da plataforma (`[A PESQUISAR]`).

**Exportação e conformidade**
- [ ] Parâmetros de exportação preenchidos com fonte e data (tabela acima).
- [ ] **Rótulo de conteúdo gerado/IA**: regra de cada plataforma consultada e aplicada (`[A PESQUISAR]`; as fontes encontradas até agora são secundárias, de 2024 ou sem data).
- [ ] Regras publicitárias brasileiras aplicáveis à fala e ao CTA consultadas (`[A PESQUISAR]`).
- [ ] Uso de nomes de terceiros ("WhatsApp", "GitHub") em peça comercial verificado (`[A PESQUISAR]`).
- [ ] Arquivo final revisado no formato exportado; nomes de arquivo conforme a convenção; sem metadados com nome de marca ou dado pessoal (política de metadados: `[A PESQUISAR]`).
- [ ] Registro por peça: ativos usados, origem, licença, data, quem aprovou (07, R9).

## Decisões e pedidos ao ECD

| # | Decisão / pedido | Base | Observação |
|---|---|---|---|
| ED-1 | A Camada B (legenda da fala) existe? Se sim: qual variante, onde no quadro, suprimida onde duplica a tela (C-5)? | 07 (conflito 3); C-4 | Não há zona livre garantida; pode exigir exceção ao "um bloco de texto por plano" |
| ED-2 | Opção por conflito de tempo (O1 a O5) e por cena de folga baixa (P1-C2, P2-C1) | Tabela de orçamento | O5 e O4 alteram o roteiro |
| ED-3 | CTA contatos: S1/S2 (C-2) e cauda de silêncio no quadro final; fala e quadro final incluem a cauda? | C-2; 04 | Depende também de D4 |
| ED-4 | Rótulo "ilustrativo": abrangência (E1), redação nos planos R-E1, função de "Modelo declarado pelo negócio" (E2), conflito de posição em P1-C4-S2 | C-6, C-7 | |
| ED-5 | Um ponto de corte por variante D2, ou uma timeline única de compromisso? | Mapa de sincronia | |
| ED-6 | Versões com e sem trilha; silenciosa com a mesma duração da narrada? | 07; H9 | |
| ED-7 | Reduzir a matriz de versões (36 bruto) ou montar só a timeline mestra até D2/D6 | Versões | |
| ED-8 | Inter: licença em vídeo comercial e substituta se indisponível | 05 (E5) | |
| ED-9 | "Valor" falado e "GitHub" em fala e tela; "seu objetivo" na tela da variante institucional (C-3) | 03, 04, 07 | Não reescrevo |
| ED-10 | Fim do quadro final e esmaecimento: fade, corte ou corte entre estados (C-10) | 04, 06 | `[A PESQUISAR]` |
| ED-11 | Pesquisa de especificações por plataforma, duração-alvo, zonas seguras, rotulagem de IA, loudness | Tabela de exportação | Registrar em `knowledge/platforms/` |
| ED-12 | Como o espectador chega ao site (D4); se vier, pedir plano de fechamento | 03, 04, 07 | NEEDS_INFO |
| ED-13 | Ferramenta de edição a adotar (nenhuma escolhida) | `integrations/capcut.md` | Fluxo manual assistido enquanto não documentada |
| ED-14 | Decupagem das variações de gancho, se H1/H2/H3 forem testadas (C-9) | 03, 04 | NEEDS_INFO |

## Rastreabilidade
Fontes: `projects/forma-digital/03-script.md` (v0.1, rascunho); `04-direction.md` (v0.1, rascunho); `05-art-bible.md` (v0.1, rascunho); `06-prompts.md` (v0.1, rascunho, 29 prompts `NÃO EXECUTADO`); `07-audio-plan.md` (v0.1, rascunho); `02-strategy.md` (v1.0, rascunho); `00-brief.v2.md`; `00-inconsistencies-report.md`; `_sources/site-extract.md` (2026-11-08, linhas 1 a 70); `templates/edit-plan.md`; `.claude/rules/*.md`; `.claude/skills/edit-planning/SKILL.md`; `knowledge/README.md`, `knowledge/platforms/README.md`, `knowledge/short-form-video/README.md` (todos VAZIOS, 2026-11-08); `integrations/README.md`, `integrations/capcut.md` (NÃO PESQUISADO, 2026-11-08).
Fatos confirmados: os textos em tela, rótulos e falas citados vêm literalmente de `03-script.md`, `04-direction.md` e `07-audio-plan.md`; as durações por plano e por cena vêm de `04-direction.md` e as somas conferem (36/32 s, 37/33 s, 36/32 s, aritmética neste documento); a decupagem tem 29 planos, igual a `06-prompts.md`; o brief v2 não define duração-alvo, proporção nem especificação de exportação; `knowledge/platforms/` e `knowledge/short-form-video/` não têm conteúdo documentado; `integrations/capcut.md` não tem campo preenchido e a API/automação oficial está "NÃO CONFIRMADA"; D1 a D6 não foram respondidas; nenhuma mídia (vídeo, imagem, áudio, legenda) existe.
Hipóteses: todas as durações e estimativas de fala (2,5 palavras/s, sem fonte; contagens manuais de palavras, coincidentes com as do audio-producer nos cinco casos listados por ele); orçamento fala × cena, folgas, totais do cenário O1 e desvios do mapa de sincronia (sem pausas); ritmo (médias de duração de plano são aritmética, a relação com retenção é hipótese H4); estrutura timeline mestra + slots; pilha de camadas; sugestão de antecipar cortes (P1-C4, P3-C4); estilo da Camada B; alerta de densidade de texto; que Camada B compete por espaço; que opacidade gera tons fora da paleta; que a versão silenciosa deve manter a timeline da narrada; convenção de nomes de arquivo; roteiro de montagem; tudo que o art bible rotula como PROPOSTA ou HIPÓTESE.
Pendências: D1 a D6; D2/D3 (voz); ED-1 a ED-14; todas as especificações de exportação por plataforma, duração-alvo, janela de gancho, zonas seguras, loudness, perfil de cor, pesos e tamanhos de fonte, raio e espessura (`[A PESQUISAR]`); rotulagem de IA e regras publicitárias (`[A PESQUISAR]`); licença de Inter, trilha, SFX e voz (`[A PESQUISAR]`); ferramenta de edição e de geração não definidas; nomes dos botões Salvar/Compartilhar; como o espectador chega ao site (NEEDS_INFO); decupagem das variações de gancho (NEEDS_INFO); aprovação do roteiro, direção, art bible, prompts e áudio (rascunhos); `scripts/validate.py` não executado por este agente (sem shell neste escopo).
Responsável: video-editor

## Relatório ao Diretor
- **agente:** video-editor
- **tarefa recebida:** gravar `projects/forma-digital/08-edit-plan.md` (inexistente) conforme `templates/edit-plan.md`: timeline por proposta (P1, P2, P3) plano a plano com ids da decupagem e camadas (gráfico, texto em tela, rótulo "ilustrativo", locução, legendas, SFX, trilha); cortes e transições como diretrizes; ritmo (H4); legendas fiéis ao roteiro; versões D2 e D6 rotuladas sem escolha; versão sem áudio (H9); tratamento dos conflitos de tempo e divergências fala × tela apontados pelo audio-producer; exportação `[A PESQUISAR]` por plataforma; fluxo manual assistido sem escolher ferramenta; checklist de QA pré-publicação; sem mídia descrita como existente, sem Daniel (D3), sem marca (D1), sem perfil/hashtag (D4).
- **arquivos consultados:** `projects/forma-digital/03-script.md`; `04-direction.md`; `05-art-bible.md`; `06-prompts.md` (leitura integral em duas páginas); `07-audio-plan.md`; `02-strategy.md`; `00-brief.v2.md`; `00-inconsistencies-report.md`; `_sources/site-extract.md` (linhas 1 a 70); `templates/edit-plan.md`; `knowledge/README.md`; `knowledge/platforms/README.md`; `knowledge/short-form-video/README.md`; `integrations/README.md`; `integrations/capcut.md`; `.claude/skills/edit-planning/SKILL.md` e regras `.claude/rules/*` (recebidas no contexto). Listei `projects/forma-digital/`, `knowledge/` e `integrations/`; `08-edit-plan.md` não existia. Não li `01-trends.md`, `00-client-audit.md`, `STATUS.md`, `knowledge/audio/README.md`, `integrations/elevenlabs.md`, `adapter-contract.md` nem os demais arquivos de `integrations/`.
- **trabalho realizado:** timeline plano a plano das 3 propostas (29 planos, ramos D6) com In–Out estimados, camadas e transições; tabela de ritmo; mapa de pontos de retenção; orçamento fala × cena nas duas variantes com folgas; **conferência independente das contagens do 07** (coincidem) e **dois riscos adicionais** (P1-C2 e P2-C1, folga de 0,2 s); totais do cenário de esticar cenas; seis opções (O1 a O6) para os conflitos de tempo; mapa de desvio entre corte e fala por cena; achados novos: (i) o CTA contatos tem S1/S2 incompatíveis com a ordem da fala (C-2), (ii) cortes ancorados mudam por variante D2, (iii) "seu objetivo" na tela contradiz "o objetivo" na fala institucional, (iv) as variações de gancho do roteiro não têm decupagem e a de P2 estoura os 3 s, (v) a Camada B não tem zona livre no quadro e conflita com "um bloco por plano", (vi) esmaecimento por opacidade gera tons fora da paleta, (vii) matriz de versões chega a 36 exportações brutas; legendas Camada A e B com temporização estimada; camadas de áudio; versões e versão silenciosa; conferência de cor; tabela de exportação com campos a preencher; fluxo manual assistido; checklist; 14 decisões ao ECD. Nada foi gerado, editado, chamado ou publicado.
- **skills aplicadas:** `edit-planning`, passos 1 a 7 (timeline fechando com as durações estimadas; pontos de retenção; cortes, transições e ritmo; legendas com temporização; camadas de áudio; exportação do brief ou `knowledge/platforms/`, senão `[A PESQUISAR]`; preenchimento do template com seções adicionais). A skill lista como pendentes as especificações por plataforma e a viabilidade de integração com CapCut; ambas ficam `[A PESQUISAR]`.
- **status:** NEEDS_INFO (parcial). Plano entregue como rascunho; montagem real depende de D1 a D6, de material gerado/gravado, das decisões ED-1 a ED-14 e da pesquisa de especificações.
- **entregáveis:** `/home/user/Site.FirmaDigital/AI-VIRAL-STUDIO/projects/forma-digital/08-edit-plan.md`
- **premissas:** (1) tempos tomados da decupagem e tratados como estimativa; (2) 0,4 s por palavra (hipótese do roteirista) para todas as estimativas de fala, sem pausas; (3) cortes secos entre planos como descrição da direção, sem afirmar efeito; (4) Camada B condicional; (5) timeline mestra + slots como organização proposta; (6) rótulos separados em R-D e R-E1 para a decisão do ECD não refazer a timeline; (7) a versão silenciosa mantém a timeline da narrada; (8) nenhuma ferramenta de edição ou de geração escolhida; (9) a legenda de estilo da Camada B segue o art bible (Inter, `#e9e9ed`, sem caixa nem sombra) como proposta.
- **pendências:** D1 a D6; ED-1 a ED-14 (em especial ED-1 Camada B, ED-2 conflitos de tempo, ED-3 CTA, ED-4 rótulo, ED-5 cortes por variante, ED-7 matriz de versões); D4 (chegada ao site); decupagem das variações de gancho; **[A PESQUISAR]**: especificações de exportação por plataforma (proporção, resolução, fps, codec, bitrate, duração e tamanho máximos, zonas seguras, loudness, perfil de cor), duração-alvo, janela de gancho, tempo mínimo de leitura, rotulagem de IA, regras publicitárias, licenças (Inter, trilha, SFX, voz), nomes dos botões Salvar/Compartilhar, efeitos de transição, formato de arquivo de legenda; ferramenta de edição (fluxo manual assistido); `scripts/validate.py` a rodar pelo ECD.
- **autoavaliação:**
  - ✘ Timeline fecha com a duração-alvo do brief: o brief não tem duração-alvo (`[A PESQUISAR]`); fecha com as durações estimadas do roteiro e da decupagem, e os conflitos de tempo estão explícitos com opções. Limitação externa.
  - ✔ Pontos de retenção da estratégia visíveis na timeline: tabela por bloco (gancho, promessa, desenvolvimento, virada, fechamento) com tempos e marcação em negrito das viradas principais; janela de gancho em segundos `[A PESQUISAR]`.
  - ✔ Legendas respeitam o roteiro: cues da Camada B e textos da Camada A copiados literalmente; nenhuma fala alterada; divergências fala × tela registradas, não corrigidas.
  - ✔ Especificações de exportação do brief ou de `knowledge/platforms/`, senão `[A PESQUISAR]`: base vazia; tabela de campos por plataforma sem nenhum valor afirmado.
  - ✔ Fluxo em editor de terceiros sem API confirmada entregue como plano manual: `integrations/capcut.md` não pesquisado; lista de cortes, texto-fonte de legendas, roteiro de montagem e checklist exportáveis.
  - ✔ Limites de atuação: não gerei nem editei mídia, não alterei roteiro nem direção, não afirmei recursos de software, não instruí outros especialistas (só pedidos de decisão e de pesquisa ao ECD).
  - ✘ Aprovabilidade: o plano não pode ser aprovado nem executado agora, por depender de D1 a D6, de material inexistente, de decisões ED-1 a ED-14 e de pesquisa de especificações (limitação externa).
