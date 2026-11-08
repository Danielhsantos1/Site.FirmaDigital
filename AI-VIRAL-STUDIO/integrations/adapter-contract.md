# Contrato de adaptador (proposta de design, sem código)

Objetivo: permitir plugar ferramentas externas no futuro sem alterar agentes ou skills.

## Princípio
Agentes produzem **especificações** (ex.: `06-prompts.md`, `07-audio-plan.md`). Um adaptador futuro lê a especificação e a executa na ferramenta. Agentes nunca chamam APIs.

## Interface lógica
- `capabilities()` → o que a ferramenta suporta (preenchido a partir da pesquisa oficial).
- `validate(spec)` → confere a especificação contra limites documentados; não executa.
- `submit(spec)` → inicia geração; **exige aprovação explícita do usuário** (custo).
- `status(job)` e `fetch(job)` → acompanha e baixa o resultado para `output/<slug>/`.

## Requisitos de qualquer adaptador
- Credenciais só em variáveis de ambiente.
- Registro de cada chamada (job, custo estimado se conhecido, data) em `output/<slug>/jobs.log`.
- Falha explícita; nunca resposta simulada.
- Linguagem e dependências decididas na fase de implementação (hoje não definidas).
