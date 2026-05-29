# Open-source boundary · 发布边界

## ✅ Ship in public repo

| Asset | Notes |
|-------|-------|
| `SKILL.md` | Portable core (v2.1+) |
| `references/*` | Templates and adapters |
| `README.md` / `README.zh.md` / `LICENSE` / `RUNS.md` | Package meta |
| `examples/*.md` | Sanitized report excerpts |

## ➖ Keep private

| Asset | Why |
|-------|-----|
| Personal portfolio snapshots | Privacy |
| API keys / wallets | Security |
| Full vault paths / internal task IDs | Internal ops |
| Reports with personal position overlay | Privacy |

## 🔗 Related public assets

- **leolabs-research-bundle** — static HTML/CSS report examples
- **APR report** — canonical published HTML

---

## Preflight (before `git push`)

```bash
# Scan for secrets and private paths (adjust patterns for your tree)
rg -nE '(api_key|sk-[a-zA-Z0-9]{10,}|BEGIN (RSA )?PRIVATE KEY|wallet.*0x)' .

# Optional: use your org's opensource-preflight script if you have one
```

Expected: **zero hits** on secrets. Review any path-like strings manually.

---

## Suggested GitHub repo

```
github.com/<org>/asset-dd-and-opportunity-evaluation
```

Topics: `claude-code`, `cursor`, `codex`, `due-diligence`, `crypto-research`, `agent-skill`

Release tag: `v2.1.0` on first public push.

---

## Fork guidance

1. Remove or rewrite `references/leo-extensions.md`
2. Run `bash scripts/fork-preflight.sh`
3. Point `tool-adapters.md` at your data stack
4. Add your own `examples/` from published reports
5. Keep `RUNS.md` updated

## External review log

- **2026-05-30 · Grok Build** — OSS readiness critique archived in `references/external-review-2026-05-30-grok.md`
