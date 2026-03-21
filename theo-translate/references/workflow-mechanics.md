# Workflow Mechanics

源文件物化、输出目录创建和冲突解决的详细说明。

## 物化源文件

| 输入类型 | 操作 |
|----------|------|
| 文件 | 原样使用（无需复制） |
| 内联文本 | 保存到 `translate/{slug}.md` |
| URL | 获取内容，保存到 `translate/{slug}.md` |

`{slug}`: 从内容主题派生的 2-4 个单词的 kebab-case 标识符。

## 创建输出目录

在源文件旁边创建子目录：`{source-dir}/{source-basename}-{target-lang}/`

示例：
- `posts/article.md` → `posts/article-zh/`
- `translate/ai-future.md` → `translate/ai-future-zh/`

## 冲突解决

如果输出目录已存在，在创建新目录前将现有目录重命名为 `{name}.backup-YYYYMMDD-HHMMSS/`。永不覆盖现有结果。
