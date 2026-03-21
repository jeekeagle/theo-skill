---
name: theo-translate
description: |
  分析后翻译文章和文档。支持自定义术语表、分块处理长文、子代理并行翻译。

  何时使用：用户请求"翻译"、"translate"、"翻译一下"、"改成中文/英文"、"localize"、"本地化"，或提供 URL/文件并表达翻译意图。

  触发词：翻译, translate, 翻译一下, 改成中文, 改成英文, convert to Chinese, localize, 本地化
allowed-tools: Read, Write, Edit, Bash, Agent
mcp_servers: []
---

# Theo Translate

分析后翻译技能：先分析内容，再进行翻译。支持术语表、分块处理、子代理并行。

## 配置 (EXTEND.md)

检查 EXTEND.md（优先级顺序）：

```bash
# macOS, Linux, WSL, Git Bash
test -f .theo-skills/theo-translate/EXTEND.md && echo "project"
test -f "$HOME/.theo-skills/theo-translate/EXTEND.md" && echo "user"
```

| 路径 | 位置 |
|------|------|
| `.theo-skills/theo-translate/EXTEND.md` | 项目目录 |
| `$HOME/.theo-skills/theo-translate/EXTEND.md` | 用户目录 |

| 结果 | 操作 |
|------|------|
| 找到 | 读取、解析、应用设置。首次使用时提示："使用 [path] 的偏好设置。可编辑 EXTEND.md 自定义术语表等。" |
| 未找到 | **必须**运行首次设置（见下文）—— **不要**静默使用默认值 |

**EXTEND.md 支持**：默认目标语言 | 目标读者 | 自定义术语表 | 翻译风格 | 分块设置

Schema: [references/config/extend-schema.md](references/config/extend-schema.md)

### 首次设置（阻塞）

**关键**：当 EXTEND.md 未找到时，**必须**在翻译前运行首次设置。这是**阻塞**操作。

使用 `AskUserQuestion` 一次性询问所有问题（目标语言、读者、风格、保存位置）。用户回答后，在选定位置创建 EXTEND.md，确认"偏好设置已保存到 [path]"，然后继续。

## 默认值

所有可配置值汇总。EXTEND.md 覆盖默认值；CLI 参数覆盖 EXTEND.md。

| 设置 | 默认值 | EXTEND.md 键 | CLI 参数 | 说明 |
|------|--------|--------------|----------|------|
| 目标语言 | `zh-CN` | `target_language` | `--to` | 翻译目标语言 |
| 目标读者 | `general` | `audience` | `--audience` | 目标读者画像 |
| 翻译风格 | `storytelling` | `style` | `--style` | 翻译风格偏好 |
| 分块阈值 | `4000` | `chunk_threshold` | — | 触发分块翻译的字数 |
| 分块最大字数 | `5000` | `chunk_max_words` | — | 每块最大字数 |

## 用法

```
/theo-translate [--from <lang>] [--to <lang>] [--audience <audience>] [--style <style>] [--glossary <file>] <source>
```

- `<source>`: 文件路径、URL 或内联文本
- `--from`: 源语言（省略则自动检测）
- `--to`: 目标语言（从 EXTEND.md 或默认 `zh-CN`）
- `--audience`: 目标读者画像（从 EXTEND.md 或默认 `general`）
- `--style`: 翻译风格（从 EXTEND.md 或默认 `storytelling`）
- `--glossary`: 额外术语表文件，与 EXTEND.md 术语表合并

**读者画像**：

| 值 | 说明 |
|----|------|
| `general` | 普通读者（默认），通俗易懂，术语加更多注释 |
| `technical` | 开发者/工程师，技术术语少注释 |
| `academic` | 研究者/学者，正式语体，术语精确 |
| `business` | 商务人士，商务友好语调，解释技术概念 |

也接受自定义描述，如 `--audience "对 AI 感兴趣的普通读者"`。

**风格预设**：

| 值 | 说明 |
|----|------|
| `storytelling` | 叙事流畅（默认），引人入胜，过渡自然，用词生动 |
| `formal` | 专业、结构化，中性语调，清晰组织，无口语化 |
| `technical` | 精确、文档风格，简洁，术语密集，最小修饰 |
| `literal` | 贴近原文结构，最小重构，保留源句式 |
| `academic` | 学术、严谨，正式语域，复杂从句可接受，引用感知 |
| `business` | 简洁、结果导向，行动导向，高管友好，要点思维 |
| `conversational` | 口语化、亲切，友好，像在给朋友解释 |

也接受自定义风格描述，如 `--style "诗意和抒情"`。

## 工作流

### 步骤 1：加载偏好

1.1 检查 EXTEND.md（见配置部分）

1.2 加载语言对的内置术语表（如可用）：
- EN→ZH: [references/glossary-en-zh.md](references/glossary-en-zh.md)

1.3 合并术语表：EXTEND.md 术语表 + 内置术语表 + `--glossary` 文件（CLI 优先级最高）

### 步骤 2：物化源文件 & 创建输出目录

物化源文件（文件原样使用，内联文本/URL → 保存到 `translate/{slug}.md`），然后创建输出目录：`{source-dir}/{source-basename}-{target-lang}/`。如未指定 `--from` 则检测源语言。

完整细节：[references/workflow-mechanics.md](references/workflow-mechanics.md)

**输出目录内容**（所有中间和最终文件）：

| 文件 | 说明 |
|------|------|
| `translation.md` | 最终翻译（固定名称） |
| `01-analysis.md` | 内容分析（领域、语调、术语） |
| `02-prompt.md` | 组装的翻译提示 |
| `chunks/` | 分块文件（如需要） |

### 步骤 3：评估内容长度

翻译前估算字数。如内容超过分块阈值（默认 4000 字）：

| 内容 | 操作 |
|------|------|
| < 阈值 | 作为单一单元翻译 |
| >= 阈值 | 分块翻译（见步骤 3.1） |

**3.1 长文准备**（>= 分块阈值）

翻译分块前：

1. **提取术语**：扫描整个文档，找出专有名词、技术术语、重复短语
2. **构建会话术语表**：合并提取的术语与已加载的术语表，建立一致翻译
3. **拆分为块**：按 Markdown AST 块边界拆分，保留结构
4. **组装翻译提示**：
   - 主代理读取 `01-analysis.md` 并组装共享上下文
   - 保存为 `02-prompt.md`（仅共享上下文，无任务指令）
5. **通过子代理翻译草稿**（如 Agent 工具可用）：
   - 每块生成一个子代理，全部并行执行
   - 每个子代理读取 `02-prompt.md` 获取共享上下文，翻译其块，保存到 `chunks/chunk-NN-draft.md`
   - 术语一致性由共享的 `02-prompt.md` 保证
   - 如无分块（内容低于阈值）：为整个源文件生成一个子代理
   - 如 Agent 工具不可用：使用 `02-prompt.md` 顺序内联翻译各块
6. **合并**：所有子代理完成后，按顺序合并翻译块。如存在 `chunks/frontmatter.md`，前置它。保存为 `translation.md`
7. 所有中间文件（源块 + 翻译块）保存在 `chunks/`

### 步骤 4：翻译

**翻译原则**（核心）：

- **准确优先**：事实、数据、逻辑必须完全匹配原文
- **意译优于直译**：翻译作者的意图，而非字面意思。当直译听起来不自然或无法传达预期效果时，自由重构以用地道的目标语言表达相同含义
- **比喻语言**：按意图解读隐喻、习语和比喻表达，而非逐字翻译。当源语言意象在目标语言中不传达相同含义时，用自然表达替换
- **情感保真**：保留用词的情感内涵，而非仅字典意义。带有主观感受的词应唤起目标语言读者的相同反应
- **自然流畅**：使用地道的目标语言语序和句式；当源结构在目标语言中不自然时，自由断句或重构
- **术语**：使用标准翻译；首次出现时在括号中注释原文
- **保留格式**：保持所有 Markdown 格式（标题、粗体、斜体、图片、链接、代码块）
- **尊重原文**：保持原意和意图；不添加、删除或评论——但可自由调整句子结构和意象以服务于含义
- **译者注释**：对于目标读者可能不理解的术语、概念或文化引用——由于行话、文化差距或领域知识——在术语后立即添加简明解释性括号注释。注释应解释*它是什么*，而非仅提供英文原文。格式：`译文（English original，通俗解释）`。根据目标读者调整注释深度：普通读者比技术读者需要更多注释。仅在真正需要时添加注释；不要过度注释明显术语

**工作流步骤**：

1. **分析** → `01-analysis.md`（领域、语调、读者、术语、读者理解难点、比喻语言和隐喻映射）
2. **组装提示** → `02-prompt.md`（翻译指令和内联上下文）
3. **翻译**（遵循 `02-prompt.md`）→ `translation.md`

### 步骤 5：输出

最终翻译始终位于输出目录的 `translation.md`。

显示摘要：
```
**翻译完成**

源文件: {source-path}
语言: {from} → {to}
输出目录: {output-dir}/
最终文件: {output-dir}/translation.md
术语应用: {count} 个
```

## 扩展支持

通过 EXTEND.md 自定义配置。见**配置**部分了解路径和支持的选项。
