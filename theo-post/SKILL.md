# Theo 博客文章发布工具

将文章发布到 Theo 博客（AstroPaper 主题）的交互式工具。处理图片、格式化内容、同步到 GitHub。

## 触发条件

- 用户说"发布文章"、"写博客"、"新建博文"、"发布到博客"
- 用户提供文章内容并想要发布
- 用户想要翻译/整理内容并发布

## 项目配置

```bash
PROJECT_PATH=E:/Theo/theo
GIT_REPO=https://github.com/jeekeagle/theo
GIT_BRANCH=main
IMAGE_DIR=src/assets/images
BLOG_DIR=src/data/blog
```

## 工作流程（6步）

### 1. 接收文章内容

询问用户提供文章内容：
- 直接粘贴文本
- 提供网页链接（抓取并整理）
- 提供文件路径

### 2. 处理图片（如有）

**如果文章包含图片**，执行以下步骤：

1. **询问图片位置**
   - 用户提供图片路径
   - 需要生成图片

2. **复制图片到项目**
   ```bash
   # 源路径（用户提供）
   SOURCE=E:/Theo/X-Writing/images/*.jpg

   # 目标路径
   TARGET={PROJECT_PATH}/src/assets/images/{slug}/
   ```

3. **在 Markdown 中引用**（⚠️ 关键）
   ```markdown
   ![封面](../../assets/images/{slug}/cover.jpg)
   ```

**正确方式** ✅：
```markdown
![封面](../../assets/images/my-article/cover.jpg)
```

**错误方式** ❌：
```markdown
import { Image } from "astro:assets";
<Image src={...} />
```
→ 这会导致代码被当作纯文本显示

### 3. 确认文章元信息

逐步确认以下 frontmatter：

| 字段 | 必填 | 说明 |
|------|------|------|
| `title` | ✅ | 文章标题 |
| `description` | ✅ | 文章描述 |
| `pubDatetime` | ✅ | **必须使用过去的时间**（见注意事项） |
| `slug` | ❌ | URL路径（从标题生成） |
| `tags` | ❌ | 标签（从内容推断） |
| `featured` | ❌ | 特色文章（默认 false） |
| `canonicalURL` | ❌ | 翻译文章必填（原文链接） |

### 4. 格式化文章内容

1. 标题层级：从 h2 开始（不使用 h1）
2. 添加目录：`## Table of contents`
3. 代码块：指定语言
4. 图片路径：使用标准 Markdown 语法

### 5. 保存文章

1. 生成文件：`{PROJECT_PATH}/src/data/blog/{slug}.md`
2. 显示预览
3. 用户确认

### 6. 同步到 GitHub

```bash
# 添加文件
git add src/assets/images/{slug}/  # 如有图片
git add src/data/blog/{slug}.md

# 提交并推送
git commit -m "docs: add {title}"
git push origin main
```

等待 Vercel/Netlify 自动部署（1-2 分钟）

---

## Frontmatter 模板

```yaml
---
title: {标题}
author: Theo
pubDatetime: {ISO8601时间，必须为过去}
slug: {url路径}
featured: false
draft: false
tags:
  - {标签1}
  - {标签2}
description: {描述}
canonicalURL: {原文链接，翻译文章必填}
---

{正文}
```

---

## ⚠️ 关键注意事项

### 1. 定时发布问题

**问题**：AstroPaper 有定时发布功能。`pubDatetime` 是未来的文章不会在生产环境显示。

**解决方案**：
- ✅ 使用**当前时间之前**的时间戳
- ✅ 格式：`2026-03-18T04:00:00Z`（北京时间 12:00 = UTC 04:00）
- ❌ 不要使用未来时间

**示例**：
```yaml
# ✅ 正确
pubDatetime: 2026-03-18T04:00:00Z

# ❌ 错误（文章不显示）
pubDatetime: 2026-03-19T20:00:00Z
```

**时区转换**：
- 北京时间（UTC+8）→ UTC：减 8 小时
- 例如：北京时间 12:00 = UTC 04:00

### 2. 图片引用方式

**❌ 不要使用 Astro Image 组件**：
```markdown
import { Image } from "astro:assets";
import coverImage from '../../assets/images/cover.jpg';

<Image src={coverImage} alt="封面" />
```

**✅ 使用标准 Markdown 语法**：
```markdown
![封面](../../assets/images/my-article/cover.jpg)
```

### 3. 图片路径规则

- Markdown 文件：`src/data/blog/xxx.md`
- 图片位置：`src/assets/images/xxx/`
- 引用路径：`../../assets/images/xxx/image.jpg`
  - 从 `blog/` 向上两级到 `src/`
  - 再进入 `assets/images/xxx/`

### 4. 图片命名规范

- 使用小写字母、数字、连字符
- 避免中文和空格
- 推荐格式：`.jpg`、`.png`、`.webp`
- Astro 会自动优化图片

### 5. 标题层级

- 不使用 h1（`#`）
- 正文从 h2（`##`）开始
- 层级：`##` → `###` → `####`

### 6. 翻译文章

- 必须添加 `canonicalURL` 指向原文
- 标题建议添加「译」前缀

### 7. 特色文章

- 设置 `featured: true` 在首页展示
- 建议只设置 3-5 篇

---

## 示例对话

**用户**: 发布一篇文章，内容是...

**助手**: 收到文章内容！让我整理并确认元信息：

**📄 标题**: Python 异步编程完全指南
**📝 描述**: 深入理解 Python asyncio...
**🏷️ 标签**: python, async, tutorial
**📅 发布时间**: 2026-03-18T04:00:00Z
**🔗 Slug**: python-async-programming-guide

确认以上信息？[确认/修改]

**用户**: 确认

**助手**: 正在保存文章...

✅ **文章发布成功！**

| 项目 | 值 |
|------|-----|
| 文件位置 | `src/data/blog/python-async-programming-guide.md` |
| 访问地址 | `/posts/python-async-programming-guide` |
| 提交 | `abc1234` |

等待 1-2 分钟后即可访问。
