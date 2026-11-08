# Plano de migração: `AI-VIRAL-STUDIO/` → repositório `Danielhsantos1/AI-Viral-Studio`

**Status: PLANO. Nada foi publicado. Aguarda autorização.**

## Estado verificado hoje
- Repositório de origem: `Danielhsantos1/Site.FirmaDigital`, branch `claude/forma-digital-creative-studio-1v6i4h`, **PR #3 aberto em rascunho**, sem merge.
- Destino `AI-Viral-Studio`: **não encontrado** entre os repositórios acessíveis à sessão (pode não existir ou a sessão não ter acesso).
- Ensaio feito em cópia descartável, sem tocar o repositório real:
  - `git subtree split --prefix=AI-VIRAL-STUDIO` gerou um histórico independente;
  - **76 de 76 arquivos**, idênticos byte a byte (`diff -r`);
  - o validador passou no repositório novo (`OK`);
  - o histórico da subpasta tinha **1 commit** (a Missão 01); o hash muda (9bb2c78 → 139bb29), o conteúdo e a mensagem, com as linhas de coautoria, são preservados.

## Pré-requisitos (ação sua)
1. Criar `github.com/Danielhsantos1/AI-Viral-Studio` **vazio** (sem README, licença ou .gitignore, para evitar históricos sem relação). Recomendo **privado**: o repositório conterá material de cliente.
2. Dar à sessão acesso de escrita a ele (a sessão só alcança repositórios anexados). Não consigo criá-lo nem conceder acesso.

## Passos (todos não destrutivos)
1. Commitar a Missão 02 na branch atual (inclui `projects/forma-digital/`, `tests/`, `docs/`). Assim o histórico migrado fica com 2 commits.
2. Em clone temporário: `git subtree split --prefix=AI-VIRAL-STUDIO -b studio-split`.
3. Em diretório novo: `git init -b main`, `git pull <clone> studio-split`.
4. Verificar: contagem de arquivos, `diff -r` contra a subpasta, `python3 scripts/validate.py`, `bash tests/orchestration/run.sh`.
5. Só então: `git remote add origin …AI-Viral-Studio.git` e `git push -u origin main`.
6. Ajustar `README.md` (remover a nota "Local deste projeto") e confirmar o carregamento abrindo o Claude Code na raiz do repositório novo.

## O que **não** será feito
Apagar a subpasta, branches ou o PR #3; reescrever o histórico do site; mexer em `index.html` ou na foto.

## Destino do PR #3 e da subpasta (decisão sua, depois da migração verificada)
| Opção | Efeito | Observação |
|---|---|---|
| Manter o PR em rascunho indefinidamente | Zero mudança | Deixa duas cópias que divergem |
| Fechar o PR sem merge e depois remover a branch | Site limpo | Irreversível para a branch remota; só após confirmar o novo repositório |
| Fazer merge | Estúdio dentro do repositório do site | **Não recomendado**: mistura site público com ferramenta interna |

## Riscos
- Repositório público do site hoje contém a pasta no branch do PR: informações do cliente em `projects/forma-digital/` serão lidas por quem acessar a branch. Hoje só contêm dados que já estão no site público, mas as perguntas do brief não são públicas. Considere manter o PR privado/fechado.
- `.gitignore` exclui `projects/*` exceto `forma-digital/`; decidir a política para futuros clientes (R6).
