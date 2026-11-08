---
projeto: forma-digital
versão: 0.1
autor-agente: growth-analyst
data: 2026-11-08
entradas-usadas: [02-strategy.md, 01-trends.md, 00-brief.v2.md, 00-inconsistencies-report.md, 03-script.md, 08-edit-plan.md, STATUS.md, _sources/site-extract.md, templates/performance-report.md, .claude/rules/*.md, .claude/skills/performance-analysis/SKILL.md, knowledge/README.md, knowledge/platforms/README.md]
status: rascunho   # sem dados reais; contém avaliação crítica da estratégia e plano de medição; resultado do relatório: NEEDS_INFO
---

# Relatório de desempenho: Forma Digital (nome provisório, D1 pendente)

**Estado deste relatório: NÃO é uma análise de desempenho.** Não existe nenhuma peça produzida como mídia, nada foi publicado e não há perfis (D4). Este documento entrega (1) a avaliação crítica da estratégia no que toca a medição, (2) o plano de medição a executar quando houver publicação e (3) as perguntas que faltam. Nenhum número de desempenho, linha de base, benchmark, meta, taxa "boa" ou tamanho de amostra aparece aqui como fato.

## Como ler este documento
- **Fato**: consta em arquivo do projeto, com o arquivo citado.
- **Opinião analítica**: julgamento deste agente. Vem marcada como `[OPINIÃO]` e pode ser contestada.
- **Proposta**: convenção ou modelo sugerido, a validar com o ECD/responsável. Marcada `[PROPOSTA]`.
- `[A PESQUISAR]`: fato técnico sem fonte. `knowledge/` está vazio (índice de `knowledge/platforms/README.md`: "VAZIO"). Nomes oficiais de métricas, formas de exportação, tipos de conta e janelas de coleta de Instagram e TikTok **não são afirmados**.

## Dados recebidos (origem, período, plataforma)

**Nenhum.**

| Item | Situação | Base |
|---|---|---|
| Métricas exportadas ou informadas | Nenhuma | Nenhuma entrega do usuário ou do ECD com dados |
| Período | n/a | Nada publicado |
| Plataforma | n/a | `site-extract.md`: "Redes sociais: Em breve"; D4 = NEEDS_INFO (`00-inconsistencies-report.md`, `STATUS.md`) |
| Mídia produzida | Nenhuma | `08-edit-plan.md`: "Nenhum vídeo, imagem, áudio, legenda ou arquivo de projeto de edição foi produzido"; os 29 prompts de `06-prompts.md` estão `NÃO EXECUTADO` (citado em `08-edit-plan.md`) |
| Resultados do site (contatos recebidos hoje) | Não informados | NEEDS_INFO (pergunta 14) |

### Resultados
**Sem dados: NEEDS_INFO.** Nada a reportar sobre alcance, retenção, salvamentos, compartilhamentos, contatos ou conversas qualificadas.

## Comparação com hipóteses

Resultado de cada hipótese: **sem dados: NEEDS_INFO**. Abaixo, em vez de resultado, a **prontidão para teste** de H1 a H9 (hipóteses de `02-strategy.md`). A coluna "Cobertura nos ativos atuais" é fato derivado de `03-script.md` e `08-edit-plan.md`; as demais colunas são `[OPINIÃO]`.

| ID | Hipótese (resumo) | Cobertura nos ativos atuais (fato) | Medível com o quê (opinião) | Risco principal de medição (opinião) |
|---|---|---|---|---|
| H1 | Gancho de dor (G1) retém mais que gancho de processo (G4), no mesmo ângulo | **Não coberta.** P1 = Ang-2 + G1 e P2 = Ang-1 + G4 (`03-script.md`): ângulos diferentes. As "variações de gancho" do roteiro são perguntas, sem decupagem (`08-edit-plan.md`, C-9; ED-14) | Retenção nativa da plataforma (nome oficial `[A PESQUISAR]`) | Confundimento gancho × ângulo; precisa de pares com mesmo ângulo |
| H2 | Abrir com resultado visual (G2) gera mais salvamentos que abrir com pergunta (G3) | Não coberta: não há par G2 vs G3 decupado | Salvamentos por alcance | Mesmo problema de H1; depende da métrica de salvamentos existir por plataforma (`[A PESQUISAR]`) |
| H3 | Carrossel (um ponto por slide) gera mais salvamentos/compartilhamentos que Reels no mesmo ponto | **Não coberta.** Nenhum arquivo de 03 a 08 menciona carrossel (busca textual sem ocorrências); só há vídeo vertical | Salvamentos e compartilhamentos por alcance | Peça inexistente; formato e conteúdo mudam juntos |
| H4 | Peça de ponto único retém mais que peça com vários pontos | Parcial: as três peças são de ponto único; **não existe variante com vários pontos** | Retenção | Sem contraponto; durações diferem entre peças (36/37/36 s com contatos, `08-edit-plan.md`) |
| H5 | Bastidor (Ang-1) gera mais conversas que dor (Ang-2) | Parcial: P2 (Ang-1) e P1 (Ang-2) existem como proposta | Contatos com origem registrada | Gancho, ângulo e duração variam juntos entre P1 e P2; volume de contatos provavelmente baixo (opinião, sem número); atribuição sem origem |
| H6 | CTA "conversa sobre seu objetivo" gera mais contatos que "solicitar orçamento" | Parcial: o roteiro prevê trocar a frase final por "Solicitar orçamento" (`03-script.md`, nota do CTA), mas o CTA contatos já cita o botão "Solicitar orçamento" e a frase de conversa juntos; a versão alternativa não está escrita (`08-edit-plan.md`: depende de o ECD devolver o texto) | Contatos por alcance, por CTA | Atribuição de contato; não há mecanismo de link definido (NEEDS_INFO, ED-12); volume |
| H7 | Mesmo conteúdo rende diferente entre Instagram e TikTok | Parcial: mesma timeline pode ser exportada para as duas | Retenção e ação por plataforma | Públicos, métricas e alcance diferem por natureza; D4 para as duas contas |
| H8 | Voz em 1ª pessoa de Daniel retém mais que voz institucional | Variantes de fala existem em texto; **nenhuma locução existe**; voz sintética de Daniel está fora (D3 não autorizado) | Retenção e contatos | Qualidade de gravação confunde com tipo de voz |
| H9 | Texto em tela claro funciona sem áudio | Versão silenciosa planejada na matriz de versões (`08-edit-plan.md`) | Retenção narrada vs silenciosa | Dois grupos de espectadores com hábitos diferentes; exige duas publicações do mesmo conteúdo |

## Avaliação crítica de `02-strategy.md` (medição, distribuição e objetivos)

Escopo: só o que afeta a capacidade de medir e aprender. Não reabro posicionamento, ângulos ou conteúdo criativo.

### Pontos fortes (fato sobre o documento + opinião)
1. **Honestidade metodológica.** A estratégia não fixa meta, não cita benchmark e declara que "a linha de base nasce do piloto" (fato: seção "Objetivo" e "Métricas de sucesso"). `[OPINIÃO]` É a postura correta para este relatório.
2. **Critérios comparativos, não absolutos**, e a regra "mesma plataforma e mesmo período" (fato: seção "Hipóteses testáveis"). `[OPINIÃO]` Adequada para volume baixo.
3. **Reconhece o limite de atribuição**: "contato sem origem identificada não pode ser creditado a uma peça" e propõe registro manual de origem (fato: seção "Objetivo").
4. **Declara o que invalida o piloto**: sem D4, sem D6, sem registro de origem (fato). `[OPINIÃO]` Bom: torna as dependências explícitas.
5. **Princípio "uma variável por teste"** e pedido de poucas hipóteses por ciclo (fato: "Pouco volume"). `[OPINIÃO]` Correto, mas ver fragilidade F1: o desenho atual das peças não o cumpre.

### Fragilidades e riscos de medição

**F1. As três propostas não isolam nenhum fator (confundimento).** Fato: P1 = Ang-2/G1, P2 = Ang-1/G4, P3 = Ang-4/G1-G2, com públicos hipotéticos diferentes (A,C / A,B,C / B) e durações estimadas diferentes (`03-script.md`; `08-edit-plan.md`). `[OPINIÃO]` Qualquer diferença observada entre P1, P2 e P3 mistura ângulo, gancho, tema, público alvo pretendido, duração e ritmo. Isso inviabiliza H1 e H5 como testes controlados com os ativos atuais: H1 e H5 ficam **confundidas entre si** em P1 vs P2 (o mesmo par serviria aos dois e não responde a nenhum). Alternativa: tratar o primeiro ciclo como **exploratório e descritivo** (registrar, não declarar vencedor) e só testar com pares que variam um fator (exemplo: mesma peça, dois ganchos).

**F2. Mais hipóteses que peças.** Fato: 9 hipóteses (H1 a H9); 3 propostas; H1 exige "2 ou mais pares" para definir direção (critério de `02-strategy.md`). Aritmética, não amostra estatística: só H1, com 2 pares, pede no mínimo 4 peças por plataforma; com 2 plataformas, 8. Se H3 e H6 receberem o mesmo tratamento, o piso aritmético implícito sobe de forma multiplicativa. Frequência e volume de peças do piloto são NEEDS_INFO (`02-strategy.md`). `[OPINIÃO]` Sem definir antes quantas peças Daniel consegue produzir e publicar, a lista de hipóteses não é planejável. Tamanho de amostra adequado e método de comparação: `[A PESQUISAR]` (a própria skill `performance-analysis` registra isso como pendente).

**F3. Priorização proposta H1/H3/H6: faz sentido em parte.**
- A seleção cobre três camadas (atenção, compartilhamento, ação) e reduz o número de hipóteses. Fato: a estratégia propõe H1, H3, H6 como prioridade e a chama de "proposta". `[OPINIÃO]` O critério de reduzir é bom.
- **H6 é a menos mensurável das três.** Depende de contatos atribuídos por peça, e o roteiro lista WhatsApp, e-mail e formulário sem vínculo com a peça (`03-script.md`: "Como o espectador chega ao site... NEEDS_INFO"). Fato: o formulário do site tem os campos Nome, Telefone/WhatsApp, E-mail e "O que você precisa?" e abre o e-mail do visitante; não há campo de origem (`site-extract.md`). `[OPINIÃO]` Contatos por peça tendem a ser poucos (sem número, é expectativa) e cada contato sem origem some do teste.
- **H3 exige uma peça que não existe** (carrossel) e mistura formato com conteúdo.
- **H1 é a mais viável analiticamente** (métrica nativa da plataforma, não depende de contato), mas pede decupagem de variações de gancho hoje inexistente (ED-14).
- `[OPINIÃO]` Recomendação alternativa: ver "Recomendações priorizadas".

**F4. Atribuição de contatos.** Fato: contato por WhatsApp/e-mail chega sem origem (estratégia, seção "Objetivo"). `[OPINIÃO]` Riscos adicionais que a estratégia não lista: (a) a pessoa não lembra ou não sabe responder "como chegou?" (viés de autorrelato); (b) contato que viu a peça e depois buscou o site por conta própria; (c) **contatos de rede pessoal ou clientes existentes**, que não vieram da campanha e inflam a contagem; (d) a resposta "não sei" não pode ser redistribuída entre peças; (e) quem registra é quem opera, o que cria viés; (f) tempo de resposta de Daniel afeta se o contato vira conversa, e isso não é efeito da peça.

**F5. "Conversa qualificada" sem definição operacional.** Fato: `02-strategy.md` define "contato que descreve um objetivo compatível com um dos três serviços (critério a ser definido por Daniel)" e marca NEEDS_INFO. `[OPINIÃO]` "Compatível com um dos três serviços" é um filtro de adequação de serviço, não de qualificação (não considera região, intenção, momento ou capacidade de atendimento). Quem classifica é também quem atende, sem regra escrita antes dos dados. Sem esta definição, a métrica de camada "Conversa qualificada" não pode ser calculada.

**F6. D4 ausente e efeito cascata.** Fato: todas as hipóteses H1 a H9 dependem de D4 (`02-strategy.md`). Sem perfis, não há dado de plataforma e não há publicação. Também não se sabe quem opera nem qual o tipo de conta, o que pode condicionar o acesso às métricas nativas (`[A PESQUISAR]`).

**F7. Objetivo de reconhecimento: métrica não mede o que o objetivo diz.** Fato: o objetivo do ramo reconhecimento é "alcance e lembrança do nome" (`02-strategy.md`); as métricas são alcance, contas alcançadas, retenção, compartilhamentos e seguidores novos. Fato: nenhuma peça tem o nome (D1 pendente; `03-script.md`: "nenhum nome em fala ou tela"), e a estratégia diz que o nome não é fixado em peça final. `[OPINIÃO]` Alcance mede exposição, não lembrança; e sem nome na peça, **lembrança do nome não é nem alcançável nem medível** neste desenho. Se D6 = reconhecimento, a meta precisa ser redefinida (por exemplo, para exposição) ou D1 e o uso do nome precisam ser resolvidos.

**F8. Comparação entre plataformas (H7).** Fato: o critério de H7 já alerta que "alcance e público diferem por natureza" e propõe comparar "ação por alcance". `[OPINIÃO]` A razão por alcance também não é comparável entre plataformas se as métricas têm definições diferentes (`[A PESQUISAR]`). Mais seguro: comparar **a direção** da diferença entre variantes dentro de cada plataforma e ver se coincide entre elas, e não o valor entre plataformas. Além disso, a estratégia pede "reaproveitar a mesma ideia com ajuste de formato" e ao mesmo tempo "variar uma só coisa por teste": o ajuste de formato é uma segunda variável (`[OPINIÃO]`).

**F9. Matriz de versões multiplica variantes.** Fato: `08-edit-plan.md` calcula até **36 exportações** antes de multiplicar por plataforma (3 propostas × 2 D2 × 2 D6 × 2 trilha = 24, mais silenciosa 6 ou 12 se houver Camada B), e **9** se D2 e D6 forem respondidas e a Camada B não existir. `[OPINIÃO]` D2 e D6 são **decisões de negócio**, não fatores de teste; tratá-las como variantes de piloto cria dezenas de células com 1 peça cada, nenhuma comparável. Fatores de áudio (com ou sem trilha, silenciosa) são fatores adicionais que confundem H1/H4/H9 se mudarem junto com gancho. Cada exportação a mais também é um item a rotular, registrar e coletar. Apoia a decisão ED-7 do video-editor: fixar D2 e D6 antes e reduzir a matriz.

**F10. D6 = contatos vs reconhecimento muda a peça.** Fato: a Cena 6 varia por D6 e muda a duração (36 vs 32 s, 37 vs 33 s; `08-edit-plan.md`). `[OPINIÃO]` Se as duas versões forem publicadas, CTA e duração mudam juntos; não comparar esses ramos como se fossem um teste de CTA.

**F11. Viés de ordem e maturação da conta.** `[OPINIÃO]` Contas novas não têm base de seguidores (D4), e o desempenho de peças publicadas em momentos diferentes pode mudar por maturação, dia e horário, não só por variante. Como o funcionamento de distribuição por algoritmo não está documentado (`[A PESQUISAR]`), não se pode presumir estabilidade. Mitigação: alternar a ordem de publicação das variantes e registrar data/hora (ver Plano de medição).

**F12. Métrica decisória não definida antes.** Fato: a estratégia lista várias métricas por hipótese e um critério comparativo. `[OPINIÃO]` Falta regra de qual métrica manda quando divergem (retenção alta com poucas ações, por exemplo). Recomenda-se fixar **antes de publicar**, por teste, uma métrica decisória e as de apoio, para evitar escolher depois a que favorece uma variante.

**F13. Capacidade e custos fora do desenho.** Fato: a estratégia cita "Dependência de Daniel" e NEEDS_INFO sobre quem opera (D4). `[OPINIÃO]` Capacidade de produzir, publicar, responder contatos e registrar dados limita todos os testes; orçamento para impulsionamento é desconhecido, e dado pago e orgânico não podem ser misturados. Não há análise de custo de produção por peça.

**F14. Lacunas de evidência herdadas.** Fato: `01-trends.md` tem confiança baixa/média-baixa, só resumos de busca, zero benchmark verificado, nenhum concorrente identificado. `[OPINIÃO]` Não há base externa para chamar nenhum resultado futuro de "bom" ou "ruim"; só comparação interna.

## Diagnóstico e limites da amostra

- **Diagnóstico de desempenho: impossível** (sem dados). Nada é diagnosticado sobre as peças.
- **Diagnóstico do desenho (opinião, ver F1 a F14):** o plano atual não permite aprender com poucas peças; o primeiro ciclo deve ser exploratório e voltado a criar linha de base e a validar o processo de medição.
- **Limites que valerão no futuro:** amostra pequena e conta nova; ruído de distribuição; correlação entre peça e contato não é causa; contato sem origem não é atribuível; tamanho mínimo de amostra `[A PESQUISAR]`; significância estatística não será invocada enquanto não houver método e volume adequados.
- **Correlação vs causa:** um contato registrado "veio do vídeo X" é autodeclaração; mostra associação, não que o vídeo causou a decisão de contratar.

## Recomendações priorizadas

Todas `[OPINIÃO]`, ligadas a hipótese testável quando aplicável.

| Pri. | Recomendação | Por quê | Liga a | Depende de |
|---|---|---|---|---|
| 1 | Responder D4 e D6 e definir quem opera, volume e período do piloto | Sem isso nada é medido | Todas | Responsável, via ECD |
| 2 | Escrever a definição de "contato" e de "conversa qualificada" **antes** de publicar, e criar o registro manual de origem | Evita classificar depois dos dados | H5, H6 | Daniel (definição) |
| 3 | Tratar o **ciclo 1 como exploratório**: publicar as peças aprovadas, coletar métricas e contatos, **não declarar vencedor**, gerar linha de base | O desenho atual confunde fatores (F1) | Linha de base; H5 só como indício | D4, D6 |
| 4 | Dentro do ciclo 1, ter **no máximo um teste controlado**: H1 (mesmo ângulo, dois ganchos, G1 vs G4), com pares repetidos conforme viabilidade | É a hipótese mais viável com métrica nativa e sem depender de contato | H1 | Variação de gancho decupada (ED-14) |
| 5 | **Adiar H6** até existir mecanismo de chegada ao site e registro de origem funcionando e algum volume de contatos | Atribuição frágil e volume provável baixo | H6 | ED-12, D4 |
| 6 | **Adiar H3** até o ECD decidir se o carrossel entra no escopo e ele existir | Não há ativo | H3 | Decisão do ECD |
| 7 | Reduzir a matriz de versões: fixar D2 e D6; um fator de áudio por vez; sem Camada B no ciclo 1 | F9 | H9, H4 | ED-7, D2, D6 |
| 8 | Usar a mesma timeline nas duas plataformas e comparar **direção** das diferenças entre variantes dentro de cada uma | F8 | H7 | D4 (duas contas) |
| 9 | Pesquisar nomes oficiais e exportação de métricas, tipo de conta, janela de estabilização e método para baixo volume; registrar em `knowledge/platforms/` | Base vazia | Todas | Pesquisa (via ECD) |
| 10 | Definir métrica decisória por teste antes de publicar | F12 | Todas | Este plano |

**Sobre priorizar H1/H3/H6 (resposta direta):** `[OPINIÃO]` manter a ideia de poucas hipóteses, mas o trio muda para **H1 como único teste controlado do ciclo 1; H6 e H3 adiados por falta de condições de medição**. H5 e H7 podem rodar como **observação descritiva** sem declarar efeito. Se o responsável quiser manter H6, o pré-requisito é resolver atribuição (mecanismo de link e registro de origem) e informar a capacidade de resposta.

## Plano de medição

Aplica-se quando D4 estiver resolvida e houver publicação. Tudo `[PROPOSTA]` até o ECD/responsável aprovar. Onde faltar base, `[A PESQUISAR]` ou "a preencher". Nenhum valor numérico de meta é sugerido.

### 1. Objetivo, métrica primária e métricas de apoio por ramo D6

| Ramo D6 | Métrica primária | Definição operacional (a preencher) | Métricas de apoio | Fonte do dado | Frequência de coleta |
|---|---|---|---|---|---|
| **Contatos** | Contatos recebidos com origem registrada, por peça/variante | A preencher por Daniel: o que conta como contato (primeira mensagem recebida? formulário enviado? pessoa única?), regra de duplicidade, janela de atribuição (em dias, a definir), exclusão de contatos de rede pessoal/clientes existentes | Conversas qualificadas (subconjunto, ver 3); cliques no link, se existir mecanismo (`[A PESQUISAR]`); salvamentos e compartilhamentos; alcance; retenção | **Contatos:** registro manual de origem (pergunta no primeiro contato; resposta "não sei" é categoria própria). **Plataforma:** analytics nativo, nomes e exportação `[A PESQUISAR]` | Contatos: a cada contato recebido. Plataforma: em janelas fixas após cada publicação (valores a definir; estabilização das métricas `[A PESQUISAR]`) |
| **Reconhecimento** | Alcance / contas alcançadas por peça (nome oficial por plataforma `[A PESQUISAR]`) | A preencher: qual métrica exata de cada plataforma representa "alcance" e se há equivalência entre elas (`[A PESQUISAR]`) | Retenção; compartilhamentos; salvamentos; seguidores novos | Analytics nativo `[A PESQUISAR]` | Janelas fixas após cada publicação (a definir) |
| **Ambos** | NEEDS_INFO | Sem primário definido não há critério de sucesso (`02-strategy.md`) | — | — | — |

**Aviso:** o objetivo de "lembrança do nome" não é medido por nenhuma métrica acima e o nome não consta das peças (F7). Ver NEEDS_INFO, pergunta 3.

Qualquer ramo: meta numérica e período **NEEDS_INFO**; a linha de base nasce do ciclo 1 e a meta só é proposta depois dela, por quem decide (ECD/responsável).

### 2. Convenção de IDs `[PROPOSTA]`

Objetivo: ligar cada dado à peça, proposta, variante, gancho, CTA, formato e plataforma. Parte da convenção de nomes de arquivo já proposta pelo video-editor (`<proposta>_<d2>_<d6>_<audio>`, exemplo `P2_inst_con_semtrilha`, `08-edit-plan.md`), sem nome de marca (D1).

**ID de peça (versão de conteúdo, igual entre plataformas):**
`<ciclo>-<proposta>-<d2>-<d6>-<audio>-<gancho>-<cta>-<formato>`

| Campo | Valores propostos | Observação |
|---|---|---|
| ciclo | `c1`, `c2`, ... | Ciclo de publicação |
| proposta | `P1`, `P2`, `P3` | De `03-script.md` |
| d2 | `dan`, `inst` | Voz; só se D2 já estiver decidida |
| d6 | `con`, `rec` | Ramo da Cena 6 |
| audio | `semtrilha`, `comtrilha`, `silenc` | Como no plano de edição |
| gancho | `gp` (principal do roteiro), `gv` (variação do roteiro), ou família `g1`..`g5` (de `02-strategy.md`) | Um valor por peça |
| cta | `cc` (conversa), `so` (solicitar orçamento) | Só se H6 for testada; senão `cc` por padrão do roteiro |
| formato | `rl` (vertical curto), `ca` (carrossel), `st` (stories) | Só `rl` existe no plano atual |

Formato de exemplo (apenas ilustra o padrão, não é registro): `c1-P2-inst-con-semtrilha-gp-cc-rl`.

**ID de publicação (peça em uma plataforma):** `<ID de peça>-<plataforma>-<seq>`, com `plataforma` = `ig` ou `tt` e `seq` = ordem de publicação daquela peça na plataforma (repetições).

**IDs auxiliares:** `T<n>` = teste (liga hipótese H, fator variado, pares e métrica decisória); `K<nnnn>` = contato (sequencial, sem dados pessoais no ID).
**Rastro de versão:** em cada publicação registrar versão dos insumos (roteiro, direção, plano de edição) usados, para que mudanças de conteúdo entre repetições sejam visíveis.

### 3. Modelos de planilha de coleta (VAZIOS)

Colunas somente; nenhuma linha preenchida. Dado só entra com origem declarada (coluna "origem do dado").

**3.1 Registro de publicações**

| id_publicação | id_peça | proposta | variante (d2/d6/áudio) | gancho | cta | formato | plataforma | conta | data_hora_publicação | duração_real | legenda/texto_de_apoio | rótulo_IA_aplicado | impulsionada (s/n) | id_teste | versão_insumos | URL | observações |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | | | | | |

**3.2 Métricas por publicação (formato longo: uma linha por métrica e coleta)**

| id_publicação | data_coleta | janela_após_publicação | plataforma | nome_oficial_da_métrica | valor | unidade | origem_do_dado (ex.: tela, exportação) | coletado_por | observações (anomalias, mudança de método) |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |

**3.3 Registro de contatos** (sem nome nem telefone; guardar dados pessoais só se necessário e conforme regra de proteção de dados: `[A PESQUISAR]`)

| id_contato | data_hora | canal (WhatsApp/e-mail/formulário/Direct) | origem_declarada (id_publicação / perfil / não sei / outra / rede pessoal) | como_foi_perguntada (a origem) | serviço_de_interesse (site local/landing/sistema/indefinido) | descreveu_objetivo (s/n) | critérios_de_qualificação (campos a definir) | classificação (qualificada/não/indefinida) | classificada_por | tempo_até_primeira_resposta | desfecho (a definir categorias) | observações |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | |

**3.4 Registro de testes e decisões**

| id_teste | hipótese (H) | fator variado (um só) | fatores mantidos fixos | pares/repetições previstas | métrica decisória (definida antes) | métricas de apoio | critério de decisão (qualitativo, escrito antes) | plataforma | período | dados completos? (s/n) | resultado (direção) | decisão (adotar provisório / repetir / inconclusivo / descartar) | limitações | data_decisão |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | | |

### 4. Regras de comparação
1. **Um fator por teste** (gancho, ou ângulo, ou CTA, ou formato, ou áudio). Tudo o mais fixo: mesma proposta de conteúdo, mesma duração (dentro do que o plano de edição permitir), mesmo áudio, mesma legenda/texto de apoio, mesmo rótulo.
2. **Mesma plataforma, mesma conta e período comparável.** Nunca comparar valores absolutos entre plataformas (F8).
3. **Mesma janela de coleta** para todas as peças comparadas (valor definido antes).
4. **Alternar a ordem de publicação** entre variantes e repetições; registrar data/hora (F11).
5. **Peças orgânicas e impulsionadas não se misturam** na mesma comparação.
6. **Não comparar peças de duração ou conteúdo estruturalmente diferentes como se fossem um teste de uma variável** (P1 vs P2 vs P3 é descrição, não teste; F1).
7. **Declarar a métrica decisória e o critério antes de publicar** (F12). Mudança depois exige registro justificado.
8. Reportar **contagem bruta junto com razões** (por alcance); razões com denominador pequeno são instáveis (`[OPINIÃO]`).
9. Contatos "não sei", "rede pessoal" e "outra origem" ficam fora das contas por peça e são reportados à parte.

### 5. Critérios de decisão (qualitativos)
Nenhum limiar numérico é fixado; tamanho de amostra e método estatístico `[A PESQUISAR]`.
- **Adotar como direção provisória**: a diferença tem o mesmo sentido em todas as repetições previstas, na métrica decisória e (se houver) nas duas plataformas, e é maior que a variação observada entre peças da mesma variante (leitura visual da planilha).
- **Repetir**: sentido consistente, mas poucas repetições, ou sentidos diferentes entre plataformas.
- **Inconclusivo (manter ambas)**: sentidos mistos, empate, ou diferença dentro da variação entre peças iguais.
- **Descartar**: apenas com contra-evidência repetida; uma peça fraca isolada não descarta uma hipótese.

### 6. O que NÃO concluir com poucos dados
- Não declarar "ganhou" ou "perdeu" com um único par ou uma única peça.
- Não afirmar causa a partir de associação peça-contato (autodeclaração).
- Não concluir que um ângulo atrai mais contatos com poucos contatos atribuídos; é anedótico.
- Não tratar ausência de contatos como fracasso da peça sem checar mecanismo de chegada, canal e capacidade de resposta.
- Não inferir preferência dos públicos A/B/C: a segmentação de público disponível em plataforma não foi pesquisada (`[A PESQUISAR]`).
- Não inferir lembrança de nome, funcionamento de algoritmo, vida útil de tendência (T1 a T4) nem efeito de rotulagem de IA.
- Não usar valores externos como régua ("taxa boa"): nenhum benchmark foi verificado (`01-trends.md`, números "não adotados").
- Não generalizar de uma conta nova para outras contas ou para outras plataformas.
- Não projetar meta futura a partir de um ciclo.

### 7. Ciclo pós-publicação (quando existirem dados)
1. **Receber os dados com origem**: plataforma, período, conta, método de exportação ou captura de tela, e quem coletou.
2. **Conferir integridade**: ids em 3.1, métricas em 3.2, contatos em 3.3; registrar lacunas e anomalias (peça removida, edição, impulsionamento).
3. **Resumo descritivo** por publicação, sem comparar ainda; contagens brutas e razões lado a lado.
4. **Aplicar os critérios pré-registrados** (3.4 e seção 5) a cada teste; rotular o resultado como adotar provisório / repetir / inconclusivo / descartar.
5. **Diagnóstico** com limites de amostra e a separação correlação/causa.
6. **Recomendações** ligadas a hipóteses testáveis e desenho do próximo ciclo (um fator por teste).
7. **Definir linha de base descritiva** do ciclo 1; só então o ECD/responsável decide se propõe meta e período.
8. **Relatório ao Diretor** com agentes a reacionar e por quê; nova versão gravada como `10-performance.v2.md` com cabeçalho `substitui:` após revisão do quality-reviewer (regra de versões em `.claude/rules/handoff-format.md`).

## Plano de testes

Proposto, condicionado a D4/D6 e à decisão do ECD. Nenhuma peça nem publicação existe.

| Ciclo | Teste | Hipótese | Fator variado | Condição para rodar | Métrica decisória (proposta) | Observação |
|---|---|---|---|---|---|---|
| c1 | Exploratório descritivo | Linha de base; H5 e H7 como observação | Nenhum (peças como são) | D4 e D6 resolvidos | Conforme ramo D6 | Sem declarar vencedor |
| c1 | T1: ganchos G1 vs G4 no mesmo ângulo | H1 | Gancho | Variações decupadas (ED-14); pares repetidos | Retenção nativa (`[A PESQUISAR]`) | Único teste controlado proposto |
| c2 ou depois | T2: CTA conversa vs orçamento | H6 | Texto do CTA | Mecanismo de chegada (ED-12), registro de origem funcionando, volume de contatos observado | Contatos atribuídos por alcance | Adiado |
| c2 ou depois | T3: carrossel vs Reels | H3 | Formato | Carrossel no escopo e produzido | Salvamentos e compartilhamentos por alcance | Adiado |
| depois | H2, H4, H8, H9 | | | Variantes não existentes; D2/D3 | `[A PESQUISAR]` | Sem plano nesta versão |

## NEEDS_INFO: perguntas ao responsável (via ECD)

1. **D4 (perfis):** existem ou serão criados perfis de Instagram e TikTok? Quais plataformas entram no piloto? Quando? Tipo de conta?
2. **D4 (operação):** quem publica e quem acompanha as métricas? Há acesso ao analytics nativo e a exportação dos dados?
3. **D6:** o objetivo primário é contatos ou reconhecimento? Se "ambos", qual é o primário? Se reconhecimento, o que significa "lembrança do nome" e como se aceita medi-lo, dado que as peças não trazem o nome (D1)?
4. **Meta e período:** existe meta (qualquer tipo) ou o piloto serve apenas para criar linha de base? Duração do piloto, quantidade de peças e frequência de publicação desejadas?
5. **Capacidade:** quantas peças Daniel consegue produzir e publicar por período? Quantas conversas consegue atender e em quanto tempo responde? Horários de atendimento?
6. **Conversa qualificada:** qual é o critério de Daniel (que informações o contato precisa trazer; região atendida; tipo de serviço; intenção)? Quem classifica?
7. **Origem do contato:** Daniel aceita perguntar "como chegou até mim?" no primeiro contato? Aceita incluir esse campo no formulário do site (decisão dele, sobre o site)? O site tem algum analytics hoje (o extrato mostra só o texto visível)?
8. **Chegada ao site:** como o espectador chega ao site ou ao WhatsApp a partir do perfil (link, botão, Direct)? Há domínio definido? (ED-12)
9. **Contatos atuais:** hoje chegam contatos pelo site? Quantos, de onde, e qual a proporção vinda de rede pessoal? (só se Daniel quiser informar, com origem e período)
10. **Orçamento:** haverá impulsionamento pago ou ferramentas pagas de analytics/planilha? Sem aprovação explícita nenhuma integração paga é configurada (`integrations-policy.md`).
11. **Dados pessoais:** como Daniel prefere guardar o registro de contatos (planilha local? qual ferramenta?) e quais dados pessoais aceita registrar? Regra de proteção de dados aplicável: `[A PESQUISAR]`.
12. **D2 e D6 como decisões:** podem ser respondidas antes do piloto para reduzir a matriz de versões (ED-7)?
13. **D1:** qual nome entra em legenda, perfil e registros? Até lá, IDs sem marca.
14. **Dados existentes:** há qualquer métrica real já disponível (por exemplo, visitas ao site, contatos recentes)? Se sim, informar com período e plataforma.

## Agentes a reacionar

Pedidos ao ECD (este agente não instrui outros especialistas):
- **ECD:** decidir D4, D6, ED-7 (matriz de versões) e se H6 e H3 ficam adiados; levar as perguntas acima ao responsável.
- **viral-strategist:** avaliar, a pedido do ECD, a revisão do desenho de testes (F1, F2, F7, F8, F12) e o objetivo de "lembrança do nome".
- **scriptwriter:** se o ECD aprovar T1 (H1), pedir variações de gancho G1 vs G4 no mesmo ângulo (ED-14) e, se H6 voltar, o texto da variante de CTA.
- **video-editor:** alinhar a matriz de versões e a convenção de nomes de arquivo ao plano de medição, quando D2/D6 estiverem decididas.
- **trend-hunter:** pesquisa das lacunas L1, L2, L3 de `01-trends.md` com foco em: nomes oficiais e exportação de métricas, tipo de conta e acesso ao analytics, janela de estabilização de métricas, regras de rotulagem de IA; registro em `knowledge/platforms/`.
- **quality-reviewer:** revisão deste relatório, no gate que o ECD definir.

## Rastreabilidade
Fontes: `projects/forma-digital/02-strategy.md` (v1.0, rascunho); `03-script.md` (v0.1); `08-edit-plan.md` (v0.1); `01-trends.md`; `00-brief.v2.md`; `00-inconsistencies-report.md`; `STATUS.md`; `_sources/site-extract.md` (2026-11-08); `templates/performance-report.md`; `.claude/rules/*.md`; `.claude/skills/performance-analysis/SKILL.md`; `knowledge/README.md` e `knowledge/platforms/README.md` (vazios, 2026-11-08). Nenhuma fonte externa consultada; nenhum dado de plataforma.
Fatos confirmados: não há dados, mídia nem publicação; D1 a D6 sem resposta; a estratégia tem H1 a H9, critérios comparativos e propõe H1/H3/H6 como prioridade; P1/P2/P3 usam ângulos e ganchos diferentes (`03-script.md`); nenhum arquivo de 03 a 08 prevê carrossel; o site tem formulário sem campo de origem e canais WhatsApp, e-mail e formulário; a matriz de versões do plano de edição chega a até 36 exportações antes de multiplicar por plataforma; `knowledge/platforms/` está vazio.
Hipóteses: todos os itens `[OPINIÃO]` (F1 a F14, prioridades, sobre H1/H3/H6) e `[PROPOSTA]` (IDs, planilhas, regras, critérios, plano de testes); a expectativa de volume baixo de contatos; efeito de ordem e maturação de conta; viés de autorrelato.
Pendências: perguntas 1 a 14; `[A PESQUISAR]` nomes oficiais e exportação de métricas por plataforma, tipo de conta e acesso ao analytics, janela de estabilização, equivalência de métricas entre plataformas, método de comparação e tamanho de amostra para baixo volume, proteção de dados no registro de contatos, segmentação de público disponível; D1 a D6; ED-7, ED-12, ED-14.
Responsável: growth-analyst

## Relatório ao Diretor
- **agente:** growth-analyst
- **tarefa recebida:** gravar `projects/forma-digital/10-performance.md` (inexistente) conforme `templates/performance-report.md`, sem dados reais: avaliação crítica de `02-strategy.md` (distribuição, objetivos, métricas, priorização H1/H3/H6, riscos de medição), plano de medição por ramo D6 (métricas, definições a preencher, fontes, frequência, IDs, planilhas vazias, regras de comparação, critérios qualitativos, o que não concluir, ciclo pós-publicação), lista NEEDS_INFO e "Dados recebidos: nenhum". Sem inventar linha de base, benchmark, meta ou nome de métrica.
- **arquivos consultados:** `projects/forma-digital/02-strategy.md`; `01-trends.md`; `00-brief.v2.md`; `00-inconsistencies-report.md`; `03-script.md` (inteiro); `08-edit-plan.md` (inteiro, em duas leituras); `STATUS.md`; `_sources/site-extract.md`; `templates/performance-report.md`; `.claude/skills/performance-analysis/SKILL.md` (recebida no contexto da sessão); regras `.claude/rules/*.md` (recebidas no contexto); `knowledge/README.md`; `knowledge/platforms/README.md`. Listei `projects/forma-digital/`; `10-performance.md` não existia. Busca textual por "carrossel|Stories|carousel" em `03` a `09`: sem ocorrências. Não li `04-direction.md`, `05-art-bible.md`, `06-prompts.md`, `07-audio-plan.md`, `00-client-audit.md` nem `00-brief.md` (v1); `06-prompts.md` e `07-audio-plan.md` só aparecem por citação do `08-edit-plan.md`.
- **trabalho realizado:** relatório de estado sem dados ("Dados recebidos: nenhum"; resultados "sem dados: NEEDS_INFO"); matriz de prontidão de H1 a H9; avaliação crítica com 5 pontos fortes e 14 fragilidades, separando fato, `[OPINIÃO]` e `[PROPOSTA]`; achados principais: (i) P1/P2/P3 confundem ângulo, gancho, público e duração, então H1 e H5 não são testáveis com os ativos atuais; (ii) H3 não tem peça (carrossel inexistente); (iii) H6 tem a pior capacidade de medição (atribuição, sem mecanismo de link, sem campo de origem no formulário, volume provável baixo); (iv) o objetivo "lembrança do nome" não é medido pelas métricas e as peças não trazem o nome; (v) a matriz de até 36 exportações trata D2/D6 como variantes quando são decisões; (vi) "conversa qualificada" sem definição operacional; (vii) comparação entre plataformas por "ação por alcance" é frágil; recomendação alternativa à priorização: ciclo 1 exploratório com no máximo H1 como teste controlado, H6 e H3 adiados; plano de medição com métrica primária/apoio por ramo, convenção de IDs, 4 modelos de planilha vazios, regras de comparação, critérios qualitativos, lista do que não concluir e ciclo pós-publicação; plano de testes proposto; 14 perguntas NEEDS_INFO; pedidos de reacionamento ao ECD.
- **skills aplicadas:** `performance-analysis`: passo 1 (registro de origem, período e plataforma: nenhum dado, estrutura de registro entregue), passo 2 (comparação com hipóteses: apenas prontidão, sem resultado), passo 3 (limites de amostra declarados), passo 4 (recomendações e testes priorizados), passo 5 (agentes a reacionar), passo 6 (template preenchido; sem dados, entrega limitada ao plano de medição e NEEDS_INFO, com seções adicionais de avaliação crítica).
- **status:** NEEDS_INFO. Sem métricas reais nem decisões D4/D6, nenhuma análise de desempenho é possível; plano de medição entregue como rascunho.
- **entregáveis:** `/home/user/Site.FirmaDigital/AI-VIRAL-STUDIO/projects/forma-digital/10-performance.md`
- **premissas:** (1) "dados reais" significam métricas exportadas ou informadas; nenhuma foi recebida; (2) IDs, colunas de planilha, regras de comparação e critérios de decisão são propostas do growth-analyst, não padrão da plataforma; (3) nenhum limiar numérico foi proposto (nem janelas de coleta, nem amostra mínima); (4) `H1/H3/H6` como "prioridade proposta" é da estratégia, e a recomendação alternativa é opinião analítica; (5) o site não tem campo de origem, mas o extrato só traz texto visível, então a existência de analytics no site é desconhecida; (6) a minimização de dados pessoais no registro de contatos é boa prática de processo, não aconselhamento jurídico.
- **pendências:** perguntas 1 a 14 deste relatório (D4, D6, meta/período, capacidade, definição de qualificada, origem do contato, mecanismo de chegada, orçamento, dados pessoais, D1/D2); `[A PESQUISAR]`: nomes oficiais e exportação de métricas por plataforma, tipo de conta e acesso ao analytics, janela de estabilização, equivalência entre plataformas, método e amostra para baixo volume, proteção de dados no registro, segmentação de público; decisões ED-7, ED-12, ED-14; `scripts/validate.py` não executado por este agente (sem shell neste escopo); revisão do quality-reviewer não acionada.
- **autoavaliação:**
  - ✔ Todo número tem origem declarada: os únicos números (9 hipóteses, 3 propostas, 36 e 9 exportações, 36/37 s etc.) vêm de `02-strategy.md`, `03-script.md` ou `08-edit-plan.md`, citados; nenhum dado de desempenho, linha de base, benchmark ou meta.
  - ✔ Sem dados reais, o relatório se limita ao plano de medição e retorna NEEDS_INFO: seção de resultados diz "sem dados: NEEDS_INFO"; nenhuma análise de desempenho.
  - ✔ Separa correlação de causa: seções de diagnóstico, regras de comparação e "O que não concluir" explicitam que atribuição de contato é autodeclaração e associação.
  - ✔ Recomendações ligadas a hipóteses testáveis: tabela de recomendações e plano de testes ligam cada item a H1 a H9 e a condição para rodar.
  - ✔ Declara limitações da amostra: sem amostra; limites futuros (conta nova, volume baixo, ruído, ordem) e `[A PESQUISAR]` para tamanho mínimo e método.
  - ✔ Não projeta nem estima métricas inexistentes: "volume baixo de contatos" aparece só como expectativa marcada `[OPINIÃO]`, sem número.
  - ✔ Não acessa plataformas nem altera artefatos de outros agentes: nada foi acessado; alterações pedidas (ED-14, ED-7, texto de CTA) estão como pedidos ao ECD.
  - ✘ Aprovabilidade e utilidade imediata: o relatório não pode ser usado para decisão de desempenho nem aprovado antes de D4/D6 e de dados reais (limitação externa); os `[A PESQUISAR]` de métricas e método seguem abertos.
