# Tool Adapters（可插拔数据源）

> **原则**：asset-dd 要求的是 **ground truth 与 attempt log**，不是特定 vendor。  
> 按你环境选 adapter；失败须写 `⚠️ blocked` + 原因，禁止静默省略。

---

## 1. 通用优先级（默认 profile）

### 1.1 社交 / 叙事（fast-moving assets · Standard+ 必做）

| 优先级 | 能力 | 开源/通用替代 |
|--------|------|----------------|
| 1 | 单帖 / 账号 / thread 原文 | X API · Nitter 实例 · 官方 status URL + 浏览器 |
| 2 | 语义讨论 / 舆情 synthesis | Web search + 多源交叉 · Grok/Perplexity 等（标 subjective） |
| 3 | 时间线 / 互动 metrics | X API advanced · 手读 profile |
| 4 | 最后手段 | 公开 profile 页 + search snippets |

**输出要求**：时间窗 + ≥2 可复核链接，或声明「未扫全量 KOL 清单」+ 补证 query（见 template §5）。

### 1.2 市场数据

| 数据 | 通用源 |
|------|--------|
| 价 / Mcap / FDV / circ | CoinGecko · CoinMarketCap · 所 API |
| DEX | DexScreener · GeckoTerminal · Birdeye |
| DeFi TVL / fee | DefiLlama · Token Terminal · Artemis |
| Unlock / vesting | TokenUnlocks · CryptoRank · 官方 transparency |
| 链上 holders / TVL | Etherscan/BscScan/Solscan API · Dune · Playwright 读 dashboard |

### 1.3 跨市场（A/HK/US/crypto）

先 **normalize**：canonical symbol · venue · asset class · quote currency · session。  
禁止混用裸 ticker。关系声称须指定窗口 + 简单统计（correlation / relative return）。

### 1.4 浏览器 fallback

SPA / 反爬 dashboard：Playwright / Puppeteer / Chrome CDP `browser_evaluate` 优先于反复 snapshot。

---

## 2. Leo profile（作者自用 · 见 `leo-extensions.md`）

在通用优先级之上，Leo 环境默认：

1. `opencli twitter` — 单帖/账号/thread
2. `leo-x reaction/verify` — X 语义 + sourced brief
3. `xreach` — 时间线 metrics
4. Grok Bridge — 仅当前三者失败

---

## 3. Attempt log 格式（所有 adapter 统一）

```markdown
- Attempt N: `<tool or URL>` → outcome: `<data / 403 / rate-limit / N/A>`
```

Standard+ 的 unlock（≥2 路径）、链上 proxy（≥1 数字句）、社交 §5（证据级或声明+query）均须可见 attempt log。

---

*Version: 1.0.0 · MIT*
