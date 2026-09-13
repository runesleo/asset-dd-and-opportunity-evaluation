---
name: asset-dd-and-opportunity-evaluation
description: Action-First asset DD and opportunity evaluation. Use for DD/尽调/值不值得买/是否值得小仓试错. For fast tradable assets, make a bounded Phase-A decision before completing Standard/Full DD.
version: 3.0.0
semantic_version: action-first-2026-09-13-v1
license: MIT
---

# Asset DD & Opportunity Evaluation — Action-First v3

## Objective

Optimize **realized probability-weighted EV per unit of risk, latency, and attention** — not certainty before action.

Core laws:

1. **Uncertainty sizes the bet; it does not veto the bet.**
2. **Action can buy information.** A small, bounded `INFORMATION_CANARY` may have both financial optionality and information value.
3. **Machine-resolvable unknowns are work, not human WAIT reasons.**
4. **Full proof is not a prerequisite for a bounded canary.** Evidence completeness controls size/confidence and later scale.
5. **Hard security facts remain hard vetoes.** Honeypot, verified unsellability, directly malicious admin/transfer logic, deployer-removable core liquidity, or equivalent direct evidence can block capital.
6. **Public endorsement and personal capital are independent gates.** `NOT_READY_FOR_ALPHACALL` must never automatically mean `NOT_READY_TO_BUY`.
7. **Price alone is never the thesis.** Price-only pumps do not Alpha-promote; price-only drawdowns do not kill or justify averaging down.
8. **No automatic trading authority.** Research/recommendation logic does not authorize buys, sells, transfers, approvals, signatures, account/credential changes, publishing, or outbound messages.

## Trigger

Use when the user asks whether an asset, token, protocol, stock, meme, launch, or other investable opportunity is worth following, buying, trading, allocating to, or researching.

Do not confuse:
- protocol / platform;
- protocol token;
- child token launched by the platform;
- company equity;
- referral wrapper / venue link;
- exact tradable asset.

For social/referral entry points, strip the referral wrapper first and bind the canonical asset or participation route before valuation.

---

# Decision order

## Phase A — minimum sufficient decision layer (mandatory for fast/tradable assets)

Run this **before** waiting for Standard/Full DD completion.

### A1. Exact object / route

Bind, where applicable:
- chain / venue;
- exact contract, mint, stock code, or canonical participation route;
- primary venue / pool / route;
- official first-party identity.

If exact object does not yet exist, use `IDENTITY_INCOMPLETE`; do not invent a valuation or order instruction.

### A2. Minimum hard-safety screen

Check the minimum safety facts needed for the proposed small size:
- sellability / transferability;
- token authority / admin controls;
- LP ownership / removability where relevant;
- taxes / restrictions / blacklist / mint risk;
- custody / settlement / counterparty risk where relevant.

A generic `wash`, concentration, same ticker, noisy volume, or unknown LP-lock status is **not** automatically a terminal hard fail without direct supporting evidence.

### A3. Small-size execution reality

For the intended first experiment, obtain or attempt:
- fresh executable quote;
- buy/sell or round-trip route;
- slippage / price impact;
- executable exit capacity.

Use exact-contract / exact-route data above generic ticker aggregators.

### A4. One non-price asymmetric thesis

State one concrete reason the asset could materially outperform that is not merely “price is rising” or “market cap is low”. Examples:
- new value-capture mechanism;
- user / transaction / revenue acceleration;
- distribution or integration expansion;
- category winner transition;
- supply/flow imbalance;
- scheduled catalyst with mispriced probability.

Also state the strongest counter-thesis and an observable kill condition.

### A5. Probability / payoff / delay

Estimate bounded ranges rather than fake precision:
- thesis-fail probability;
- base-success probability / payoff;
- strong-success probability / payoff;
- tail/category-winner probability / payoff when relevant;
- executable loss if wrong;
- remaining multiple;
- market pricing;
- `cost_of_delay`;
- information value of acting now.

At minimum ask:
`Is the probability-weighted upside + information value attractive relative to bounded executable loss, security risk, execution cost, and opportunity cost?`

### A6. UNKNOWN taxonomy

Every decision-relevant unknown must be typed immediately:

- `AUTO_RESOLVABLE` — fresh quote, exit depth, holder sample, LP/admin readback, supply, exact-CA binding, mechanism execution, recent revenue/buyback, route existence, etc. **Attempt automatically now** using available safe read-only tools; persist provenance and recompute.
- `EXTERNAL_PENDING` — the fact does not exist yet: future launch, vote, unlock, payout epoch, mainnet activation, settlement. Real waiting is allowed; define the trigger.
- `OWNER_GATED` — next action changes funds, signs, changes accounts/credentials, publishes/sends externally, or is otherwise consequential. Finish all safe preflight first, then present one bounded decision.
- `TEMPORARILY_UNOBSERVABLE` — evidence should exist but bounded primary + failover sources failed. Record failed sources and stale evidence; continue independent lanes. Do not turn missing telemetry into zero.

Forbidden human-facing ending:
`Next step: verify X` when X is safely machine-resolvable.

Required behavior:
`Verified/attempted X/Y/Z automatically. Remaining owner decision: [exact consequential action], if any.`

### A7. Phase-A capital purpose

Return one of:
- `NO_CAPITAL / PASS`
- `INFORMATION_CANARY`
- `PREPOSITION`
- `SCALE_REVIEW`
- `HOLD / REDUCE / EXIT` for an existing position

Reference first-experiment bands for Leo-style micro/early opportunities when execution supports them:
- `20U DIAGNOSTIC_CANARY` — thin but information-rich;
- `50U CANARY` — default meaningful bounded experiment;
- `100U STRONG_CANARY` — stronger asymmetry + adequate execution.

These are **recommendation bands, never automatic orders**. Use the user's own risk envelope when known.

A bounded canary may be rational before full proof when all are true:
1. exact tradable identity/route is known;
2. no direct hard-security fail exists;
3. proposed small-size sellability is bounded;
4. one concrete non-price asymmetric thesis exists;
5. remaining upside is plausibly convex to total loss;
6. an explicit kill condition exists.

Missing payout/repeatability/public-proof may block **scale or public call** without blocking the first canary when not required for basic capital safety.

---

# Phase B — Standard DD (continues after Phase A)

Default depth for substantive research remains **Standard**. The difference is sequencing: Standard DD improves confidence and scale decisions; it is not a universal prerequisite for the first bounded decision.

Standard should cover, where applicable:

## B1. Foundational facts
- exact identity / official site/docs/X/TG;
- venue and price formation;
- circulating / total / max supply;
- market cap / FDV with source hierarchy;
- fees / slippage / settlement / redemption / liquidation mechanics.

## B2. Tokenomics / supply stress
For crypto:
- attempt at least two independent unlock/vesting paths;
- circ / total / max / FDV / market cap / FDV÷Mcap;
- 90d unlock/emission risk;
- value-capture sentence;
- if no day-level schedule exists, label any linear extrapolation as **scenario bound, not forecast**.

Missing tokenomics evidence is an explicit uncertainty and scale blocker; it does not silently become zero.

## B3. Competitive set
For Standard+ use at least two relevant peers with at least one numeric anchor per row where possible.
Answer: is the premium/discount likely asset-specific alpha or category beta?

## B4. Social discovery
For fast assets, social is mandatory for signal generation but never treated as truth. Cross-check important claims on first-party or onchain/market sources.

## B5. Onchain / holder / market structure proxy
For assets with contracts, attempt at least one reproducible proxy with timestamp and a numeric statement, or mark `blocked` with the attempted path.

## B6. Five professional pillars
Use `references/professional-pillars.md`; no silent blanks:
- Foundational
- Technical / security
- Tokenomics / capital structure
- Traction / PMF / economics
- Market structure / distribution

## B7. Mechanics baseline
Before a strong EV/scale claim, explain:
- money in;
- money out;
- who gets paid;
- marginal buyer/seller;
- main reflexive loop;
- main failure mode;
- measurable variable on which the alpha thesis hangs.

---

# Phase C — Full DD / scale diligence

Use Full when the user explicitly asks for deep work, when material capital is being considered, or when Phase A/B suggests scale.

Add:
- ≥4 competitors when useful;
- bull/base/bear or multi-scenario terminal-value ranges;
- at least one decision-critical number cross-checked through two independent paths;
- fresh planned-size executable depth;
- portfolio concentration/correlation;
- supply overhang vs sustainable demand / buy pressure;
- repeatability / value-capture evidence;
- independent adversarial review for material scale.

Scale only when incremental non-price evidence improves forward EV, or execution/capacity materially improves without thesis deterioration.

A falling price alone is not a scale trigger.

---

# Portfolio / sizing discipline

Portable defaults:
- separate investment from speculation;
- social/referral microcaps default speculative until disproven;
- unclear identity or unbounded sellability => no actionable canary yet;
- position size must respect both portfolio loss budget and venue depth;
- position vs pool/route capacity: use the tighter constraint.

If fresh portfolio NAV is unavailable, **do not fabricate portfolio percentages**. NAV unknown may block material `SCALE_REVIEW`, but it does not by itself block a fixed-loss bounded canary whose route and downside are independently bounded. Personal extensions live in `references/leo-extensions.md`.

---

# Existing-position logic

For a held asset, always return an action state:
- `HOLD`
- `ADD / SCALE_REVIEW`
- `REDUCE`
- `EXIT`

Do not return generic WAIT merely because one evidence field is unknown. Auto-resolve safe unknowns first, separate scale blockers from hold/exit logic, and state the next material thesis trigger.

---

# Output

Use `references/report-template.md`.

For fast/tradable opportunities, the first screen must expose a **Phase-A Decision Snapshot** before the long report:
- exact identity / route;
- hard-security state;
- planned small-size execution state;
- strongest non-price edge;
- strongest counter-thesis / kill condition;
- automatic checks completed;
- remaining unknowns by class;
- scenario ranges / remaining multiple;
- information gain;
- cost of delay;
- recommended capital purpose / canary band;
- scale blockers;
- exact owner action required, if any.

Then continue with Standard/Full evidence as appropriate.

Keep investment thesis and speculation thesis separate.

---

# Independent review rule

Independent models/reviewers are **adversarial evidence sources, not a voting committee**.

- A directly evidenced hard-security contradiction can veto capital.
- A material factual contradiction triggers re-check / lower confidence / lower size.
- Ordinary disagreement is surfaced; it does not mechanically create WAIT.
- Material scale should consume independent review.
- A bounded canary does not require model consensus.

---

# Transient failure policy

For machine-resolvable source failures:
1. bounded retry;
2. switch approved adapter/source hierarchy;
3. mark provenance and degradation;
4. if all bounded paths fail, classify `TEMPORARILY_UNOBSERVABLE`;
5. continue independent research lanes;
6. do not delegate the refresh to the user.

---

# Verification checklist

Before finalizing:
- exact object / participation route bound?
- Phase A completed before waiting for Standard/Full?
- hard-security facts distinguished from generic risk tags?
- planned small-size sellability attempted?
- at least one non-price thesis + one kill condition?
- probability/payoff/downside/cost-of-delay/information value stated?
- every unknown typed?
- all safe `AUTO_RESOLVABLE` checks attempted before owner escalation?
- `NOT_READY_FOR_ALPHACALL` kept independent from personal canary?
- missing evidence stayed UNKNOWN rather than zero/PASS?
- price-only move prevented from promotion/kill?
- Standard/Full depth matches the claim and capital scale?
- output contains an exact owner decision only when a consequential action remains?

Semantic version: `action-first-2026-09-13-v1`
