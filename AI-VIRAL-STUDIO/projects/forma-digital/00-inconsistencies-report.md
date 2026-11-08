---
projeto: forma-digital
versão: 1.0
autor-agente: executive-creative-director
data: 2026-11-08
entradas-usadas: [00-brief.md, 00-client-audit.md, _sources/site-extract.md]
status: rascunho   # aguarda decisões do responsável
---

# Relatório de inconsistências e decisões pendentes

Legenda: **CONFIRMADO** (consta no extrato do site, com trecho citado) · **HIPÓTESE** (proposta do estúdio, sem fonte do cliente) · **NEEDS_INFO** (ausente; depende do responsável).
Fonte primária: `_sources/site-extract.md` (extrato do `index.html`, 2026-11-08).

## (a) Auditoria dos 10 pontos

| # | Ponto | Classificação | Evidência / observação |
|---|---|---|---|
| 1 | Nome comercial | **NEEDS_INFO** | Site: "Firma Digital — Daniel Henrique — Desenvolvimento de Sites e Sistemas Web" e "Firma Digital" no menu. O pedido usa "Forma Digital". Nome em uso no projeto: "Forma Digital (provisório, confirmação pendente)". |
| 2 | Serviços | **CONFIRMADO** | "01 · Institucional — Site para negócio local"; "02 · Conversão — Landing page"; "03 · Sob medida — Sistema ou painel simples". Descrições: "Apresentação da empresa, serviços, contato e localização"; "Página única focada em um objetivo: captar contato, apresentar um produto ou divulgar um evento"; "Formulários, cadastros ou painéis de controle para organizar um processo específico do seu negócio". |
| 3 | Públicos | **CONFIRMADO** (A) / **HIPÓTESE** (B, C, D) | A: oferta "pronto para clientes encontrarem você" e "negócio local". B (gestor com processo manual) e C (divulgação de evento) derivam de textos de oferta/caso, mas o site não nomeia públicos-alvo; D (autônomos) sem base alguma. Porte e região atendida: NEEDS_INFO (só "Votorantim, SP" consta). |
| 4 | Diferenciais comprovados | **HIPÓTESE** (declarados, não comprovados) | Declarados: "escopo definido, prazo combinado e nada de 'ajustezinho' que vira retrabalho"; "Pacotes fechados, sem cobrança por hora perdida em ajustes"; "Quatro etapas, aprovação em cada uma"; "código versionado no GitHub"; "HTTPS ativo". Nenhuma evidência anexada (proposta-modelo, exemplo autorizável). Devem ser comunicados como declaração do próprio negócio, não como prova. |
| 5 | Estudos de caso autorizados | **NEEDS_INFO** | Site lista três casos (Plataforma de gestão de treinamentos — "Em produção"; Controle de solicitações de serviço — "Uso interno"; SaaS de ciclo de vida de contratos — "Em desenvolvimento") e diz "Nomes de clientes e materiais internos não são divulgados publicamente". Nenhuma autorização para uso em campanha consta. SaaS de contratos não é oferta (instrução do projeto). |
| 6 | Indicadores comerciais | **NEEDS_INFO** | Site traz "03 Sistemas web em produção", "100% Deploy com HTTPS por padrão", "1:1 Acompanhamento direto comigo". O "03" conflita com os casos (só 1 "Em produção") e **não será usado**. Sem preço, prazo típico, depoimento ou métrica de resultado no site. |
| 7 | Redes sociais | **NEEDS_INFO** | Site: "Redes sociais — Em breve". Nenhum perfil de Instagram/TikTok divulgado. Canais existentes: WhatsApp, e-mail e formulário que abre o e-mail (extrato, linha 5). |
| 8 | Identidade visual | **CONFIRMADO** (parcial) | Extrato: fundo #161826, superfície #232532, texto #e9e9ed, acento #9184d9 / #a7a1db, fonte Inter. Logotipo e manual de marca: NEEDS_INFO. Foto do fundador existe no repositório, não referenciada no HTML; uso NEEDS_INFO. |
| 9 | Restrições de publicidade | **CONFIRMADO** (parcial) | Confirmado: confidencialidade de clientes e materiais internos (trecho acima). Estúdio impõe: sem clientes/telas reais, sem números ou depoimentos inventados, sem "nós" (o site fala em 1ª pessoa: "Acompanhamento direto comigo"). Regras de plataforma/regulatórias (ex.: publicidade, uso de IA rotulada): [A PESQUISAR]. |
| 10 | Pendências | **NEEDS_INFO** | Consolidadas na seção (c) e nas 12 perguntas de `00-brief.md`. |

## (b) Tabela de inconsistências

| # | Inconsistência | Onde | Risco | Tratamento provisório |
|---|---|---|---|---|
| I1 | "Firma Digital" (site) vs. "Forma Digital" (pedido) | Site × pedido | Nome errado em tela/prompts/@ | Usar "Forma Digital (provisório)"; não finalizar peças com nome em tela |
| I2 | "03 Sistemas web em produção" vs. casos (1 "Em produção", 1 "Uso interno", 1 "Em desenvolvimento") | Site, indicadores × estudos de caso | Afirmação falsa/enganosa | Não usar o indicador |
| I3 | "Redes sociais: Em breve" vs. campanha para Instagram/TikTok | Site × objetivo | Sem perfil para publicar | Produção só de planejamento; publicação bloqueada até perfis oficiais |
| I4 | Marca "Digital" institucional vs. texto em 1ª pessoa ("comigo", "Atuo", "Construí") e negócio de uma pessoa | Site | Uso de "nós" seria afirmação não confirmada | Voz condicional à decisão D2 |
| I5 | Foto do fundador no repositório, sem referência no HTML | Repositório × HTML | Uso de imagem/voz por IA sem consentimento | Nenhum avatar/clonagem sem D3 |
| I6 | Caso "Uso interno" com origem profissional possivelmente distinta | Site | Exposição de empregador/contexto | Não citar até confirmação |
| I7 | Casos com tecnologias e detalhes públicos vs. "detalhes sensíveis ficam fora" | Site | Mostrar telas/dados reais | Só ilustrações próprias rotuladas |
| I8 | Diferenciais declarados sem evidência | Site | Parecer promessa/prova | Linguagem de declaração, sem superlativos |

## (c) Etapa 2: decisões do responsável

Nenhuma foi fornecida. Roteiros não podem ser aprovados antes delas.

| # | Decisão | Status | Pergunta objetiva | Bloqueia |
|---|---|---|---|---|
| D1 | Nome oficial | **Forma Digital (provisório, confirmação pendente)** | O nome da marca nas peças é "Forma Digital" ou "Firma Digital"? Há logotipo com grafia definida? | Nome em tela, @, prompts, aprovação de qualquer roteiro |
| D2 | Voz: Daniel ou institucional | **NEEDS_INFO** | As peças falam em 1ª pessoa (Daniel: "eu construo") ou em voz institucional/narrador? | Roteiros, plano de áudio |
| D3 | Autorização de imagem/voz de Daniel por IA | **NEEDS_INFO** | Daniel autoriza, por escrito, avatar ou voz sintética baseados nele? Se sim: quais usos, quais limites, rotulagem? Ou só vídeo real / personagens fictícios rotulados? | Estilo pessoas/avatares, art bible, prompts, áudio |
| D4 | Perfis oficiais de Instagram e TikTok | **NEEDS_INFO** | Existem ou serão criados perfis? Quais @ e quem opera? | Distribuição, CTA, publicação |
| D5 | Situação dos três sistemas em produção | **NEEDS_INFO** | O que o indicador "03" representa? Quais sistemas podem ser citados (e em que nível: setor, função, tela ilustrada)? O de "Uso interno" pode ser citado? | Prova, estudos de caso, qualquer número em tela |
| D6 | Objetivo principal | **NEEDS_INFO** | O objetivo principal é reconhecimento de marca ou geração de contatos (WhatsApp/e-mail/formulário)? Há meta ou período de piloto? | Estratégia, CTA, métricas |

## Rastreabilidade
Fontes: `_sources/site-extract.md` (2026-11-08); `00-brief.md`; `00-client-audit.md`.
Fatos confirmados: serviços, descrições, processo em 4 etapas, estudos de caso e status, indicadores como aparecem no site, "Redes sociais: Em breve", restrição de confidencialidade, paleta e fonte.
Hipóteses: públicos B/C/D; diferenciais como "comprovados"; prioridade de comunicação.
Pendências: D1 a D6; logotipo; autorização de casos e foto; regras de plataforma [A PESQUISAR].
Responsável: executive-creative-director
