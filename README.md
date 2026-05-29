# asset-dd-and-opportunity-evaluation

Institutional-grade asset due diligence workflow for AI coding agents (Claude Code, Cursor, Codex, etc.).

**Default depth:** Standard — five pillars, competitive set, on-chain proxy, provenance table, separate investment vs speculation theses, participation buckets.

---

## Quick start

1. Copy this folder into your agent's skills directory (Claude Code, Cursor, Codex, etc.).
2. Invoke when the user asks: *DD / due diligence / is this asset worth buying / research this token*.
3. Agent reads `SKILL.md` → executes workflow → outputs report using `references/report-template.md`.

**Optional:** Delete or replace `references/leo-extensions.md` (author-specific portfolio/KOL tooling).

---

## Depth tiers

| Tier | When | Output |
|------|------|--------|
| **Quick** | User explicitly asks for a fast scan | `[Quick DD]` · object + mechanism + risks + verdict |
| **Standard** | Default | Full checklist through §2.5–4.6 |
| **Full** | Deep dive / publish | Standard + ≥4 comps + bull/base/bear scenarios + dual-source cross-check |

---

## File layout

```
asset-dd-and-opportunity-evaluation/
├── SKILL.md                          # Core workflow (portable)
├── README.md / README.zh.md
├── LICENSE
├── OPEN-SOURCE.md
├── RUNS.md                           # Documented production runs
├── references/
│   ├── report-template.md
│   ├── professional-pillars.md
│   ├── tool-adapters.md              # Pluggable data sources
│   ├── leo-extensions.md             # Optional author overlay
│   ├── rwa-composability-tier.md
│   └── roadmap-v2.md
└── examples/
    └── pearl-standard-dd-excerpt.md
```

---

## Public examples

| Asset | Format | Link |
|-------|--------|------|
| APR / aPriori | Full HTML report | [leolabs.me/research/apr-apriori-2026-05/report.html](https://leolabs.me/research/apr-apriori-2026-05/report.html) |
| Pearl $PRL | Standard DD excerpt (sanitized) | `examples/pearl-standard-dd-excerpt.md` |
| Layout starter | Minimal static HTML | `examples/report-starter.html` |

**Reading dense reports:** see `references/reader-guide.md`.

**Known gap (pre-launch):** website currently has **one** live HTML sample (APR). A second public sample (English Full or meme/on-chain failure case) improves OSS credibility — tracked in `references/roadmap-v2.md`.

---

## Design principles

1. **Identify the object first** — platform ≠ token ≠ referral wrapper.
2. **Facts before narrative** — social discovery generates hypotheses; chain/market data falsifies them.
3. **No silent gaps** — every pillar is ✅ / ⚠️ / ➖ with reason.
4. **Investment ≠ speculation** — two separate thesis paragraphs, always.
5. **Venue depth binds sizing** — portfolio % cap is meaningless if you are 30% of the AMM pool.

---

## License

MIT — see `LICENSE`. Sample reports in `examples/` are CC BY 4.0 where noted.

---

## Changelog

- **2.1.0** (2026-05-30) — Open-source package layout; tool adapters; Leo extensions split; roadmap R1–R3; mcap scenario §3.5
- **2.0.x** — Standard five-pillar template; APR public HTML; roadmap-v2
