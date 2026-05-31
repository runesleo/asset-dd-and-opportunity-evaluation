# Open-source review pass · asset-dd-and-opportunity-evaluation

- **Date:** 2026-05-31
- **Scope:** v2.1.1 documentation / compliance release (post v2.1.0 first public push)
- **Reviewer:** Cursor agent (preflight + manual tree review; independent Codex CLI not re-run for doc-only delta)

## 🔴 Blockers

_None after fork-preflight pattern fix._

## 🟡 Warnings

| Item | Notes | Disposition |
|------|-------|-------------|
| `references/leo-extensions.md` | Author-specific paths (`~/.claude/portfolio`, `@runes_leo`) | **Keep** — optional overlay; documented in README + `OPEN-SOURCE.md`; fork may delete |
| First public tag was `v2.1.0` not `v0.1.0` | Semver vs internal methodology version | **Document** in CHANGELOG; forward fixes use 2.1.x |
| Only one live HTML sample (APR) | OSS credibility gap | Tracked in `roadmap-v2.md`; not blocking doc release |
| Pro Pack zip not in repo | Paid deliverable ships via TG | **By design** — see leolabs product page |

## 🟢 OK

- `opensource-preflight.sh` exit 0 (after fork-preflight fix)
- `fork-preflight.sh` exit 0
- MIT `LICENSE` present
- `README.md` + `README.zh.md` present with mutual links
- No API keys / wallets in tree or obvious git-log grep hits
- `.gitignore` covers `.env`
- Public reports in `examples/` are sanitized excerpts

## Smoke

```bash
bash scripts/fork-preflight.sh          # exit 0
test -f SKILL.md && test -f references/report-template.md
```

## Sign-off

**Approved for tag `v2.1.1`** — documentation and publish-compliance release only; no workflow logic change in `SKILL.md` since v2.1.0.
