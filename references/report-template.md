# Asset DD Report Template — Action-First v3

Semantic version: `action-first-2026-09-13-v1`

与 `SKILL.md` 对齐。默认仍可做 Standard DD，但 fast/tradable asset 必须先给 **Phase-A Decision Snapshot**，不能等完整报告写完才出现可执行结论。

---

# Mode A — Single Asset

## Metadata

- **Depth tier:** Phase-A / Quick / Standard / Full
- **Report as-of (UTC):** `YYYY-MM-DDTHH:MMZ`
- **Decision horizon:** 24h / 72h / 7d / longer
- **Canonical identity:** chain + exact contract/mint/stock code/route
- **Semantic version:** `action-first-2026-09-13-v1`

---

## 0. Phase-A Decision Snapshot — first screen

This section comes before the long provenance/detail sections for a fast or tradable opportunity.

### 0.1 Decision

- **Verdict:**
- **Capital purpose:** `NO_CAPITAL / INFORMATION_CANARY / PREPOSITION / SCALE_REVIEW / HOLD / REDUCE / EXIT`
- **Suggested bounded band:** `0 / 20U / 50U / 100U / other`
- **Why now:**
- **Latest useful decision time / cost of delay:**
- **Exact owner action required:** `NONE` or one concrete consequential action

No automatic order is implied by this report.

### 0.2 Identity / execution

- Exact asset / route:
- Primary venue / pool:
- Fresh quote observed at:
- Planned small-size buy state:
- Planned small-size sell / round-trip state:
- Slippage / impact:
- Executable exit capacity:

### 0.3 Hard security

- Hard-security state: `PASS / SECURITY_HARD_FAIL / UNKNOWN`
- Direct evidence:
- Non-terminal risk tags:

Do not treat generic wash, concentration, same ticker, or missing LP data as a terminal hard fail without direct evidence.

### 0.4 Thesis / counter-thesis

- Strongest **non-price** asymmetric thesis:
- Strongest counter-thesis:
- Explicit kill condition:

### 0.5 Probability / payoff

| Scenario | Probability range | Payoff / terminal-value range | Main condition |
|---|---:|---:|---|
| Thesis fail | | | |
| Base success | | | |
| Strong success | | | |
| Tail / category winner | | | |

- Executable loss if wrong:
- Remaining multiple:
- Market pricing: underpriced / partially priced / priced / over-priced / unknown
- Information gain from acting now: low / medium / high + why
- Cost of delay: low / medium / high / critical + why

### 0.6 Auto-checks completed

- [ ] exact identity / first-party binding
- [ ] hard-security readback
- [ ] planned-size quote
- [ ] sellability / exit-capacity
- [ ] supply / valuation normalization
- [ ] non-price thesis evidence
- [ ] creator / holder / overhang check if material
- [ ] market-data conflict reconciliation if material

### 0.7 Remaining unknowns

| Unknown | Class | What happens next |
|---|---|---|
| | `AUTO_RESOLVABLE` | machine attempts now; do not delegate to Leo |
| | `EXTERNAL_PENDING` | define real future trigger |
| | `OWNER_GATED` | exact consequential decision after preflight |
| | `TEMPORARILY_UNOBSERVABLE` | record failover attempts; continue independent lanes |

### 0.8 Scale blockers

- NAV / portfolio fit:
- planned-size depth:
- incremental EV:
- repeatability / economics:
- supply / unlock / overhang:
- independent review:

A blocker may prevent **scale** without erasing a valid canary/HOLD/Alpha state.

Forbidden ending: `Next step: verify X` when X is machine-resolvable.

Required ending form: `Auto-checks completed/attempted: X/Y/Z. Remaining owner decision: [exact action]` or `NONE`.

---

## 1. Data Provenance

| Claim | Source | As-of UTC | Confidence | Authority / notes |
|---|---|---|---|---|
| Price / executable quote | | | | |
| Market cap / FDV / supply | | | | |
| Unlock / vesting | | | | |
| Primary venue depth | | | | |
| Onchain / filing proxy | | | | |
| Social / narrative | | | | signal only |

Exact-contract / exact-route executable data outranks generic ticker aggregation for sizing.

---

## 2. Asset Identification

- What it is:
- What it is NOT:
- Ticker:
- Contract / mint / stock code:
- Chain / venue:
- Website:
- Docs:
- X:
- TG / Discord:

---

## 3. Hard Facts

- Price / market cap / FDV:
- Circulating / total / max supply:
- Liquidity / volume / depth:
- Fees / slippage:
- Admin / upgrade / mint / blacklist permissions:
- Audit / bug bounty / security facts:
- Governance / dev activity:
- Operating KPIs:

Unknown stays UNKNOWN. Never coerce missing data to zero.

---

## 4. Tokenomics / Supply Stress — Standard+

- Circ / total / max / FDV / market cap / FDV÷Mcap:
- Emissions / inflation:
- 90d unlock / vesting:
- Attempt 1 URL -> outcome:
- Attempt 2 URL -> outcome:
- Value capture:
- Supply overhang vs sustainable demand / buy pressure:
- If no daily unlock table: scenario-bound extrapolation, explicitly **not forecast**.

---

## 5. Mechanism Layer

### Elevator

- Money in:
- Money out:
- Who gets paid:
- Marginal buyer / seller:
- Main reflexive loop:
- Main failure mode:
- Measurable variable on which alpha hangs:

---

## 6. Competitive Set — Standard+

| Peer | Positioning | Numeric anchor | Relative edge/gap | Falsifier |
|---|---|---:|---|---|
| | | | | |
| | | | | |

- Asset-specific alpha vs category beta:

---

## 7. Onchain / Holder / Market-Structure Proxy — Standard+

- Chosen proxy:
- Tool/source path:
- Dated numeric observation:
- Holder / creator / treasury / LP notes:
- What is blocked / missing:

Do not substitute a static TVL number for fresh planned-size sellability when the decision depends on exit capacity.

---

## 8. Social / Community Read

- 7d / 14d heat check:
- Main narrative:
- Who is pushing it:
- Founder / dev social graph:
- Independent propagation vs coordinated/reflexive promotion:
- Signal vs noise:

Social evidence generates hypotheses; it does not prove product/value capture/security.

---

## 9. Risk Register

- Technical / security:
- Liquidity / execution:
- Dilution / unlock:
- Governance / admin:
- Counterparty / settlement:
- Regulatory:
- Narrative collapse:
- Opportunity cost:

---

## 10. Why There May Be Money to Make

- Mispricing hypothesis:
- Bull case:
- Bear case:
- What has to happen:
- Why the market may be wrong:
- Why it may already be crowded/priced:

### 10a. Investment thesis

- ≥1y sustainable cashflow / moat / share / regulatory carry, or explicitly: `no independent investment thesis; speculation only`.

### 10b. Speculation thesis

- days/weeks catalyst / crowding / beta / narrative rotation / reflexivity.

Keep 10a and 10b separate.

---

## 11. Participation Guidance for Leo

- Current personal-capital state:
- Entry style:
- Current bounded canary / preposition cap:
- Next scale trigger:
- Next reduce trigger:
- Exit trigger:

### Kill / invalidation table

| Metric / fact | Source | Threshold type | Trigger |
|---|---|---|---|
| | | absolute / vs peer / MoM / direct fact | |

For held positions, always return `HOLD / ADD-SCALE_REVIEW / REDUCE / EXIT`; do not end with generic WAIT after safe machine checks are available.

---

## 12. Independent Adversarial Review

- Reviewer / model:
- Hard-security contradiction: yes/no
- Material factual contradiction:
- Non-terminal disagreement:
- Re-checks completed:
- Effect on size/confidence:

Independent review is evidence, not a vote. A bounded canary does not require consensus. Material scale should consume independent review.

---

## 13. Data Limitations

- Unverified claims:
- Missing datasets:
- `AUTO_RESOLVABLE` items already attempted:
- `TEMPORARILY_UNOBSERVABLE` sources and failovers:
- Real `EXTERNAL_PENDING` triggers:

---

## 14. Monitoring Checklist

- Price / executable route:
- Holder / creator / LP:
- Product / user / transaction:
- Revenue / fee / buyback / value capture:
- Supply / unlock:
- Social / narrative:
- Catalyst calendar:
- Re-entry / scale / reduce / exit triggers:

Notify on material semantic/action deltas, not clock-only refreshes.

---

## 15. Five-Pillar Self-Check — Standard+

| Pillar | Status | Evidence pointer |
|---|---|---|
| Foundational | ✅ / ⚠️ / ➖ | |
| Technical / security | ✅ / ⚠️ / ➖ | |
| Tokenomics / capital structure | ✅ / ⚠️ / ➖ | |
| Traction / PMF / economics | ✅ / ⚠️ / ➖ | |
| Market structure / distribution | ✅ / ⚠️ / ➖ | |

---

## 16. Full-DD Scenarios — Full only

| Scenario | Probability | Assumptions | Terminal value / payoff | Falsifier |
|---|---:|---|---:|---|
| Bear | | | | |
| Base | | | | |
| Bull | | | | |

For material scale also include portfolio concentration/correlation and fresh planned-size executable depth.

---

# Mode B — Cross-Asset Comparison

Use the same Phase-A philosophy when the comparison informs a capital decision.

## 0. Decision relevance
- hedge / signal / narrative filter / relative-value / no actionable edge
- exact assets / venues
- aligned window
- key relative metric
- owner action, if any

## 1. Alignment
- symbols / identifiers:
- currencies:
- sessions:
- time window / granularity:
- data sources:

## 2. Unified Feature Table
- price / return:
- volume / turnover:
- volatility / range:
- liquidity / depth:
- fundamentals / onchain KPI:

## 3. Relationship Read
- correlation / relative return / regime:
- structural link vs coincidence:
- lead-lag hypothesis:
- falsifier:

## 4. Actionability
- what changes in positioning/monitoring:
- what not to over-interpret:
- cost of delay:
- owner action:

## 5. Limitations / monitoring
- missing data:
- alignment weakness:
- triggers:
- kill conditions:

---

Public-facing exports may remove internal tool names and personal sizing details while preserving evidence, reasoning, and disclosure boundaries.
