# Professional DD pillars（机构级自检清单）

> 吸收公开框架中常见维度（如 **Foundational / Technical / Tokenomics / Traction / Market structure** 五支柱思想），映射到本 skill 的可执行检查项。  
> **不是**法律/合规意见；**是**研究完整性自检。

## Pillar A — Foundational integrity（主体与治理）

| 检查项 | 标准 |
|--------|------|
| 团队 / 基金会 / 运营主体 | 能否指到 **具名实体** 或 **可验证注册信息**？匿名程度过高 → 风险段 **加粗** |
| 披露与沟通 | 官网 / 文档 / X 是否 **可打开**、**最近更新**？长期停更 → 记为黄旗 |
| 治理 | 有无链上治理、多签、时间锁？**升级权限** 谁握？ |
| 监管与地理 | 主要用户/所上地区；**证券/utility 叙事** 是否自洽（仅陈述事实与不确定性） |

## Pillar B — Technical resilience（技术与安全）

| 检查项 | 标准 |
|--------|------|
| 审计 | **审计机构 + 日期 + 范围**；有无 **critical 未修复** 公开记录 |
| Bug bounty | Immunefi 等 **有无计划/赏金池** |
| 代码活跃度 | GitHub **commits / releases** 近 90d 趋势（量化一句） |
| 合约风险 | **代理升级 / owner / mint / pause** 权限一句话；无法读取则写明「链上未读 ABI」 |

## Pillar C — Tokenomics & value accrual（筹码与价值捕获）

| 检查项 | 标准 |
|--------|------|
| 流通 / 总量 / FDV | **必须**有表；**FDV/Mcap** 有则必算 |
| Unlock / vesting | **必须尝试**公开源（见 SKILL 主文 **2.5**）；每次尝试 **记录 URL + 结果** |
| 通胀 / 排放 | 若有 **emissions schedule** 或 API，写入；无则写假设区间并标 **assumption** |
| 价值捕获 | 费用 **流向**（staker / treasury / burn / LP）— **无则写「无直接捕获」** |

## Pillar D — Traction & PMF（牵引与经营）

| 检查项 | 标准 |
|--------|------|
| 链上活跃 | **TVL / DAU / tx / fee** 之一或多个；DefiLlama 无则 **替代指标**（官方 dashboard、subgraph、累计交易量） |
| 商业 | **集成方 / 客户 / 付费** 任一可验证事实；无则写「未披露」 |
| 路线图 vs 交付 | **已交付 vs 承诺** 对照表（至少 3 行） |

## Pillar E — Market structure & liquidity（市场结构与流动性）

| 检查项 | 标准 |
|--------|------|
| 场所表 | **主要 venue + 24h 深/额**（能拉则拉满；拉不到写「未拉取原因」） |
| 衍生品 | perp：**OI（USD）/ funding / Top L/S**（若存在）；**basis**（mark-index） |
| 集中度 | **大户 / LP / CEX 余额** 任一 proxy；无则 Explorer 尝试后记失败 |
| 滑点假设 | 对 **计划入场规模** 一句 venue-depth 逻辑（沿用 skill 内 venue cap 规则） |

## 投资 vs 投机（必须在报告中分两段）

- **Investment thesis**：现金流、护城河、可持续份额、监管可承载性——**时间尺度 ≥ 1 年** 亦可证伪。  
- **Speculation thesis**：事件、拥挤度、β、叙事轮动——**时间尺度天～周**，与上段 **不得混写成一个「故事」**。

## 数据溯源表（报告中独立一节）

| Claim | Source (URL 或 API) | As-of (UTC) | Confidence |
|-------|---------------------|-------------|--------------|

---

*内部 reference；对外报告可删本附件路径，只保留方法论段落。*
