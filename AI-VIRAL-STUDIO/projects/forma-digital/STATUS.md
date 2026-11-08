---
projeto: forma-digital
versão: 0.4
autor-agente: executive-creative-director
data: 2026-11-08
entradas-usadas: [00-brief.v2.md, 00-inconsistencies-report.md, 01-trends.md, 02-strategy.md, 03-script.md, 03-script.v2.md, 04-direction.md, 05-art-bible.md, 06-prompts.md, 07-audio-plan.md, 08-edit-plan.md, 09-qa-report.md, 09-qa-report.rev2.md, 10-performance.md, _qa-test/03-script.SEEDED-DEFECTS.md, _qa-test/03-script.SEEDED-DEFECTS.v2.md]
status: rascunho
---

# Status do projeto: forma-digital (nome provisório)

## Workflow em uso
`workflows/viral-short-video.md` (rascunho). Missão 03, Execução 3c: Revisão 1 e Revisão 2 do Quality Reviewer executadas. Nenhuma mídia gerada, nenhuma API de geração chamada, nada publicado.

## Estado real
**Nenhum roteiro está aprovado para produção.** Enquanto D1 a D6 estiverem pendentes, nenhuma etapa pode ser aprovada. O que o revisor aprovou "com ressalvas" é aprovação operacional de rascunho para continuar o trabalho, não liberação de produção nem promoção de status.

## Vereditos do Quality Reviewer
- **Revisão 1** (`09-qa-report.md`, intacto): `03-script.md` REPROVADO (1 bloqueante RO-01, 6 importantes, 2 menores); 00-brief.v2, 00-inconsistencies-report, 01, 02, 04, 05, 06, 07, 08 e 10 APROVADO COM RESSALVAS; roteiro de teste REPROVADO (9 bloqueantes, 5 importantes).
- **Revisão 2** (`09-qa-report.rev2.md`, escopo só 03.v2 e teste v2): `03-script.v2.md` **APROVADO COM RESSALVAS** (0 bloqueantes, 4 importantes: NP-01 placeholders L_* não substituídos nas linhas 18 a 26; NP-05 "Intenção" em 15 de 18 cenas; mais RO-03 e RO-07 parciais, ligados a NP-04 e NP-02; menores NP-03, NP-06 a NP-08). RO-01, 02, 04, 05, 06, 08, 09 resolvidos. Teste v2 **APROVADO COM RESSALVAS** (SD-01 a SD-16 resolvidos; menores NT-01 a NT-03; sem bloqueante ou importante).
- Aritmética palavras × duração recontada pelo revisor: confere (23 linhas, folga mínima +0,2 s), **somente sob a hipótese de ritmo 0,4 s/palavra, sem fonte** (`[A PESQUISAR]`).

## Versão vigente
| Arquivo | Dono | Vigente | Situação |
|---|---|---|---|
| 00-brief | ECD | 00-brief.v2.md | rascunho, aprovado com ressalvas (B2-01, B2-03 pendentes) |
| 00-inconsistencies-report.md | ECD | v1 | aprovado com ressalvas (IR-01 pendente) |
| 01-trends.md | trend-hunter | v1 | aprovado com ressalvas (TR-01; fontes externas não verificadas) |
| 02-strategy.md | viral-strategist | v1 | aprovado com ressalvas (ES-02) |
| 03-script | scriptwriter | **03-script.v2.md** (substitui 03-script.md, que segue intacto e REPROVADO) | rascunho, aprovado com ressalvas; NÃO aprovado para produção |
| 04-direction.md | film-director | v1 | **desatualizado frente ao 03.v2**: reconfirmar |
| 05-art-bible.md | art-director | v1 | ressalva menor AB-01 |
| 06-prompts.md | prompt-engineer | v1 | **reconfirmar** (P3 e ganchos mudaram) |
| 07-audio-plan.md | audio-producer | v1 | **reconfirmar** (falas, sincronia, CTA) |
| 08-edit-plan.md | video-editor | v1 | **reconfirmar** (contagens, matriz de exportação, CTA) |
| 09-qa-report | quality-reviewer | 09-qa-report.md (Rev. 1) + 09-qa-report.rev2.md (Rev. 2) | existem; Rev. 2 não cobre 04 a 08 |
| 10-performance.md | growth-analyst | v1 | ressalvas menores PF-01, PF-02 |
| _qa-test/03-script.SEEDED-DEFECTS.v2.md | harness/scriptwriter | v2 (não é entregável) | aprovado com ressalvas |

## Decisões (nenhuma tomada pelo responsável)
| # | Decisão | Status |
|---|---|---|
| D1 | Nome oficial | NEEDS_INFO (provisório) |
| D2 | Voz Daniel ou institucional | NEEDS_INFO |
| D3 | Imagem/voz de Daniel por IA | NEEDS_INFO (nada previsto) |
| D4 | Perfis Instagram/TikTok | NEEDS_INFO (publicação bloqueada) |
| D5 | Situação dos sistemas | NEEDS_INFO |
| D6 | Objetivo principal | NEEDS_INFO (CTA em dois ramos) |
| D-ECD-01 | Landing page (Ang-3): incluir P4 ou aceitar omissão | pendente do ECD |

## Pendências
1. **Próxima missão:** reconfirmar 04, 07, 08 e 06 contra o 03.v2 (durações, falas, CTA por proposta, ganchos, P3 com exemplo "Item · Quantidade · Local"). Não feito nesta execução.
2. Pequena v3 do 03 para NP-01 (placeholders), NP-05, NP-02, NP-04 e menores; o 03.v2 não foi editado após a revisão. Teste v2: NT-01 a NT-03 (opcional).
3. D1 a D6 e D-ECD-01; GL-01 (ordem Rastreabilidade × Relatório) e demais itens da Rev. 1 fora do 03 (B2-01, B2-03, IR-01, TR-01, ES-02, achados de 04 a 10).
4. Medir ritmo real de fala; duração-alvo por plataforma, janela de gancho, licenças e regras de rotulagem: `[A PESQUISAR]`.
5. Verificar fontes externas do 01 (revisor sem acesso web).

## Anomalias de processo (registradas)
- A Revisão 1 foi gravada pelo revisor, mas o retorno da delegação veio cortado ("stopped"); conteúdo conferido lendo `09-qa-report.md` (303 linhas, completo).
- A execução 3b foi cortada por limite de uso (429) na delegação 2a; o retorno veio "failed", porém `03-script.v2.md` estava gravado e completo (372 linhas, `substitui: 03-script.md`, tabela, Rastreabilidade com 5 linhas, Relatório). O revisor encontrou nele placeholders não substituídos (NP-01).
- Na Rev. 2 o revisor não tinha shell: o validador é rodado pelo ECD.
