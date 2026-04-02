# EXTEND.md Schema for theo-translate

## 格式

EXTEND.md 使用 YAML 格式：

```yaml
# 默认目标语言（ISO 代码或常用名称）
target_language: zh-CN

# 目标读者（影响注释深度和语域）
audience: general  # general | technical | academic | business | 或自定义字符串

# 翻译风格偏好
style: storytelling  # storytelling | formal | technical | literal | academic | business | conversational | 或自定义字符串

# 触发分块翻译的字数阈值
chunk_threshold: 4000

# 每块最大字数
chunk_max_words: 5000

# 自定义术语表（与内置术语表合并）
# CLI --glossary 参数覆盖这些
glossary:
  - from: "Reinforcement Learning"
    to: "强化学习"
  - from: "Transformer"
    to: "Transformer"
    note: "保留英文"

# 语言对特定术语表
glossaries:
  en-zh:
    - from: "AI Agent"
      to: "AI 智能体"
  ja-zh:
    - from: "人工知能"
      to: "人工智能"
```

## 字段

| 字段 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `target_language` | string | `zh-CN` | 默认目标语言代码 |
| `audience` | string | `general` | 目标读者画像（`general` / `technical` / `academic` / `business` / 自定义） |
| `style` | string | `storytelling` | 翻译风格（`storytelling` / `formal` / `technical` / `literal` / `academic` / `business` / `conversational` / 自定义） |
| `chunk_threshold` | number | `4000` | 触发分块翻译的字数阈值 |
| `chunk_max_words` | number | `5000` | 每块最大字数 |
| `glossary` | array | `[]` | 通用术语表条目 |
| `glossaries` | object | `{}` | 语言对特定术语表条目 |

## 术语表条目

| 字段 | 必填 | 说明 |
|------|------|------|
| `from` | 是 | 源术语 |
| `to` | 是 | 目标翻译 |
| `note` | 否 | 使用说明（如 "保留英文"、"仅技术上下文"） |

## 优先级

1. CLI `--glossary` 文件条目
2. EXTEND.md `glossaries[pair]` 条目
3. EXTEND.md `glossary` 条目
4. 内置术语表（如 `references/glossary-en-zh.md`）

后条目覆盖前条目的相同源术语。
