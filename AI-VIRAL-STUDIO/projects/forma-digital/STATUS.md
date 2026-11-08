---
projeto: forma-digital
versão: 0.3
autor-agente: executive-creative-director
data: 2026-11-08
entradas-usadas: [00-brief.v2.md, 00-inconsistencies-report.md, 01-trends.md, 02-strategy.md, 03-script.md, 04-direction.md, 05-art-bible.md, 06-prompts.md, 07-audio-plan.md, 08-edit-plan.md, 10-performance.md]
status: rascunho
---

# Status do projeto: forma-digital (nome provisório)

## Workflow em uso
`workflows/viral-short-video.md` (rascunho). Missão 03, Execução 2: etapas 3 a 8 e 10 produzidas em rascunho; **nenhum gate do Quality Reviewer executado**. Nenhuma mídia foi gerada, nenhuma API de geração chamada, nada publicado.

## Etapa atual
Rascunhos de 03 a 08 e 10 existem. Todos condicionais a D1 a D6. **Nenhum roteiro está aprovado** e nenhuma etapa pode ser aprovada antes das decisões. Próximo passo: respostas do responsável a D1 a D6 e depois gate do Quality Reviewer (09-qa-report.md, não criado).

## Etapas
| Arquivo | Dono | Status | QA |
|---|---|---|---|
| 00-client-audit.md | executive-creative-director | rascunho (inalterado) | não revisado |
| 00-brief.md | executive-creative-director | rascunho (v1, inalterado; substituído logicamente pela v2) | não revisado |
| 00-inconsistencies-report.md | executive-creative-director | rascunho, existe | não revisado |
| 00-brief.v2.md | executive-creative-director | rascunho, **versão vigente do brief**; aguarda D1 a D6 | não revisado |
| 01-trends.md | trend-hunter | entregue, DONE com ressalvas; evidência fraca (só resumos de busca) | não revisado |
| 02-strategy.md | viral-strategist | entregue, NEEDS_INFO parcial; condicional a D1 a D6 | não revisado |
| 03-script.md | scriptwriter | entregue, NEEDS_INFO parcial; 3 propostas (P1, P2, P3), variantes D2 e D6; **não aprovado**. Uma correção de rótulo de rastreabilidade (ciclo 1 de 2) após o validador | não revisado |
| 04-direction.md | film-director | entregue, NEEDS_INFO parcial; 29 planos; 14 riscos de IA; só gráfico/motion, sem pessoa | não revisado |
| 05-art-bible.md | art-director | entregue, NEEDS_INFO parcial; só paleta/fonte do site; sem personagens; decisões E1 a E12 pendentes ao ECD | não revisado |
| 06-prompts.md | prompt-engineer | entregue, NEEDS_INFO parcial; 29 prompts em formato genérico, **NÃO EXECUTADOS**; nenhuma ferramenta definida | não revisado |
| 07-audio-plan.md | audio-producer | entregue, NEEDS_INFO parcial; voz de Daniel/clone = NEEDS_INFO (D3); direitos [A PESQUISAR] | não revisado |
| 08-edit-plan.md | video-editor | entregue, NEEDS_INFO parcial; exportação [A PESQUISAR]; decisões ED-1 a ED-14 pendentes | não revisado |
| 09-qa-report.md | quality-reviewer | **não acionado, não existe** | n/a |
| 10-performance.md | growth-analyst | entregue, NEEDS_INFO; sem dados reais, só crítica da estratégia e plano de medição | não revisado |

## Decisões
Nenhuma do responsável. Nome em uso: "Forma Digital (provisório, confirmação pendente)".

| # | Decisão | Status |
|---|---|---|
| D1 | Nome oficial | provisório, confirmação pendente |
| D2 | Voz Daniel ou institucional | NEEDS_INFO (roteiro/áudio/edição em variantes) |
| D3 | Autorização de imagem/voz de Daniel por IA | NEEDS_INFO (nada previsto com avatar/voz sintética) |
| D4 | Perfis oficiais Instagram/TikTok | NEEDS_INFO (publicação bloqueada) |
| D5 | Situação dos sistemas em produção | NEEDS_INFO |
| D6 | Objetivo principal | NEEDS_INFO (CTA em dois ramos) |

## Pendências
- D1 a D6 (perguntas em `00-inconsistencies-report.md`, seção c). Publicação bloqueada por D4.
- Conflitos de tempo fala × cena (07 e 08) e divergências fala × texto em tela: exigem decisão do ECD e eventual revisão do roteiro pelo scriptwriter.
- Decisões ao ECD registradas nos arquivos: E1 a E12 (05), ED-1 a ED-14 (08), ED-7/ED-12/ED-14 (10), abrangência do rótulo "ilustrativo", "valor" e "GitHub" em tela, como o espectador chega ao site.
- Ferramentas de geração, edição e voz: nenhuma definida; `knowledge/` e `integrations/` sem informação pesquisada.
- Itens `[A PESQUISAR]`: durações, proporção, zonas seguras, exportação, loudness, rotulagem de IA, regras publicitárias, licenças (Inter, trilha, SFX, voz), nomes de métricas.
- Quality Reviewer não acionado para nenhum entregável (01 a 08, 10).
- Validador: `python3 scripts/validate.py` retornou OK após a correção de rótulo no 03.
