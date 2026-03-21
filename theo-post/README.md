# Theo 博客文章发布工具

将文章发布到 Theo 博客（AstroPaper 主题）。处理图片、格式化内容、同步到 GitHub。

## 快速开始

```
/theo-post
```

或说：**"发布文章"**、**"写博客"**、**"新建博文"**

## 功能特性

- ✅ 自动处理图片上传和引用
- ✅ 格式化文章内容（标题、代码块、目录）
- ✅ 生成 frontmatter 元信息
- ✅ 自动同步到 GitHub
- ✅ 等待 Vercel/Netlify 部署

## 关键经验

### 图片引用

**正确** ✅：
```markdown
![封面](../../assets/images/my-article/cover.jpg)
```

**错误** ❌：
```markdown
import { Image } from "astro:assets";
<Image src={...} />
```

### 定时发布

- `pubDatetime` 必须使用**过去的时间**
- 未来时间的文章不会在生产环境显示

## 项目信息

- **仓库**: https://github.com/jeekeagle/theo
- **分支**: main
- **部署**: Vercel/Netlify

## 配置

见 `config.md`
