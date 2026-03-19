# Theo's Agent Skills

个人定制的 Claude Code Agent Skills 集合。

## 简介

这个仓库存放了我为自己定制开发的 Agent Skills，用于增强 Claude Code 的能力，提升日常开发和内容创作的效率。

每个 Skill 都针对我的具体工作流程和需求设计，遵循渐进式披露原则，让 AI 助手能够更好地理解和执行我的任务。

## 可用 Skills

### 📝 [theo-post](./theo-post)

**Theo 博客文章发布工具**

将文章发布到 Theo 博客（AstroPaper 主题）的交互式工具。

**功能特性：**
- ✅ 自动处理图片上传和引用
- ✅ 格式化文章内容（标题、代码块、目录）
- ✅ 生成 frontmatter 元信息
- ✅ 自动同步到 GitHub
- ✅ 等待 Vercel/Netlify 部署

**触发方式：**
- `/theo-post`
- 说"发布文章"、"写博客"、"新建博文"

**适用场景：**
- 发布技术博客文章
- 翻译文章并发布
- 整理笔记并发布到博客

## 使用方法

这些 Skills 设计用于 Claude Code 环境。要使用某个 Skill：

1. **命令方式**：输入斜杠命令，如 `/theo-post`
2. **自然语言**：直接说出触发词，如"发布文章"

## 技术栈

- **Skill 框架**：基于 Agent-Skills 规范
- **配置管理**：每个 Skill 独立配置文件
- **渐进式披露**：SKILL.md → README.md → config.md

## 后续计划

随着我的需求增加，会持续添加新的 Skills：

- [ ] 自动化工作流相关 Skills
- [ ] 数据处理和分析 Skills
- [ ] 内容创作辅助 Skills
- [ ] 项目管理 Skills

## 相关链接

- **博客仓库**：[jeekeagle/theo](https://github.com/jeekeagle/theo)
- **Claude Code**：[anthropics/claude-code](https://github.com/anthropics/claude-code)

## 许可证

MIT License

---

> 💡 **提示**：这是个人定制工具集，会根据我的实际需求持续迭代。如果你觉得某个 Skill 有用，欢迎参考和改进！
