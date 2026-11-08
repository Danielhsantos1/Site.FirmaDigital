---
projeto: forma-digital
versão: 0.1
autor-agente: prompt-engineer
data: 2026-11-08
entradas-usadas: [04-direction.md, 05-art-bible.md, 03-script.md, 00-brief.v2.md, 00-inconsistencies-report.md, _sources/site-extract.md, templates/prompt-sheet.md, .claude/rules/*.md, .claude/skills/media-prompt-engineering/SKILL.md, knowledge/README.md, knowledge/prompts-image/README.md, knowledge/prompts-video/README.md, knowledge/consistency/README.md, integrations/README.md, integrations/veo.md, integrations/kling.md, integrations/runway.md]
status: rascunho   # todos os prompts NÃO EXECUTADO; formato genérico; direção, art bible e roteiro também são rascunho; condicional a D1 a D6
---

# Folha de prompts: forma-digital (P1, P2, P3 e CTA comum)

Tudo neste documento é **plano e texto de prompt**. Nenhuma imagem, vídeo ou áudio foi gerado. Nenhuma ferramenta foi chamada. **Todos os 29 prompts têm status `NÃO EXECUTADO`.** Nada aqui prevê como qualquer ferramenta vai interpretar o texto: a qualidade, a fidelidade de cor e a obediência às proibições são **desconhecidas** até teste (que não foi feito).

## Ferramentas-alvo e status de documentação

Nenhuma ferramenta-alvo foi definida pelo ECD nesta entrega. Verificação feita:

| Fonte | Situação em 2026-11-08 |
|---|---|
| `knowledge/prompts-image/README.md` | VAZIO (índice sem arquivos) |
| `knowledge/prompts-video/README.md` | VAZIO (índice sem arquivos) |
| `knowledge/consistency/README.md` | VAZIO (índice sem arquivos) |
| `integrations/veo.md`, `kling.md`, `runway.md` | Status "NÃO PESQUISADO"; todos os campos (entradas aceitas, limites, guia de prompt, consistência) estão `[A PESQUISAR]` |
| Gerador de imagem | Nenhum escolhido nem documentado |

Consequência (regra `no-fabrication.md`): **todos os prompts abaixo estão em "formato genérico, não específico de ferramenta"**. Não há sintaxe de ferramenta, nem parâmetros (ferramenta, modelo, proporção, resolução, duração, seed, referência de imagem, peso de negativo, etc.). Todo parâmetro é `[A PESQUISAR]`. Ferramentas **bloqueadas por falta de documentação**: todas (Veo, Kling, Runway e qualquer gerador de imagem).

"Negativo" neste documento é uma **lista descritiva do que evitar**, não campo ou sintaxe de ferramenta. Se a ferramenta futura não tiver campo de negativo, a conversão da lista em frases afirmativas é **[A PESQUISAR]**.

Idioma: corpo dos prompts em inglês (regra do projeto); textos em tela e rótulos em português do Brasil, entre aspas, em campo próprio.

## Como usar esta folha

- **Montagem do prompt (genérica):** `[BLK-ESTILO] + [BLK-PALETA] + [BLK-QUADRO] + [BLK-SEM-TEXTO] + parte específica do plano`. Os blocos são colados **literalmente** (seção "Bloco comum"), para que as descrições fixas do art bible não variem entre planos (R2). A parte específica já traz o hex dos elementos principais.
- **Duas variantes de texto:**
  - **Variante A (recomendada, HIPÓTESE):** o prompt pede quadro **sem texto**, e o texto em tela e os rótulos entram como **camada composta na edição** (R1, R5; RC4, RC5 do art bible). Motivo: o texto em tela exige grafia, acentos e fonte (Inter) exatos, e não há evidência de que uma ferramenta de geração os entregue; não testado.
  - **Variante B (não recomendada, só para teste):** acrescenta-se `[BLK-TEXTO-GERADO]` com o texto exato do campo "Texto em tela". Qualquer erro de grafia reprova o quadro.
- **Estados em vez de morph (HIPÓTESE):** onde a decupagem pede transformação (R10) ou acúmulo/sequência (R11), o campo "Estados" descreve os quadros inicial e final para gerar **como imagens separadas** e animar/cortar na edição. Se a ferramenta gerar clipe, o campo "Movimento" traz a descrição em inglês. Qual saída (imagem ou clipe) é a pretendida: **[A PESQUISAR]**; não decidido.
- **Duração de cada plano** é a da decupagem (referência para a edição). **Não é parâmetro de ferramenta.**
- **Rótulo "ilustrativo":** a coluna "Rótulo" marca `[direção]` (previsto em `04-direction.md`) ou `[proposta E1]` (extensão recomendada em `05-art-bible.md`, E1; decisão do ECD pendente). O texto do rótulo nos planos estendidos é **proposta minha** (usar o rótulo da própria peça); ver Lacunas.

## Bloco comum (reutilizável)

### BLK-ESTILO
```
Flat 2D graphic design, vector-like, solid fills and clean outlines only. Minimal diagram aesthetic made of simple repeatable shapes. One single line thickness and one single corner radius used consistently across every shape. No drop shadows, no glow, no gradients, no textures, no 3D, no photographic elements. Generous empty space. Exactly one clear focal element.
```

### BLK-PALETA
```
Solid, uniform background color #161826 across the entire frame. Cards, blocks, fields and columns filled with #232532. Main outlines in #e9e9ed. Approval marks, the active node, the closed outline and the progress indicator in accent color #9184d9. Secondary highlight, only if needed, in #a7a1db. No other colors: no pure white, no pure black, no extra grays, no status colors (no red, green or yellow).
```
Base: hex do site (`_sources/site-extract.md`, linha 7). Papéis de cada cor = PROPOSTA do art bible (sem base no site). Fidelidade do hex após geração/exportação: **[A PESQUISAR]** (aprovar sobre o quadro exportado).

### BLK-QUADRO
```
Vertical frame composition. Keep every element away from the frame edges with equal margins. Keep the bottom strip of the frame empty and clean. Keep the top third free whenever a text block is indicated below. Center the main element on a single vertical axis.
```
Proporção exata, resolução e zonas seguras por plataforma: **[A PESQUISAR]**.

### BLK-SEM-TEXTO (variante A)
```
Do not render any text, letters, digits, character-like marks, captions or watermarks anywhere in the frame. Leave clean, empty areas where text will be composed later.
```

### BLK-TEXTO-GERADO (variante B, só teste)
```
Render this on-screen text exactly, character by character, with correct Portuguese accents, in a clean sans-serif font similar to Inter, color #e9e9ed, in a single text block: «<TEXTO EM TELA DO PLANO>»
```
(Substituir `<TEXTO EM TELA DO PLANO>` pelo campo do plano. Substitui o `[BLK-SEM-TEXTO]`.)

### BLK-EVITAR (lista descritiva, reutilizável em todos os planos)
- Fotografia, realismo, cenário, textura, grão, ruído, vinheta, 3D, sombra projetada, brilho, gradiente, partículas, lens flare, glitch, zoom dramático, rotação decorativa, balanço.
- **Qualquer pessoa, rosto, mão, corpo, silhueta, avatar ou personagem** (D3 pendente; RC14). Nenhuma semelhança com Daniel ou com qualquer pessoa real.
- Texto, letras, dígitos ou símbolos parecidos com caracteres (variante A); código com caracteres legíveis (R9).
- Números, moeda, símbolos monetários, porcentagem, datas, hora legível, gráficos com eixo ou valores (R4; RC11).
- Logotipos, ícones ou aparência de produtos de terceiros: apps de mensagem, GitHub, navegadores, planilhas, redes sociais, plataformas; barra de menus, abas ou botões no estilo de um produto (R3, R8; RC12).
- Tela real, captura de tela, dados reais, nome de cliente, "03 sistemas", SaaS de contratos, estudos de caso do site.
- Nome de marca, logotipo próprio, @, URL, telefone, e-mail, "link na bio" (D1, D4; RC13).
- Cores fora das cinco da paleta, incluindo branco e preto puros, cinzas avulsos e cores de status (RC2).
- Elementos "virais" ou de urgência: selos, explosões, setas chamativas, faíscas.
- Mais de um foco por plano; elementos decorativos que preencham o espaço vazio.
- Referência a filmes, artistas, perfis ou estilos "tipo X" (nenhuma referência externa registrada).

### Elementos fixos reutilizáveis (descrições para colar nos planos)
- **EL-NOS** (CEN-03): `Four identical circles (nodes), same diameter, stacked in one single vertical column, perfectly aligned, equal spacing, fixed order from top to bottom. Empty state: outline only in #e9e9ed with no fill. Active state: filled #9184d9. Approved state: outline in #e9e9ed plus one single simple check mark in #9184d9.`
- **EL-VISTO** (marca de aprovação, RC9): `One single simple check mark, same line thickness and rounded line ends as all other shapes, color #9184d9.`
- **EL-CARTAO** (CEN-04/05): `Rounded rectangle card filled #232532, same corner radius as every other shape, with no content, no text and no marks.`
- **EL-FOLHA** (CEN-04): `Tall rounded rectangle sheet filled #232532 containing a few horizontal bars of different lengths in #e9e9ed outline or in #161826 fill, standing for text lines. The bars are solid abstract shapes, never letters.`
- **EL-GRADE** (CEN-06): `Generic grid of rounded cells filled #232532 separated by thin #161826 gaps; each cell contains one or two short solid horizontal bars (abstract, never letters or digits).`

## Ordem de geração (proposta, HIPÓTESE; sem ferramenta documentada)

Ordem pensada para fixar primeiro os elementos que atravessam planos (R2, R11) e só depois os planos que os reutilizam. Se a ferramenta futura tiver técnica de consistência, ela é **[A PESQUISAR]**; sem ela, a recomendação é gerar os âncoras uma vez e **compor na edição** (hipótese do art bible, não testada).

| Ordem | Grupo | Planos | Observação |
|---|---|---|---|
| 0 | Âncoras | Fundo liso (CEN-01); marca de aprovação única (EL-VISTO); 4 nós (EL-NOS) nos 3 estados; retângulo-base (EL-CARTAO/EL-FOLHA) | Não são planos da decupagem; ficam como âncoras de consistência. Gerar ou desenhar uma vez; conferir RC1, RC6, RC8, RC9 |
| 1 | P2 (recomendada no roteiro, hipótese) | P2-C1-S1, P2-C5-S2 (nós), depois P2-C2-S1 a P2-C5-S1 | P2-C1-S1 e P2-C5-S2 devem ser sobreponíveis (RC6) |
| 2 | P1 | P1-C5-S1/S2 (mesmos nós de P2), depois P1-C1 a P1-C4 | P1-C5 reutiliza a disposição de P2 |
| 3 | P3 | P3-C1-S1 a P3-C5-S1 | Estados de grade, campos e colunas separados (R10) |
| 4 | CTA comum | Px-C6a-S1/S2, Px-C6b-S1 | Quadro quase só de texto; geração dispensável (hipótese), ver notas |

## Prompts (plano, prompt, evitar, parâmetros, consistência, risco)

Convenções por plano: **Saída** = estado(s)/movimento; **Texto em tela** = camada de edição recomendada (variante A); **Rótulo** = camada fixa; **Evitar** = `[BLK-EVITAR]` mais o específico; **Parâmetros** = `[A PESQUISAR]` (todos). **Status** = `NÃO EXECUTADO` em todos. Riscos globais, valem para todos os planos e não são repetidos: R6, R7, R14 (sem pessoa nem voz) e R13 (rotulagem de IA) e R12 (zonas seguras), todos hipóteses da direção.

---

### P1. O "ajustezinho" que vira retrabalho

#### P1-C1-S1
- **Objetivo:** card de tipografia que reconhece a situação (decupagem: texto no centro, rótulo no canto inferior; sem figura).
- **Prompt (EN):** `[BLK-ESTILO] [BLK-PALETA] [BLK-QUADRO] [BLK-SEM-TEXTO]` + `A completely plain, empty frame in solid #161826. No shapes, no decoration. The center of the frame is left clean for a single centered text block, and a small clean area is kept near the bottom for a tiny label.`
- **Saída / movimento:** quadro estático liso. Animação de entrada do texto (texto aparece, reticências por último) é feita na edição.
- **Texto em tela (camada):** "Só um ajustezinho..."
- **Rótulo:** "Situação ilustrativa" `[direção]`, canto inferior.
- **Evitar:** `[BLK-EVITAR]`; qualquer forma além do fundo.
- **Consistência:** CEN-01 e CEN-02; Inter, `#e9e9ed`, um bloco de texto; RC1, RC3, RC4.
- **Riscos:** R1, R5. Geração dispensável (hipótese): é fundo liso mais texto composto.
- **Parâmetros:** [A PESQUISAR]. **Status:** NÃO EXECUTADO.

#### P1-C2-S1
- **Objetivo:** mostrar a repetição sem cliente (bloco-base ao centro; cartão "pedido" sem texto encaixa).
- **Prompt (EN):** `[BLK-ESTILO] [BLK-PALETA] [BLK-QUADRO] [BLK-SEM-TEXTO]` + `At the center, one simple abstract base structure: a wide rounded rectangle block filled #232532 with an outline in #e9e9ed. Entering from the left side, one small rounded card (EL-CARTAO, filled #232532, outlined #e9e9ed) is about to snap into the top of the block; no content on the card. Nothing else in the frame. The top third is empty for a short text line.`
- **Estados / movimento:** inicial: bloco sozinho. Final: cartão encaixado. Motion (EN): `the small card slides in from the left and snaps into the block; simple linear entry, no rotation, no bounce.`
- **Texto em tela (camada):** "Mais um."
- **Rótulo:** "Situação ilustrativa" `[proposta E1]` (texto proposto; ver Lacunas).
- **Evitar:** `[BLK-EVITAR]`; balão de conversa, tela de mensagem, pessoa pedindo, texto no cartão.
- **Consistência:** CEN-05; cartão e bloco com o mesmo raio e linha dos demais; RC8, RC14.
- **Riscos:** R1, R2, R5, R11.
- **Parâmetros:** [A PESQUISAR]. **Status:** NÃO EXECUTADO.

#### P1-C2-S2
- **Objetivo:** o conjunto cresce além do bloco; indicador de progresso que nunca fecha.
- **Prompt (EN):** `[BLK-ESTILO] [BLK-PALETA] [BLK-QUADRO] [BLK-SEM-TEXTO]` + `The same base block as in the previous shot, now with many identical small rounded cards (filled #232532, outlined #e9e9ed, no content) snapped on and stacked around it so the whole cluster grows past the original block and tends to fill the frame. In the background, one large circular progress ring drawn as an open arc in #9184d9 that does not close (a visible gap remains). The top third is kept empty for a short text line.`
- **Estados / movimento:** final: cluster grande e anel aberto. Motion (EN): `more cards snap on one after another and accumulate; the ring arc keeps turning without ever completing; no rotation of the cards.`
- **Texto em tela (camada):** "E mais outro."
- **Rótulo:** "Situação ilustrativa" `[proposta E1]`, mesma posição de S1.
- **Evitar:** `[BLK-EVITAR]`; anel fechado; porcentagem no anel; cartões com texto.
- **Consistência:** mesmos cartões e bloco de S1 (tamanho relativo, cor, linha); eixo vertical; RC8, RC16.
- **Riscos:** R1, R2, R5, R11 (acúmulo pode perder ordem; sem contagem exigida).
- **Parâmetros:** [A PESQUISAR]. **Status:** NÃO EXECUTADO.

#### P1-C3-S1
- **Objetivo:** virada visual de bagunça para ordem (cartões se alinham em folha ilustrativa).
- **Prompt (EN):** `[BLK-ESTILO] [BLK-PALETA] [BLK-QUADRO] [BLK-SEM-TEXTO]` + `One tall rounded sheet (EL-FOLHA) filled #232532, centered, containing neatly aligned horizontal bars (solid abstract shapes, no letters) in even rows with even spacing, all on the same vertical axis. Order and symmetry replace the previous pile of cards. Nothing else in the frame.`
- **Estados / movimento:** estado A: cartões desordenados (reaproveitar P1-C2-S2); estado B: folha alinhada. Montar como corte entre estados (R10). Motion (EN, se clipe): `scattered cards slide into rows and merge into the sheet.`
- **Texto em tela (camada):** nenhum.
- **Rótulo:** "Situação ilustrativa" `[proposta E1]`.
- **Evitar:** `[BLK-EVITAR]`; linhas que pareçam letras ou lorem ipsum.
- **Consistência:** CEN-04 (mesma folha reutilizada em P1-C3-S2, P1-C4-S1); eixo vertical.
- **Riscos:** R2, R5, R10.
- **Parâmetros:** [A PESQUISAR]. **Status:** NÃO EXECUTADO.

#### P1-C3-S2
- **Objetivo:** plano de detalhe do topo da folha, ancorando a declaração do negócio.
- **Prompt (EN):** `[BLK-ESTILO] [BLK-PALETA] [BLK-QUADRO] [BLK-SEM-TEXTO]` + `Close-up of the top part of the same sheet (filled #232532, same corner radius), cropped so only the upper portion is visible, with a few aligned abstract bars below. A large clean empty area at the upper part of the frame, with high contrast against #161826, is kept free for a text block.`
- **Estados / movimento:** estático; texto entra na edição.
- **Texto em tela (camada):** "Escopo combinado por escrito, antes de começar."
- **Rótulo:** "Situação ilustrativa" `[proposta E1]`.
- **Evitar:** `[BLK-EVITAR]`; qualquer assinatura, selo ou carimbo com texto.
- **Consistência:** mesma folha de P1-C3-S1; texto sobre área limpa (regra de composição 1).
- **Riscos:** R1, R5.
- **Parâmetros:** [A PESQUISAR]. **Status:** NÃO EXECUTADO.

#### P1-C4-S1
- **Objetivo:** primeiro apoio, "fechado": contorno fechado ao redor da folha.
- **Prompt (EN):** `[BLK-ESTILO] [BLK-PALETA] [BLK-QUADRO] [BLK-SEM-TEXTO]` + `The same sheet (EL-FOLHA) centered, now enclosed by a closed rounded rectangular outline in accent #9184d9, with even clear space between the sheet and the outline. The outline is a single continuous closed line.`
- **Estados / movimento:** inicial: folha sem contorno; final: contorno fechado. Motion (EN): `the outline draws itself around the sheet until it closes.`
- **Texto em tela (camada):** "Pacotes fechados"
- **Rótulo:** "Situação ilustrativa" `[proposta E1]`.
- **Evitar:** `[BLK-EVITAR]`; cadeado, cifrão, selo, "etiqueta de preço".
- **Consistência:** CEN-05; contorno em acento (estado "fechado"); mesma folha.
- **Riscos:** R2, R4, R5.
- **Parâmetros:** [A PESQUISAR]. **Status:** NÃO EXECUTADO.

#### P1-C4-S2
- **Objetivo:** segundo apoio: relógio genérico com traço riscado (sem moeda, valor ou número).
- **Prompt (EN):** `[BLK-ESTILO] [BLK-PALETA] [BLK-QUADRO] [BLK-SEM-TEXTO]` + `On the left, one generic clock icon drawn only with the project's single line style in #e9e9ed: a circle with two plain hands and no tick marks, no numerals and no readable time. Across it, one diagonal strike-through line in #e9e9ed. The right side of the frame is left clean for a text column, and a small clean area at the bottom for a label.`
- **Estados / movimento:** inicial: relógio; final: relógio riscado. Motion (EN): `the strike-through line is drawn across the clock.`
- **Texto em tela (camada):** "Sem cobrança por hora perdida em ajustes"
- **Rótulo:** "Modelo declarado pelo negócio" `[direção]`, tratado como segundo texto de nível secundário (E2, proposta; função pendente). Se E1 valer, também "Situação ilustrativa": **conflito de posição único no canto inferior, pendência ao ECD**.
- **Evitar:** `[BLK-EVITAR]`; numerais, ponteiros apontando hora legível, cifrão, moeda.
- **Consistência:** ícone na mesma linha e cantos dos demais; riscado em `#e9e9ed` (proposta; art bible deixa "`#e9e9ed` ou acento, fixar em revisão").
- **Riscos:** R1, R4, R5.
- **Parâmetros:** [A PESQUISAR]. **Status:** NÃO EXECUTADO.

#### P1-C5-S1
- **Objetivo:** apresentar a estrutura de 4 (quatro nós vazios, sem nomes).
- **Prompt (EN):** `[BLK-ESTILO] [BLK-PALETA] [BLK-QUADRO] [BLK-SEM-TEXTO]` + `EL-NOS in the empty state for all four nodes: four identical circles, outline only in #e9e9ed, no fill, stacked in one vertical column, equal spacing, perfectly aligned, centered. No labels beside the nodes. The top of the frame is kept empty.`
- **Estados / movimento:** final: 4 nós vazios. Motion (EN): `the four nodes appear one after another from top to bottom.`
- **Texto em tela (camada):** nenhum.
- **Rótulo:** "Situação ilustrativa" `[proposta E1]`.
- **Evitar:** `[BLK-EVITAR]`; número de nós diferente de 4; nomes ou números nos nós; linhas de conexão não previstas.
- **Consistência:** CEN-03; **disposição idêntica** a P2-C1-S1 e P2-C5-S2 (RC6); sobrepor quadros.
- **Riscos:** R2, R5, R11 (contagem de 4).
- **Parâmetros:** [A PESQUISAR]. **Status:** NÃO EXECUTADO.

#### P1-C5-S2
- **Objetivo:** ligar retrabalho à aprovação por etapa: nós recebem marca um a um.
- **Prompt (EN):** `[BLK-ESTILO] [BLK-PALETA] [BLK-QUADRO] [BLK-SEM-TEXTO]` + `EL-NOS with all four nodes in the approved state, in the exact same column, size, spacing and position as the previous shot: each circle outlined in #e9e9ed with one identical check mark (EL-VISTO) in #9184d9. The top of the frame is kept free for a fixed text block.`
- **Estados / movimento:** estados: 0, 1, 2, 3 e 4 marcas (montar por camadas na edição, R11). Motion (EN): `check marks appear one at a time, top to bottom, one per node.`
- **Texto em tela (camada):** "4 etapas · aprovação em cada uma"
- **Rótulo:** "Situação ilustrativa" `[proposta E1]`.
- **Evitar:** `[BLK-EVITAR]`; marcas diferentes entre si; cores de status.
- **Consistência:** CEN-03; RC6, RC9; mesmo visto único em toda a peça.
- **Riscos:** R1, R2, R5, R11.
- **Parâmetros:** [A PESQUISAR]. **Status:** NÃO EXECUTADO.

---

### P2. Quatro etapas com aprovação

Disposição fixa (direção): linha vertical, de cima para baixo: Escopo, Protótipo, Construção, Publicação. Os **nomes das etapas não entram nos nós** gerados (camada de edição; ver P2-C1-S1).

#### P2-C1-S1
- **Objetivo:** processo em uma linha: 4 nós acendem em sequência, cada um seguido de marca de aprovação.
- **Prompt (EN):** `[BLK-ESTILO] [BLK-PALETA] [BLK-QUADRO] [BLK-SEM-TEXTO]` + `EL-NOS: four identical circles stacked in one vertical column, equal spacing, centered, shown at the moment all four are approved: each circle outlined in #e9e9ed with one identical check mark (EL-VISTO) in #9184d9. The top third of the frame is kept empty for a text block.`
- **Estados / movimento:** estados: vazio, ativo (preenchido `#9184d9`), aprovado, por nó. Motion (EN): `each node lights up in accent #9184d9 in sequence from top to bottom and is followed by its check mark.`
- **Texto em tela (camada):** "4 etapas. Aprovação em cada uma."
- **Rótulo:** "Ilustrativo" `[proposta E1]` (a direção propõe rótulo em P2-C2, C3 e C5; C1 é extensão).
- **Evitar:** `[BLK-EVITAR]`; mais ou menos de 4 nós; nomes nos nós.
- **Consistência:** **âncora de P2**; CEN-03; RC6 com P1-C5 e P2-C5-S2; RC9.
- **Riscos:** R1, R2, R5, R11.
- **Parâmetros:** [A PESQUISAR]. **Status:** NÃO EXECUTADO.

#### P2-C2-S1
- **Objetivo:** etapa 1: o nó 1 se amplia e vira lista ilustrativa com três marcadores genéricos.
- **Prompt (EN):** `[BLK-ESTILO] [BLK-PALETA] [BLK-QUADRO] [BLK-SEM-TEXTO]` + `One tall rounded sheet (EL-FOLHA) filled #232532, centered, showing a list: three identical small round bullet markers in #9184d9, each followed by one solid horizontal bar (abstract, never letters). Clean empty space above the sheet for a title line, and a small clean area at the bottom for a label.`
- **Estados / movimento:** estado A: nó 1 (de P2-C1); estado B: lista. Montar como corte (R10). Motion (EN, se clipe): `the first node expands into the list sheet.`
- **Texto em tela (camada):** "1 · Escopo"
- **Rótulo:** "Ilustrativo" `[direção]`.
- **Evitar:** `[BLK-EVITAR]`; texto legível nas barras; número ou data; assinatura.
- **Consistência:** CEN-04; mesma folha base de P1-C3 e dos planos seguintes; "1 ·" pode ser destacado em acento (proposta do art bible, na edição).
- **Riscos:** R1, R2, R4, R5, R10.
- **Parâmetros:** [A PESQUISAR]. **Status:** NÃO EXECUTADO.

#### P2-C2-S2
- **Objetivo:** ancorar "por escrito": selo/linha de "registrado" no canto da lista.
- **Prompt (EN):** `[BLK-ESTILO] [BLK-PALETA] [BLK-QUADRO] [BLK-SEM-TEXTO]` + `Close-up of the corner of the same list sheet (filled #232532). In that corner, one small plain seal: a simple circle outlined in #9184d9 containing one check mark (EL-VISTO), with no text and no date. Clean space at the top for a text block.`
- **Estados / movimento:** final: selo no canto. Motion (EN): `the seal slides into the corner of the sheet.`
- **Texto em tela (camada):** "Tudo registrado por escrito"
- **Rótulo:** "Ilustrativo" `[proposta E1]`, mesma posição de S1 (a lista persiste em dois planos seguidos).
- **Evitar:** `[BLK-EVITAR]`; valor numérico, data, assinatura, carimbo com texto; selo de "garantia".
- **Consistência:** o selo usa o mesmo visto único (RC9); mesma folha de S1.
- **Riscos:** R1, R4, R5.
- **Parâmetros:** [A PESQUISAR]. **Status:** NÃO EXECUTADO.

#### P2-C3-S1
- **Objetivo:** etapa 2; virada visual: lista vira esboço de página (wireframe com blocos genéricos).
- **Prompt (EN):** `[BLK-ESTILO] [BLK-PALETA] [BLK-QUADRO] [BLK-SEM-TEXTO]` + `A vertical page wireframe, centered: one tall rounded rectangle outlined in #e9e9ed, containing three empty block shapes filled #232532: a wide header block at the top, a large image block in the middle and a text block at the bottom. The blocks are completely empty: no text, no icon, no picture. Clean space above for a title line and a small clean area at the bottom for a label.`
- **Estados / movimento:** estado A: lista de P2-C2; estado B: wireframe. Montar como corte (R10). Motion (EN, se clipe): `the list rearranges into the three blocks of the wireframe.`
- **Texto em tela (camada):** "2 · Protótipo"
- **Rótulo:** "Ilustrativo" `[direção]`.
- **Evitar:** `[BLK-EVITAR]`; barra de menu, botão, aparência de navegador/CMS; lorem ipsum; imagem dentro do bloco de imagem; cinza novo (usar `#232532`).
- **Consistência:** CEN-04; mesmo raio e linha; blocos vazios; a direção diz "blocos cinza", traduzido para `#232532` (art bible).
- **Riscos:** R1, R2, R3, R5, R10.
- **Parâmetros:** [A PESQUISAR]. **Status:** NÃO EXECUTADO.

#### P2-C3-S2
- **Objetivo:** o wireframe ganha marca de aprovação; blocos continuam vazios.
- **Prompt (EN):** `[BLK-ESTILO] [BLK-PALETA] [BLK-QUADRO] [BLK-SEM-TEXTO]` + `The same wireframe as in the previous shot, same size and position, blocks still completely empty, with one check mark (EL-VISTO, #9184d9) placed in the upper corner of the wireframe. Clean space above for a text block.`
- **Estados / movimento:** final: wireframe com visto. Motion (EN): `the check mark appears in the corner.`
- **Texto em tela (camada):** "Estrutura e visual aprovados antes do conteúdo final"
- **Rótulo:** "Ilustrativo" `[proposta E1]`, mesma posição.
- **Evitar:** `[BLK-EVITAR]`; qualquer conteúdo final dentro dos blocos; visto diferente do padrão.
- **Consistência:** idêntico a P2-C3-S1 exceto o visto; RC9.
- **Riscos:** R1, R2, R5.
- **Parâmetros:** [A PESQUISAR]. **Status:** NÃO EXECUTADO.

#### P2-C4-S1
- **Objetivo:** etapa 3, parte 1: o wireframe recua; surge bloco com linhas curtas abstratas (sugestão de código, sem caracteres).
- **Prompt (EN):** `[BLK-ESTILO] [BLK-PALETA] [BLK-QUADRO] [BLK-SEM-TEXTO]` + `Two elements side by side on the same horizontal alignment, vertical axis kept: on the left, the same wireframe (outlined #e9e9ed, empty blocks #232532) shown smaller; on the right, one rounded rectangle block filled #232532 containing several short solid horizontal bars of varying lengths in #a7a1db and #e9e9ed, with indentation steps, standing for code. The bars are plain shapes with no characters at all. Clean space at the top for a text block.`
- **Estados / movimento:** final: wireframe pequeno + bloco de linhas. Motion (EN): `the wireframe moves back and shrinks while the bar block enters from the right.`
- **Texto em tela (camada):** "3 · Construção" / "Código versionado" (sem "GitHub", conforme direção).
- **Rótulo:** "Ilustrativo" `[proposta E1]`.
- **Evitar:** `[BLK-EVITAR]`; caracteres, chaves, tags, símbolos de programação, cores de sintaxe, logotipo do GitHub, ícone de ramificação com aparência de produto.
- **Consistência:** CEN-04; mesmo wireframe; barras só nas cores da paleta.
- **Riscos:** R1, R2, R5, R8, R9.
- **Parâmetros:** [A PESQUISAR]. **Status:** NÃO EXECUTADO.

#### P2-C4-S2
- **Objetivo:** etapa 3, parte 2: cópia do wireframe desliza para uma área de teste.
- **Prompt (EN):** `[BLK-ESTILO] [BLK-PALETA] [BLK-QUADRO] [BLK-SEM-TEXTO]` + `Two areas side by side: on the left, the original wireframe (outlined #e9e9ed, empty blocks #232532); on the right, one rounded rectangular area outlined in #9184d9 with a dashed or plain frame, containing a copy of the same wireframe at the same relative size. The right area has no text, no address bar and no browser parts. Clean space at the top for a text block.`
- **Estados / movimento:** final: cópia dentro da área. Motion (EN): `a copy of the wireframe slides from the left element into the right area.`
- **Texto em tela (camada):** "Ambiente de teste"
- **Rótulo:** "Ilustrativo" `[proposta E1]`.
- **Evitar:** `[BLK-EVITAR]`; URL, navegador, abas, "localhost"; texto "Teste" gerado (é camada).
- **Consistência:** CEN-04; origem à esquerda e destino à direita; mesmo wireframe.
- **Riscos:** R1, R2, R3, R5.
- **Parâmetros:** [A PESQUISAR]. **Status:** NÃO EXECUTADO.

#### P2-C5-S1
- **Objetivo:** etapa 4, parte 1: wireframe com cadeado genérico e barra de endereço vazia.
- **Prompt (EN):** `[BLK-ESTILO] [BLK-PALETA] [BLK-QUADRO] [BLK-SEM-TEXTO]` + `The same wireframe, centered. At its top, one empty rounded address bar shape filled #232532 with no text inside, and at its left end one generic padlock icon drawn only with the project's single line style in #9184d9 (simple closed body and simple shackle, no keyhole detail, no brand traits). Clean space above for a text block and a small clean area at the bottom for a label.`
- **Estados / movimento:** final: wireframe + barra + cadeado. Motion (EN): `the padlock appears; no camera movement.`
- **Texto em tela (camada):** "4 · Publicação" / "Domínio · HTTPS"
- **Rótulo:** "Ilustrativo" `[direção]`.
- **Evitar:** `[BLK-EVITAR]`; texto na barra; URL; "https"; aparência de navegador real (botões, abas); semelhança com ícone de produto.
- **Consistência:** CEN-04; ícone na mesma linha e cantos; barra no topo do wireframe.
- **Riscos:** R1, R2, R3, R5, R8.
- **Parâmetros:** [A PESQUISAR]. **Status:** NÃO EXECUTADO.

#### P2-C5-S2
- **Objetivo:** fechar o caminho: quatro marcas concluídas na linha de nós (retorno da composição de P2-C1).
- **Prompt (EN):** `[BLK-ESTILO] [BLK-PALETA] [BLK-QUADRO] [BLK-SEM-TEXTO]` + `EL-NOS with all four nodes in the approved state, each circle outlined in #e9e9ed with one identical check mark (EL-VISTO) in #9184d9, in exactly the same column, size, spacing and position as the first shot of this piece. The top of the frame is kept free for a text block.`
- **Estados / movimento:** final: 4 vistos. Motion (EN): `the fourth check mark appears last and completes the set.`
- **Texto em tela (camada):** "Revisão final"
- **Rótulo:** "Ilustrativo" `[proposta E1]`.
- **Evitar:** `[BLK-EVITAR]`; variação de posição ou de contagem.
- **Consistência:** **sobreposição obrigatória** com P2-C1-S1 e P1-C5-S2 (RC6, RC9); reutilizar o mesmo ativo.
- **Riscos:** R1, R2, R5, R11.
- **Parâmetros:** [A PESQUISAR]. **Status:** NÃO EXECUTADO.

---

### P3. Da planilha ao painel

Todo o conteúdo é **genérico e fictício**. Linhas mostram barras abstratas, sem dígitos. Rótulo base da peça: "Exemplo fictício, ilustrativo". Três cabeçalhos/campos/colunas (RC7).

#### P3-C1-S1
- **Objetivo:** gancho: grade de planilha genérica preenche o quadro; texto sobre faixa de contraste.
- **Prompt (EN):** `[BLK-ESTILO] [BLK-PALETA] [BLK-QUADRO] [BLK-SEM-TEXTO]` + `EL-GRADE: a generic grid of rounded cells filled #232532 with thin #161826 gaps, filling most of the frame. Each cell holds one or two short solid horizontal bars (abstract, no letters, no digits). The grid has no toolbar, no menu, no column letters, no row numbers, no tabs. A horizontal band is left clean across the upper third as a contrast area for a text block, using only #161826 or #232532 for that band.`
- **Estados / movimento:** final: grade completa. Motion (EN): `the grid builds up cell by cell.`
- **Texto em tela (camada):** "Tem processo que mora numa planilha."
- **Rótulo:** "Exemplo fictício, ilustrativo" `[proposta E1]` (o roteiro exige rótulo só em C2 a C4; texto proposto; ver Lacunas).
- **Evitar:** `[BLK-EVITAR]`; cabeçalhos A, B, C; números de linha; ícone ou aparência de planilha de terceiros; faixa em cor nova (a direção diz "faixa de contraste": usar só cores da paleta).
- **Consistência:** CEN-06; célula com o mesmo raio e linha.
- **Riscos:** R1, R2, R3, R4, R5.
- **Parâmetros:** [A PESQUISAR]. **Status:** NÃO EXECUTADO.

#### P3-C2-S1
- **Objetivo:** grade com três cabeçalhos genéricos; mostrar a dispersão do exemplo fictício.
- **Prompt (EN):** `[BLK-ESTILO] [BLK-PALETA] [BLK-QUADRO] [BLK-SEM-TEXTO]` + `EL-GRADE, centered, with exactly three header cells aligned along the top row, filled #232532 and outlined #e9e9ed, each header cell empty (no text). Below them, rows of cells with short solid bars (abstract, no letters, no digits). Exactly three columns. Small clean area at the bottom for a label.`
- **Estados / movimento:** estados: 0, 1, 2, 3 cabeçalhos acesos (acento `#9184d9` no contorno). Motion (EN): `the three header cells light up one after another, left to right, with an accent outline.`
- **Texto em tela (camada):** "Pedido · Status · Prazo" (cada palavra sobre o respectivo cabeçalho; os três cabeçalhos são texto composto, **hipótese** para evitar erro de grafia). Rótulo na camada.
- **Rótulo:** "Exemplo fictício, ilustrativo" `[direção]`.
- **Evitar:** `[BLK-EVITAR]`; mais ou menos de 3 colunas; letras de coluna; dados nas células.
- **Consistência:** CEN-06; RC7 (contagem 3).
- **Riscos:** R1, R2, R3, R4, R5, R11.
- **Parâmetros:** [A PESQUISAR]. **Status:** NÃO EXECUTADO.

#### P3-C2-S2
- **Objetivo:** abas em cascata atrás da grade (ideia de "outra aba"), sem nomes legíveis.
- **Prompt (EN):** `[BLK-ESTILO] [BLK-PALETA] [BLK-QUADRO] [BLK-SEM-TEXTO]` + `The same grid as in the previous shot, centered, same size and position. Behind it, three or four identical copies of the grid frame are stacked in a cascade offset toward the lower right corner, each offset by the same step, filled #232532 and outlined #e9e9ed. The cascade sheets show no tab names, no text and no content. Wider framing than the previous shot. Small clean area at the bottom for a label.`
- **Estados / movimento:** final: grade + cascata. Motion (EN): `the cascade sheets appear one after another behind the main grid, toward the lower right.`
- **Texto em tela (camada):** nenhum (rótulo mantido).
- **Rótulo:** "Exemplo fictício, ilustrativo" `[direção]`.
- **Evitar:** `[BLK-EVITAR]`; abas com lingueta e texto; nomes de aba; contagem exagerada (sem sugerir estatística).
- **Consistência:** CEN-06; grade principal idêntica à de S1.
- **Riscos:** R2, R3, R5, R11.
- **Parâmetros:** [A PESQUISAR]. **Status:** NÃO EXECUTADO.

#### P3-C3-S1
- **Objetivo:** virada visual: a grade se dissolve e as colunas viram três campos empilhados.
- **Prompt (EN):** `[BLK-ESTILO] [BLK-PALETA] [BLK-QUADRO] [BLK-SEM-TEXTO]` + `Three input fields stacked vertically and centered, identical in width and height with equal spacing: each a wide rounded rectangle filled #232532 and outlined #e9e9ed, completely empty (no text, no cursor, no placeholder). Nothing else in the frame.`
- **Estados / movimento:** estado A: grade (P3-C2-S1); estado B: três campos. **Planejar como corte entre estados ou montagem na edição** (R10). Motion (EN, se clipe): `the three columns of the grid detach and re-form as three stacked fields.`
- **Texto em tela (camada):** nenhum.
- **Rótulo:** "Exemplo fictício, ilustrativo" `[direção, C3]`.
- **Evitar:** `[BLK-EVITAR]`; mais ou menos de 3 campos; ícones de formulário de terceiros.
- **Consistência:** CEN-06; eixo vertical centralizado; mesmo estado "vazio" (contorno).
- **Riscos:** R2, R3, R5, R10.
- **Parâmetros:** [A PESQUISAR]. **Status:** NÃO EXECUTADO.

#### P3-C3-S2
- **Objetivo:** formulário com três campos e botão sem texto; campos se preenchem com barras; registro novo aparece.
- **Prompt (EN):** `[BLK-ESTILO] [BLK-PALETA] [BLK-QUADRO] [BLK-SEM-TEXTO]` + `One illustrative form centered on a vertical axis: three identical stacked fields (rounded rectangles filled #232532, outlined #e9e9ed), each now containing one short solid bar in #e9e9ed standing for filled content (no letters, no digits). Under the fields, one plain rounded button shape filled #9184d9 with no text and no icon. To one side of the button, one new small rounded card (EL-CARTAO) appears as the new record. The top is kept clean for a text block; small clean area at the bottom for a label.`
- **Estados / movimento:** estados: campos vazios, campos preenchidos, botão pressionado (variação sutil de preenchimento em `#a7a1db`, se necessário), registro novo. Motion (EN): `bars fill the fields one by one, the button is pressed, then the new card appears.`
- **Texto em tela (camada):** "Formulário para registrar" (os rótulos de campo "Pedido", "Status", "Prazo" da direção, se mostrados, também como camada).
- **Rótulo:** "Exemplo fictício, ilustrativo" `[direção]`.
- **Evitar:** `[BLK-EVITAR]`; texto no botão; cursor de mouse com aparência de sistema; mão pressionando; marcas de checkbox de produto.
- **Consistência:** CEN-06; mesmos 3 campos de S1; botão sem marca.
- **Riscos:** R1, R2, R3, R5, R10, R11.
- **Parâmetros:** [A PESQUISAR]. **Status:** NÃO EXECUTADO.

#### P3-C4-S1
- **Objetivo:** o registro do formulário viaja e vira cartão (exceção horizontal: esquerda para direita, só neste plano).
- **Prompt (EN):** `[BLK-ESTILO] [BLK-PALETA] [BLK-QUADRO] [BLK-SEM-TEXTO]` + `Horizontal left-to-right movement shown in a static frame: on the left, one small record card (EL-CARTAO) at its starting point; on the right, one narrow empty column outlined #e9e9ed with a slot at its top that the card is heading to. A faint path is not drawn; no arrow. No other elements.`
- **Estados / movimento:** inicial: cartão à esquerda; final: cartão na coluna. Motion (EN): `the small card slides from the left to the right and settles at the top of the empty column.`
- **Texto em tela (camada):** nenhum.
- **Rótulo:** "Exemplo fictício, ilustrativo" `[proposta E1]`.
- **Evitar:** `[BLK-EVITAR]`; setas chamativas; efeitos de rastro ou brilho.
- **Consistência:** CEN-06; eixo horizontal **só neste plano** (declarado na direção); mesmo cartão do registro de C3-S2.
- **Riscos:** R2, R5, R10.
- **Parâmetros:** [A PESQUISAR]. **Status:** NÃO EXECUTADO.

#### P3-C4-S2
- **Objetivo:** painel ilustrativo com três colunas de status e cartões abstratos; sem números e sem gráficos com valores.
- **Prompt (EN):** `[BLK-ESTILO] [BLK-PALETA] [BLK-QUADRO] [BLK-SEM-TEXTO]` + `A wide overview of one illustrative dashboard: exactly three symmetrical columns of identical width and height, each a tall rounded rectangle outlined #e9e9ed, containing different numbers of identical small abstract cards (EL-CARTAO). The column headers are plain empty bars with no text. No charts, no axes, no values, no gauges, no digits. Top kept clean for a text block; small clean area at the bottom for a label.`
- **Estados / movimento:** final: cartões distribuídos nas 3 colunas. Motion (EN): `the cards settle into the three columns one by one.`
- **Texto em tela (camada):** "Painel para acompanhar"
- **Rótulo:** "Exemplo fictício, ilustrativo" `[direção]`.
- **Evitar:** `[BLK-EVITAR]`; gráfico de barras ou pizza, indicadores, contadores, avatar em cartão, aparência de painel de terceiros ou do sistema real do site.
- **Consistência:** CEN-06; colunas simétricas (regra de composição 6); RC7, RC11.
- **Riscos:** R1, R2, R3, R4, R5, R11.
- **Parâmetros:** [A PESQUISAR]. **Status:** NÃO EXECUTADO.

#### P3-C5-S1
- **Objetivo:** enquadramento da oferta: o painel recua e esmaece para fundo neutro; texto de tipografia.
- **Prompt (EN):** `[BLK-ESTILO] [BLK-PALETA] [BLK-QUADRO] [BLK-SEM-TEXTO]` + `Final state: the plain solid background #161826 with, optionally, the three-column dashboard from the previous shot reduced in size and faded into the background using only palette colors (no new gray, no transparency effect beyond the palette). The center is left clean for one centered text block.`
- **Estados / movimento:** estado A: painel de P3-C4-S2; estado B: fundo liso (ou painel mínimo ao fundo). Esmaecimento (efeito): [A PESQUISAR]; alternativa: corte entre estados. Motion (EN, se clipe): `the dashboard moves back and fades out leaving the plain background.`
- **Texto em tela (camada):** "Sistema ou painel simples, sob medida"
- **Rótulo:** "Exemplo fictício, ilustrativo" `[direção]`, **somente se o painel permanecer visível**.
- **Evitar:** `[BLK-EVITAR]`; qualquer elemento novo; transparência que crie tom fora da paleta.
- **Consistência:** CEN-02 e CEN-06; fundo `#161826` contínuo (RC1).
- **Riscos:** R1, R2, R5 (se painel ficar), R10.
- **Parâmetros:** [A PESQUISAR]. **Status:** NÃO EXECUTADO.

---

### CTA comum às três propostas (Px = P1, P2 ou P3)

Quadros de tipografia sobre fundo liso. **Geração dispensável (hipótese):** o quadro é fundo liso com texto composto; o prompt consta para rastreio e completude. Nenhum prompt traz logotipo, ícone de canal, telefone, e-mail, endereço, @, URL ou nome da marca. A **área de assinatura reservada `[NOME-D1]`** fica **vazia** (o marcador `[NOME-D1]` só pode aparecer em material interno, nunca em exportação final e nunca dentro do prompt). Como o espectador chega ao site (D4): sem plano, pendência.

#### Px-C6a-S1 (ramo D6 = contatos)
- **Objetivo:** mostrar os canais existentes como lista de texto, entrada sequencial.
- **Prompt (EN):** `[BLK-ESTILO] [BLK-PALETA] [BLK-QUADRO] [BLK-SEM-TEXTO]` + `A completely plain frame in solid #161826 with no shapes. The center is left clean for a vertical list of three short text lines with equal spacing, and a small empty area is reserved at the bottom center for a signature that stays empty.`
- **Estados / movimento:** quadro liso; entrada sequencial dos três rótulos na edição (um por vez).
- **Texto em tela (camada):** "WhatsApp" / "E-mail" / "Solicitar orçamento" (só texto, em Inter, sem ícone).
- **Rótulo:** nenhum (não há elemento ilustrativo).
- **Evitar:** `[BLK-EVITAR]`; logotipo ou ícone do WhatsApp, de e-mail ou de plataforma; botão recriado; telefone, e-mail, endereço, @.
- **Consistência:** CEN-07 e CEN-02; espaçamento igual; quadro final construído igual nas três propostas.
- **Riscos:** R1, R8.
- **Parâmetros:** [A PESQUISAR]. **Status:** NÃO EXECUTADO.

#### Px-C6a-S2 (ramo D6 = contatos)
- **Objetivo:** convite sem pressão; a lista sobe e abre espaço para a frase final; quadro final estático.
- **Prompt (EN):** `[BLK-ESTILO] [BLK-PALETA] [BLK-QUADRO] [BLK-SEM-TEXTO]` + `The same completely plain solid #161826 frame. The upper portion is left clean for the three-line list, and a clean area below it is left for one separate sentence. Nothing else; an empty reserved area stays at the bottom center.`
- **Estados / movimento:** quadro estático final; a lista sobe e a frase entra na edição.
- **Texto em tela (camada):** "A primeira conversa é para entender seu objetivo." (mais a lista do S1, subida).
- **Rótulo:** nenhum.
- **Evitar:** `[BLK-EVITAR]`; nome e logotipo no quadro final; "link na bio".
- **Consistência:** CEN-07; fundo igual a S1; **opcional na direção:** em P1 e P2 pode haver elemento reduzido da peça ao fundo (decisão de edição); em P3 não. Não incluído nos prompts.
- **Riscos:** R1.
- **Parâmetros:** [A PESQUISAR]. **Status:** NÃO EXECUTADO.

#### Px-C6b-S1 (ramo D6 = reconhecimento)
- **Objetivo:** ação de baixa fricção, texto centralizado, quadro final estático.
- **Prompt (EN):** `[BLK-ESTILO] [BLK-PALETA] [BLK-QUADRO] [BLK-SEM-TEXTO]` + `A completely plain frame in solid #161826 with no shapes. The center is left clean for one short centered text line; an empty reserved area stays at the bottom center.`
- **Estados / movimento:** quadro estático; texto entra na edição.
- **Texto em tela (camada):** "Salvar · Compartilhar"
- **Rótulo:** nenhum.
- **Evitar:** `[BLK-EVITAR]`; recriar botões, ícones de coração/compartilhar/salvar de plataforma (nomes e aparência por plataforma: [A PESQUISAR]).
- **Consistência:** CEN-07.
- **Riscos:** R1, R8.
- **Parâmetros:** [A PESQUISAR]. **Status:** NÃO EXECUTADO.

Ramo D6 = ambos / sem resposta: NEEDS_INFO (igual ao roteiro e à direção); sem prompt.

## Cobertura plano → prompt

| Proposta | Planos da decupagem | Prompts nesta folha | Total |
|---|---|---|---|
| P1 | C1-S1; C2-S1/S2; C3-S1/S2; C4-S1/S2; C5-S1/S2 | os mesmos 9 ids | 9 |
| P2 | C1-S1; C2-S1/S2; C3-S1/S2; C4-S1/S2; C5-S1/S2 | os mesmos 9 ids | 9 |
| P3 | C1-S1; C2-S1/S2; C3-S1/S2; C4-S1/S2; C5-S1 | os mesmos 8 ids | 8 |
| CTA | Px-C6a-S1/S2; Px-C6b-S1 | os mesmos 3 ids | 3 |
| **Total** | | | **29** (igual à direção) |

## Itens [A PESQUISAR]

| # | Item | Observação |
|---|---|---|
| AP1 | Ferramentas-alvo de imagem e de vídeo; acesso, entradas, saídas, limites, custo, termos, guia oficial de prompt, controle de consistência | `knowledge/prompts-*` vazios; `integrations/veo.md`, `kling.md`, `runway.md` "NÃO PESQUISADO" |
| AP2 | Todos os parâmetros: proporção, resolução, duração, seed, modelo, imagem de referência, peso/campo de negativo | Nenhum afirmado |
| AP3 | Sintaxe para negativos e conversão da lista "evitar" em frases afirmativas | Depende da ferramenta |
| AP4 | Saída pretendida: imagem estática por estado (com animação na edição) ou clipe | Hipótese: estados + edição (R10, R11) |
| AP5 | Técnica de consistência entre planos por ferramenta (`knowledge/consistency/` vazio) | Hipótese não testada: âncoras + composição por camadas |
| AP6 | Morph/esmaecimento/transições e catálogo de movimentos | R10; direção e art bible |
| AP7 | Fidelidade de cor (hex) após geração, edição e compressão | Aprovar sobre quadro exportado |
| AP8 | Valores de espessura de linha, raio de canto, margem, tamanhos de fonte, zonas seguras | CSS completo do site (E12 do art bible) |
| AP9 | Licença de Inter em vídeo comercial; fonte substituta se indisponível | NEEDS_INFO ao ECD |
| AP10 | Rotulagem de conteúdo de IA e regra publicitária do rótulo "ilustrativo"; uso de marcas de terceiros em texto ("WhatsApp", "GitHub") | R13 e divergência 6 da direção |
| AP11 | Nome e aparência dos botões "Salvar/Compartilhar" por plataforma | Não recriados |

## Lacunas e pendências para o ECD

1. **Ferramenta-alvo não definida** (e nenhuma documentada): esta folha não é executável como está sem a etapa de pesquisa e escolha.
2. **E1, abrangência do rótulo "ilustrativo"** (art bible; divergências 1 a 3 da direção). Usei a recomendação do art bible como **proposta**: rótulo em todo plano com elemento ilustrativo. **O texto do rótulo nos planos estendidos (`[proposta E1]`) não consta no roteiro; usei o rótulo da própria peça** ("Situação ilustrativa" em P1, "Ilustrativo" em P2, "Exemplo fictício, ilustrativo" em P3). Decisão e redação: ECD. Os prompts não geram rótulo (variante A), então a mudança de decisão não altera os prompts; só a camada de edição.
3. **E2, "Modelo declarado pelo negócio" (P1-C4-S2):** função (rótulo de declaração ou de ilustração) pendente; se E1 valer, há dois rótulos na mesma posição no mesmo plano. Pedido de decisão.
4. **Papel do traço riscado (P1-C4-S2):** o art bible deixa `#e9e9ed` ou acento "a fixar em revisão". Usei `#e9e9ed` como proposta.
5. **Papéis dos dois acentos:** proposta do art bible (E4); `#a7a1db` só é usado como secundário (barras de código em P2-C4-S1, destaque eventual em P3-C3-S2).
6. **Texto "GitHub" e "valor" em tela:** nenhum prompt ou texto em tela inclui "GitHub" (a direção usa "Código versionado"); "valor" não aparece. Se o ECD aprovar usar o texto, os campos de texto em tela mudam; pendência E10 do art bible.
7. **Cabeçalhos "Pedido · Status · Prazo" (P3-C2-S1) e campos (P3-C3-S2):** tratei como texto composto na edição (hipótese). A direção os descreve dentro da grade; se a decisão for gerá-los, usar variante B, aceitando o risco R1.
8. **D1 a D6:** nome oficial (`[NOME-D1]`, nunca fixado), voz, D3 (nenhum plano com pessoa, avatar, rosto ou voz de Daniel), perfis (D4), prova (D5), objetivo (D6, define o ramo do CTA).
9. **Como o espectador chega ao site:** sem plano e sem prompt (D4).
10. **Estilos fora do gráfico/motion** (cinematográfico, com pessoas, do brief): sem prompts; exigem nova decupagem e art bible (E9).
11. **Prompts de áudio/voz:** fora do escopo desta folha.
12. **Estimativa de duração dos planos** vem do roteiro (estimativa); não é parâmetro de geração.
13. **Revisão antes de qualquer aprovação de quadro (checklist do art bible):** RC1 a RC16, em especial ausência de números, moeda, logotipos, dados reais, nome de cliente, "03", SaaS de contratos e pessoas.

## Rastreabilidade
Fontes: `projects/forma-digital/04-direction.md` (v0.1, rascunho); `05-art-bible.md` (v0.1, rascunho); `03-script.md` (v0.1, rascunho); `00-brief.v2.md`; `00-inconsistencies-report.md`; `_sources/site-extract.md` (2026-11-08); `templates/prompt-sheet.md`; `.claude/rules/*.md`; `.claude/skills/media-prompt-engineering/SKILL.md`; `knowledge/README.md`, `knowledge/prompts-image/README.md`, `knowledge/prompts-video/README.md`, `knowledge/consistency/README.md` (todos VAZIOS, 2026-11-08); `integrations/README.md`, `integrations/veo.md`, `integrations/kling.md`, `integrations/runway.md` (NÃO PESQUISADO, 2026-11-08).
Fatos confirmados: hex `#161826`, `#232532`, `#e9e9ed`, `#9184d9`, `#a7a1db` e fonte Inter segundo o extrato do site; textos em tela e rótulos citados vêm de `03-script.md` e `04-direction.md`; a decupagem tem 29 planos e esta folha tem 29 prompts com os mesmos ids (conferência por contagem neste documento); `knowledge/prompts-*` e `consistency` estão vazios e `integrations/` das ferramentas de vídeo não tem campos preenchidos, portanto nenhuma sintaxe ou parâmetro de ferramenta tem base documentada.
Hipóteses: que o texto em tela e os rótulos devem ser camadas de edição; que estados separados mais edição reduzem R10 e R11; que as descrições em inglês aqui produzem os quadros descritos (não testado, nenhuma ferramenta usada); a ordem de geração; que geração é dispensável nos quadros de tipografia; os papéis das cores (proposta do art bible); a extensão do rótulo (E1) e o texto do rótulo nos planos estendidos; o uso de `#e9e9ed` no traço riscado.
Pendências: ferramenta-alvo e toda a documentação em `knowledge/` e `integrations/`; todos os parâmetros ([A PESQUISAR]); D1 a D6; E1, E2, E4, E10 do art bible; AP1 a AP11; aprovação de direção, art bible e roteiro (rascunhos).
Responsável: prompt-engineer

## Relatório ao Diretor
- **agente:** prompt-engineer
- **tarefa recebida:** gravar `projects/forma-digital/06-prompts.md` conforme `templates/prompt-sheet.md`, com um prompt por plano (29 planos da decupagem, mesmos ids) em formato genérico rotulado, bloco comum de estilo/paleta/negativos, seção de lacunas, texto em tela como camada de edição (recomendação), todos "NÃO EXECUTADO", sem pessoa/Daniel, sem dados/logotipos de terceiros, `[NOME-D1]` como espaço reservado, todo parâmetro `[A PESQUISAR]`.
- **arquivos consultados:** `projects/forma-digital/04-direction.md`; `05-art-bible.md`; `03-script.md`; `00-brief.v2.md`; `00-inconsistencies-report.md`; `_sources/site-extract.md`; `templates/prompt-sheet.md`; `knowledge/README.md`; `knowledge/prompts-image/README.md`; `knowledge/prompts-video/README.md`; `knowledge/consistency/README.md`; `integrations/README.md`; `integrations/veo.md`; `integrations/kling.md`; `integrations/runway.md`; regras `.claude/rules/*` e a skill `media-prompt-engineering` (recebidas no contexto da invocação). Listei `projects/forma-digital/`, `knowledge/` e `integrations/`; `06-prompts.md` não existia. Não li `01-trends.md`, `02-strategy.md`, `00-client-audit.md`, `STATUS.md`, `integrations/elevenlabs.md`, `capcut.md`, `adapter-contract.md` nem os demais README de `knowledge/`.
- **trabalho realizado:** folha com status de documentação (nenhuma ferramenta documentada), instruções de montagem, bloco comum (estilo, paleta, quadro, sem texto, texto gerado para teste, lista "evitar" e 5 elementos fixos), ordem de geração com âncoras, 29 prompts (P1 = 9, P2 = 9, P3 = 8, CTA = 3) com objetivo, prompt em inglês, estados/movimento, texto em tela como camada, rótulo, evitar, consistência (CEN, RC), riscos (R1 a R14) e parâmetros `[A PESQUISAR]`, tabela de cobertura, itens `[A PESQUISAR]` e 13 lacunas. Nada foi executado, gerado ou chamado.
- **skills aplicadas:** `media-prompt-engineering`, passos 1 a 5 (planos listados; ferramentas sem documentação, então formato genérico rotulado e `[A PESQUISAR]`; um prompt por plano reutilizando descrições fixas do art bible; parâmetros, ordem e riscos registrados; template preenchido, com rastreio plano para prompt).
- **status:** NEEDS_INFO (parcial). Folha entregue como rascunho com todos os 29 planos cobertos; ferramentas Veo, Kling, Runway e geradores de imagem **bloqueados por falta de documentação**; execução depende de escolha e pesquisa da ferramenta, de D1 a D6 e das decisões E1, E2 e E10.
- **entregáveis:** `/home/user/Site.FirmaDigital/AI-VIRAL-STUDIO/projects/forma-digital/06-prompts.md`
- **premissas:** (1) formato genérico, sem sintaxe nem parâmetro de ferramenta; (2) variante A (sem texto no quadro, texto e rótulo em camada de edição) como recomendação, hipótese não testada; (3) rótulo ilustrativo estendido a todo plano com elemento fictício conforme E1 do art bible, com texto do rótulo da própria peça (proposta minha); (4) papéis das cores como no art bible; (5) "blocos cinza" e "faixa de contraste" traduzidos para `#232532` e `#161826`; (6) estados separados para transformações e sequências; (7) sem logotipos, sem "GitHub" e sem "valor" em tela; (8) durações da decupagem só como referência.
- **pendências:** ferramenta-alvo e documentação; todos os parâmetros; E1 (abrangência e redação do rótulo), E2, E4, E10; D1 a D6; D4 (chegada ao site); saída pretendida (imagem ou clipe); AP1 a AP11.
- **autoavaliação:**
  - ✔ Todo plano de `04-direction.md` tem prompt: 29 de 29, mesmos ids (tabela de cobertura).
  - ✔ Prompts reutilizam as descrições fixas do art bible: blocos comuns e elementos EL-* colados literalmente, com hex e CEN/RC referenciados.
  - ✔ Sintaxe e parâmetros só de ferramentas documentadas, senão `[A PESQUISAR]` e formato genérico marcado: nenhuma ferramenta documentada; nenhum parâmetro afirmado; formato rotulado como genérico.
  - ✔ Sem promessas de resultado do modelo: tudo "NÃO EXECUTADO"; hipóteses rotuladas; nenhuma mídia descrita como existente.
  - ✔ Limites de atuação: não criei conceito, roteiro nem direção; não executei nada; não instruí outros especialistas (só pedidos de decisão ao ECD).
  - ✔ Restrições do projeto: sem pessoa, rosto, avatar ou voz de Daniel; sem telas/dados reais, clientes, SaaS, "03 sistemas", logotipos de terceiros, números ou moeda; marca ausente (`[NOME-D1]` só como espaço reservado); sem referências "no estilo de X".
  - ✘ Executabilidade: a folha não pode ser executada nem aprovada agora, por falta de ferramenta documentada e das decisões D1 a D6 (limitação externa).
