# Changelog

All notable changes to this project are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [2.1.1] - 2026-05-31

### Added

- `CHANGELOG.md` and `REVIEW-codex-pass.md` (open-source publish compliance)
- README ↔ README.zh mutual links at top
- README sections: what you get, requirements, verified runs, limitations, roadmap, about author
- `report-template.md`: optional **Post-trade addendum** for public HTML

### Changed

- README pricing aligned with [leolabs.me/tools/asset-dd](https://leolabs.me/tools/asset-dd) (Pro Pack $45 · Full Run $35 · Standard $12)
- `RUNS.md`: APR v2 readability + author post-trade note (non-recommendation boundary)
- `reader-guide.md`: APR sample marked v2 (TL;DR + collapsible provenance)

### Fixed

- `scripts/fork-preflight.sh`: pattern literals no longer trip org preflight scanner

## [2.1.0] - 2026-05-30

### Added

- Open-source package layout (`OPEN-SOURCE.md`, `RUNS.md`, `examples/`)
- Pluggable `references/tool-adapters.md`
- Optional `references/leo-extensions.md` (author overlay, fork-deletable)
- `references/rwa-composability-tier.md`, `references/roadmap-v2.md`
- Public tag `v2.1.0` on first GitHub release

### Changed

- `SKILL.md` v2.1: five-pillar Standard default, depth tiers, public-facing rules
- Report template: provenance table, §2.5–4.6, investment vs speculation split

## [2.0.x] - 2026-05 (pre-public)

- Standard five-pillar template; APR public HTML on leolabs.me
- Methodology roadmap (`references/roadmap-v2.md`)

[2.1.1]: https://github.com/runesleo/asset-dd-and-opportunity-evaluation/compare/v2.1.0...v2.1.1
[2.1.0]: https://github.com/runesleo/asset-dd-and-opportunity-evaluation/releases/tag/v2.1.0
