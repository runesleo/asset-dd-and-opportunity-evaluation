# Leo Extensions — Action-First Personal Overlay

Semantic version: `action-first-2026-09-13-v1`

用途：Leo 个人部署时的仓位、工具栈、复核与参与路径扩展。它补充 core DD，不改变公开仓库的无自动交易边界。

---

## 1. 与 `leo-position-overlay` 的串联

| 模块 | 作用 |
|---|---|
| `asset-dd-and-opportunity-evaluation` | 标的、机制、安全、赔率、Phase-A / Standard / Full DD |
| `leo-position-overlay` | 真实仓位、费率、清算距离、个人动作菜单 |

顺序不再是“完整 DD 全跑完才谈仓位”。

对于 fast/tradable opportunity：

`Phase-A 标的判断 -> bounded canary / no-capital decision -> deeper DD -> position overlay -> scale/reduce/exit`

若用户已经持仓，可先做 held-position action review，同时后台继续补标的证据。

---

## 2. 工具栈（Leo profile）

优先使用可验证、可复现的精确对象数据：
- 精确合约 / mint / pool / route；
- fresh executable quote；
- explorer / direct RPC / first-party docs；
- X / TG / 社群只作信号与叙事来源，不替代链上和市场事实。

工具故障时：bounded retry -> failover -> `TEMPORARILY_UNOBSERVABLE`，不把“你去查一下”丢回 Leo。

---

## 3. Portfolio 与 sizing

Fresh NAV 仍然是 **material scale** 的重要前提，但不是所有第一笔信息仓的前提。

### 3.1 Fresh NAV 可用

Portfolio cap 与 venue-depth cap 取更小值。

参考桶：

| Bucket | Reference cap |
|---|---:|
| tiny / information canary | ≤0.5% T，通常绝对额也应很小 |
| research / preposition | ≤2% T |
| conviction（crypto 单名） | ≤5% T，仅强证据+流动性+组合适配 |
| avoid / hard fail | $0 |

所有 social-driven microcap 的聚合风险仍需单独约束，不能因为每笔都小就无限堆叠相关尾部风险。

### 3.2 Fresh NAV 不可读或 stale >24h

旧规则“只给 % cap、不写绝对美元”会导致第一笔实验不可执行，现废止。

新规则：
- **禁止**伪造总资产百分比或 material scale target；
- 可在 Phase-A 满足时给固定最大损失的 `20U / 50U / 100U` bounded canary 建议；
- 必须有 exact identity、无 direct hard-security fail、该小额 route/sellability 可界定、非价格 thesis、kill condition；
- 标记 `SCALE_BLOCKED_NAV_UNKNOWN`；
- `>100U` 的 preposition / scale 默认等待 fresh NAV 或同等组合风险证据。

换句话说：NAV unknown 决定“不能放大到多大”，不自动决定“第一笔是否永远为 0”。

### 3.3 Venue-depth cap

位置相对池子/可执行深度的约束仍然有效：
- ≤3% pool TVL/可执行容量：通常可接受区间，但仍看实际 route/slippage；
- 3–10%：高冲击，仅特殊信息/事件仓；
- >10%：你本身可能成为 market event。

报告必须优先使用 fresh planned-size quote/depth，而不是用 TVL 百分比替代真实可卖性。

---

## 4. Information Canary

第一笔仓位可以同时购买两样东西：
1. upside optionality；
2. decision-relevant information。

参考目的：
- `20U DIAGNOSTIC_CANARY`：薄、早、信息价值高；
- `50U CANARY`：默认 meaningful early experiment；
- `100U STRONG_CANARY`：赔率更强且执行充足；
- `100–200U PREPOSITION`：需要更强 forward EV；
- `200U+ SCALE`：必须进入更高证据/NAV/深度/组合门。

这些只是 recommendation bands，绝不代表自动下单授权。

第一笔信息仓的价值可理解为：

`financial optionality + information value - execution cost - hard/security risk penalty`

---

## 5. Independent review / Codex rule

旧的“research / conviction position 必须 Codex 同意才通过”改为 **adversarial review**，不是投票委员会。

规则：
1. reviewer 找到直接 hard-security contradiction → 可阻止资本；
2. reviewer 找到可验证的重大事实冲突 → 自动复核，降低 confidence/size，必要时阻止当前层级；
3. reviewer 只是观点不同、概率不同、偏好不同 → 并列呈现，不机械 WAIT；
4. bounded `INFORMATION_CANARY` **不要求模型 consensus**；
5. `PREPOSITION` 建议消费一次独立反方 review 为佳；
6. `SCALE_ON_CONFIRMATION / CONVICTION_SCALE` 应强制消费独立 review，并检查 reviewer 提出的事实问题是否闭环。

标记方式：
- `INDEPENDENT_REVIEW_CLEAR`
- `INDEPENDENT_REVIEW_DISAGREEMENT_NONTERMINAL`
- `INDEPENDENT_REVIEW_FACT_CONFLICT_RECHECK`
- `INDEPENDENT_REVIEW_HARD_SECURITY_VETO`

不要写“仅当 Codex 同意才可买”。

---

## 6. KOL / builder 参与模式

除纯买币外，继续比较：
- A `Content-first + small stake`
- B `Neutral analyst`
- C `Stakeholder outreach`
- D `Hybrid A+C`

但对外发送、公开发布、合作承诺、allocation / rev-share 协议、账号动作仍是 `OWNER_GATED`，必须 fresh Leo approval。

Leo 自己的发布带来的新增注意力/买盘不得反过来算作 thesis evidence。

---

## 7. Scale / reduce discipline

### Scale

只有新增的非价格证据、执行容量或 forward EV 改善，才能支持加仓，例如：
- catalyst probability materially rises；
- first real mechanism/value-capture event occurs；
- recurring economics improve；
- independent users/holders/market selection strengthen；
- route/depth improves while valuation remains attractive。

价格下跌本身不是加仓理由；价格上涨本身也不是确认理由。

### Reduce / Exit

在以下情况降低或退出：
- thesis-fail probability materially rises；
- kill condition appears；
- hard-security / execution risk worsens；
- success case 已被价格充分透支而概率没提升；
- 更高 EV 的机会显著占优；
- 原始 asymmetry 被消耗。

---

## 8. 人类注意力规则

Leo 应只被打断在：
- 真实资金/签名/账号/公开动作；
- 非机械判断 materially changes EV；
- time-critical high-EV capital decision；
- existing position 的 material risk/action delta。

不得因为 fresh quote、LP readback、route check、普通机制验证、NAV-for-canary 等机器可解决问题而生成“请 Leo 继续指令”。

---

Version: 2.0.0 · personal extension · Action-First
