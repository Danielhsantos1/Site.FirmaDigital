---
projeto: forma-digital
versão: 0.1
autor-agente: art-director
data: 2026-11-08
entradas-usadas: [04-direction.md, 03-script.md, 00-brief.v2.md, 02-strategy.md, 00-inconsistencies-report.md, _sources/site-extract.md, templates/art-bible.md, .claude/rules/*.md, .claude/skills/visual-identity-consistency/SKILL.md, knowledge/consistency/README.md, knowledge/prompts-image/README.md]
status: rascunho   # condicional a D1 a D6; direção (04) e roteiro (03) também são rascunho; nada aqui foi produzido ou testado
---

# Art bible: Forma Digital (nome provisório, D1 pendente)

Tudo neste documento é **plano e especificação**. Nenhuma imagem, vídeo ou áudio foi produzido. Nenhuma ferramenta de geração é escolhida. Este documento não contém prompts.

## Como ler este documento
Rótulos usados:
- **FATO (site)**: consta em `_sources/site-extract.md` (linha 7, "Fatos de CSS"). É a única base de cor e fonte aqui.
- **PROPOSTA (sem base no site)**: decisão de estúdio para preencher lacuna. Não é identidade confirmada. Pode ser trocada.
- **HIPÓTESE**: expectativa não validada.
- **[A PESQUISAR]** / **NEEDS_INFO**: sem base documentada ou dependente do responsável.

`knowledge/consistency/` e `knowledge/prompts-image/` estão **VAZIOS**. Nenhuma técnica de consistência por ferramenta está documentada; todas ficam `[A PESQUISAR]`.

## Conceito visual

**Ideia.** O vídeo se parece com o site: escuro, sóbrio, tipográfico, com formas simples e repetíveis. O mundo visual é o de **diagrama em tela**: cartões, nós, blocos, linhas e marcas de aprovação sobre fundo liso. Sem pessoa, sem foto, sem cenário realista (conforme `04-direction.md`).

**Porquê (hipótese).** (1) A direção é gráfica/motion, então a identidade precisa viver em poucos elementos. (2) Peças com poucas formas reduzem o risco de inconsistência entre planos (R2 da direção). (3) Usar só a paleta e a fonte do site liga a peça ao site sem inventar identidade nova. Nenhum dos três pontos foi validado.

**Tom visual (do brief v2, hipótese):** direto, profissional, próximo; sem hype, sem superlativo, sem urgência artificial. Traduzido em regra: sem brilho exagerado, sem efeitos chamativos, sem cores fora da paleta. "Sem efeitos chamativos" é decisão de estilo, não afirmação de eficácia.

**Sem pessoa nesta versão.** D2 e D3 pendentes. Ver "Fichas de personagem".

**Estilos do brief v2** (motion, animação, tecnologia, viral, cinematográfico): este art bible cobre **somente o estilo gráfico/motion**, o único decupado em `04-direction.md`. Estilo cinematográfico ou com pessoas exige decisão do ECD, nova decupagem e novo art bible (ver Pendências).

## Paleta, tipografia e estilo

### Paleta (FATO, site)
| Papel | Hex | Base |
|---|---|---|
| Fundo | `#161826` | FATO (site, CSS) |
| Superfície | `#232532` | FATO (site, CSS) |
| Texto | `#e9e9ed` | FATO (site, CSS) |
| Acento 1 | `#9184d9` | FATO (site, CSS) |
| Acento 2 | `#a7a1db` | FATO (site, CSS) |

Limites do que o extrato diz: ele lista as cinco cores, mas **não informa em que elemento cada acento é usado** (botão, link, hover, destaque) nem proporções. Portanto:

- **PROPOSTA (sem base no site):** acento 1 `#9184d9` para elementos gráficos preenchidos ou traçados (marca de aprovação, nó concluído, contorno de pacote); acento 2 `#a7a1db` para destaque secundário ou texto pequeno em acento. A divisão é minha; o site pode usar de outro modo. **[A PESQUISAR]** no CSS completo se quiser alinhar.
- **Nenhuma outra cor.** Sem branco puro, sem preto puro, sem cinza avulso, sem vermelho/verde/amarelo de status. Se uma peça precisar de cor auxiliar, ela **não está autorizada** por este documento; o ECD decide e a cor entra rotulada "proposta, sem base no site".
- **Tons intermediários** (transparência, mistura entre as cores) **não estão no site**. PROPOSTA: evitar; quando indispensável para hierarquia, usar apenas as cinco cores acima (ex.: elemento secundário em `#232532` sobre `#161826`, em vez de um cinza novo). A direção cita "blocos cinza" no wireframe (P2-C3) e "ícone/traço"; este documento traduz "cinza" para **superfície `#232532`**.
- **Mapa de uso (PROPOSTA):**
  - Fundo do quadro: `#161826`, liso, mesmo tom do primeiro ao último quadro.
  - Cartões, blocos, wireframe, campos, colunas: `#232532`.
  - Texto em tela e linhas de contorno principais: `#e9e9ed`.
  - Marcas de aprovação, nó ativo, contorno "fechado", indicador de progresso: acento.
  - Rótulo "ilustrativo": `#e9e9ed` (ver regra do rótulo).
- **Contraste:** não calculei razão de contraste. **HIPÓTESE:** texto `#e9e9ed` sobre `#161826` e sobre `#232532` é claro/escuro o bastante para leitura em tela pequena; o acento sobre `#161826` idem. Verificação com método (razão de contraste conforme norma adotada) e teste em tela real de celular: **[A PESQUISAR]** antes de aprovar. Texto em acento sobre `#232532` é o par mais incerto: evitar texto longo nesse par até a verificação.
- **Cor no vídeo exportado:** o hex do site é referência de tela web. Comportamento da cor após geração, edição e compressão por plataforma (perfil de cor, fidelidade do hex): **[A PESQUISAR]**; a aprovação da cor deve ser feita sobre o quadro exportado, não sobre o hex.

### Tipografia
- **Família: Inter** (FATO, site: Google Fonts). Nenhuma outra família. Sem fonte de apoio.
- **Pesos, tamanhos, entrelinha, espaçamento entre letras:** o extrato **não** os registra. Ficam **[A PESQUISAR]** (CSS completo do site). Até lá, não declaro escala tipográfica como fato.
  - **PROPOSTA (sem base no site), apenas relações, sem valores:** dois níveis de texto em tela: (1) **principal** (uma frase do roteiro, maior), (2) **secundário** (rótulo ou apoio, menor). Rótulo "ilustrativo" é o menor da peça. Os tamanhos reais dependem de proporção e zona segura, **[A PESQUISAR]** (R12 da direção).
- **Licença de uso de Inter em vídeo comercial:** **[A PESQUISAR]** (não confirmada neste projeto).
- **Se Inter não estiver disponível na ferramenta de edição:** substituição não decidida; **NEEDS_INFO**/ECD. Não improvisar outra fonte.
- **Acentuação:** o texto em tela é em português do Brasil com acentos; fonte deve renderizar acentos corretamente (R1). Verificar quadro a quadro.
- **Texto em tela é camada de edição**, não imagem gerada (R1 da direção). Esta regra vale para o art bible: a fonte Inter só é garantida quando o texto é composto, não gerado.

### Estilo gráfico
Atributos fixos do estilo (todos PROPOSTA de estúdio, sem base no site, salvo cores e fonte):
- **2D chapado.** Sem sombra projetada, sem brilho, sem gradiente, sem textura, sem 3D, sem fotografia. Os valores de efeitos (se o site usa sombra/gradiente) não constam no extrato: **[A PESQUISAR]**; na dúvida, não usar.
- **Formas básicas permitidas** (as mesmas da direção): retângulo/cartão com cantos, nó (círculo), contorno aberto/fechado, linha, marca de aprovação, indicador circular de progresso, grade, coluna. Raio de canto: **[A PESQUISAR]**; regra: **um único raio em todo o projeto**.
- **Linha:** uma única espessura em todo o projeto (valor **[A PESQUISAR]**, dependente de proporção). Extremidades e cantos iguais em todos os elementos.
- **Marca de aprovação:** **um símbolo único** (um "visto" simples), igual em P1-C5, P2 inteiro, e onde mais aparecer. Mesma espessura, mesma cor de acento.
- **Ícones genéricos** (relógio em P1-C4, cadeado em P2-C5): desenhados na mesma linha e cantos das demais formas, sem detalhe de marca, sem semelhança deliberada com ícone de produto real. O site não traz ícones no extrato, então são PROPOSTA.
- **Hierarquia:** uma coisa em foco por plano. Foco = elemento em acento ou texto principal; o resto em superfície/contorno.
- **Movimento (estilo, não técnica):** entradas simples; sem rotação decorativa, sem balanço, sem partículas. Catálogo de movimentos e curvas: **[A PESQUISAR]** (direção).

### Composição gráfica (regras)
1. **Um bloco de texto por plano** (direção). Texto sobre área limpa (fundo liso ou superfície).
2. **Eixo de leitura:** vertical, de cima para baixo, em P1 e P2 (direção). P3 centralizado, com a única exceção horizontal em P3-C4-S1 (esquerda para direita).
3. **Disposição fixa dos 4 nós** (P1-C5, P2-C1, P2-C5): mesma coluna, mesmo espaçamento, mesmo tamanho, mesma ordem (Escopo, Protótipo, Construção, Publicação); só muda o estado (vazio, ativo, aprovado). Contagem sempre conferida: 4 nós, 3 cabeçalhos em P3.
4. **Margens iguais** em todas as peças; **nenhum texto ou rótulo colado na borda**. Valores e zonas seguras por plataforma: **[A PESQUISAR]**.
5. **Terço superior** para texto principal quando houver diagrama abaixo (conforme direção em P1-C2-S2, P2-C1, P3-C3-S2); **centro** para cartão de tipografia (P1-C1, CTA).
6. **Simetria:** colunas de P3-C4-S2 simétricas e do mesmo tamanho.
7. **Respiro:** área vazia é parte do estilo. Sem preencher o quadro com elementos decorativos.
8. **Fundo contínuo:** mesmo `#161826` do início ao fim da peça. Mudança de "ambiente" entre cenas é feita só pela mudança de elementos, nunca do fundo.
9. **Quadro final do CTA estático** e sem elemento além do texto previsto no roteiro.

### Regras de texto em tela
1. Só o texto previsto em `03-script.md` mais: os rótulos de ilustração e os 3 cabeçalhos genéricos de P3 (direção). Nada de texto extra "de enfeite".
2. **Fonte única** Inter; **cor** `#e9e9ed` por padrão; acento só em destaque curto (uma palavra ou numeração de etapa, como "1 ·", **PROPOSTA**).
3. **Sem hashtags, sem @, sem "link na bio", sem URL, sem telefone/e-mail/endereço** (D4, direção).
4. **Sem nome de marca** (D1): onde um nome seria necessário, **espaço reservado `[NOME-D1]`**. Espaço reservado = área de assinatura vazia e alinhada ao eixo, **não** preenchida com "Forma Digital" nem "Firma Digital". Em quadro de trabalho, `[NOME-D1]` pode aparecer como marcador **somente em material interno**, nunca em exportação final.
5. **Sem números** que pareçam dado, preço, prazo ou estatística. Exceção: a numeração de etapas do próprio roteiro ("4 etapas", "1 · Escopo"…) e o "4" de "4 etapas"; são fatos do site (quatro etapas).
6. **Legível sem som** (H9 da estratégia, hipótese): o texto carrega o sentido; sem depender de áudio.
7. Capitalização e pontuação **exatamente como no roteiro**; revisão ortográfica obrigatória quadro a quadro (R1).
8. Tamanho mínimo, tempo mínimo de leitura, número máximo de palavras por plano: **[A PESQUISAR]**.
9. **Canais** (WhatsApp, E-mail, Solicitar orçamento) e **GitHub**: só como **texto** em Inter, sem ícone e sem logotipo de terceiros. Aceitação do texto "GitHub" em tela: pendência para o ECD (divergência 6 da direção).
10. **Legendas** da fala: formato/posição **[A PESQUISAR]**; não definidas aqui.

### Rótulo "ilustrativo" (aparência, HIPÓTESE)
Textos do rótulo (do roteiro/direção): "Situação ilustrativa" (P1-C1), "Ilustrativo" (P2), "Exemplo fictício, ilustrativo" (P3), "Modelo declarado pelo negócio" (P1-C4, função em dúvida; ver pendências).
- **Aparência (HIPÓTESE de legibilidade; PROPOSTA de estilo):** Inter, nível secundário (o menor da peça), `#e9e9ed`, sem acento, sem caixa colorida; fica **legível mas discreto**.
- **Posição:** canto inferior, **sempre a mesma posição** e alinhamento em todos os planos onde aparece; afastado da borda; posição final sujeita à zona segura (**[A PESQUISAR]**).
- **Camada fixa na edição** (R5): não gerada, não animada em movimento próprio, não some no meio de uma cena.
- **Se o rótulo cobrir o que for rotulado**, o rótulo vale a cena; se o elemento ilustrativo aparecer em dois planos seguidos, o rótulo permanece nos dois.
- **Abrangência (decisão do ECD):** ver Pendências. Recomendação PROPOSTA no fim deste documento.
- Redação do rótulo em conformidade com regra publicitária ou de plataforma: **[A PESQUISAR]**. Este rótulo **não substitui** o rótulo de conteúdo de IA da plataforma (R13), cuja regra também é **[A PESQUISAR]**.

### Estilo de demos e interfaces fictícias (abstratas)
Valem para: grade/planilha, formulário, painel, wireframe, barra de endereço, bloco de código, documento/folha (P1-C3, P2-C2/C3/C4/C5, P3).
1. **Abstratas e genéricas.** Conteúdo de células, campos, cartões e linhas = **barras e blocos sólidos** (cor de superfície ou contorno), nunca texto legível, **exceto** os rótulos de coluna/campo genéricos previstos: "Pedido", "Status", "Prazo" (P3) e títulos de etapa (P2).
2. **Zero números e moeda:** sem dígitos em células, sem R$, sem %, sem gráfico com eixo ou valores, sem data, sem relógio com hora legível.
3. **Zero logotipo, ícone ou aparência de produto de terceiros:** nada que lembre planilha, navegador, rede social, app de mensagem ou plataforma específica (barra de menus, abas, botões no estilo de um produto). Sem tela real, sem captura de tela, sem dado real.
4. **Sem texto de marca em botão:** botão do formulário = forma sem texto (direção).
5. **Barra de endereço vazia** (sem URL) e **cadeado genérico** na mesma linha das demais formas.
6. **Código = linhas curtas abstratas**, sem caracteres (R9).
7. **Sem relação com o SaaS de contratos, "03 sistemas", nomes de cliente ou telas reais do site** (brief v2). Nada nas formas deve parecer o painel ou os casos de estudo do site.
8. **Mesma linguagem visual das outras formas** (cantos, linha, paleta): a "interface" é um diagrama, não uma simulação de produto.
9. **Estado "vazio"** (nós, blocos) em contorno; **estado "ativo"** com acento; **estado "aprovado"** com marca de aprovação em acento. Mesmo código em todas as peças.
10. **Morph** entre estados (grade → campos → cartões): técnica **[A PESQUISAR]**; alternativa de planejamento é montar estados e cortar/compor na edição (R10).

## Fichas de personagem (atributos fixos)

**Nenhum personagem é necessário nem previsto nas três propostas.** Não há ficha.

Regras para o caso de a decisão mudar (condicionais; nada disso está autorizado hoje):
- **Daniel Henrique:** nenhum avatar, imagem, rosto, corpo, silhueta reconhecível ou voz de Daniel (D3 pendente). **A foto do fundador existe no repositório do site, mas não é usada**; uso é **NEEDS_INFO**. Nenhum personagem pode ter semelhança deliberada ou acidental com Daniel; essa semelhança deve ser checada em revisão se houver personagem.
- **Personagem fictício rotulado:** só se o ECD decidir, com rótulo visível ("personagem fictício") e **ficha completa** (aparência, proporção, figurino, paleta restrita às 5 cores, expressão) a ser escrita **antes** de qualquer geração. **Ficha não existe nesta versão.** Consistência de personagem entre planos por ferramenta: **[A PESQUISAR]** (`knowledge/consistency/` vazio).
- **Plano sem rosto** (detalhe de objeto, sem figura humana identificável): possível pela direção, mas não previsto; mesma restrição de paleta e estilo.
- **Voz:** fora do escopo do art bible. Nenhuma voz sintética de Daniel (D3).

## Fichas de cenário (atributos fixos)

"Cenário" aqui = **ambiente gráfico** (fundo + elementos fixos). Todos usam fundo `#161826`, Inter, a paleta e as regras de estilo acima. A coluna "Planos" refere-se à decupagem de `04-direction.md`.

### CEN-01. Fundo liso
- **Descrição:** quadro totalmente liso `#161826`, sem textura, sem gradiente, sem elemento decorativo.
- **Atributos fixos:** cor única; igual em todas as cenas e nas três propostas.
- **Planos:** todos. **Aberto:** se o fundo do CTA pode reaproveitar elemento da peça (opcional na direção; decisão de edição).
- **Não pode:** variar de tom entre planos; ter vinheta, ruído ou grão (não há base no site).

### CEN-02. Cartão de tipografia
- **Descrição:** texto centralizado em bloco único, com rótulo (quando houver) no canto inferior.
- **Atributos fixos:** Inter, `#e9e9ed`, margens iguais, um bloco de texto.
- **Planos:** P1-C1-S1; CTA (Px-C6a-S1/S2, Px-C6b-S1); P3-C5-S1 (texto).
- **Não pode:** logotipo, nome, @, ícone de rede/canal.

### CEN-03. Diagrama de nós (4 etapas)
- **Descrição:** coluna vertical com 4 nós, espaçamento igual, ordem fixa (Escopo, Protótipo, Construção, Publicação); estados vazio / ativo / aprovado.
- **Atributos fixos:** 4 nós, mesmo diâmetro, mesma linha de conexão (se houver), marca de aprovação única em acento, texto no topo.
- **Planos:** P1-C5-S1/S2; P2-C1-S1; P2-C5-S2; versão reduzida em canto no CTA de P2 (se a edição optar).
- **Não pode:** número de nós diferente de 4 (R11); nomes nos nós em P1-C5 (a direção os quer sem nomes); mudança de ordem/posição entre planos.

### CEN-04. Folha, lista e wireframe (documento ilustrativo)
- **Descrição:** retângulo em superfície `#232532` com linhas/barras abstratas; evolui de lista (P2-C2) para wireframe (P2-C3/C4/C5) com blocos para cabeçalho, imagem e texto, **vazios**.
- **Atributos fixos:** mesmo retângulo-base, mesmo raio, mesmo eixo vertical, blocos vazios, sem texto legível exceto o rótulo previsto.
- **Planos:** P1-C3-S1/S2, P1-C4-S1 (contorno fechado sobre a folha), P2-C2 a C5.
- **Não pode:** conteúdo final, lorem ipsum, URL, logotipo, código legível, aparência de navegador/CMS de terceiros.

### CEN-05. Acúmulo e pacote (P1-C2, P1-C4)
- **Descrição:** bloco-base abstrato com cartões abstratos que encaixam e se acumulam; indicador circular de progresso que nunca fecha; depois contorno fechado, ícone genérico de relógio e traço riscado.
- **Atributos fixos:** cartões em superfície, contorno em acento no estado "fechado"; indicador em acento; riscado em `#e9e9ed` ou acento (um só, fixar em revisão).
- **Planos:** P1-C2-S1/S2; P1-C4-S1/S2.
- **Não pode:** pessoa, balão de conversa, tela de mensagem (interface inventada), cifra, moeda, hora legível.

### CEN-06. Grade, formulário e painel (P3, exemplo fictício)
- **Descrição:** grade genérica com barras; 3 cabeçalhos ("Pedido", "Status", "Prazo"); abas em cascata; formulário de 3 campos e botão sem texto; painel de 3 colunas de status com cartões abstratos.
- **Atributos fixos:** 3 cabeçalhos / 3 campos / 3 colunas; mesma superfície e mesma linha; rótulo "Exemplo fictício, ilustrativo" na posição fixa; sem números.
- **Planos:** P3-C1 a C5.
- **Não pode:** células com números, gráficos com valores, nomes de aba legíveis, aparência de planilha/painel de terceiros ou do sistema real do site.

### CEN-07. Quadro final (CTA)
- **Descrição:** fundo liso; lista vertical de três rótulos de texto (contatos) ou texto "Salvar · Compartilhar" (reconhecimento); frase final em área limpa.
- **Atributos fixos:** Inter, `#e9e9ed`, espaçamento igual, quadro final estático, **área de assinatura reservada `[NOME-D1]` vazia**.
- **Planos:** Px-C6a, Px-C6b.
- **Não pode:** logotipo do WhatsApp, e-mail ou plataforma; botões de plataforma recriados; telefone, e-mail, endereço, @ ou URL; nome da marca.

## Referências visuais (origem)

Referências = **apenas os elementos do próprio site**, sem imagem copiada, gerada ou anexada aqui:
| Referência | Origem | O que se tira dela |
|---|---|---|
| Cores `#161826`, `#232532`, `#e9e9ed`, `#9184d9`, `#a7a1db` | `_sources/site-extract.md`, linha 7 (CSS do `index.html`, commit 6423482, extraído em 2026-11-08) | Paleta |
| Fonte Inter (Google Fonts) | idem | Tipografia |
| Estrutura de 4 etapas numeradas ("Etapa 1" a "Etapa 4") | `_sources/site-extract.md`, linhas 78 a 91 | Ordem e rótulos dos nós |
| Numeração/rotulagem de serviços ("01 · Institucional", etc.) | idem, linhas 45 a 53 | Padrão de rótulo curto |

**Não foram consultadas imagens do site renderizado, captura de tela, logotipo ou manual de marca** (inexistentes no extrato / NEEDS_INFO). Nenhuma referência externa (filme, artista, perfil, estilo "tipo X") é citada. Referências externas poderão entrar depois, só com origem e data.

## Regras de consistência

Verificáveis (checklist, cada item sim/não em revisão; atributos fixos):
| # | Regra | Como verificar |
|---|---|---|
| RC1 | Fundo = `#161826` em 100% dos quadros | Conferir cor do fundo no quadro exportado |
| RC2 | Só as 5 cores do site aparecem | Inspeção visual; qualquer cor fora da lista reprova |
| RC3 | Só Inter | Inspeção do texto composto; nenhuma outra família |
| RC4 | Texto = o do roteiro, com acentos, sem erro | Comparar quadro a quadro com `03-script.md` |
| RC5 | Texto em camada composta, não gerado | Verificar na edição |
| RC6 | 4 nós, mesma coluna, mesma ordem nos planos P1-C5, P2-C1, P2-C5 | Sobrepor quadros |
| RC7 | 3 cabeçalhos/campos/colunas em P3 | Contagem |
| RC8 | Uma espessura de linha e um raio de canto em todo o projeto | Medir após definir os valores ([A PESQUISAR]) |
| RC9 | Marca de aprovação: um símbolo único, em acento | Comparar |
| RC10 | Rótulo "ilustrativo" na mesma posição, mesma aparência, sem sumir no meio da cena | Comparar planos |
| RC11 | Nenhum número, moeda, data, gráfico com valor | Revisão de cada quadro |
| RC12 | Nenhum logotipo, ícone ou aparência de produto de terceiros | Revisão de cada quadro |
| RC13 | Nenhum nome de marca, @, URL, telefone, e-mail | Revisão de cada quadro |
| RC14 | Nenhuma pessoa, rosto, mão, avatar, silhueta | Revisão de cada quadro |
| RC15 | Sem 3D, sombra, gradiente, textura, brilho | Revisão de cada quadro |
| RC16 | Cada plano tem um foco só | Revisão |

Consistência **entre as 3 propostas** (P1, P2, P3):
- Mesmo fundo, mesma paleta, mesma fonte, mesmas margens, mesma linha, mesmo raio, mesmo símbolo de aprovação, mesma posição e aparência do rótulo.
- As propostas se diferenciam por **conteúdo gráfico** (acúmulo/pacote em P1; 4 nós e wireframe em P2; grade/formulário/painel em P3), nunca por estilo, cor ou fonte. Peças comparáveis em piloto (H1, H4) não devem variar de estilo (hipótese: variar só uma coisa por teste, como na estratégia).
- O quadro final (CTA) tem a mesma construção nas três (CEN-07), variando só o texto do ramo D6.

Consistência **entre planos**:
- Elementos que atravessam planos (cartão, nó, folha) mantêm tamanho relativo, cor e linha; mudam só de posição/estado.
- Ordem de planos e cortes conforme direção; transição "corte seco" é descrição de direção, não afirmação de efeito.

**Técnicas de consistência por ferramenta:** **[A PESQUISAR]** (documentar e testar antes de qualquer geração). Mitigação já proposta pela direção: elementos simples e repetíveis; montagem por camadas na edição (R2, R11). Aqui acrescento: montar o quadro como camadas compostas (fundo, forma, texto, rótulo) reduz a dependência de consistência de geração. Isso é **hipótese**, não testada.

## O que evitar

- Cores fora das 5 (incluindo branco/preto puros, cinzas avulsos, cores de status).
- Qualquer fonte que não seja Inter; texto gerado por IA em imagem.
- Pessoas, rostos, mãos, avatares, silhuetas; semelhança com Daniel; uso da foto do fundador; voz sintética de Daniel.
- Nome de marca (Forma/Firma Digital) em tela ou prompts; logotipo próprio (NEEDS_INFO); @ ou "link na bio".
- Logotipos, ícones ou aparência de WhatsApp, GitHub, plataformas sociais, navegadores, planilhas, painéis de terceiros.
- Telas reais, capturas, dados reais, nomes de cliente, "03 sistemas", SaaS de contratos, estudos de caso do site.
- Números, preços, moedas, datas, porcentagens, estatísticas, gráficos com valores, depoimentos.
- Efeitos: 3D, sombra, brilho, gradiente, textura, partículas, lens flare, glitch, zoom dramático.
- Estética de "urgência", "promoção", "viral", superlativo visual (selos, explosões, setas chamativas).
- Referência a filmes, artistas, perfis, estilos "tipo X" (nenhuma referência externa registrada).
- Rótulo ilustrativo que desapareça, mude de posição ou fique ilegível.
- Mudança de ordem, contagem ou posição dos nós e cabeçalhos.
- Descrever, citar ou apresentar como existente qualquer imagem/vídeo ainda não produzido.
- Texto longo no par acento sobre superfície (contraste não verificado).
- Dependência de uma ferramenta de geração específica: nenhuma foi escolhida.

## Pendências e propostas para decisão do ECD

| # | Item | Minha recomendação (PROPOSTA, não decisão) |
|---|---|---|
| E1 | **Abrangência do rótulo "ilustrativo"** (peça inteira ou só onde o roteiro cita; divergências 1 a 3 da direção) | Rótulo em **todo plano com elemento ilustrativo**, mesma posição e aparência, e persistente dentro da cena. Motivo: evita deixar um quadro fictício sem rótulo. Reduz o risco de a demo parecer real (R3). Custo: mais texto em tela (compete com o texto principal). Regra publicitária/plataforma: [A PESQUISAR] |
| E2 | Função de "Modelo declarado pelo negócio" (P1-C4): rótulo de declaração ou de ilustração? | Tratar como **segundo texto em tela, nível secundário**, mesma aparência do rótulo, sem acento, na posição do rótulo. Confirmar com o roteirista via ECD |
| E3 | Cor auxiliar ou tons intermediários | **Não usar**. Se o ECD autorizar, entra como "proposta, sem base no site" |
| E4 | Atribuição de papéis aos dois acentos | Usar a divisão proposta acima, ou ECD obter o CSS completo para confirmar |
| E5 | Se Inter não estiver disponível na ferramenta de edição | NEEDS_INFO; não decidir substituta |
| E6 | Logotipo e manual de marca | **NEEDS_INFO**; área `[NOME-D1]` reservada |
| E7 | Foto do fundador | **NEEDS_INFO**; não usada |
| E8 | D1 (nome), D2 (voz), D3 (IA de Daniel), D4, D5, D6 | Pendentes; D3 condiciona qualquer personagem |
| E9 | Ampliar para outros estilos do brief (cinematográfico, com pessoas) | Só após D2/D3; novo art bible |
| E10 | Aparência do texto "GitHub" e do "valor" em tela | Aceitar só como texto em Inter, se o ECD aprovar (divergências 5 e 6 da direção) |
| E11 | Fundo do CTA reaproveita elemento da peça? | Opcional, só P1 e P2, como a direção; em P3 não |
| E12 | Valores de espessura de linha, raio, margem, tamanhos de fonte, zonas seguras, proporção | **[A PESQUISAR]** (CSS do site e documentação das plataformas) |

## Rastreabilidade
Fontes: `_sources/site-extract.md` (2026-11-08; paleta e fonte, linha 7; etapas, linhas 78 a 91); `projects/forma-digital/04-direction.md` (v0.1, rascunho); `03-script.md` (v0.1, rascunho); `00-brief.v2.md`; `02-strategy.md`; `00-inconsistencies-report.md`; `templates/art-bible.md`; `.claude/rules/*.md`; `.claude/skills/visual-identity-consistency/SKILL.md`; `knowledge/consistency/README.md` e `knowledge/prompts-image/README.md` (ambos VAZIOS, 2026-11-08).
Fatos confirmados: cores `#161826`, `#232532`, `#e9e9ed`, `#9184d9`, `#a7a1db` e fonte Inter (Google Fonts), segundo o extrato do site; o processo tem quatro etapas com nomes Escopo, Protótipo, Construção, Publicação; a foto do fundador existe no repositório e não é referenciada no HTML; logotipo e manual de marca não constam; `knowledge/consistency/` e `knowledge/prompts-image/` não têm conteúdo documentado.
Hipóteses: atribuição de papéis às cores (fundo, superfície, texto, acentos); legibilidade e contraste das combinações de cor (não calculados); aparência e posição do rótulo "ilustrativo"; estilo 2D chapado, formas, linha única, raio único, marca de aprovação única; ícones genéricos; escala tipográfica em dois níveis; montar por camadas reduz dependência de consistência de geração; peças com poucas formas reduzem risco de inconsistência.
Pendências: D1 a D6; logotipo e manual de marca (NEEDS_INFO); foto do fundador (NEEDS_INFO); decisões E1 a E12 do ECD; [A PESQUISAR]: CSS completo (papéis dos acentos, pesos, tamanhos, raio, espessura, sombras/gradientes), licença de Inter em vídeo comercial, método de verificação de contraste, comportamento de cor após exportação, proporção e zonas seguras, tamanho mínimo e tempo de leitura, regra de rotulagem de IA e publicitária, técnicas de consistência por ferramenta, catálogo de movimentos/morph.
Responsável: art-director

## Relatório ao Diretor
- **agente:** art-director
- **tarefa recebida:** gravar `projects/forma-digital/05-art-bible.md` segundo `templates/art-bible.md`, usando só a paleta e a fonte reais do site (#161826, #232532, #e9e9ed, #9184d9/#a7a1db; Inter); definir composição, texto em tela, rótulo "ilustrativo", estilo de demos fictícias abstratas, consistência entre planos e entre as 3 propostas, e o que não fazer; sem personagens (ou só fictícios rotulados), sem Daniel (D3), sem foto do fundador, logotipo NEEDS_INFO, `[NOME-D1]` reservado, sem referências inventadas, sem prompts, sem instruir outros especialistas.
- **arquivos consultados:** `projects/forma-digital/04-direction.md`; `03-script.md`; `00-brief.v2.md`; `02-strategy.md`; `00-inconsistencies-report.md`; `_sources/site-extract.md`; `templates/art-bible.md`; `knowledge/consistency/README.md`; `knowledge/prompts-image/README.md`; regras `.claude/rules/*` (recebidas no contexto da sessão). Listei `projects/forma-digital/` (`05-art-bible.md` não existia). `.claude/skills/visual-identity-consistency/SKILL.md` foi recebido no contexto da invocação (não reaberto). Não li `01-trends.md`, `00-client-audit.md`, `00-brief.md` nem `STATUS.md`.
- **trabalho realizado:** art bible com conceito visual; paleta (5 cores do site, papéis propostos e rotulados); tipografia (Inter; escala e pesos `[A PESQUISAR]`); estilo 2D chapado; regras de composição (9) e de texto em tela (10); aparência proposta do rótulo "ilustrativo"; regras de demos fictícias (10); "sem ficha de personagem" com regras condicionais; 7 fichas de cenário (ambientes gráficos) mapeadas aos planos da direção; referências restritas aos elementos do site; 16 regras de consistência verificáveis, mais consistência entre propostas e entre planos; lista do que evitar; 12 pendências/propostas para o ECD.
- **skills aplicadas:** `visual-identity-consistency`, passos 1 a 5 (conceito, paleta e estilo a partir do brief e do site; fichas de cenário; referências reais com origem, restritas ao site; regras verificáveis e lista do que evitar; preenchimento do template com seções extras de pendências). Passo 2 para personagem: não aplicável (nenhum personagem). Técnicas por ferramenta: `[A PESQUISAR]`, como a skill manda.
- **status:** NEEDS_INFO (parcial). Art bible entregue como rascunho; aprovação depende de D1 a D6, de decisões E1 a E12 e do CSS completo do site para valores de estilo.
- **entregáveis:** `/home/user/Site.FirmaDigital/AI-VIRAL-STUDIO/projects/forma-digital/05-art-bible.md`
- **premissas:** (1) só o estilo gráfico/motion da direção; (2) paleta e fonte do extrato são a identidade visual vigente, sem logotipo nem manual; (3) papéis das cores e dos dois acentos são minha proposta, o extrato não os informa; (4) "bloco cinza" da direção foi traduzido para a superfície `#232532` para não criar cor nova; (5) ícones genéricos (relógio, cadeado) e a marca de aprovação são proposta de estúdio; (6) nenhuma cor, tamanho, espessura ou raio numérico foi afirmado como fato; (7) rótulo "ilustrativo" aplicado a todo plano com elemento fictício é recomendação, não decisão.
- **pendências:** D1 a D6; logotipo/manual de marca e foto do fundador (NEEDS_INFO); E1 a E12 acima (em especial E1 abrangência do rótulo, E2 função de "Modelo declarado pelo negócio", E5 fonte substituta, E9 ampliar estilos); `[A PESQUISAR]`: CSS completo, licença de Inter, método de contraste, cor após exportação, proporção/zonas seguras, tamanho e tempo de leitura, rotulagem de IA e publicitária, técnicas de consistência por ferramenta, morph. Conflito leve levantado: a direção cita "blocos cinza" e "faixa de contraste" (P3-C1); este art bible usa superfície `#232532` e não cria cinza nem faixa de cor nova.
- **autoavaliação:**
  - ✔ Cada personagem/cenário tem ficha reutilizável: sem personagens (justificado e com regras condicionais); 7 fichas de cenário com descrição, atributos fixos, planos e proibições.
  - ✔ Regras de consistência verificáveis: 16 itens com método de verificação; atributos fixos listados (cores, fonte, contagem de nós/cabeçalhos, posição do rótulo). Valores numéricos de linha/raio dependem de [A PESQUISAR].
  - ✔ Respeita ativos e restrições de marca do brief: só paleta e fonte do site; sem nome, logotipo, foto, Daniel, clientes, SaaS, "03", números; `[NOME-D1]` reservado.
  - ✔ Referências com origem e nenhuma imagem fictícia: só elementos do extrato, com linha e data; nenhuma referência externa; nenhuma mídia descrita como existente.
  - ✔ Técnicas de consistência por ferramenta em [A PESQUISAR]: `knowledge/` vazio; nada afirmado como técnica documentada.
  - ✔ Limites de atuação: sem imagens, sem prompts finais, sem alterar roteiro ou decupagem, sem instruir outros especialistas (só pedidos de decisão ao ECD).
  - ✘ Aprovabilidade e completude de estilo: não aprovável (D1 a D6 pendentes) e sem valores de tamanho, peso, espessura e raio por falta do CSS completo (limitação externa).
