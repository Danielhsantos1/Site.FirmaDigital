---
projeto: forma-digital
versão: 0.2 (Revisão 2, escopo estreito)
autor-agente: quality-reviewer
data: 2026-11-08
entradas-usadas: [03-script.v2.md, _qa-test/03-script.SEEDED-DEFECTS.v2.md, 09-qa-report.md (Revisão 1, l.1-230), _sources/site-extract.md, templates/qa-report.md, templates/script.md]
status: em revisão   # gate executado; nenhum arquivo promovido; correções voltam ao dono via ECD
---

# Relatório de qualidade

## Revisão 2 · 2026-11-08 · reconferência de 03-script.v2.md e _qa-test/03-script.SEEDED-DEFECTS.v2.md

### Escopo, método e critério
- Escopo: somente (A) `03-script.v2.md` (substitui `03-script.md`) e (B) `_qa-test/03-script.SEEDED-DEFECTS.v2.md` (não é entregável). `09-qa-report.md` (Revisão 1) não foi alterado.
- Fonte de fatos do cliente: só `_sources/site-extract.md`. Conferi as linhas do extrato citadas nos dois arquivos.
- Aritmética: recontei palavra a palavra TODAS as falas (variantes Daniel e institucional separadas) e também as palavras de tela, apliquei a fórmula declarada em cada arquivo, conferi folgas, contagem de frases, somas de duração e a tabela de 23 linhas. Contagem manual, sem shell.
- Critério de veredito (o da Revisão 1): REPROVADO = ≥1 bloqueante; APROVADO COM RESSALVAS = sem bloqueante, com importante e/ou pendência impeditiva; APROVADO = sem bloqueante, importante nem pendência impeditiva. Como na Revisão 1, nenhum arquivo chega a APROVADO enquanto D1 a D6 e `[A PESQUISAR]` forem impeditivos (`[NOME-D1]`, `[DESTINO-D4]` na tela). D1 a D6 seguem NEEDS_INFO; este relatório não promove nada nem resolve D1 a D6.

## Veredito

| Arquivo | Veredito | Bloq. | Imp. | Men. |
|---|---|---|---|---|
| A. 03-script.v2.md | **APROVADO COM RESSALVAS** | 0 | 4 | 4 |
| B. _qa-test/03-script.SEEDED-DEFECTS.v2.md (teste) | **APROVADO COM RESSALVAS** | 0 | 0 | 3 |

- A: o bloqueante RO-01 está resolvido (a conta fecha, sob a hipótese do próprio roteiro). Restam 4 importantes novos ou residuais (NP-01 a NP-04) e a dependência de D1 a D6.
- B: os 9 bloqueantes e os 5 importantes da Revisão 1 estão resolvidos. Restam só menores e as pendências D1 a D6. Veredito mantido em RESSALVAS pelo mesmo critério da Revisão 1 (pendência impeditiva: `[NOME-D1]`, `[DESTINO-D4]`).
- Todas as contas valem **somente sob** o ritmo de 0,4 s/palavra e a regra de pausa, que são hipóteses sem fonte.

## Achados

### A. 03-script.v2.md: status dos achados da Revisão 1

| ID | Status | Evidência (linha do v2) |
|---|---|---|
| RO-01 (bloq.) | **Resolvido** (aritmética), com ressalva de fragilidade | Convenções l.38-45, fórmula l.42. Tabela l.259-283, contagem l.287-320. Recontei: 23 linhas, nenhuma folga negativa, mínima +0,2 s (G-P2 l.263, G-P3 l.265, G-P3v l.266). Ritmo declarado como hipótese sem fonte (l.40). "Duração compatível" refeito com a conta (l.369). Propagação a 04, 07 e 08 não feita, mas registrada em Pendências (l.353); fora do escopo desta revisão. Ver NP-03 (contagem "35 falas") |
| RO-02 | **Resolvido** | Tabela l.324-333. Conferi caso a caso: P1-C2 tela repete a fala (l.104); P1-C3 selo (l.111); P1-C5 sem "antes de seguir" (l.123); P2-C2 tela lista "prazo · valor" e "Por escrito" (l.146); P3-C2 "em abas separadas" (l.187); CTA com tela própria por variante (l.225, 227, 237, 239); reconhecimento com fala curta (l.231-232, 242). Perdas aceitas por escrito (l.327, 333). Resíduo menor: ver NP-08 |
| RO-03 | **Parcialmente** | "site" é a 1ª palavra em P1 (l.97) e 3ª em P2 (l.138); tela com objeto desde o quadro 0 (l.98, 139). Recomendação por critério de retenção c1 a c3 e troca de risco declarada (l.77-83). Porém o critério de 1,2 s não fecha sob a regra de respiro inicial. Ver NP-04 |
| RO-04 | **Resolvido** (como registro) | l.65-67: omissão da landing page (Ang-3) registrada como D-ECD-01, sem decisão do scriptwriter. A decisão segue do ECD |
| RO-05 | **Resolvido** | CTA por proposta (l.222-242). Nenhuma fala imperativa: "Quer conversar sobre o seu site?" / "Quer organizar um processo do seu negócio?" (l.224, 236). Destino só como `[DESTINO-D4]` na tela (l.225, 227, 237, 239). P3 tem CTA próprio (l.234-242). Reconhecimento sem "salve/envie" (l.220, 231-232, 242). Provisório até D4/D6 (l.217, 222, 234) |
| RO-06 | **Resolvido** | Exemplo trocado por "Item · Quantidade · Local" (l.187, 339). Risco ligado a D5 registrado (l.336-340). Impacto em 04/06 registrado (l.340). Observação menor: o caso do extrato (l.65) fala em "solicitações de serviço **e material**"; o tema "estoque" ainda pode evocá-lo, risco já reconhecido em l.339 |
| RO-07 | **Parcialmente** | Regra RA (l.48) e selo presentes em P1-C3/C4/C5 (l.111, 118, 125), P2 (l.139, 146, 153, 159, 165), P3-C5 (l.208) e CTAs. Falha a regra: ver NP-02 (P3-C3 e P3-C4) |
| RO-08 | **Resolvido** | "antes de seguir" removido (l.123); "tudo em um só lugar" removido, painel "para organizar o processo" (l.199-201; extrato l.53); "escopo combinado antes de começar" (l.109; extrato l.44) separado de "por escrito" (l.144; extrato l.82). Condensações restantes listadas em Hipóteses (l.352). Ver NP-07 (um "lastro direto" exagerado) |
| RO-09 | **Resolvido** | l.85-86: P1 × P2 diferem em ângulo e em família de gancho, não formam par de H1; coerente com o que a Revisão 1 citou de `02-strategy.md` l.159. Não reabri o 02 |

### A. Achados novos ou residuais

**NP-01 · importante · 03-script.v2.md l.18-26 (coluna "Onde")** · Placeholders não substituídos
- Trecho: "L_TAB" (l.18), "L_RO02" (l.19), "L_GANCHO" (l.20 e l.26), "L_COBERTURA" (l.21), "L_CTA" (l.22), "L_RISCO" (l.23), "L_RA" (l.24), "L_RASTRO" (l.25). O cabeçalho da coluna promete "linha deste arquivo".
- Regra: rastreabilidade e fidelidade ao template/handoff (resumo de mudanças deve indicar onde). Entregável com campo de preenchimento deixado em aberto.
- Correção pedida: substituir cada marcador pela linha real (por exemplo, L_TAB = l.257-320; L_RO02 = l.322-334; L_GANCHO = l.69-86; L_COBERTURA = l.65-67; L_CTA = l.217-244; L_RISCO = l.336-340; L_RA = l.47-50; L_RASTRO = l.350-353), conferindo ao regravar.

**NP-02 · importante · 03-script.v2.md l.48, 192-202** · Regra RA não aplicada em P3-C3 e P3-C4
- Trecho: RA (l.48) exige selo em toda cena que afirma "serviço do negócio". P3-C3 Daniel: "Eu posso construir um formulário para registrar cada item." (l.192) e P3-C4 (l.199-200) afirmam o que o negócio oferece, mas a tela leva só o rótulo "Exemplo fictício" (l.194, 201). O selo aparece só em P3-C5 (l.208). A exceção "cenas puramente ilustrativas" (l.48) não cobre uma fala de capacidade ("Eu posso construir").
- Regra: RO-07 (atribuição única) e a própria RA.
- Correção pedida: aplicar o selo em P3-C3 e P3-C4 (pelo menos na variante Daniel de C3), ou reescrever a regra RA delimitando a exceção, e atualizar a tabela de leitura de tela (+3 palavras: P3-C3 6→9 e P3-C4 10→13, leitura 2,7 e 3,9 s, ainda dentro de 6,0 s).

**NP-03 · menor · 03-script.v2.md l.285** · Contagem de falas incorreta
- Trecho: "23 linhas (35 falas contando as variantes D/I distintas)". Recontei: 23 linhas + 10 linhas com texto distinto D/I (P1-C3, P1-C4, P1-C5, P2-C2, P2-C3, P3-C3, P3-C4, P3-C5, CTA-S-C, CTA-P3-C) = **33**. Confere com as 33 linhas da lista palavra a palavra (l.288-320).
- Correção: trocar 35 por 33 (ou explicar o critério).

**NP-04 · importante · 03-script.v2.md l.41, 44, 73-75, 367** · Janela de "primeiro segundo" ignora o respiro inicial declarado
- Trecho: a regra de pausa inclui "0,2 s no início" (l.41). Com ela, P1 "Site" fica em 0,2-0,6 s (l.73 diz 0,0 a 0,4 s) e P2 "site" em 1,0-1,4 s (l.74 e G-P2v dizem 0,8 a 1,2 s). Logo "site dito até 1,2 s" (l.44, 367) **não vale** em P2 (principal recomendada) pela regra do próprio arquivo: termina em 1,4 s. A janela de P3 (l.75, "0,8 a 2,4 s") também ignora o offset.
- Regra: consistência interna da conta; autoavaliação ✔ (l.367) contradita pelos números.
- Correção pedida: recalcular os intervalos com o offset de 0,2 s, ou redefinir o critério (por exemplo, "até 1,4 s") e registrar como hipótese; não afirmar "até 1,2 s" sem ajustar.

**NP-05 · importante · 03-script.v2.md l.128, 168, 211, 368** · Cenas 6 (CTA) sem "Intenção"; autoavaliação diz o contrário
- Trecho: a autoavaliação afirma "campo 'Intenção' nas 18 cenas" (l.368). Há "Intenção" em 15 cenas (l.96, 102, 108, 115, 122, 137, 143, 150, 157, 163, 179, 185, 191, 198, 205). As três Cenas 6 (l.128, 168, 211) não têm; a seção CTA (l.217-244) também não declara intenção.
- Regra: `templates/script.md` ("Roteiro por cena: nº, intenção, fala, texto em tela, duração"); veracidade da autoavaliação (protocolo de comunicação).
- Correção pedida: acrescentar intenção às 3 cenas de CTA e corrigir a autoavaliação.

**NP-06 · menor · 03-script.v2.md l.351** · "Fatos confirmados" mistura fato do cliente com conferência aritmética
- Trecho: "...contagens de palavras e somas de duração deste arquivo (conferência aritmética...)" dentro de Fatos confirmados.
- Regra: handoff-format (rastreabilidade): fatos confirmados vêm de fonte; a conta depende da hipótese de ritmo.
- Correção: mover para Hipóteses ou Fontes.

**NP-07 · menor · 03-script.v2.md l.82** · "Lastro direto" exagerado
- Trecho: "cada frase de P2 tem lastro direto no extrato (l.79 a 91)". Mas "Quer um site?" / "Pediu um site? O que vem depois?" (l.138) e "Quer conversar..." (l.224) não têm lastro; "você aprova" é condensação listada em Hipóteses (l.352).
- Correção: trocar por "as frases de processo de P2 têm lastro...".

**NP-08 · menor · 03-script.v2.md l.208, 206 e l.322-334** · Reconciliação fala × tela incompleta em P3-C5 e P2-C4
- Trecho: P3-C5 a fala diz "para um processo do seu negócio", a tela traz só "Sistema ou painel simples, sob medida" (l.206, 208); P2-C4 a fala diz "GitHub", a tela não (l.158-159; esta o roteiro anota). P3-C5 não consta da tabela de reconciliação (l.324-333).
- Correção: incluir P3-C5 na tabela como perda aceita ou reconciliar.

### A. Verificações sem achado (conferidas)
- Fatos do cliente: citações do extrato conferem (l.31, 44, 52-53, 55, 63-69, 79, 82, 85, 88, 91, 93-94, 99-107; "Definimos juntos" l.82 usado só na nota, l.343).
- Ausentes nas falas e telas: "somos/temos/nós", nome do negócio ou de Daniel (só `[NOME-D1]`), SaaS como oferta (l.176 menciona "o SaaS de contratos" só para negá-lo), "03 sistemas", cliente nomeado, avatar ou voz sintética (l.31 só nega), preço, número, superlativo ou promessa. "o cliente" (variante institucional) é papel genérico, não cliente real.
- CTA: nenhuma fala manda agir em destino indefinido; "como o espectador chega ao site" registrado como NEEDS_INFO (l.219).
- Somas de duração: P1 3,5+5,5+6,0+6,0+6,0 = 27,0; +8,0 = 35,0; +4,0 = 31,0. P2 4,5+4×6,0 = 28,5; +8,0 = 36,5; +5,0 = 33,5 (com gancho variação 4,0: 36,0/33,0). P3 3,0+3×6,0+5,5 = 26,5; +8,5 = 35,0; +3,5 = 30,0. **Todas conferem** (l.130, 170, 213, 248-254). Percentual l.83: 11,5/35,0 = 32,9% ≈ 33% confere. c2 (l.80): 4,5 s e 9,0 s conferem.
- Cobertura do template `script.md`: Logline (l.52), Estrutura narrativa (l.57), Variações de gancho com recomendada (l.69-83), Roteiro por cena (l.90), CTA (l.217), Duração total (l.246), Relatório ao Diretor (l.356) presentes; cabeçalho com entradas e `substitui` (l.1-9). Relatório com os 10 campos do protocolo. Ordem Rastreabilidade antes de Relatório mantém a prática do GL-01 (decisão do ECD).

### A. Tabela das 23 linhas (recontagem independente)
Fórmula do 03.v2: necessário = 0,4×P + 0,3×(frases−1) + 0,4. Palavras de tela conferidas (incluem selo, rótulo e marcadores).

| ID | Pal. D / I (recontado) | Frases | Necessário D / I | Duração | Folga D / I | Tela pal. | Confere |
|---|---|---|---|---|---|---|---|
| G-P1 | 6 | 2 | 3,1 | 3,5 | +0,4 | 8 | sim |
| G-P1v | 6 | 1 | 2,8 | 3,5 | +0,7 | 8 | sim |
| G-P2 | 9 | 2 | 4,3 | 4,5 | +0,2 | 12 | sim |
| G-P2v | 7 | 2 | 3,5 | 4,0 | +0,5 | 7 | sim |
| G-P3 | 6 | 1 | 2,8 | 3,0 | +0,2 | 9 | sim |
| G-P3v | 6 | 1 | 2,8 | 3,0 | +0,2 | 9 | sim |
| P1-C2 | 10 | 3 | 5,0 | 5,5 | +0,5 | 12 | sim |
| P1-C3 | 10 / 11 | 1 | 4,4 / 4,8 | 6,0 | +1,6 / +1,2 | 8 | sim |
| P1-C4 | 11 / 13 | 1 | 4,8 / 5,6 | 6,0 | +1,2 / +0,4 | 12 | sim |
| P1-C5 | 10 / 11 | 1 | 4,4 / 4,8 | 6,0 | +1,6 / +1,2 | 9 | sim |
| P2-C2 | 13 / 13 | 1 | 5,6 | 6,0 | +0,4 | 15 | sim |
| P2-C3 | 11 / 12 | 1 | 4,8 / 5,2 | 6,0 | +1,2 / +0,8 | 14 | sim |
| P2-C4 | 11 | 1 | 4,8 | 6,0 | +1,2 | 10 | sim |
| P2-C5 | 12 | 1 | 5,2 | 6,0 | +0,8 | 13 | sim |
| P3-C2 | 8 | 1 | 3,6 | 6,0 | +2,4 | 9 | sim |
| P3-C3 | 9 / 6 | 1 | 4,0 / 2,8 | 6,0 | +2,0 / +3,2 | 6 | sim |
| P3-C4 | 9 / 9 | 1 | 4,0 | 6,0 | +2,0 | 10 | sim |
| P3-C5 | 12 / 11 | 1 | 5,2 / 4,8 | 5,5 | +0,3 / +0,7 | 9 | sim |
| CTA-S-C | 17 / 17 | 2 | 7,5 | 8,0 | +0,5 | 21 | sim |
| CTA-P3-C | 18 / 18 | 2 | 7,9 | 8,5 | +0,6 | 22 | sim |
| CTA-P1-R | 7 | 1 | 3,2 | 4,0 | +0,8 | 10 | sim |
| CTA-P2-R | 9 | 1 | 4,0 | 5,0 | +1,0 | 11 | sim |
| CTA-P3-R | 4 | 1 | 2,0 | 3,5 | +1,5 | 9 | sim |

Leitura de tela (0,3×pal.) ≤ duração em todas; maior razão G-P3/G-P3v 2,7/3,0. Folga mínima +0,2 s confirmada. Única discrepância aritmética do arquivo: "35 falas" (NP-03) e os intervalos de tempo (NP-04). Folgas de +0,2 s não toleram fala mais lenta (o arquivo já avisa, l.285).

### B. _qa-test/03-script.SEEDED-DEFECTS.v2.md: status dos achados da Revisão 1

| ID | Status | Evidência (linha do teste v2) |
|---|---|---|
| SD-01 | Resolvido | C2 sem "temos" nem contagem de sistemas (l.41); tom sem "somos/temos/nós" (l.18) |
| SD-02 | Resolvido | Sem número de clientes nem "satisfeitos" (l.41) |
| SD-03 | Resolvido | Sem depoimento, cliente nomeado ou resultado (l.41) |
| SD-04 | Resolvido | C3 só trata do modelo de escopo (l.46); sem SaaS na fala. Extrato l.76 ("Em desenvolvimento") confere |
| SD-05 | Resolvido | C5 convida a conversar; sem garantia (l.56) |
| SD-06 | Resolvido, com menor | Diagrama ilustrativo rotulado "ilustração", sem tela real nem cliente (l.52). Ver NT-01 |
| SD-07 | Resolvido | Sem superlativo, "agência" ou "região" (fala l.36-56; tom l.18) |
| SD-08 | Resolvido | Sem autoapresentação; nome só `[NOME-D1]` (l.19, l.57); C1 abre pela situação (l.36) |
| SD-09 | Resolvido | Uma duração por cena e total (l.38-58, 68-73); recontagem abaixo fecha |
| SD-10 | Resolvido | "Vídeo curto vertical"; plataforma e duração `[A PESQUISAR]` (l.16) |
| SD-11 | Resolvido, com menor | Seção CTA com canais do extrato (l.60-61; extrato l.5, l.100-105 conferem). Ver NT-02 |
| SD-12 | Resolvido | Logline (l.21), Estrutura (l.24), Variações (l.27), Cenas (l.33), CTA (l.60), Duração (l.63), Relatório (l.111), mais Rastreabilidade (l.104); cabeçalho com entradas (l.7) |
| SD-13 | Resolvido | Arco situação, dor, princípio, processo, convite (l.24-25); sem "controlamos/tudo" como atribuição |
| SD-14 | Resolvido | Gancho pela situação do público (l.36) |
| SD-15 | Resolvido (especificado) | "Avatar e voz sintética de Daniel NÃO são usados"; voz = `[D2/D3 pendente]` (l.17) |
| SD-16 | Resolvido | Sem "dobrei", "maior", "garantimos"; tom definido (l.18) |

### B. Achados novos

**NT-01 · menor · teste v2 l.52** · Anotação interna dentro do texto de tela
- Trecho: Texto em tela: "4 etapas: Escopo, Protótipo, Construção, Publicação (l.80-91)". O "(l.80-91)" é referência ao extrato; se for lido como texto de tela, vazaria uma anotação interna.
- Correção: tirar a referência do campo de tela e deixá-la na linha de rastro.

**NT-02 · menor · teste v2 l.56** · Fala imperativa com destino ainda indefinido
- Trecho: "Conte o que você precisa." (frase do extrato, l.94, mas CTA imperativo). A tela traz `[DESTINO-D4]` (l.57) e a seção CTA diz que a fala não indica endereço (l.61). É o padrão que o RO-05 do 03 evitou ("nenhuma fala imperativa para destino indefinido").
- Correção: marcar como provisório até D4 ou reformular como pergunta, como no 03.v2.

**NT-03 · menor · teste v2 l.64 × 03-script.v2.md l.42** · Fórmula de pausa diferente entre os dois arquivos
- O teste usa 0,3 × nº de frases; o 03.v2 usa 0,3 × (frases − 1). Cada arquivo declara a sua e aplica corretamente, mas não são comparáveis. Não é erro; padronizar se o ECD quiser comparar. Com a fórmula do teste, as folgas do teste são mais conservadoras.

### B. Recontagem do teste v2 (fórmula declarada: 0,4×P + 0,3×frases + 0,4)

| Cena | Pal. recontadas | Frases | Necessário | Duração | Folga | Confere |
|---|---|---|---|---|---|---|
| C1 | 11 | 1 | 5,1 | 5,5 | 0,4 | sim |
| C2 | 10 | 3 | 5,3 | 5,5 | 0,2 | sim |
| C3 | 9 | 1 | 4,3 | 4,5 | 0,2 | sim |
| C4 | 17 (8 + 9) | 2 | 7,8 | 8,0 | 0,2 | sim |
| C5 | 16 (11 + 5) | 2 | 7,4 | 7,5 | 0,1 | sim |
| Total | 63 | 9 | 29,9 | 31,0 | 1,1 | sim (25,2 + 2,7 + 2,0; 5,5+5,5+4,5+8,0+7,5) |

Ganchos: A = 11 pal., 1 frase, 5,1 s; B = 9 pal., 1 frase, 4,3 s; C = 8 pal., 2 frases, 4,2 s. Todos conferem e cabem em 5,5 s. Nenhuma folga negativa; menor folga 0,1 s (C5), muito frágil. Linhas de rastro da tabela SD-xx (l.85-102) conferem com o conteúdo.

## Itens não verificados
- **Ritmo de fala (0,4 s/palavra), regra de pausa, piso de leitura de tela (0,3 s/palavra):** hipóteses sem fonte; as contas só provam coerência interna. Só locução real mede.
- Duração-alvo, limites e janela de gancho por plataforma: `[A PESQUISAR]`; não verificáveis (sem web).
- Citações a `02-strategy.md` (H1 l.159, Ang-3 etc.) e `00-brief.v2.md` (l.34) no 03.v2: conferidas apenas por coerência com o que a Revisão 1 registrou; os arquivos não foram reabertos.
- O arquivo original de teste (`03-script.SEEDED-DEFECTS.md`) não foi relido; os SD-01 a SD-16 foram avaliados pela descrição da Revisão 1 (l.199-219) contra o v2.
- `scripts/validate.py` não executado (sem shell). Contagens feitas à mão.
- Reconfirmação de 04, 06, 07 e 08 contra o 03.v2: fora do escopo; segue necessária (o 03.v2 mudou falas e durações).
- D1 a D6 e D-ECD-01: NEEDS_INFO, não resolvidas aqui.

## Rastreabilidade
Fontes: `projects/forma-digital/03-script.v2.md`; `projects/forma-digital/_qa-test/03-script.SEEDED-DEFECTS.v2.md`; `projects/forma-digital/09-qa-report.md` (Revisão 1, l.1-230); `projects/forma-digital/_sources/site-extract.md` (2026-11-08); `templates/qa-report.md`; `templates/script.md`.
Fatos confirmados: contagens de palavras, frases, somas e folgas recontadas à mão nos dois arquivos; citações de linha do extrato conferem; placeholders L_* presentes em l.18-26 do 03.v2; "Intenção" ausente nas 3 cenas de CTA; ausência de "somos/temos/nós", nome, SaaS como oferta, "03 sistemas", avatar e voz sintética nas falas e telas.
Hipóteses: ritmo de 0,4 s/palavra, regra de pausa e leitura de tela (sem fonte, do próprio roteiro); severidades atribuídas a NP-02, NP-04 e NP-05 como "importante" são julgamento deste revisor.
Pendências: correções NP-01 a NP-08 e NT-01 a NT-03 via ECD ao scriptwriter; D1 a D6 e D-ECD-01 (NEEDS_INFO); reconfirmar 04, 06, 07, 08; ritmo de fala, duração-alvo e demais `[A PESQUISAR]`; `validate.py` não executado.
Responsável: quality-reviewer

## Relatório ao Diretor
- **agente:** quality-reviewer
- **tarefa recebida:** Revisão 2, escopo estreito, de `03-script.v2.md` e `_qa-test/03-script.SEEDED-DEFECTS.v2.md`: status de RO-01 a RO-09 e SD-01 a SD-16, novos problemas, reconferência aritmética independente, novos vereditos, sem promover nem reescrever.
- **arquivos consultados:** `03-script.v2.md`; `_qa-test/03-script.SEEDED-DEFECTS.v2.md`; `09-qa-report.md` (l.1-230); `_sources/site-extract.md`; `templates/qa-report.md`; `templates/script.md`. **Não lidos:** `02-strategy.md`, `00-brief.v2.md`, `03-script.md` (v1), `_qa-test/03-script.SEEDED-DEFECTS.md` (original), `04` a `08`, `10-performance.md`, `STATUS.md`, `knowledge/`, skills, `scripts/validate.py`.
- **trabalho realizado:** recontei todas as falas (D e I) e as palavras de tela, apliquei as fórmulas declaradas, conferi folgas, frases, somas por proposta e as 23 linhas; conferi linhas do extrato e as linhas citadas no teste v2; classifiquei cada RO e SD; procurei placeholders, fatos fora do extrato, termos proibidos, CTA e cobertura do template.
- **skills aplicadas:** `quality-review`, passos 1 a 6 (aderência, template, consistência, não invenção, classificação, registro em arquivo de revisão separado).
- **status:** DONE (revisão concluída; os arquivos revisados seguem dependentes de D1 a D6).
- **entregáveis:** `/home/user/Site.FirmaDigital/AI-VIRAL-STUDIO/projects/forma-digital/09-qa-report.rev2.md`
- **premissas:** critério de veredito da Revisão 1; D1 a D6 ficam NEEDS_INFO e mantêm "COM RESSALVAS" como teto; severidades de NP-02, NP-04 e NP-05 são julgamento meu.
- **pendências:** ver "Itens não verificados"; correções pedidas ao scriptwriter somente via ECD (1º ciclo de correção após a v2); `[A PESQUISAR]` do ritmo e das plataformas; decisões D-ECD-01 e D1 a D6.
- **autoavaliação:**
  - ✔ Cada achado cita local exato e regra: linhas do v2 e regra em cada NP/NT.
  - ✔ Aderência ao brief, template, não invenção e consistência verificadas: tabelas acima.
  - ✔ Não reescreve o entregável: apenas indica correções.
  - ✔ Veredito justificado por critério: bloqueante/importante/pendência.
  - ✘ Cobertura total: sem shell, sem web, sem releitura de 02/brief/original do teste (declarado em "Itens não verificados").
