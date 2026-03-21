#!/usr/bin/env python3
"""Theo Github - GitHub 仓库深度分析工具

这个脚本实现了 GitHub 仓库的自动分析和学习笔记生成功能。
"""

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List


class GitHubAnalyzer:
    """GitHub 仓库分析器"""

    def __init__(self, github_url: str, depth: str = "standard", output_dir: str = "01 - Notes", user_notes: str = ""):
        """初始化分析器

        Args:
            github_url: GitHub 仓库 URL
            depth: 分析深度 (quick/standard/deep)
            output_dir: 输出目录
            user_notes: 用户的个人想法和备注
        """
        self.github_url = github_url
        self.depth = depth
        self.output_dir = Path(output_dir)
        self.user_notes = user_notes
        self.repo_info = {}

    def validate_url(self) -> bool:
        """验证 GitHub URL 有效性

        Returns:
            URL 是否有效
        """
        pattern = r'^https://github\.com/[^/]+/[^/]+$'
        if not re.match(pattern, self.github_url):
            return False

        # 提取仓库信息
        parts = self.github_url.rstrip('/').split('/')
        self.repo_info['owner'] = parts[-2]
        self.repo_info['repo_name'] = parts[-1]
        self.repo_info['full_name'] = f"{self.repo_info['owner']}/{self.repo_info['repo_name']}"

        return True

    def fetch_metadata(self) -> Dict[str, Any]:
        """获取仓库元数据

        Returns:
            仓库元数据字典
        """
        # 这里使用 GitHub CLI (gh) 获取信息
        # 在实际使用中，会通过 Bash tool 调用
        metadata = {
            'url': self.github_url,
            'owner': self.repo_info['owner'],
            'repo_name': self.repo_info['repo_name'],
            'full_name': self.repo_info['full_name'],
            # 以下信息需要通过 GitHub API 获取
            'stars': 'N/A',
            'language': 'N/A',
            'description': 'N/A',
            'topics': [],
            'license': 'N/A',
            'last_updated': 'N/A'
        }

        return metadata

    def generate_filename(self) -> str:
        """生成输出文件名

        Returns:
            文件名
        """
        # 根据 CLAUDE.md 规范：除 Newsletters/Tweets/Reviews 外，其他文件不使用日期前缀
        repo_name = self.repo_info['repo_name'].lower().replace('_', '-')
        return f"{repo_name}-github-analysis.md"

    def generate_frontmatter(self, metadata: Dict[str, Any]) -> str:
        """生成 YAML frontmatter

        Args:
            metadata: 仓库元数据

        Returns:
            YAML frontmatter 字符串
        """
        # 根据项目类型推断 subjects
        subjects = self._infer_subjects(metadata)

        frontmatter = {
            'categories': ['[[Literature Notes]]'],
            'subjects': subjects,
            'type': 'article',  # 根据 CLAUDE.md：Literature Notes 使用 article/book/video/podcast/course
            'status': 'saved',
            'created': datetime.now().strftime('%Y-%m-%d')
        }

        # 转换为 YAML 格式
        lines = ['---']
        for key, value in frontmatter.items():
            if isinstance(value, list):
                lines.append(f"{key}:")
                for item in value:
                    lines.append(f"  - {item}")
            else:
                lines.append(f"{key}: {value}")
        lines.append('---')

        return '\n'.join(lines)

    def _infer_subjects(self, metadata: Dict[str, Any]) -> List[str]:
        """根据项目信息推断 subjects

        Args:
            metadata: 仓库元数据

        Returns:
            subjects 列表
        """
        subjects = []

        # 根据语言推断
        lang = metadata.get('language', '').lower()
        if lang in ['typescript', 'javascript', 'python', 'go', 'rust']:
            subjects.append('[[Productivity]]')

        # 根据 topics 推断
        topics = metadata.get('topics', [])
        topic_str = ' '.join(topics).lower()

        if any(word in topic_str for word in ['ai', 'ml', 'machine-learning']):
            subjects.append('[[Productivity]]')

        return subjects if subjects else ['[[Productivity]]']

    def generate_content_template(self, metadata: Dict[str, Any]) -> str:
        """生成笔记内容模板

        Args:
            metadata: 仓库元数据

        Returns:
            Markdown 内容
        """
        repo_name = metadata['repo_name']
        full_name = metadata['full_name']

        content = f"""

# [[{repo_name}]] - GitHub 仓库分析

> 📊 仓库地址：[{full_name}]({metadata['url']})

---

## 📊 基础信息（What）

| 字段 | 内容 |
|------|------|
| **仓库地址** | {metadata['url']} |
| **Star 数** | {metadata.get('stars', 'N/A')} |
| **主要语言** | {metadata.get('language', 'N/A')} |
| **项目类型** | 待分析 |
| **最后更新** | {metadata.get('last_updated', 'N/A')} |

**一句话描述：** {metadata.get('description', '待分析...')}

---

## 🎯 核心价值（Why）

### 解决什么问题？

<!-- AI 分析后将填充这部分内容 -->

### 差异化优势

1. **优势1：** 待分析
2. **优势2：** 待分析
3. **优势3：** 待分析

### 为什么值得关注？

<!-- AI 分析后将填充这部分内容 -->

---

## 🚀 如何使用（How）

### 安装

\`\`\`bash
# 待分析
\`\`\`

### 快速上手

\`\`\`typescript
// 基本用法示例
\`\`\`

### 核心概念

- **概念1：** 待分析
- **概念2：** 待分析

---

## 💡 学习要点

### 值得借鉴的设计

1. **架构设计：** 待分析
2. **代码组织：** 待分析
3. **性能优化：** 待分析

### 可复用的模式

- 待分析

---

## 🔗 相关资源

- 官方文档：待添加
- 示例项目：待添加
- 社区讨论：待添加

---

## 📝 个人笔记

> 这里可以添加你自己的理解和备注

<!-- 在这里记录你的学习心得、疑问、想法 -->

{self.user_notes if self.user_notes else "*你可以在这里添加你的想法和备注*"}

---
*分析时间：{datetime.now().strftime('%Y-%m-%d %H:%M')}*
*分析深度：{self.depth}*
"""

        return content

    def save_to_vault(self, content: str) -> Path:
        """保存笔记到 Vault

        Args:
            content: Markdown 内容

        Returns:
            保存的文件路径
        """
        filename = self.generate_filename()
        filepath = self.output_dir / filename

        # 确保输出目录存在
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # 写入文件
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        return filepath

    def analyze(self) -> Path:
        """执行完整的分析流程

        Returns:
            生成的文件路径
        """
        # 1. 验证 URL
        if not self.validate_url():
            raise ValueError(f"无效的 GitHub URL: {self.github_url}")

        # 2. 获取元数据
        metadata = self.fetch_metadata()

        # 3. 生成 frontmatter
        frontmatter = self.generate_frontmatter(metadata)

        # 4. 生成内容
        content_template = self.generate_content_template(metadata)

        # 5. 组合最终内容
        final_content = frontmatter + '\n' + content_template

        # 6. 保存到 Vault
        filepath = self.save_to_vault(final_content)

        return filepath


def main():
    """命令行入口"""
    parser = argparse.ArgumentParser(
        description='Theo Github - GitHub 仓库深度分析工具'
    )
    parser.add_argument(
        'github_url',
        help='GitHub 仓库 URL'
    )
    parser.add_argument(
        '--depth',
        choices=['quick', 'standard', 'deep'],
        default='standard',
        help='分析深度 (默认: standard)'
    )
    parser.add_argument(
        '--output-dir',
        default='01 - Notes',
        help='输出目录 (默认: "01 - Notes")'
    )
    parser.add_argument(
        '--notes',
        default='',
        help='你的个人想法和备注，会添加到笔记的"个人笔记"部分'
    )

    args = parser.parse_args()

    try:
        # 创建分析器
        analyzer = GitHubAnalyzer(
            github_url=args.github_url,
            depth=args.depth,
            output_dir=args.output_dir,
            user_notes=args.notes
        )

        # 执行分析
        filepath = analyzer.analyze()

        print(f"✅ 分析完成！")
        print(f"📄 笔记已保存到: {filepath}")
        print(f"🔗 GitHub 仓库: {args.github_url}")

    except Exception as e:
        print(f"❌ 错误: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
