# RWA Composability Tier 字段（asset-dd 扩展 · 2026-05-24）

> **来源**：T-M20260524-03 a16z「The tokenization boom in 7 charts」memo（详见 `~/.claude/memory/memo_T-M20260524-03_a16z-rwa-composability.md`）。
> **加入方式**：本文件为 asset-dd 的扩展 reference（atomic 增量，未改 SKILL.md core 流程）。下次评估 RWA 类资产时，主 prompt 应在「分类/标签」环节引用本字段。
> **状态**：v0 草案（Cursor daemon 起草，待 Codex / Leo 复验后再考虑提升为 SKILL.md 一级字段）。

---

## 1. 为什么要这个字段

a16z 给出的硬数据：tokenized assets（不含 stablecoin）已到 ~$34B，但最大类别 U.S. Treasury debt（约 $15B）中只有 ~5%（~$800M）真正进入 DeFi 协议。意味着 95% 的「tokenization」实际上只是 **digitization**——记录上链，但 transferability / 可作为抵押品 / 可被其他协议 compose 几乎不存在。

旧版 asset-dd 对 RWA 类资产只问「是否上链 / 谁发行 / 监管定位」，**没有问「上链之后能不能被链上其他协议用」**，导致 BlackRock BUIDL 类「合规白名单 PDF」和 Ondo USDY / Maple syrupUSDC 类「为链上抵押设计」的资产在 DD 结论里被错误并列。本字段补这一缺。

## 2. 字段定义

```yaml
composability_tier:
  type: enum
  values: [distributed, hybrid, represented]
  required_for: [RWA, tokenized-treasury, tokenized-credit, tokenized-equity, tokenized-commodity]
```

### Tier 定义（沿用 RWA.xyz 二分 + 中间态）

| Tier | 判定条件 | 典型资产 |
|---|---|---|
| **distributed** | 可在公链自由转账（无白名单 / 无 KYC gate），且至少被 1 个非自家 DeFi 协议作为抵押/borrow base/perp margin 集成 | Ondo USDY、Mountain USDM、Maple syrupUSDC |
| **hybrid** | 链上 transferable 但有白名单 / per-jurisdiction 限制；或已上链但 DeFi 集成 < 1 个真协议 | Backed bIB01、Superstate USTB、部分 Centrifuge pool |
| **represented** | 记录上链但 transferability 受 issuer 单点控制（赎回/转账需 issuer 名单审核），DeFi 集成基本为零 | BlackRock BUIDL、Franklin BENJI 早期、多数 institutional RWA |

## 3. 必填子字段（评估时同步收集）

- **on_chain_supply_usd**：链上发行总量（统一美元）
- **defi_integrated_supply_usd**：实际进入 DeFi 协议（lending / DEX / perp margin / collateral）的部分
- **defi_integration_ratio** = `defi_integrated_supply / on_chain_supply`
  - > 20%：高 composability 渗透
  - 5–20%：中
  - < 5%：digitization-only（对照 a16z：Treasuries 整体 ~5%）
- **integrated_protocols**：实际接入的协议清单（≥ 3 个 = 强信号）
- **transfer_restriction**：`none | whitelist | kyc-per-jurisdiction | issuer-approval`

## 4. 评估输出锚点

在 asset-dd 最终 report 里，RWA 类资产必须显式给出：

> **Composability Tier**: distributed / hybrid / represented
> **DeFi Integration Ratio**: X% （on-chain supply $A → DeFi $B）
> **Integrated Protocols**: [Aave, Pendle, Morpho, ...]
> **Composability 风险**：如果 ratio < 5% 或 transfer_restriction != none，必须在「投资视角」一节中明示「该资产的『链上』属性目前是 marketing 而非 mechanics」。

## 5. 投机/叙事 hook（供 PM Intelligence / 内容线引用）

- 叙事 rotation 时，distributed-tier 资产相对 represented-tier 大概率跑赢，因为前者真正吃到「上链美债 → 进 lending market → 拉杆 → 二阶 yield」的乘数。
- 反向信号：如果某 represented-tier 资产突然宣布「接入 Aave/Pendle」类公告，是 tier 跃迁事件，应即时进入 DD reopened 队列。

## 6. 待 Codex 复验项

- [ ] 是否升级为 SKILL.md 一级字段（当前为 references 扩展）
- [ ] integrated_protocols 数据源 SSOT（候选：RWA.xyz、DefiLlama RWA 板块、各协议公告）
- [ ] hybrid 中间态判定阈值是否需要细化（目前用「至少 1 个协议」做下限，可能过宽）

---

*v0 by Cursor daemon · 2026-05-24 · T-M20260524-03*
