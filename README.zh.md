# asset-dd-and-opportunity-evaluation

面向 AI Agent 的**机构级资产尽调**工作流（Claude Code / Cursor / Codex 等）。

**默认深度：Standard** — 五支柱、竞品集、链上 proxy、溯源表、投资/投机 thesis 分述、参与桶。

---

## 快速开始

1. 将本目录复制到所用 Agent 的 skills 目录即可。
2. 用户说 **尽调 / DD / 这个币怎么样 / 值不值得买** 时触发。
3. Agent 读 `SKILL.md` → 按 `references/report-template.md` 产出报告。

**可选：** fork 时可删除 `references/leo-extensions.md`（作者个人仓位/工具配置，非必需）。

---

## 深度档位

| 档位 | 触发 | 产出 |
|------|------|------|
| **Quick** | 用户明确「快扫」 | `[Quick DD]` |
| **Standard** | 默认 | §2.5–4.6 全执行 |
| **Full** | 深度/发布 | + ≥4 竞品 + 三情景 + 双源交叉 |

---

## 公开范例

| 标的 | 形态 |
|------|------|
| APR / aPriori | [leolabs 线上 HTML](https://leolabs.me/research/apr-apriori-2026-05/report.html)（**目前网站唯一完整范例**） |
| Pearl $PRL | `examples/pearl-standard-dd-excerpt.md`（脱敏，float 带 ⚠️） |
| 排版 starter | `examples/report-starter.html` |

**怎么读 dense 报告：** `references/reader-guide.md`

**已知缺口：** 网站仅 1 篇 live HTML；开源 credibility 建议再补 1 篇（英文 Full 或 meme 失败案例）。

---

## 核心原则

1. **先识别标的** — 平台 ≠ 代币 ≠ 返佣链接。
2. **事实先于叙事** — 社交生成假设，链上/市场数据证伪。
3. **禁止静默留白** — 五支柱必须 ✅ / ⚠️ / ➖。
4. **投资 ≠ 投机** — 两段 thesis 不可混写。
5. **场所深度约束 sizing** — 池子太浅时 portfolio % 无意义。

---

## 许可

MIT — 见 `LICENSE`。`examples/` 样例报告注明处为 CC BY 4.0。

---

## 变更

- **2.1.0** — 开源包结构 · tool adapters · Leo 扩展拆分 · R1–R3 · 市值情景 §3.5
