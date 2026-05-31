# Asset DD Report Template

与 `SKILL.md` 及 `references/professional-pillars.md` 对齐。**默认 Standard depth**；若产出为 Quick / Full，须在 Metadata 中显式标注。

Use one of the two modes below. Default to Single-Asset Mode unless the task explicitly compares or screens across multiple assets / markets.

---

## Mode A — Single-Asset Report

### Metadata（必填）

- **Depth tier:** `[Quick DD]` / **Standard（默认）** / `[Full DD]`
- **Report as-of (UTC):** `YYYY-MM-DDTHH:MMZ`（精确到分钟为佳）
- **Analyst note:** 若某支柱整段为 ➖，须写 **「非适用原因」** 或 **「已尝试，blocked」**（禁止静默留白）
- **Public URL / 外发**（若适用）：可加 **≤8 行「如何阅读 / TL;DR」** 于溯源表之前；正文 **禁止**出现 `asset-dd`、Claude/Codex 等内部工具名（见 `SKILL.md` Public-facing 节）。若导出独立 HTML：建议 **`twitter:description`** 与 **`og:description`** 同文，便于 X 卡片摘要。
- **首屏可读性（v2.1+）**：Metadata 之后 **≤400 字内** 必须出现 **TL;DR + Verdict + 至少 1 张关键图或核心表**；**溯源表默认后置**（HTML 用 `<details>` 折叠）。见 `references/reader-guide.md`。

### Data provenance table（必填，独立小节）

| Claim | Source (URL or API name) | As-of (UTC) | Confidence (H/M/L) |
|-------|----------------------------|---------------|----------------------|
| Mcap / FDV / circ supply | | | |
| Unlock / vesting conclusion | | | |
| Primary venue volume / depth | | | |
| On-chain proxy (if applicable) | | | |
| … | | | |

### 0. Recommendation First

- Verdict:
- Opportunity type: long-term compounding / medium-term thematic / short-term momentum / one-shot gamble
- Action bucket: avoid / watch only / research position / tiny speculative position / conviction position
- Suggested sizing:（凡写 `%T` 或美元试探上限，**同小节**须写防火墙句：**非对任何读者的仓位或交易建议**；`T` 为读者自行定义的总资产；以下为作者匿名化自用框架。）
- Why now:

### 1. Asset Identification

- Asset analyzed as:
- What it is:
- What it is NOT:
- Canonical identifier:
  - ticker:
  - contract / mint / stock code:
  - chain / exchange / venue:
- Official links:
  - website:
  - docs:
  - X:
  - Telegram / Discord:

### 2. Where the Key Data Is Found

- Primary sources:
- Market data sources:
- On-chain / filings / registry sources:
- Social / community sources:
- What is still missing:

### 2.5 Tokenomics, emissions & unlock attempts（Standard+）

- Circulating / total / max supply; **FDV/Mcap** if both exist:
- Emissions / inflation (or **「无直接排放 / 未披露」**):
- **Unlock / vesting — attempt log（至少 2 条路径，写 URL + 结果）**
  - Attempt 1: … → outcome:
  - Attempt 2: … → outcome:
  - If both fail: `⚠️ blocked` + reason（禁止静默省略）
- **若无日级 unlock 表（Standard+）**：补 **一行最坏线性外推上界**（`(total - circ) / N months` × 参考价，标 **scenario bound not forecast**）。

### 2.6 Competitive set（Standard+, ≥2 peers）

| Peer | One-line positioning vs subject | Numeric anchor (as-of) | **One falsifiable** relative edge or gap |
|------|-----------------------------------|--------------------------|------------------------------------------|
| | | | |
| | | | |

### 3. Hard Facts

- Price / market cap / FDV:
- Liquidity / volume:
- Supply structure:
- Fees / slippage / trading venue:
- Security / audit / bug bounty:
- Governance / dev activity:
- Key operating KPIs:

### 3.5 Market cap scenario framework（`[Full DD]` 或用户问「能到多少 mcap」）

- **Primary metric:** circulating market cap（PoW/早期 FDV 常虚高）
- **Comps table:** ≥3 named peers · narrative · circ mcap · one-line read
- **Scenarios:**

| Tier | Circ mcap range | What must become true | Falsifier |
|------|-----------------|-------------------------|-----------|
| Bear | | | |
| Base | | | |
| Bull | | | |

### 3.6 On-chain & holder proxy（Standard+，有合约 / 主链资产时必尝试）

- Chosen proxy(es): top holders % / labeled treasury moves / main DEX pool TVL / CEX attestation / Dune or official dashboard
- Tool path used: explorer API → GeckoTerminal → Dune → Playwright, or `⚠️ blocked` + reason
- **须写入至少一句带日期的数字**（例：Etherscan Top10 合计约 __% 流通，UTC __ 手读 UI）；**禁止**仅以「读者自行打开 Holders」交差；做不到则整节 `⚠️ blocked` + 已尝试链。

### 4. Mechanism Layer

**Elevator (R1 · 开篇两句 · Standard+)**
- Money in (one verifiable sentence):
- Money out (one verifiable sentence):
- If alpha exists, it hangs on this measurable variable:

- How money comes in:
- How money leaves:
- Who gets paid:
- Who is the marginal buyer:
- Main reflexive loop:
- Main failure mode:

### 5. Social / X / Community Read

- **Heat check (R3 · Standard):** window 7d / 14d · sample links · warming / cooling / flat
- Main narrative:
- Who is pushing it:（Standard+ **二选一**：**(A)** 近 7d/14d + **≥2 可点开链接**或具名 handle+URL；**(B)** 首句声明「仅为传播渠道类型归纳，未做命名 KOL 清单」→ 须在 §2「仍缺」或监控清单写 **具体补证检索 query**。）
- Is discourse growing or fading:
- Founder / dev identity and social graph:
- Signal vs noise judgment:

### 6. Risk Register

- Technical risk:
- Liquidity risk:
- Dilution / unlock risk:
- Governance / admin risk:
- Regulatory risk:
- Narrative collapse risk:

### 7. Why There May or May Not Be Money to Make

- Bull case:
- Bear case:
- What has to happen for upside to continue:
- Why this may already be crowded:
- Mispricing hypothesis:

### 7a. Investment thesis（独立段落，≥1y 可证伪）

- Cashflow / moat / sustainable share / regulatory carry（若无：**「本标的当前无独立 investment thesis，仅投机结构」** + 理由）

### 7b. Speculation thesis（独立段落，天～周；不得与 7a 混写成一个故事）

- Catalyst / crowding / β / narrative rotation:

### 8. Participation Guidance for Leo

- Best fit bucket: core / satellite / speculative
- Entry style: spot / staggered / event-driven / no trade
- Initial size cap:
- Scale-in condition:
- **Invalidations / kill conditions (R2):** each row = metric + data source + threshold type (absolute / vs peer / MoM)
  | Metric | Source | Threshold type | Trigger |
  |--------|--------|------------------|---------|
  | | | | |
- Exit triggers:

### 9. Data Limitations

- Unverified claims:
- Missing datasets:
- What would most improve confidence:

### 10. Monitoring Checklist

- Price / volume metrics:
- Chain / holder metrics:
- Fundamental / operating metrics:
- Social / sentiment metrics:
- Catalyst calendar:

### 11. Behavioral Guardrail

- Is this FOMO or analysis?
- Am I anchored to someone else's screenshot / PnL?
- What evidence would disconfirm the thesis?
- What loss is tolerable if wrong?

### Appendix A — Five-pillar self-check（Standard+，压缩表）

| Pillar | Status (✅/⚠️/➖) | Evidence pointer (section or URL) |
|--------|-------------------|-------------------------------------|
| A Foundational | | |
| B Technical | | |
| C Tokenomics | | |
| D Traction / PMF | | |
| E Market structure | | |

（定义见 `professional-pillars.md`。）

### Appendix B — Scenarios（仅 `[Full DD]`）

| Scenario | Key assumptions | Price or KPI triggers | Invalidation |
|----------|-----------------|-------------------------|--------------|
| Bear | | | |
| Base | | | |
| Bull | | | |

---

## Mode B — Cross-Asset Comparison Report

### Metadata（必填）

- **Depth tier:** `[Quick DD]` / Standard / `[Full DD]`
- **Report as-of (UTC):**

### Data provenance table（必填）

| Claim | Source | As-of (UTC) | Confidence |
|-------|--------|-------------|--------------|
| Per-asset prices / returns | | | |
| Cross-asset statistic (e.g. correlation) | | | |

### 0. Recommendation First

- Verdict:
- Decision relevance for Leo: hedge / signal / narrative filter / no actionable edge
- Primary takeaway:
- Why now:

### 1. Comparison Objective

- What question is being answered:
- Why these assets / markets are being compared:
- What would count as a useful conclusion:

### 2. Assets Compared

- Asset A:
  - canonical symbol:
  - market / venue:
  - asset class:
  - quote currency:
- Asset B:
  - canonical symbol:
  - market / venue:
  - asset class:
  - quote currency:
- Additional assets if applicable:

### 3. Window and Data Alignment

- Comparison window:
- Time granularity:
- Session alignment method:
- Data sources:
- Symbol mapping / normalization notes:

### 4. Unified Feature Table

- Latest price:
- Return over selected windows:
- Volume / turnover:
- Range / volatility:
- Indicators actually used in the conclusion:

### 5. Relationship Read

- Correlation / relative return / regime contrast:
- Lead-lag impression if any:
- What appears structurally linked:
- What appears coincidental:
- What would invalidate the linkage claim:

### 6. Market-Structure Caveats

- Venue / liquidity differences:
- Session-hour mismatch:
- Leverage / funding / basis effects:
- Macro / policy distortions:

### 7. Actionability for Leo

- How this helps:
- What not to over-interpret:
- Whether it changes positioning, monitoring, or nothing:

### 7a / 7b. Investment vs Speculation framing（若对比服务于仓位决策）

- **Investment:** …
- **Speculation:** …

### 8. Data Limitations

- Missing datasets:
- Alignment weaknesses:
- Unverified assumptions:

### 9. Monitoring Checklist

- Trigger metrics:
- Thresholds to re-check:
- Catalyst calendar:
- Kill conditions for the relationship thesis:

### Post-trade addendum（可选 · 公开 HTML）

> 作者事后有实盘且愿意披露时追加；**须与报告 Verdict 分离**，写清边界。

- **What happened（事实）：** venue · open/close UTC · size（可区间）· realized PnL（可选）
- **Boundary（必填）：** 个人记录 · **非**对读者的交易指令 · 盈利 ≠ 验证 Verdict · 不构成投资建议
- **Data freeze：** 正文行情/结论时点**不变**；后记不触发全文重拉 API（除非另开 revision）

### Appendix A — Five-pillar self-check（可选；若对比涉及单标的深度则按 Mode A 支柱逐资产压缩）

---

*对外交付时可删本文件路径，保留方法论与表格结构即可。*
