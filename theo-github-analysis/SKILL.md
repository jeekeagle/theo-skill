---
name: theo-github-analysis
description: |
  GitHub 仓库深度分析工具 - 自动获取仓库信息、AI 深度分析、生成符合 Obsidian Vault 规范的学习笔记。

  何时使用：
  - 发现优质开源项目，想要深度学习时
  - 需要记录和收藏有价值的 GitHub 项目时
  - 想要系统化分析项目架构和设计模式时
  - 需要生成可复用的项目学习笔记时

  触发词：github分析, 仓库分析, /theo-github, 分析GitHub项目

allowed-tools: Read, Write, Edit, Bash, Glob, Grep, WebSearch
mcp_servers: []
---

# Theo Github - GitHub 仓库深度分析工具

## 技能概述

**Theo Github** 是一个专为学习者设计的 GitHub 仓库分析工具。它不仅仅是获取项目信息，而是通过 AI 深度分析项目的**核心价值**、**设计亮点**和**可学习之处**，最终生成一份结构化的学习笔记并自动保存到你的 Obsidian Vault 中。

### 为什么需要这个技能？

- **个人收藏**：系统化记录有价值的项目，方便日后查阅
- **深度学习**：通过分析理解优秀项目的架构和设计
- **知识复用**：提取可复用的模式和最佳实践

## 核心能力

1. **🔍 智能信息收集**
   - 自动获取仓库元数据（星标数、语言、描述）
   - 提取 README 和核心文档
   - 分析项目结构和依赖关系

2. **🧠 AI 深度分析**
   - **What**：项目是什么？技术栈？架构？
   - **Why**：解决了什么问题？有什么独特价值？
   - **How**：如何使用？有哪些设计亮点？

3. **📝 自动生成笔记**
   - 符合 Obsidian Vault 规范的 Markdown 格式
   - 包含 YAML frontmatter（自动分类到 Literature Notes）
   - 结构化内容：基础信息、核心价值、使用方法、学习要点

4. **💾 自动归档**
   - 保存到 `E:\Theo-Obsidian\LiteSeed-OS\01 - Notes\` 目录
   - 自动添加分类标签
   - 文件命名：`{{repo-name}}-github-analysis.md`（符合 Vault 规范，无日期前缀）

## 使用方法

### 基本用法

```
/theo-github https://github.com/owner/repo
```

**示例：**
```
/theo-github https://github.com/vercel/next.js
```

### 高级用法

#### 1. 自定义分析深度

```
/theo-github https://github.com/vercel/next.js --depth=deep
```

**深度选项：**
- `quick`：快速分析（基础信息 + 一句话概括）
- `standard`：标准分析（What + Why + How，默认）
- `deep`：深度分析（+ 代码分析 + 架构图 + 对比）

#### 2. 指定输出位置

默认输出到 `E:\Theo-Obsidian\LiteSeed-OS\01 - Notes\`，如需自定义：

```
/theo-github https://github.com/vercel/next.js --output=/custom/path
```

#### 3. 批量分析

```
/theo-github https://github.com/vercel/next.js https://github.com/facebook/react
```

#### 4. 添加个人想法 💡

```
/theo-github https://github.com/vercel/next.js --notes="这个项目的架构很值得学习，特别是它的路由系统"
```

**或者使用更自然的表达：**

```
分析这个项目 https://github.com/vercel/next.js，我觉得它的服务端渲染做得很好
```

你的想法会自动添加到笔记的"📝 个人笔记"部分！

## 输出格式

生成的笔记包含以下结构：

```markdown
---
categories:
  - "[[Literature Notes]]"
subjects:
  - "[[Productivity]]"  # 根据项目类型自动判断
type: article
status: saved
created: 2025-03-21
---

# [[Repo Name]] - GitHub 仓库分析

## 📊 基础信息（What）

| 字段 | 内容 |
|------|------|
| **仓库地址** | https://github.com/owner/repo |
| **Star 数** | 12.5k |
| **主要语言** | TypeScript |
| **项目类型** | CLI 工具 / Web 应用 / 库 |
| **最后更新** | 2025-03-15 |

**一句话描述：** 用一句话概括这个项目是什么

---

## 🎯 核心价值（Why）
## 🚀 如何使用（How）
## 💡 学习要点
## 🔗 相关资源
## 📝 个人笔记
```

> **注意**: GitHub 仓库的具体信息（URL、星标数、语言等）保存在笔记内容中，而非 YAML frontmatter 中，以符合 Vault 规范。

## 工作流程

```
1. 输入 GitHub URL
   ↓
2. 验证仓库有效性
   ↓
3. 获取仓库元数据（通过 GitHub API）
   ↓
4. AI 深度分析（What + Why + How）
   ↓
5. 生成结构化 Markdown
   ↓
6. 自动保存到 E:\Theo-Obsidian\LiteSeed-OS\01 - Notes\
   ↓
7. 返回笔记路径
```

## 注意事项

- **网络要求**：需要能够访问 GitHub API
- **文件命名**：自动使用日期 + 仓库名，避免冲突
- **分类规则**：自动添加到 `[[Literature Notes]]`，可根据需要调整
- **已有文件**：如果文件已存在，会询问是否覆盖

## 参考资源

- [功能规划文档](github-analyzer-feature-plan.md)
- [Obsidian Vault 规范](../CLAUDE.md)
- [Literature Notes 分类](../02%20-%20Categories/Literature%20Notes.md)
