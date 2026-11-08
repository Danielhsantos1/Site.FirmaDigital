# Integrações

**Nenhuma integração está implementada ou simulada.** Cada ferramenta tem um arquivo em `integrations/` com campos `[A PESQUISAR]` que só podem ser preenchidos com fonte oficial e data. Política em `.claude/rules/integrations-policy.md`; contrato genérico em `integrations/adapter-contract.md`.

| Ferramenta | Função prevista | Consumidor | Status | Observação |
|---|---|---|---|---|
| Google Veo | Vídeo | prompt-engineer, film-director | Não pesquisado | Forma de acesso, limites e custos desconhecidos nesta fase |
| Kling AI | Vídeo | prompt-engineer, film-director | Não pesquisado | Idem |
| Runway | Vídeo | prompt-engineer, film-director | Não pesquisado | Idem |
| ElevenLabs | Voz/áudio | audio-producer | Não pesquisado | Direitos de voz e termos precisam de leitura dos termos oficiais |
| CapCut | Edição | video-editor | Não pesquisado | Integração automatizada viável **não confirmada**; fallback: plano manual |

## Requisitos transversais (já decididos)
- Credenciais em variáveis de ambiente; nunca no git.
- Toda geração externa exige aprovação explícita do usuário (custo e direitos).
- Log de jobs em `output/<slug>/jobs.log`.
- Falha explícita; sem respostas simuladas.

## Riscos comuns a documentar por ferramenta
Duração máxima por clipe e impacto na consistência; mudanças frequentes de API/planos; direitos sobre a saída e uso comercial; limites de taxa; custo por geração.
