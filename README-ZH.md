![GitHub stars](https://img.shields.io/github/stars/phuryn/pm-skills)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](https://github.com/phuryn/pm-skills/blob/main/LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](https://github.com/phuryn/pm-skills/blob/main/CONTRIBUTING.md)
[![Companion: pm-skills](https://img.shields.io/badge/companion-pm--brain-blue)](https://github.com/phuryn/pm-brain)
[![English README](https://img.shields.io/badge/README-English-blue?style=flat-square)](README.md)

# PM Skills 市场：更好产品决策的 AI 操作系统

> 68 个 PM 技能与 42 个链式工作流，分布于 9 个插件。支持 Claude Code、Cowork 及更多工具。覆盖从发现、策略、执行、上市、增长到 AI 代码交付的完整流程。

![PM Skills marketplace: skills, commands, and all 9 plugins at a glance](.docs/images/plugins.png)

为 Claude Code 和 Cowork 设计。技能兼容其他 AI 助手。

## 从这里开始

有新想法？→ `/discover`  
需要战略清晰度？→ `/strategy`  
在写 PRD？→ `/write-prd`  
计划上市？→ `/plan-launch`  
定义指标？→ `/north-star`

如果这个项目对你有帮助，请为仓库点 ⭐。

## 为什么选择 PM Skills 市场？

通用 AI 给你文字。PM Skills 市场给你结构。

每个技能都编码了经过验证的 PM 框架——发现、假设映射、优先级排序、战略——并引导你一步一步完成。你能将 Teresa Torres、Marty Cagan 和 Alberto Savoia 的严谨方法融入日常工作流，而不是让它们束之高阁。

结果：更好的产品决策，而不仅仅是更快的文档。

## 工作原理（技能、命令、插件）

![Example prompts: a skill and two commands (/write-prd, /ship-check) in action](.docs/images/examples.png)

**技能**是市场的基本构件。每个技能为 Claude 提供特定 PM 任务所需的领域知识、分析框架或引导式工作流。部分技能还作为多个命令共享的可复用基础。

技能在与对话相关时自动加载——无需显式调用。如需要（例如，优先使用技能而非通用知识），可以使用 `/plugin-name:skill-name` 或 `/skill-name` **强制加载技能**（Claude 会自动添加前缀）。

**命令**是使用 `/command-name` 调用的用户触发工作流。它们将一个或多个技能串联成端到端流程。例如，`/discover` 将四个技能串联在一起：brainstorm-ideas → identify-assumptions → prioritize-assumptions → brainstorm-experiments。

**插件**将相关技能和命令组合成可安装的包。每个插件覆盖一个 PM 领域——发现、策略、执行等。安装整个市场可一次获得全部 9 个插件。

命令使用技能。部分技能服务于多个命令。部分技能（如 `prioritization-frameworks` 或 `opportunity-solution-tree`）是独立参考，Claude 在相关时随时调用——无需命令。

命令设计为相互衔接，与 PM 工作流匹配。任何命令完成后，都会建议相关的后续命令——只需跟随提示即可。

## 安装

### Claude Cowork（推荐非开发者使用）

1. 打开 **自定义**（左下角）
2. 前往 **浏览插件** → **个人** → **+**
3. 选择 **从 GitHub 添加市场**
4. 输入：`phuryn/pm-skills`

全部 9 个插件自动安装。你将获得命令（`/discover`、`/strategy` 等）和技能。

![Installing PM Skills in Claude Cowork](.docs/images/pm-skills-install.gif)

### Claude Code（CLI）

```bash
# 第一步：添加市场
claude plugin marketplace add phuryn/pm-skills

# 第二步：安装各个插件
claude plugin install pm-toolkit@pm-skills
claude plugin install pm-product-strategy@pm-skills
claude plugin install pm-product-discovery@pm-skills 
claude plugin install pm-market-research@pm-skills 
claude plugin install pm-data-analytics@pm-skills
claude plugin install pm-marketing-growth@pm-skills
claude plugin install pm-go-to-market@pm-skills
claude plugin install pm-execution@pm-skills
claude plugin install pm-ai-shipping@pm-skills
```

### Codex CLI（OpenAI）

Codex 读取与 Claude Code 相同的插件市场文件，因此你可以原生安装 PM Skills——无需转换或复制文件：

```bash
# 第一步：添加市场
codex plugin marketplace add phuryn/pm-skills

# 第二步：安装所需插件
codex plugin add pm-toolkit@pm-skills
codex plugin add pm-product-strategy@pm-skills
codex plugin add pm-product-discovery@pm-skills
codex plugin add pm-market-research@pm-skills
codex plugin add pm-data-analytics@pm-skills
codex plugin add pm-marketing-growth@pm-skills
codex plugin add pm-go-to-market@pm-skills
codex plugin add pm-execution@pm-skills
codex plugin add pm-ai-shipping@pm-skills
```

**你将获得：**每个技能（PM 框架），可供 Codex 使用并按名称调用。安装完整插件而非单独挑选技能——一个工作流通常依赖多个一起发布的技能。

**与 Claude Code 的区别：**`/slash` 命令（`/discover`、`/write-prd`……）可以安装，但不能作为 Codex 斜杠命令运行——Codex 插件不暴露命令。要运行工作流，只需用自然语言描述步骤，例如：

> 对*[你的想法]*进行产品发现：头脑风暴选项，映射假设，优先考虑风险较高的假设，然后设计实验——每步之间暂停。

**可选——让 Codex 将工作流转为技能。**由于命令文件随每个已安装插件一起发布，你可以要求 Codex 转换你最常用的那些：

> 读取 pm-execution 插件中的命令文件，为我最常使用的工作流创建等效的 Codex 技能。

这是一种尽力而为的、由模型驱动的转换（某些 Claude 特有的命令语法无法转换），但这是在不离开 CLI 的情况下获得 Codex 引导式工作流的快捷方式。

### 其他 AI 助手（仅技能）

`skills/*/SKILL.md` 文件遵循通用技能格式，适用于任何能读取它的工具。命令（`/slash-commands`）是 Claude 特有的。

| 工具 | 使用方式 | 有效内容 |
|------|-----------|------------|
| **Gemini CLI** | 将技能文件夹复制到 `.gemini/skills/` | 仅技能 |
| **OpenCode** | 将技能文件夹复制到 `.opencode/skills/` | 仅技能 |
| **Cursor** | 将技能文件夹复制到 `.cursor/skills/` | 仅技能 |
| **Kiro** | 将技能文件夹复制到 `.kiro/skills/` | 仅技能 |

```bash
# 示例：复制所有技能到 OpenCode（项目级别）
for plugin in pm-*/; do
  mkdir -p .opencode/skills/
  cp -r "$plugin/skills/"* .opencode/skills/ 2>/dev/null
done

# 示例：复制所有技能到 Gemini CLI（全局）
for plugin in pm-*/; do
  cp -r "$plugin/skills/"* ~/.gemini/skills/ 2>/dev/null
done
```

---

## 可用插件

<details>
<summary><strong>1. pm-product-discovery</strong> — 创意构思、实验、假设测试、机会树、访谈（13 个技能，5 个命令）</summary>

**技能（13 个）：**

- `brainstorm-ideas-existing` — 现有产品的多视角创意构思（PM、设计师、工程师）
- `brainstorm-ideas-new` — 初始发现阶段新产品的创意构思
- `brainstorm-experiments-existing` — 为现有产品设计假设测试实验
- `brainstorm-experiments-new` — 为新产品设计精益创业预型（Alberto Savoia）
- `identify-assumptions-existing` — 识别价值、可用性、可行性和技术可行性层面的风险假设
- `identify-assumptions-new` — 识别包括上市、战略和团队在内的 8 个风险类别的假设
- `prioritize-assumptions` — 使用影响 × 风险矩阵并附带实验建议对假设进行优先级排序
- `prioritize-features` — 基于影响、工作量、风险和战略一致性对功能待办列表进行优先级排序
- `analyze-feature-requests` — 按主题和战略契合度分析和分类客户功能请求
- `opportunity-solution-tree` — 构建机会解决方案树（Teresa Torres）——结果 → 机会 → 解决方案 → 实验
- `interview-script` — 创建包含 JTBD 探索性问题的结构化客户访谈脚本
- `summarize-interview` — 将访谈记录总结为 JTBD、满意度信号和行动事项
- `metrics-dashboard` — 设计包含北极星指标、输入指标和预警阈值的产品指标仪表板

**命令（5 个）：**

- `/discover` — 完整发现周期：创意构思 → 假设映射 → 优先级排序 → 实验设计
- `/brainstorm` — 多视角创意构思（`ideas|experiments` × `existing|new`）
- `/triage-requests` — 分析和优先处理一批功能请求
- `/interview` — 准备访谈脚本或总结记录（`prep|summarize`）
- `/setup-metrics` — 设计产品指标仪表板

**示例：**

技能：
- `我们 AI 写作助手想法中最有风险的假设是什么？`
- `帮我为提升用户激活率构建机会解决方案树`
- `优先处理这 12 条来自企业客户的功能请求 [附 CSV]`

命令：
- `/discover 面向远程团队的 AI 会议摘要工具`
- `/brainstorm experiments existing — 我们需要降低入职流程的流失率`
- `/interview prep — 我们正在访谈企业买家了解他们的采购流程`

</details>

<details>
<summary><strong>2. pm-product-strategy</strong> — 愿景、商业模式、定价、竞争格局（12 个技能，5 个命令）</summary>

产品战略、愿景、商业模式、定价和宏观环境分析。涵盖从愿景制定到竞争格局扫描的完整战略工具集。

**技能（12 个）：**

- `product-strategy` — 全面的 9 节产品战略画布（愿景 → 可防御性）
- `startup-canvas` — 结合产品战略（9 节）+ 商业模式的创业画布——新产品的 BMC 和精益画布替代方案
- `product-vision` — 打造鼓舞人心、切实可行且富有情感的产品愿景
- `value-proposition` — 6 部分 JTBD 价值主张（目标用户、动机、之前状态、如何实现、之后状态、替代方案）
- `lean-canvas` — 面向初创企业和新产品的精益画布商业模式
- `business-model` — 包含全部 9 个构建模块的商业模式画布
- `monetization-strategy` — 头脑风暴 3–5 种货币化策略并附带验证实验
- `pricing-strategy` — 定价模型、竞争分析、支付意愿和价格弹性
- `swot-analysis` — 包含可行建议的 SWOT 分析
- `pestle-analysis` — 宏观环境：政治、经济、社会、技术、法律、环境
- `porters-five-forces` — 竞争力量分析（竞争对手、供应商、买家、替代品、新进入者）
- `ansoff-matrix` — 跨市场和产品的增长战略映射

**命令（5 个）：**

- `/strategy` — 创建完整的 9 节产品战略画布
- `/business-model` — 探索商业模式（`lean|full|startup|value-prop|all`）
- `/value-proposition` — 使用 6 部分 JTBD 模板设计价值主张
- `/market-scan` — 结合 SWOT + PESTLE + 波特五力 + 安索夫的宏观环境分析
- `/pricing` — 设计包含竞争分析和实验的定价策略

**示例：**

技能：
- `比较精益画布、商业模式画布和创业画布对我的市场创业公司的适用性`
- `为我们面向非母语英语使用者的 AI 写作助手设计价值主张`
- `对项目管理 SaaS 市场进行波特五力分析`

命令：
- `/strategy 面向代理机构的 B2B 项目管理工具`
- `/business-model startup — 面向非母语英语使用者的 AI 写作工具`
- `/value-proposition 面向企业客户的 SaaS 入职工具`

</details>

<details>
<summary><strong>3. pm-execution</strong> — PRD、OKR、路线图、冲刺、回顾、发布说明、利益相关者管理（16 个技能，11 个命令）</summary>

日常产品管理：PRD、OKR、路线图、冲刺、回顾、发布说明、预演、利益相关者管理、用户故事和优先级框架。

**技能（16 个）：**

- `create-prd` — 全面的 8 节 PRD 模板
- `brainstorm-okrs` — 与公司目标对齐的团队级 OKR
- `outcome-roadmap` — 将功能列表转化为以结果为导向的路线图
- `sprint-plan` — 包含容量估算、故事选择和风险识别的冲刺计划
- `retro` — 结构化冲刺回顾引导
- `release-notes` — 从工单、PRD 或变更日志生成面向用户的发布说明
- `pre-mortem` — 使用虎、纸老虎、大象分类法进行风险分析
- `stakeholder-map` — 权力 × 利益矩阵，附带定制沟通计划
- `summarize-meeting` — 会议记录 → 决策 + 行动事项
- `user-stories` — 遵循 3C 和 INVEST 标准的用户故事
- `job-stories` — 工作故事：当[情境]时，我想要[动机]，这样我就能[结果]
- `wwas` — Why-What-Acceptance 格式的产品待办事项
- `test-scenarios` — 测试场景：正常路径、边界情况、错误处理
- `dummy-dataset` — CSV、JSON、SQL 或 Python 格式的逼真虚拟数据集
- `prioritization-frameworks` — 9 种优先级框架参考指南（机会评分、ICE、RICE、MoSCoW、Kano 等）
- `strategy-red-team` — 对计划进行对抗性压力测试：找出关键假设，指出每个假设的失败条件，并按最低成本测试排序

**命令（11 个）：**

- `/write-prd` — 从功能想法或问题陈述创建 PRD
- `/plan-okrs` — 头脑风暴团队级 OKR
- `/transform-roadmap` — 将基于功能的路线图转换为以结果为导向的路线图
- `/sprint` — 冲刺生命周期（`plan|retro|release`）
- `/pre-mortem` — 对 PRD 或上市计划进行预演风险分析
- `/red-team-prd` — 对 PRD、路线图或战略进行对抗性压力测试，按最低成本测试排列最高风险假设
- `/meeting-notes` — 将会议记录整理成结构化笔记
- `/stakeholder-map` — 绘制利益相关者地图并制定沟通计划
- `/write-stories` — 将功能拆解为待办事项（`user|job|wwa`）
- `/test-scenarios` — 从用户故事生成测试场景
- `/generate-data` — 创建逼真的虚拟数据集

**示例：**

技能：
- `我应该使用哪种优先级框架来处理 50 个待办事项的积压？`
- `为平台迁移项目绘制利益相关者地图`
- `机会评分、ICE 和 RICE 有什么区别？`

命令：
- `/write-prd 减少告警疲劳的智能通知系统`
- `/sprint retro — 这是我们上次冲刺的笔记`
- `/write-stories job — 将"团队仪表板"功能拆解为工作故事`

</details>

<details>
<summary><strong>4. pm-market-research</strong> — 用户画像、细分、旅程地图、市场规模、竞品分析（7 个技能，3 个命令）</summary>

用户研究和竞品分析：用户画像、细分、旅程地图、市场规模、竞品分析和反馈分析。

**技能（7 个）：**

- `user-personas` — 从研究数据创建精细化用户画像
- `market-segments` — 识别 3–5 个客户细分，包含人口统计、JTBD 和产品契合度
- `user-segmentation` — 基于行为、JTBD 和需求从反馈数据对用户进行细分
- `customer-journey-map` — 包含阶段、触点、情绪和痛点的端到端旅程地图
- `market-sizing` — TAM、SAM、SOM，采用自上而下和自下而上两种方法
- `competitor-analysis` — 竞争对手优势、劣势和差异化机会
- `sentiment-analysis` — 用户反馈的情感分析和主题提取

**命令（3 个）：**

- `/research-users` — 构建用户画像、细分用户并绘制客户旅程
- `/competitive-analysis` — 分析竞争格局
- `/analyze-feedback` — 用户反馈的情感分析和细分洞察

**示例：**

技能：
- `估算 AI 代码审查工具在美国市场的 TAM/SAM/SOM`
- `为我们的电商结账流程创建客户旅程地图`
- `按行为和需求对这些调查受访者进行细分 [附 CSV]`

命令：
- `/research-users 我们有来自健身应用 12 位用户的访谈数据`
- `/competitive-analysis 设计工具领域的 Figma 竞争对手`
- `/analyze-feedback 这是 Q4 的 200 条 NPS 回复 [附文件]`

</details>

<details>
<summary><strong>5. pm-data-analytics</strong> — SQL 生成、队列分析、A/B 测试分析（3 个技能，3 个命令）</summary>

面向 PM 的数据分析：SQL 查询生成、队列分析和 A/B 测试分析。

**技能（3 个）：**

- `sql-queries` — 从自然语言生成 SQL（BigQuery、PostgreSQL、MySQL）
- `cohort-analysis` — 按队列划分的留存曲线、功能采用率和参与度趋势
- `ab-test-analysis` — 统计显著性、样本量验证以及发布/延续/停止建议

**命令（3 个）：**

- `/write-query` — 从自然语言生成 SQL 查询
- `/analyze-cohorts` — 对用户参与数据进行队列分析
- `/analyze-test` — 分析 A/B 测试结果

**示例：**

技能：
- `对于 2% MDE，95% 置信度需要多大的样本量？`
- `订阅应用应该跟踪哪些留存指标？`

命令：
- `/write-query 显示 Q4 2025 按国家分类的月活跃用户（BigQuery）`
- `/analyze-test 这是我们结账流程 A/B 测试的结果 [附 CSV]`
- `/analyze-cohorts 一月和二月注册用户的周留存对比`

</details>

<details>
<summary><strong>6. pm-go-to-market</strong> — 滩头细分市场、ICP、信息传递、增长飞轮、GTM 动作、竞争卡片（6 个技能，3 个命令）</summary>

上市战略：滩头细分市场、理想客户画像、信息传递、增长飞轮、GTM 动作和竞争卡片。

**技能（6 个）：**

- `gtm-strategy` — 完整 GTM 战略：渠道、信息传递、成功指标和上市计划
- `beachhead-segment` — 识别首个滩头市场细分
- `ideal-customer-profile` — 包含人口统计、行为、JTBD 和需求的 ICP
- `growth-loops` — 设计可持续的增长飞轮
- `gtm-motions` — 评估 GTM 动作和工具（产品主导、销售主导等）
- `competitive-battlecard` — 包含异议处理和赢单策略的销售就绪竞争卡片

**命令（3 个）：**

- `/plan-launch` — 从滩头市场到上市计划的完整 GTM 战略
- `/growth-strategy` — 设计增长飞轮并评估 GTM 动作
- `/battlecard` — 创建竞争卡片

**示例：**

技能：
- `开发者生产力工具的最佳滩头细分市场是什么？`
- `为拥有免费增值层的 B2B SaaS 设计增长飞轮`
- `为 AI 驱动的 HR 筛选平台定义我们的 ICP`

命令：
- `/plan-launch 面向中型工程团队的 AI 代码审查工具`
- `/battlecard 我们的 CRM 对比 Salesforce（SMB 市场）`
- `/growth-strategy 连接自由职业者与初创企业的双边市场`

</details>

<details>
<summary><strong>7. pm-marketing-growth</strong> — 营销创意、定位、价值主张、产品命名、北极星指标（5 个技能，2 个命令）</summary>

产品营销与增长：营销创意、定位、价值主张表述、产品命名和北极星指标。

**技能（5 个）：**

- `marketing-ideas` — 具有渠道和信息传递的创意且具成本效益的营销想法
- `positioning-ideas` — 与竞争对手差异化的产品定位
- `value-prop-statements` — 用于营销、销售和入职的价值主张表述
- `product-name` — 与品牌价值观和受众契合的产品命名头脑风暴
- `north-star-metric` — 北极星指标 + 附带业务模式分类的输入指标

**命令（2 个）：**

- `/market-product` — 头脑风暴营销创意、定位、价值主张和产品名称
- `/north-star` — 定义你的北极星指标和支持性输入指标

**示例：**

技能：
- `头脑风暴 5 个与 Notion 差异化的定位角度`
- `双边市场的北极星指标应该是什么？`
- `为我们销售团队的演示文稿生成价值主张表述`

命令：
- `/market-product 面向电商经理的 B2B 分析仪表板`
- `/north-star 连接自由职业者与客户的双边市场`

</details>

<details>
<summary><strong>8. pm-toolkit</strong> — 简历审查、法律文件、校对（4 个技能，5 个命令）</summary>

核心产品工作之外的 PM 实用工具：简历审查、法律文件和校对。

**技能（4 个）：**

- `review-resume` — PM 简历审查和针对 10 个最佳实践的优化（XYZ+S 公式、关键词、结构）
- `draft-nda` — 包含司法管辖区适当条款的保密协议
- `privacy-policy` — 涵盖 GDPR/CCPA 合规的隐私政策
- `grammar-check` — 语法、逻辑和流畅性检查，附带针对性修改

**命令（5 个）：**

- `/review-resume` — 全面的 PM 简历审查
- `/tailor-resume` — 针对特定职位描述定制简历
- `/draft-nda` — 起草保密协议
- `/privacy-policy` — 起草隐私政策
- `/proofread` — 检查语法、逻辑和流畅性

**示例：**

技能：
- `按最佳实践审查我的 PM 简历 [附 PDF]`
- `检查这份产品公告的语法和清晰度`

命令：
- `/review-resume [附上你的 PM 简历]`
- `/tailor-resume [附简历 + 粘贴职位描述]`
- `/proofread 这是我们 Q1 投资者更新的草稿`

</details>

<details>
<summary><strong>9. pm-ai-shipping</strong> — AI 交付套件：记录 vibe-coded 应用、审计安全与性能、梳理测试覆盖率、编译交付包（2 个技能，5 个命令）</summary>

面向负责 AI 编写代码的 PM 和创始人。AI 代理写代码速度很快，但不留下*意图*记录——系统应该做什么、谁可以做什么、密钥存在哪里、哪些规则实际经过验证。这个套件恢复了可审查性：它记录系统，然后审计文档所说内容与代码实际行为之间的差距——这类漏洞是通用扫描器会遗漏的。

**技能（2 个）：**

- `shipping-artifacts` — 使 AI 构建的应用可审查的持久文档集：每个应用都需要的核心（架构、用户/权限流程、权限、变量/密钥、测试覆盖率图谱）以及仅在适用时添加的条件文档（电子邮件、定时任务、SEO、嵌入式代理/自动化）。定义每个文档必须捕获的内容以及审查者如何使用它
- `intended-vs-implemented` — 找出系统文档说明与代码实际行为之间差距的方法，双方均附有引用证据

**命令（5 个）：**

- `/ship-check` — 将 vibe-coded 仓库转化为审查就绪的交付包：记录、关联代理上下文、运行安全和性能审计、梳理测试覆盖率并汇总结果
- `/document-app` — 将代码库逆向工程为审查者和审计者所需的系统文档——核心文档集（架构、流程、权限、变量）加上适用时的条件文档（电子邮件、定时任务、SEO、自动化）
- `/derive-tests` — 将文档化意图转化为测试覆盖率图谱：盘点当前已有测试，将其与建议测试和未验证缺口分开，并推荐合并前绿色 CI 门槛
- `/security-audit-static` — 静态安全审计：绘制信任边界、交叉参照文档意图、自我反驳每项发现，仅报告有证据支持的风险
- `/performance-audit-static` — 静态性能审计：找出过度获取、缺失索引和缓存机会，按工作量和影响排序

**示例：**

技能：
- `在有人审查之前，我的 Supabase 应用需要哪些文档？`
- `这段代码的实际行为与文档说明应该做的事情在哪里出现了偏差？`

命令：
- `/ship-check 支付服务`
- `/document-app — 逆向工程此仓库的系统文档`
- `/derive-tests — 哪些已记录的规则还没有测试？`
- `/security-audit-static src/api`

</details>

---

## 关于

这个市场随着产品实践和 AI 能力的发展而演进。

部分技能基于以下人员的工作成果：

- Teresa Torres — [*Continuous Discovery Habits*](https://www.amazon.com/Continuous-Discovery-Habits-Discover-Products/dp/1736633309/)
- Marty Cagan — [*INSPIRED*](https://www.amazon.com/INSPIRED-Create-Tech-Products-Customers/dp/1119387507/) 和 [*TRANSFORMED*](https://www.amazon.com/dp/1119697336/)
- Alberto Savoia — [*The Right It*](https://www.amazon.com/Right-Many-Ideas-Yours-Succeed/dp/0062884654)
- Dan Olsen — [*The Lean Product Playbook*](https://www.amazon.com/dp/1118960874/)
- Roger L. Martin — [*Playing to Win*](https://www.amazon.com/Playing-Win-Expanded-Bonus-Articles/dp/B0F25SDYWV/)
- Ash Maurya — [*Running Lean*](https://www.amazon.com/dp/B004J4XGN6/)
- Strategyzer — [*Business Model Generation*](https://www.amazon.com/dp/0470876417/) 和 [*Value Proposition Design*](https://www.amazon.com/dp/1118968050/)
- Christina Wodtke — [*Radical Focus*](https://www.amazon.com/Radical-Focus-Achieving-Important-Objectives/dp/0996006052)
- Anthony W. Ulwick — [*Jobs to Be Done*](https://jobs-to-be-done-book.com/)
- Alistair Croll & Benjamin Yoskovitz — [*Lean Analytics*](https://www.amazon.com/Lean-Analytics-Better-Startup-Faster/dp/1449335675/)
- Sean Ellis — [*Hacking Growth*](https://www.amazon.com/Hacking-Growth-Fastest-Growing-Companies-Breakout/dp/045149721X/)
- Maja Voje — [*Go-To-Market Strategist*](https://gtmstrategist.com/)

由 Paweł Huryn 策划，来自 [The Product Compass Newsletter](https://www.productcompass.pm)。

## 与 PM Brain 组合使用

![PM Brain composes with PM Skills](.docs/images/pm-brain-pm-skills.webp)

[PM Brain](https://github.com/phuryn/pm-brain) 是产品经理的第二大脑。纯 Markdown 文件，存放在你笔记本电脑的一个文件夹里。Claude 在回答前读取它们，回答后写入它们，每周五进行整理。无需向量数据库，无需云存储，无需代理记忆技巧。

## 贡献

参见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## Windows 已知问题

如果你的 Cowork 不稳定且无法启动 VM（[claude-code/issues/27010](https://github.com/anthropics/claude-code/issues/27010)），请尝试：

```powershell
$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-WindowStyle Hidden -Command `"if ((Get-Service CoworkVMService).Status -ne 'Running') { Start-Service CoworkVMService }`""

$trigger = New-ScheduledTaskTrigger -RepetitionInterval (New-TimeSpan -Minutes 1) -Once -At (Get-Date)

$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries

Register-ScheduledTask -TaskName "CoworkVMServiceMonitor" `
  -Action $action `
  -Trigger $trigger `
  -Settings $settings `
  -RunLevel Highest `
  -User "SYSTEM"
```

这能解决 Windows 上 90% 的问题。  
剩余 10%：打开 services.msc > 手动启动"Claude"服务

## 许可证

MIT — 参见 [LICENSE](LICENSE)。
