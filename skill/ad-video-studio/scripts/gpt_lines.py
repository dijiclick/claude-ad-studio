#!/usr/bin/env python3
"""Ask ChatGPT (OpenAI API, direct) for ad lines/hooks.

Usage: gpt_lines.py BRIEF_FILE OUT_MD [--system "…" | --system-file F] [--model gpt-5.6-sol]
Key: $OPENAI_API_KEY, else OPENAI_API_KEY= in the skill's .env (~/.claude/skills/ad-video-studio/.env).
Writes the answer to OUT_MD (with model + cost header) and prints it.
"""
import argparse, json, os, sys, urllib.request

SKILL_ENV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env")

def key(name):
    if os.environ.get(name):
        return os.environ[name]
    if os.path.exists(SKILL_ENV):
        for line in open(SKILL_ENV):
            if line.startswith(name + "="):
                return line.split("=", 1)[1].strip().strip('"')
    sys.exit(f"no {name} (set it or add it to {SKILL_ENV})")

ap = argparse.ArgumentParser()
ap.add_argument("brief"); ap.add_argument("out")
ap.add_argument("--system", default="You are a native-speaking performance-ad copywriter. Write natural, spoken, UGC-style lines — never announcer copy.")
ap.add_argument("--system-file")
ap.add_argument("--model", default=os.environ.get("GPT_MODEL", "gpt-5.6-sol"))
a = ap.parse_args()

system = open(a.system_file).read() if a.system_file else a.system
body = {"model": a.model, "messages": [{"role": "system", "content": system},
                                       {"role": "user", "content": open(a.brief).read()}]}
req = urllib.request.Request("https://api.openai.com/v1/chat/completions", data=json.dumps(body).encode(),
                             headers={"Authorization": "Bearer " + key("OPENAI_API_KEY"), "Content-Type": "application/json"})
try:
    res = json.load(urllib.request.urlopen(req, timeout=300))
except urllib.error.HTTPError as e:
    sys.exit(f"HTTP {e.code}: {e.read().decode()[:500]}")
text = res["choices"][0]["message"]["content"]
u = res.get("usage", {})
open(a.out, "w").write(f"# Lines — {res.get('model', a.model)} (OpenAI direct; tokens in/out {u.get('prompt_tokens')}/{u.get('completion_tokens')})\n\n{text}\n")
print(text)
