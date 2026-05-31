# asset-dd-and-opportunity-evaluation

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Institutional-grade asset due diligence workflow for AI coding agents (Claude Code, Cursor, Codex, etc.).

**中文文档：** [README.zh.md](./README.zh.md)

**Default depth:** Standard — five pillars, competitive set, on-chain proxy, provenance table, separate investment vs speculation theses.

---

## What you get

- **Structured DD checklist** — Quick / Standard / Full tiers in `SKILL.md`
- **Report scaffold** — `references/report-template.md` with provenance table and §2.5–4.6
- **Pluggable data sources** — `references/tool-adapters.md` (no vendor lock-in)
- **Public samples** — APR HTML on leolabs + Pearl excerpt in `examples/`
- **Optional author overlay** — `references/leo-extensions.md` (delete on fork)

---

## How it works

```text
User: "DD this token / 尽调 APR"
  → Agent reads SKILL.md
  → Picks tier (default Standard)
  → Fills report-template.md (Markdown or HTML)
  → Every claim: source URL + UTC as-of + ✅/⚠️/➖ on five pillars
```

**Not included:** live price feeds, auto-trading, or investment advice.

---

## Paths

| Path | For |
|------|-----|
| **Open Core (this repo)** | Clone → copy into your agent skills folder |
| **[Sample report](https://leolabs.me/research/apr-apriori-2026-05/report.html)** | See output quality first |
| **[leolabs.me/tools/asset-dd](https://leolabs.me/tools/asset-dd)** | Pro Pack zip · on-demand Run (optional paid paths) |

Pricing (2026-05): Standard Run $12 · Full Run $35 · Pro Pack $45 — details on the product page, not required for self-host.

---

## Quick start

```bash
git clone https://github.com/runesleo/asset-dd-and-opportunity-evaluation.git
# Copy into your agent skills directory, then invoke:
# "Run a Standard DD on <ticker>"
```

1. Copy this folder into Claude Code / Cursor / Codex skills path.
2. Trigger on: *DD / due diligence / is this worth buying / 尽调*.
3. Agent reads `SKILL.md` → outputs using `references/report-template.md`.

**Fork:** delete or replace `references/leo-extensions.md` · run `bash scripts/fork-preflight.sh`

---

## Requirements

- Any agent that can read local skill files and follow Markdown instructions
- **Data:** your own API keys / browser tools per `tool-adapters.md` (CoinGecko, exchange APIs, X search, etc.)
- **Privacy:** if you use browser-cookie or logged-in dashboards, that stays on your machine — not shipped in this repo

---

## Depth tiers

| Tier | When | Output |
|------|------|--------|
| **Quick** | User asks for a fast scan | `[Quick DD]` |
| **Standard** | Default | Full checklist through §2.5–4.6 |
| **Full** | Deep dive / publish | + ≥4 comps + bull/base/bear + dual-source cross-check |

---

## Verified

| Run | Tier | Evidence |
|-----|------|----------|
| APR / aPriori | Standard → public HTML | [leolabs report](https://leolabs.me/research/apr-apriori-2026-05/report.html) · `RUNS.md` #1 |
| Pearl $PRL | Standard excerpt | `examples/pearl-standard-dd-excerpt.md` |

See full ledger: [`RUNS.md`](./RUNS.md)

---

## Known limitations (v2.1)

- Website has **one** full public HTML sample (APR); second sample planned — `references/roadmap-v2.md`
- Unlock calendars often ⚠️ blocked without paid data vendors
- `leo-extensions.md` is author-specific; not required for core workflow
- Pro Pack zip is **not** in this repo (delivered separately via leolabs)

---

## Roadmap

- [ ] Second public sample (English Full or on-chain failure case)
- [ ] Pearl full HTML on leolabs research hub
- [ ] Template v2.1+ first-screen TL;DR enforced in all exports — see `references/reader-guide.md`

Details: `references/roadmap-v2.md`

---

## File layout

```
asset-dd-and-opportunity-evaluation/
├── SKILL.md
├── README.md / README.zh.md
├── CHANGELOG.md
├── LICENSE · OPEN-SOURCE.md · RUNS.md
├── references/          # templates, adapters, reader-guide
├── examples/            # sanitized excerpts
└── scripts/fork-preflight.sh
```

---

## About the author

*Leo ([@runes_leo](https://x.com/runes_leo)) — AI × Crypto independent builder. Trading on [Polymarket](https://polymarket.com/?via=runes-leo&r=runesleo&utm_source=github&utm_content=asset-dd-and-opportunity-evaluation), building data and content pipelines with Claude Code and Codex.*

*[leolabs.me](https://leolabs.me) — writing · community · open-source tools · indie projects*

*[X Subscription](https://x.com/runes_leo/creator-subscriptions/subscribe) — paid content weekly*

*Learn in public, Build in public.*

---

## License

MIT — see [`LICENSE`](LICENSE). Sample reports in `examples/` are CC BY 4.0 where noted.

**Changelog:** [`CHANGELOG.md`](CHANGELOG.md)
