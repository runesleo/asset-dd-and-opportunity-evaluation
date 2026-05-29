# Leo Extensions（可选 · 非开源必需）

> **用途**：Leo 个人部署时的 **下游模块、仓位规则、工具栈、交叉复核**。  
> **开源边界**：公开 repo 可保留本文件作「作者自用配置示例」；第三方 fork 可删或替换，**不影响 core workflow**。

---

## 1. 与 `leo-position-overlay` 的串联

| 模块 | Skill | 作用 |
|------|--------|------|
| **① 标的侧尽调** | `asset-dd-and-opportunity-evaluation` | 公开信息、机制、风险、参与桶 |
| **② 个人仓位** | `leo-position-overlay` | perp 快照、费率、清算距离、个人动作菜单 |

**顺序**：默认 **先 ① 后 ②**。若只有 `position_report` 且说「先别看叙事」→ 可只做 ②，文首标注 **标的公开信息尽调未跑或待补**。

**公开闸门**：发推/文章/给朋友 PDF 以 ① 为主；② 仅保留匿名化结构句。合并文件时拆 **`§ 标的（公开）`** / **`§ 仓位与动作（个人，不公开）`**，导出前删后节或另存 `-private`。

---

## 2. 工具栈（Leo profile）

见 `references/tool-adapters.md` § Leo profile。要点：

- X 语义讨论：`leo-x reaction/verify`（xAI `x_search`）
- 精确推文 ground truth：`opencli twitter` / `xreach`
- URL 路由 SSOT：`~/.claude/docs/url-routing.md`
- 浏览器读 dashboard：`mcp__playwright__*` 或 Chrome CDP

---

## 3. Portfolio 快照与 sizing caps

开跑 sizing 前读取 `~/.claude/portfolio/latest.json`（`T` = total net worth）。若不可读或 stale >24h：**只给 % cap，不写绝对美元**。

**Per-asset bucket caps**（本标的）：

| Bucket | Cap |
|--------|-----|
| tiny speculative | ≤ 0.5% T，绝对上限 $500 |
| research | ≤ 2% T |
| conviction（crypto 单名） | ≤ 5% T |
| avoid / watch-only | $0 |

**Aggregate**：所有 social-driven microcap 投机合计 ≤ 3% T；超限须 swap-out 而非 stack。

**Venue-depth cap**（与 portfolio cap 取 min）：

- position ≤ 3% pool TVL → ~5% slippage，可接受
- 3–10% → 10–25% slippage，仅 experience fee
- \>10% → 你是 market event

报告里必须写 venue-depth 算式（例：「$50 = 3% of $1.7K TVL pool」）。

---

## 4. KOL / builder 参与模式

默认 DD 假设 retail buyer。Leo 作为垂直 KOL（@runes_leo，BTC/Runes/PM）时，**额外**提供四模式供选：

| 模式 | 要点 |
|------|------|
| **A** Content-first + 小仓 | 小 stake + 写稿 + 持仓披露 |
| **B** Neutral analyst | 无仓，纯结构拆解 |
| **C** Stakeholder outreach | DM 创始团队，换 allocation / rev share |
| **D** Hybrid A+C | 最高 EV，最高声誉风险 |

**Heuristic**：缺中文区 + 垂直 fit + early stage → C 常最高 EV；纯 meme 无团队 → A 或 skip。

**披露**：推荐 A/D 时，报告内草稿披露句（例：「I hold $X — DYOR — not financial advice」）。

---

## 5. Codex cross-review gate

`research position` 或 `conviction position` 级建议须独立 Codex review（`~/.claude/CLAUDE.md` P0）：

1. 产出 DD 报告
2. `/codex review` + reasoning_effort=xhigh
3. 仅当 Codex 同意才标 `✅ Codex reviewed`；分歧则并列呈现
4. `tiny speculative` / `watch-only`：可选；`avoid`：不需要

---

## 6. 公开示例（内部路径）

| 标的 | 产物 |
|------|------|
| APR / aPriori | `https://leolabs.me/research/apr-apriori-2026-05/report.html` · bundle `Projects/content/research/leolabs-research-bundle/` |
| Pearl $PRL | `examples/pearl-standard-dd-excerpt.md`（脱敏 excerpt） |

---

*Version: 1.0.0 · optional module · MIT*
