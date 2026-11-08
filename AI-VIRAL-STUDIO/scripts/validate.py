#!/usr/bin/env python3
"""Validador estrutural do AI Viral Studio. Somente biblioteca padrão.
Uso: python3 scripts/validate.py   (código de saída 1 se houver erro)"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
AGENTS = ["executive-creative-director", "trend-hunter", "viral-strategist", "scriptwriter",
          "film-director", "art-director", "prompt-engineer", "audio-producer",
          "video-editor", "quality-reviewer", "growth-analyst"]
SECTIONS = ["## Identidade e responsabilidade", "## Objetivo", "## Entradas esperadas",
            "## Saídas obrigatórias", "## Critérios de qualidade", "## Limites de atuação",
            "## Regras de comunicação com o diretor"]
DIRS = [".claude/agents", ".claude/skills", ".claude/rules", "knowledge", "templates", "workflows",
        "integrations", "projects", "output", "packages", "scripts"]
FILES = ["CLAUDE.md", "README.md", "ARCHITECTURE.md", "AGENTS.md", "SKILLS.md", "WORKFLOWS.md",
         "INTEGRATIONS.md", "IMPLEMENTATION-ROADMAP.md", ".gitignore"]
errors, warns = [], []
err = lambda m: errors.append(m)

def frontmatter(p):
    t = p.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n", t, re.S)
    if not m: return None, t
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1); fm[k.strip()] = v.strip()
    return fm, t

def backtick_paths(text):
    for s in re.findall(r"`([^`\n]+)`", text):
        if re.match(r"^(templates|knowledge|integrations|workflows|\.claude)/[\w./-]+$", s) or (re.match(r"^[A-Z-]+\.md$", s) and s != "STATUS.md"):
            yield s

for d in DIRS:
    if not (ROOT / d).is_dir(): err(f"diretório ausente: {d}")
for f in FILES:
    if not (ROOT / f).is_file(): err(f"arquivo ausente: {f}")

found = sorted(p.stem for p in (ROOT / ".claude/agents").glob("*.md"))
if found != sorted(AGENTS):
    err(f"agentes divergem da lista oficial: extras={set(found)-set(AGENTS)} faltando={set(AGENTS)-set(found)}")
skills_dirs = {p.name for p in (ROOT / ".claude/skills").iterdir() if p.is_dir()}
agent_skills = {}
for a in AGENTS:
    p = ROOT / ".claude/agents" / f"{a}.md"
    if not p.exists(): continue
    fm, text = frontmatter(p)
    if not fm: err(f"{a}: frontmatter ausente"); continue
    if fm.get("name") != a: err(f"{a}: name do frontmatter != arquivo")
    for k in ("description", "tools"):
        if not fm.get(k): err(f"{a}: frontmatter sem {k}")
    for s in SECTIONS:
        if s not in text: err(f"{a}: seção ausente '{s}'")
    if "Relatório ao Diretor" not in text: err(f"{a}: sem referência ao Relatório ao Diretor")
    fm_sk = re.findall(r"^\s+-\s+([\w-]+)\s*$", text.split("\n---\n")[0], re.M)
    m = re.search(r"## Skills associadas\n(.*)", text)
    sk = re.findall(r"`([\w-]+)`", m.group(1).split("\n##")[0]) if m else []
    agent_skills[a] = sk
    if not sk: err(f"{a}: sem skills associadas")
    if sorted(fm_sk) != sorted(sk): err(f"{a}: frontmatter 'skills' {fm_sk} difere de 'Skills associadas' {sk}")
    for s in sk:
        if s not in skills_dirs: err(f"{a}: skill inexistente '{s}'")
    if a != "executive-creative-director" and "Agent" in fm.get("tools", ""):
        err(f"{a}: especialista não deve ter a ferramenta Agent")
    if a == "executive-creative-director":
        if not re.search(r"(^|,\s*)Skill(,|$)", fm.get("tools", "")): err("ECD: ferramenta Skill ausente (sem ela não invoca skills)")
        m2 = re.search(r"Agent\(([^)]*)\)", fm.get("tools", ""))
        listed = {x.strip() for x in m2.group(1).split(",")} if m2 else set()
        if listed != set(AGENTS) - {a}: err(f"ECD: Agent(...) deve listar exatamente os 10 especialistas (atual: {sorted(listed)})")
    for ref in backtick_paths(text):
        if not (ROOT / ref).exists(): err(f"{a}: referência quebrada '{ref}'")

owned = {s for v in agent_skills.values() for s in v}
for sd in sorted(skills_dirs):
    p = ROOT / ".claude/skills" / sd / "SKILL.md"
    if not p.is_file(): err(f"skill {sd}: SKILL.md ausente"); continue
    fm, text = frontmatter(p)
    if not fm: err(f"skill {sd}: frontmatter ausente"); continue
    if fm.get("name") != sd or not re.fullmatch(r"[a-z0-9-]{1,64}", sd): err(f"skill {sd}: name inválido/diferente da pasta")
    d = fm.get("description", "")
    if not d: err(f"skill {sd}: description vazia")
    elif len(d) > 1024: err(f"skill {sd}: description > 1024 caracteres")
    for s in ("## Quando usar", "## Procedimento", "## Saída", "## Referências", "## Conhecimento a pesquisar"):
        if s not in text: err(f"skill {sd}: seção ausente '{s}'")
    if sd not in owned: err(f"skill {sd}: não associada a nenhum agente")
    mo = re.search(r"\*\*Agente responsável:\*\* `([\w-]+)`", text)
    if not mo or sd not in agent_skills.get(mo.group(1), []): err(f"skill {sd}: agente responsável não confere com o agente")
    for ref in backtick_paths(text):
        if not (ROOT / ref).exists(): err(f"skill {sd}: referência quebrada '{ref}'")

claude, agents_md = (ROOT / "CLAUDE.md").read_text(), (ROOT / "AGENTS.md").read_text()
skills_md = (ROOT / "SKILLS.md").read_text()
for a in AGENTS:
    if a not in claude: err(f"CLAUDE.md não cita {a}")
    if f"`{a}`" not in agents_md: err(f"AGENTS.md não cita {a}")
for s in skills_dirs:
    if s not in skills_md: err(f"SKILLS.md não cita {s}")
for t in re.findall(r"`(templates/[\w-]+\.md)`", (ROOT / ".claude/rules/handoff-format.md").read_text()):
    if not (ROOT / t).exists(): err(f"handoff-format cita template inexistente {t}")
for t in ("veo", "kling", "runway", "elevenlabs", "capcut"):
    if not (ROOT / f"integrations/{t}.md").exists(): err(f"integração sem documento: {t}")
for md in ROOT.rglob("*.md"):
    if ".git" in md.parts: continue
    for m in re.finditer(r"\]\(([^)#]+)\)", md.read_text(encoding="utf-8")):
        if not m.group(1).startswith("http") and not (md.parent / m.group(1)).exists():
            err(f"{md.relative_to(ROOT)}: link quebrado {m.group(1)}")
for f in ("package.json", "requirements.txt", "pyproject.toml"):
    if (ROOT / f).exists(): warns.append(f"dependência declarada ({f}): confirmar necessidade")
for p in ROOT.rglob("*"):
    if p.is_file() and p.suffix in (".md", ".py") and ".git" not in p.parts and p.name != "validate.py":
        if re.search(r"(sk-[A-Za-z0-9]{20,}|AIza[0-9A-Za-z_-]{30,})", p.read_text(encoding="utf-8", errors="ignore")):
            err(f"possível segredo em {p.relative_to(ROOT)}")

print(f"agentes: {len(found)}/11 · skills: {len(skills_dirs)} · templates: {len(list((ROOT/'templates').glob('*.md')))-1}")
for w in warns: print("AVISO:", w)
for e in errors: print("ERRO:", e)
print("OK" if not errors else f"FALHOU: {len(errors)} erro(s)")
sys.exit(1 if errors else 0)
