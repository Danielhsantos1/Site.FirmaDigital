#!/usr/bin/env python3
"""Extrai evidência de um log stream-json do Claude Code (claude -p --output-format stream-json --verbose).
Fontes: eventos task_started / task_notification (delegação real, profundidade, status, uso) e
a transcrição de cada subagente (output_file) para listar suas ferramentas e arquivos escritos.
Uso: python3 tests/orchestration/evidence.py log.jsonl [rotulo] > evidencia.md   (somente biblioteca padrão)"""
import json, os, sys, collections
path, label = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else "execução")
started, done, main_tools, final = {}, {}, collections.Counter(), None
for line in open(path, encoding="utf-8"):
    try: e = json.loads(line)
    except Exception: continue
    t, st = e.get("type"), e.get("subtype")
    if t == "system" and st == "task_started": started[e["task_id"]] = e
    elif t == "system" and st == "task_notification": done[e["task_id"]] = e
    elif t == "assistant" and e.get("parent_tool_use_id") is None:
        for c in e["message"].get("content", []):
            if c.get("type") == "tool_use": main_tools[c["name"]] += 1
    elif t == "result": final = e

def transcript_ops(output_file):
    ops = []
    try: real = os.path.realpath(output_file)
    except Exception: return None
    if not os.path.isfile(real): return None
    for line in open(real, encoding="utf-8", errors="ignore"):
        try: e = json.loads(line)
        except Exception: continue
        msg = e.get("message") or {}
        if e.get("type") == "assistant" and isinstance(msg.get("content"), list):
            for c in msg["content"]:
                if c.get("type") == "tool_use": ops.append((c["name"], c.get("input", {})))
    return ops

print(f"# Evidência: {label}\n")
print(f"- Log: `{os.path.basename(path)}` · resultado: `{final.get('subtype') if final else 'sem resultado'}` · custo total US$ {final.get('total_cost_usd') if final else '?'}")
print(f"- Ferramentas da thread principal (ECD): {dict(main_tools)}")
print("- Delegação real = evento `task_started` com `spawn_depth: 1` e `subagent_type`; retorno = `task_notification`.\n")
print("| # | Subagente | Tarefa | Prof. | Status | Ferramentas (uso) | Arquivos escritos | Web | Skill | Delegou? |")
print("|---|---|---|---|---|---|---|---|---|---|")
nested = 0
for i, (tid, s) in enumerate(started.items(), 1):
    d = done.get(tid, {}); u = d.get("usage", {})
    ops = transcript_ops(d.get("output_file", ""))
    if ops is None: files = web = sk = "transcrição indisponível"; dele = "?"
    else:
        files = ", ".join(sorted({o[1].get("file_path", "?").split("/projects/")[-1] for o in ops if o[0] in ("Write", "Edit")})) or "nenhum"
        web = f"{sum(o[0] in ('WebSearch','WebFetch') for o in ops)} chamada(s)"
        sk = ", ".join(sorted({o[1].get("skill", "?") for o in ops if o[0] == "Skill"})) or "-"
        n = sum(o[0] in ("Agent", "Task") for o in ops); nested += n; dele = f"sim ({n})" if n else "não"
    print(f"| {i} | `{s.get('subagent_type')}` | {s.get('description','')[:45]} | {s.get('spawn_depth')} | {d.get('status','sem retorno')} | {u.get('tool_uses','?')} chamadas / {round(u.get('duration_ms',0)/1000)}s | {files} | {web} | {sk} | {dele} |")
print(f"\n- Total de delegações reais: {len(started)} · retornos recebidos: {len(done)} · subagentes que tentaram delegar: {nested}")
