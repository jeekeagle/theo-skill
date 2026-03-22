# Theo Skills

> 精心设计的 Claude Code 技能生态

## 概述

Theo Skills 是一个专业的 Claude Code 技能集合网站，展示了一系列精心设计的工具和技能。

## 特性

- 🎨 **高级感设计** - 极简主义 + 现代视觉
- ⚡ **自动索引** - 自动扫描和更新技能列表
- 📱 **响应式布局** - 完美适配各种设备
- 🚀 **快速加载** - 纯静态站点，无需构建

## 技能列表

### Theo-infocard
高级信息卡视觉设计工具 - 将复杂信息转化为具有现代杂志质感的 HTML 信息卡

## 本地运行

```bash
# 克隆仓库
git clone https://github.com/yourusername/theo-skill.git
cd theo-skill

# 直接用浏览器打开 index.html
# 或使用本地服务器
python -m http.server 8000
```

然后访问 http://localhost:8000

## 添加新技能

1. 在 `skills/` 目录下创建新文件夹
2. 将技能的 `index.html` 放入该文件夹
3. 运行更新脚本：

```bash
python update-index.py
```

脚本会自动：
- 扫描 `skills/` 目录
- 提取技能元数据
- 更新 `index.html` 和 `skills.json`

## 目录结构

```
theo-skill/
├── index.html              # 首页（自动生成）
├── update-index.py         # 索引更新脚本
├── skills.json             # 技能索引（自动生成）
├── skills/
│   └── theo-infocard/
│       └── index.html      # 技能页面
└── README.md
```

## 技术栈

- HTML5
- CSS3 (Grid + Flexbox)
- Vanilla JavaScript
- Python 3 (索引脚本)

## 设计原则

- **极简主义** - 去除一切不必要的元素
- **深色主题** - 突出专业感和高级感
- **网格布局** - 清晰的视觉层次
- **流畅动画** - 提升用户体验

## 贡献

欢迎提交 Pull Request 或创建 Issue！

## 许可证

MIT License

---

**TheoSkills** - 精心设计，专业工具
