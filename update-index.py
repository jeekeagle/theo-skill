#!/usr/bin/env python3
"""
Theo Skills 自动索引生成器

自动扫描 skills/ 目录下的所有技能文件夹，
并提取元数据更新到 index.html
"""

import os
import json
import re
from pathlib import Path
from datetime import datetime


def extract_skill_metadata(skill_path):
    """从技能目录提取元数据"""
    index_file = skill_path / "index.html"

    if not index_file.exists():
        return None

    # 读取 HTML 文件
    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 提取标题
    title_match = re.search(r'<title>(.*?)</title>', content)
    title = title_match.group(1) if title_match else skill_path.name

    # 提取描述（从 meta tag 或第一个段落）
    desc_match = re.search(r'<meta name="description" content="(.*?)"', content)
    description = desc_match.group(1) if desc_match else f"{title} - 技能页面"

    # 提取 tag
    tag_match = re.search(r'<div class="tag">(.*?)</div>', content)
    tag = tag_match.group(1) if tag_match else "SKILL"

    return {
        "slug": skill_path.name,
        "name": title.split('-')[0].strip(),
        "description": description,
        "category": tag,
        "icon": "⚡",
        "version": "1.0.0",
        "path": f"skills/{skill_path.name}/index.html"
    }


def scan_skills_directory(root_dir):
    """扫描 skills 目录"""
    skills_dir = root_dir / "skills"

    if not skills_dir.exists():
        print(f"警告: skills 目录不存在: {skills_dir}")
        return []

    skills = []
    for item in skills_dir.iterdir():
        if item.is_dir() and not item.name.startswith('.'):
            metadata = extract_skill_metadata(item)
            if metadata:
                skills.append(metadata)

    return skills


def update_index_html(root_dir, skills):
    """更新 index.html 中的技能元数据"""
    index_file = root_dir / "index.html"

    if not index_file.exists():
        print(f"错误: index.html 不存在: {index_file}")
        return False

    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 生成新的元数据对象
    metadata_obj = "{\n"
    for skill in skills:
        metadata_obj += f"        '{skill['slug']}': {{\n"
        metadata_obj += f"            name: '{skill['name']}',\n"
        metadata_obj += f"            description: '{skill['description'][:80]}...',\n"
        metadata_obj += f"            category: '{skill['category']}',\n"
        metadata_obj += f"            icon: '{skill['icon']}',\n"
        metadata_obj += f"            version: '{skill['version']}'\n"
        metadata_obj += f"        }},\n"
    metadata_obj = metadata_obj.rstrip(',\n') + '\n    }'

    # 替换 skillsMetadata 对象
    pattern = r'const skillsMetadata = \{[^}]*\};'
    replacement = f'const skillsMetadata = {metadata_obj};'

    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    # 写回文件
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"✅ 已更新 {index_file}")
    print(f"   发现 {len(skills)} 个技能")
    return True


def generate_skills_json(root_dir, skills):
    """生成 skills.json 索引文件"""
    output_file = root_dir / "skills.json"

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({
            "updated": datetime.now().isoformat(),
            "count": len(skills),
            "skills": skills
        }, f, ensure_ascii=False, indent=2)

    print(f"✅ 已生成 {output_file}")


def main():
    """主函数"""
    root_dir = Path(__file__).parent

    print("🔍 扫描技能目录...")
    skills = scan_skills_directory(root_dir)

    if not skills:
        print("❌ 未发现任何技能")
        return

    print(f"✅ 发现 {len(skills)} 个技能:")
    for skill in skills:
        print(f"   - {skill['name']} ({skill['slug']})")

    print("\n📝 更新 index.html...")
    update_index_html(root_dir, skills)

    print("\n📄 生成 skills.json...")
    generate_skills_json(root_dir, skills)

    print("\n✨ 完成!")


if __name__ == "__main__":
    main()