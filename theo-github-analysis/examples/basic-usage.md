# Theo Github 使用示例

## 示例 1：基本用法 - 分析单个仓库

### 命令
```
/theo-github https://github.com/vercel/next.js
```

### 预期结果
```
✅ 分析完成！
📄 笔记已保存到: 01 - Notes/nextjs-github-analysis.md
🔗 GitHub 仓库: https://github.com/vercel/next.js
```

### 生成的笔记结构
```markdown
---
categories:
  - "[[Literature Notes]]"
subjects:
  - "[[Productivity]]"
type: article
status: saved
created: 2025-03-21
---

# [[Next.js]] - GitHub 仓库分析

## 📊 基础信息（What）
## 🎯 核心价值（Why）
## 🚀 如何使用（How）
...
```

---

## 示例 2：快速分析 - 只获取基础信息

### 命令
```
/theo-github https://github.com/facebook/react --depth=quick
```

### 预期结果
- 快速生成基础信息卡片
- 包含星标数、语言、描述
- 不包含深度分析内容

---

## 示例 3：深度分析 - 完整的代码审查

### 命令
```
/theo-github https://github.com/microsoft/vscode --depth=deep
```

### 预期结果
- 完整的项目架构分析
- 代码设计模式提取
- 性能优化技巧总结
- 可复用的代码模式

---

## 示例 4：自定义输出位置

### 命令
```
/theo-github https://github.com/github/copilot --output-dir="Custom/Path"
```

### 预期结果
```
✅ 分析完成！
📄 笔记已保存到: Custom/Path/2025-03-21-copilot-github-analysis.md
```

---

## 示例 4：添加个人想法 💡

### 命令
```
/theo-github https://github.com/vercel/next.js --notes="这个项目的路由系统设计非常优雅，值得深入学习"
```

### 预期结果
```
✅ 分析完成！
📄 笔记已保存到: 01 - Notes/nextjs-github-analysis.md
💭 你的想法已添加到"个人笔记"部分
```

### 生成的笔记中会包含

```markdown
## 📝 个人笔记

> 这里可以添加你自己的理解和备注

这个项目的路由系统设计非常优雅，值得深入学习

---
```

### 自然语言方式

你也可以用更自然的方式表达：

```
分析 https://github.com/vercel/next.js，我觉得它的服务端渲染做得很好
```

系统会自动提取你的想法并添加到笔记中！

---

## 示例 5：批量分析多个仓库

### 命令
```
/theo-github https://github.com/vercel/next.js https://github.com/facebook/react
```

### 预期结果
```
✅ 分析完成！
📄 已生成 2 份笔记：
   - 2025-03-21-nextjs-github-analysis.md
   - 2025-03-21-react-github-analysis.md
```

---

## 示例 6：错误处理 - 无效的 URL

### 命令
```
/theo-github https://invalid-url.com/repo
```

### 预期结果
```
❌ 错误: 无效的 GitHub URL: https://invalid-url.com/repo
```

---

## 示例 7：实际使用场景

### 场景 1：发现优质项目，想要收藏学习

```
你在浏览 GitHub 时发现了一个优质项目，想要深度学习：

/theo-github https://github.com/microsoft/playwright
```

### 场景 2：技术选型前的调研

```
需要对比几个框架，生成分析报告：

/theo-github https://github.com/vercel/next.js --depth=deep
/theo-github https://github.com/remix-run/remix --depth=deep
/theo-github https://github.com/nuxt/nuxt --depth=deep
```

### 场景 3：系统化学习开源项目

```
每天分析一个优质项目，建立知识库：

/theo-github https://github.com/tailwindlabs/tailwindcss
/theo-github https://github.com/prisma/prisma
/theo-github https://github.com/pnpm/pnpm
```

---

## 示例 8：与 Obsidian 集成

### 在 Obsidian 中查看生成的笔记

1. 打开 Obsidian Vault
2. 导航到 `01 - Notes/`
3. 找到生成的分析笔记
4. 通过 `[[Literature Notes]]` 分类自动聚合

### 使用 Obsidian Bases 查看所有 GitHub 分析

在 `02 - Categories/Literature Notes.md` 中会自动显示所有通过这个 skill 生成的笔记，因为它们都有 `type: code-review` 属性。

---

## 示例 9：结合其他技能使用

### 与 theo-paper 结合 - 分析论文项目

```
# 先分析论文的 GitHub 仓库
/theo-github https://github.com/facebookresearch/detr

# 然后阅读论文
/theo-paper https://arxiv.org/abs/2005.12872
```

### 与 todo 结合 - 创建学习任务

```
# 分析项目
/theo-github https://github.com/vercel/next.js

# 创建学习任务
/todo 深入学习 Next.js 源码
```
