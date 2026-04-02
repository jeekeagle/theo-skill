# Theo Github 工作流步骤

本文档描述 Theo Github 技能的完整工作流程。

## 完整工作流

```
用户输入 GitHub URL
    ↓
步骤 1: 验证 URL 有效性
    ↓
步骤 2: 获取仓库元数据
    ↓
步骤 3: AI 深度分析
    ↓
步骤 4: 生成 Markdown 笔记
    ↓
步骤 5: 保存到 Obsidian Vault
    ↓
返回笔记路径
```

---

## 步骤 1: 验证 URL 有效性

### 输入
- `github_url`: 用户提供的 GitHub URL

### 处理
1. 使用正则表达式验证 URL 格式
2. 提取 owner 和 repo_name
3. 检查仓库是否可访问

### 输出
- `valid`: boolean
- `owner`: string
- `repo_name`: string

### 错误处理
- URL 格式无效 → 返回错误提示
- 仓库不存在 → 返回错误提示

---

## 步骤 2: 获取仓库元数据

### 输入
- `owner`: 仓库所有者
- `repo_name`: 仓库名称

### 处理
使用 GitHub CLI 或 GitHub API 获取以下信息：

#### 基础信息
- `stars`: Star 数量
- `language`: 主要编程语言
- `description`: 仓库描述
- `topics`: 仓库主题标签
- `license`: 开源协议
- `last_updated`: 最后更新时间

#### 扩展信息（深度模式）
- `contributors`: 贡献者数量
- `open_issues`: 开放 Issue 数量
- `forks`: Fork 数量
- `size`: 仓库大小

### 输出
```python
metadata = {
    'url': str,
    'owner': str,
    'repo_name': str,
    'full_name': str,
    'stars': str,
    'language': str,
    'description': str,
    'topics': List[str],
    'license': str,
    'last_updated': str
}
```

---

## 步骤 3: AI 深度分析

### 输入
- `metadata`: 仓库元数据
- `depth`: 分析深度 (quick/standard/deep)

### 处理

#### Quick 模式
- 生成一句话项目概括
- 提取核心技术栈

#### Standard 模式（默认）
- **What**: 基础信息分析
- **Why**: 差异化优势、核心价值
- **How**: 基本使用方法

#### Deep 模式
- Standard 模式的所有内容
- 架构设计分析
- 代码组织模式
- 性能优化技巧
- 可复用的设计模式

### 输出
- `analysis_content`: 结构化的分析内容

---

## 步骤 4: 生成 Markdown 笔记

### 输入
- `metadata`: 仓库元数据
- `analysis_content`: AI 分析内容

### 处理

#### 4.1 生成 YAML Frontmatter
```yaml
---
categories:
  - "[[Literature Notes]]"
subjects:
  - "[[Productivity]]"
type: article
status: saved
created: 2025-03-21
---
```

#### 4.2 生成内容结构
```markdown
# [[Repo Name]] - GitHub 仓库分析

## 📊 基础信息（What）
## 🎯 核心价值（Why）
## 🚀 如何使用（How）
## 💡 学习要点
## 🔗 相关资源
## 📝 个人笔记
```

#### 4.3 生成文件名
格式：`{{repo_name}}-github-analysis.md`（符合 Vault 规范，无日期前缀）

示例：`nextjs-github-analysis.md`

### 输出
- `markdown_content`: 完整的 Markdown 内容
- `filename`: 文件名

---

## 步骤 5: 保存到 Obsidian Vault

### 输入
- `markdown_content`: Markdown 内容
- `filename`: 文件名
- `output_dir`: 输出目录（默认：`01 - Notes/`）

### 处理

#### 5.1 检查文件是否已存在
```python
if filepath.exists():
    confirm = input("文件已存在，是否覆盖？(y/n): ")
    if not confirm:
        return  # 不覆盖，退出
```

#### 5.2 保存文件
```python
output_dir = Path("01 - Notes")
filepath = output_dir / filename

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(markdown_content)
```

#### 5.3 验证文件
```python
if filepath.exists():
    print(f"✅ 笔记已保存到: {filepath}")
else:
    print("❌ 保存失败")
```

### 输出
- `filepath`: 保存的文件路径
- `success`: boolean