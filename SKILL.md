---

name: asset-dd-and-opportunity-evaluation
description: Institutional asset DD (Standard): five pillars, comps, on-chain, sourcing. Use for DD/尽调/值不值得买. NOT price-only or profile-address; 快扫 = Quick tier; personal overlay → optional leo-extensions.
version: 2.1.0
license: MIT
---

## Package · 开源包

| 文件 | 作用 |
|------|------|
| **`SKILL.md`** | 可移植 core workflow（本文件） |
| **`references/report-template.md`** | 报告 scaffold |
| **`references/professional-pillars.md`** | 五支柱自检 |
| **`references/tool-adapters.md`** | 可插拔数据源（无 vendor lock-in） |
| **`references/leo-extensions.md`** | **可选** · 作者个人仓位/工具/sizing（fork 可删） |
| **`references/rwa-composability-tier.md`** | RWA 类资产扩展字段 |
| **`examples/`** | 脱敏样例报告 |
| **`OPEN-SOURCE.md`** | 发布边界 + preflight |
| **`RUNS.md`** | 历史跑法记录 |

公开 HTML 范例：`leolabs-research-bundle`（APR）；方法论 v2 路线图：`references/roadmap-v2.md`。

---

## Trigger Phrases

Use when user says **DD / 尽调 / 做个调研 / 评估一下 / 这个币/股票怎么样 / 值不值得买** — default **Standard**：五支柱 + 竞争集 + 链上 proxy + 溯源表 + 投资/投机分述 + 参与桶。

- **Quick tier**：用户 **明确**「快扫 / 口头判断」
- **NOT** price-only / Polymarket 地址画像（`profile-address`）
- **Personal overlay**（实盘张数、perp、个人动作）：可选模块 `references/leo-extensions.md` → `leo-position-overlay`

---

## Skill 质量闭环

- 对外 DD 读起来「空、怪、不像机构级」→ **先改 skill + template**，不只改单篇报告
- 缺数据只允许 **✅ / ⚠️ / ➖ + URL/原因**；禁止用泛泛类别话顶替 checklist
- Public-facing 正文：**禁止** `asset-dd…skill`、Claude/Codex 等内部名；**%T / 分桶** 须跟防火墙句（见 template §0）
- §谁在推（template §5）：**(A) 证据级**（时间窗 + ≥2 链接）或 **(B) 声明未扫全量 + 补证 query**

---

When to use
- User asks whether an asset is worth following, buying, trading, or allocating to.
- Asset can be stock, major crypto, protocol token, microcap alt, meme token, or platform-launched token.
- Especially important when the prompt comes from chat screenshots, community chatter, X posts, referral links, or fast-moving social narratives.

Core rule
- First identify the asset object precisely before discussing market cap, valuation, or opportunity.
- Never assume the shared link is the tradable asset. Distinguish between:
  1) platform/protocol
  2) platform token
  3) token launched on the platform
  4) company equity

0. Referral / promo-link pre-gate (mandatory when entry is social)
- If the asset surfaced via a referral link, group dump, DM, affiliate code, or KOL screenshot, answer these BEFORE entering step 1:
  - Is the link a trading venue or a referral wrapper? (e.g. `rise.rich/ref/XXXX` is a referral wrapper, not an asset)
  - Who benefits if the user signs up / buys? The sender? The platform? A referral pool?
  - Is the "asset" actually a platform account, a platform token, or a token listed on the platform?
  - Is there a tradable canonical identifier (contract / mint / ticker) outside the referral context?
- If answers are: referral wrapper + no canonical identifier + only social pressure to enter → stop here, classify as `avoid` or `watch-only`, skip full DD.
- If answers point to a real underlying asset, strip the referral wrapper and proceed to step 1 using only the canonical identifier.

Mandatory workflow

### Depth tiers（开跑前先选；**默认 Standard**）
- **Quick**：≤~20min；标的 + 机制 + 核心风险 + 结论；无链上锚点时可跳过 §链上/竞品细表。标题 `[Quick DD]`。
- **Standard（默认）**：下文 **2.5–4.6** 全执行。标题 `[Standard DD]` 或省略。
- **Full**：Standard + **≥4 竞品** + **bull/base/bear 三情景** + 关键数字 **双源交叉** 至少一处；标题 `[Full DD]`。

### 专业度对齐（五支柱）
打开 `references/professional-pillars.md`。每一支柱三态：**✅ / ⚠️ / ➖** — 禁止留白。

### RWA 分支（可选）
评估 tokenized treasury / credit / equity / commodity 时，加读 `references/rwa-composability-tier.md`，填 **composability_tier** + **defi_integration_ratio**。

1. Identify the object
- Determine exactly what is being analyzed: stock/ETF · L1/L2 · protocol · token/meme · company equity
- Lock identifier: ticker · contract/mint · stock code · official URL
- DO NOT classify from bio/handle alone. Run ≥1 social-discovery attempt (see `tool-adapters.md`) before locking object class.
- If prior turn classified the object, state whether new evidence **contradicts/confirms** prior verdict.

2. Confirm basic facts
- Chain / venue / market · official site/docs/X/TG
- Where it trades: CEX / DEX / internal
- Supply: circulating · FDV · total/max
- If exact asset unknown, stop short of hard valuation claims.

2.5 Tokenomics, unlocks & supply stress（crypto 必做；股票换「股本+激励」）
- **≥2 独立路径** unlock/vesting，每条 `URL → outcome`
- 供应表：circ / total / max / FDV / Mcap / **FDV÷Mcap**；90d unlocks → catalyst or risk
- 价值捕获一句；仅治理 → **无现金流捕获**
- 全失败 → **Tokenomics 证据缺口** + 下一步动作
- 无日级 unlock 表 → **线性外推边界一句**（scenario bound not forecast）

2.6 Competitive set（Standard+ · **≥2 peers**）
- 同叙事桶或同交易结构；每行 **≥1 数字锚** 或整行 ⚠️
- 一句：**溢价像 α 还是板块 β？** + falsify 路径

3. Build a source hierarchy
- **Stocks**：IR/filings/earnings · quality market data · comps · KPI checklist
- **Crypto majors**：docs/tokenomics/governance/audits · CoinGecko/CMC · DefiLlama/Token Terminal/Dune · explorer/GitHub/X
- **Small-cap / meme / fresh launch**：contract first · Birdeye/DexScreener/GMGN · holder/LP/permissions · founder social graph

4. Social discovery（fast assets · mandatory）
- 按 `references/tool-adapters.md` §1.1 选 adapter；**禁止**把 social 当 truth，须链上/数据交叉
- Treat social as signal generation, not truth.

4.5 Cross-market data layer
- Normalize symbol/venue/class/currency/session before compare
- Relationship claims need explicit window + statistic (correlation / relative return)

4.6 On-chain & holder proxy（有合约时 Standard+ 必尝试）
- ≥1 可复核 proxy + **日期 + 数字句**，或 **⚠️ blocked** + attempt log
- 禁止仅「读者自行打开 Holders」

5. Force the mechanics baseline
Before any EV/opportunity claim, extract:
- how price is formed · fees · liquidity/LP/counterparty · slippage · unlock/dilution/mint/admin · leverage/liquidation · settlement/redemption/peg

**§4 电梯间两句（R1 · Standard+ 机制层开篇强制）**
1. **钱从哪进、从哪出各一句**（可验证路径，非 slogan）
2. **若存在 alpha，挂在哪个可验证变量**（一句；例：主网 TPS / 日 fee / OI 变化）

Mechanics extraction is the agent's job. API locked → switch tools per `tool-adapters.md` §1.4.  
Mcap unknown → bounded estimate from pool depth with **stated assumption**.

6. Evaluate in six layers
A. Object · B. Mechanism · C. Evidence · D. Risk · E. Opportunity · F. Participation

Participation buckets: **avoid / watch only / research position / tiny speculative / conviction position**

7. Output format
- Scaffold：`references/report-template.md`
- 文首：**Depth tier** + **UTC as-of**（分钟级为佳）
- **溯源表**（Mcap/supply/unlock/volume/on-chain）
- **投资 thesis** + **投机 thesis**（独立两段；无投资 thesis 须明写）
- Standard+：**五支柱自检** 附录
- **失效/降仓条件（R2）**：每条 = **指标名 + 数据源 + 阈值类型**（绝对/相对竞品/环比）；禁止无来源魔法数字
- **§5 讨论热度（R3 · Standard 低配）**：近 7d/14d 社交检索各一次 → 样例链接 + 升温/降温判断；或声明未扫全量 + 补证 query
- **§3.5 市值情景（Full 或用户问「能到多少 mcap」时）**：circ 为主（PoW 早期 FDV 常虚高）· ≥3 可比标的 · bull/base/bear 三档 + 每档 **可证伪触发器**（见 Pearl 范例 `examples/pearl-standard-dd-excerpt.md` §3.5）

Report modes:
- **Single-asset**（default）：recommendation first → identification → data map → facts → social → risks → opportunity → participation → invalidations → limitations → monitoring
- **Cross-asset**：comparison objective → identifiers → aligned window → feature table → relationship read → caveats → actionability

8. Behavioral guardrail
- FOMO vs analysis · anchored to others' PnL? · disconfirmers? · tolerable loss?
- Explicit for social/referral/fast-moving setups.

Portfolio guidance (portable defaults)
- Separate investment from speculation.
- Social/referral microcaps → default speculative unless disproven.
- No reliable liquidity or unclear identity → watch-only or tiny experimental.
- State horizon: compounding / thematic / momentum / one-shot gamble.
- **Venue-depth cap**：position vs pool TVL（≤3% / 3–10% / >10% 三档）；与 portfolio % cap **取 min**；报告须写算式。
- **Optional personal caps**：若部署者提供 portfolio snapshot，见 `references/leo-extensions.md` §3–§5。

Pitfalls
- Protocol ≠ token · FDV ≠ circ mcap · X excitement ≠ chain data · polished docs ≠ liquidity

Transient failure policy
- Up to 3 retries + backoff · switch adapter · mark degraded · cooldown retry later

Verification checklist
- Depth tier 与产出一致？
- 五支柱无静默留白？Pillar B 审计 ✅/⚠️？
- 2.5 双路径 + scenario bound？2.6 ≥2 竞品 + 数字锚？
- 4.6 数字句或 ⚠️ blocked？
- **R1** 机制层电梯间两句？
- **R2** 失效条件含 指标+源+阈值类型？
- **R3** §5 证据级或声明+query？
- Public-facing：无 skill 名、%T 防火墙？
- 溯源表、投资/投机分述、监控清单齐全？
- Object/venue/sources/social/facts/participation guidance 均已覆盖？
