# asset-dd-and-opportunity-evaluation

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

面向 AI Agent 的**机构级资产尽调**工作流（Claude Code / Cursor / Codex 等）。

**English:** [README.md](./README.md)

**默认深度：Standard** — 五支柱、竞品集、链上 proxy、溯源表、投资/投机 thesis 分述。

---

## 你能得到什么

- **结构化尽调清单** — Quick / Standard / Full（`SKILL.md`）
- **报告模板** — 溯源表、§2.5–4.6、投资/投机分述（`references/report-template.md`）
- **可插拔数据源** — 无 vendor 锁定（`references/tool-adapters.md`）
- **公开样例** — APR 线上 HTML + Pearl 脱敏 excerpt
- **可选作者扩展** — `references/leo-extensions.md`（fork 可删）

---

## 怎么工作

```text
用户：「尽调 APR / 这个币怎么样」
  → Agent 读 SKILL.md
  → 默认 Standard 档
  → 按 report-template 产出报告
  → 每个数字：来源 URL + UTC 时点 + 五支柱 ✅/⚠️/➖
```

**不包含：** 实时行情服务、自动下单、投资建议。

---

## 三条路径

| 路径 | 适合 |
|------|------|
| **开源（本仓库）** | 会折腾 · clone 装进 Agent |
| **[样例报告](https://leolabs.me/research/apr-apriori-2026-05/report.html)** | 先看产出长什么样 |
| **[leolabs 产品页](https://leolabs.me/tools/asset-dd)** | Agent 完整包 / 代跑报告（可选付费） |

定价（2026-05）：Standard 代跑 $12 · Full $35 · Agent 完整包 $45 — 以产品页为准；**自建不花钱**。

---

## 快速开始

```bash
git clone https://github.com/runesleo/asset-dd-and-opportunity-evaluation.git
# 复制到 Agent 的 skills 目录，然后：
# 「对 XXX 跑一份 Standard 尽调」
```

1. 复制本目录到 Claude Code / Cursor / Codex skills 路径。
2. 触发词：**尽调 / DD / 值不值得买**。
3. Agent 读 `SKILL.md` → 按 `references/report-template.md` 输出。

**Fork：** 可删 `references/leo-extensions.md` · 跑 `bash scripts/fork-preflight.sh`

---

## 环境要求

- 能读本地 skill 文件的任意 Agent
- **数据：** 自备 API / 浏览器工具（见 `tool-adapters.md`）
- **隐私：** 若用浏览器 Cookie 或登录态抓数据，只在你本机，不进仓库

---

## 深度档位

| 档位 | 触发 | 产出 |
|------|------|------|
| **Quick** | 用户明确「快扫」 | `[Quick DD]` |
| **Standard** | 默认 | §2.5–4.6 全执行 |
| **Full** | 深度/发布 | + ≥4 竞品 + 三情景 + 双源交叉 |

---

## 已验证

| 标的 | 档位 | 证据 |
|------|------|------|
| APR / aPriori | Standard → 公开 HTML | [leolabs 报告](https://leolabs.me/research/apr-apriori-2026-05/report.html) · `RUNS.md` #1 |
| Pearl $PRL | Standard 脱敏 | `examples/pearl-standard-dd-excerpt.md` |

完整记录：[`RUNS.md`](./RUNS.md)

---

## 已知限制（v2.1）

- 网站目前 **1 篇** 完整 HTML 样例（APR）；第二篇规划中 — `roadmap-v2.md`
- Unlock 日历常需 ⚠️ 或付费数据源
- `leo-extensions.md` 为作者自用，非 core 必需
- Agent 完整包 zip **不在** 本仓库（通过 leolabs 单独交付）

---

## 路线图

- [ ] 第二篇公开样例（英文 Full 或链上失败案例）
- [ ] Pearl 完整 HTML 上 research hub
- [ ] 公开稿首屏 TL;DR 强制 — `reader-guide.md`

详见 `references/roadmap-v2.md`

---

## 关于作者

*Leo（[@runes_leo](https://x.com/runes_leo)）— AI × Crypto 独立构建者。在 [Polymarket](https://polymarket.com/?via=runes-leo&r=runesleo&utm_source=github&utm_content=asset-dd-and-opportunity-evaluation) 做量化，用 Claude Code 和 Codex 搭数据与内容管线。*

*[leolabs.me](https://leolabs.me) — 写作 · 社群 · 开源工具 · 独立项目*

*[X 订阅](https://x.com/runes_leo/creator-subscriptions/subscribe) — 付费内容周刊*

*Learn in public, Build in public.*

---

## 许可

MIT — 见 [`LICENSE`](LICENSE)。`examples/` 样例注明处为 CC BY 4.0。

**变更记录：** [`CHANGELOG.md`](CHANGELOG.md)
