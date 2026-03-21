---
name: theo-infocard
description: |
  高级信息卡视觉设计工具 - 将复杂信息转化为具有现代杂志质感的 HTML 信息卡。

  何时使用：
  - 需要将内容转化为视觉精美的信息卡时
  - 需要创建具有社论质感的设计时
  - 需要输出专业级 HTML/CSS 代码时

  触发词：信息卡, infocard, 设计卡片, 视觉卡片, 编辑卡片
allowed-tools: Read, Write, Edit
mcp_servers: []
---

# Theo Infocard

## 技能概述

专业社论视觉设计师工具，擅长将复杂信息转化为具有现代杂志质感的 HTML 信息卡。结合瑞士国际主义的严谨结构与现代杂志的视觉冲击力，在保持美感的同时确保信息的可读性与视觉张力。

## 核心能力

1. **信息密度分析**：智能分析内容并评估信息密度（高/中/低），选择最佳布局策略
2. **专业排版系统**：完整的字体、字号、行高、空间系统，确保视觉一致性
3. **响应式布局**：根据内容量自动选择"大字符主义"或"多栏网格"布局
4. **完整代码输出**：生成包含完整 CSS 的 HTML 代码，可直接使用

## 核心设计原则

- **字号提升**：正文 18-20px，确保清晰可读
- **紧凑排版**：优化留白，增强视觉张力
- **强化密度**：用粗线条、大字号填补空余空间

## 字体系统

### 字体库引入
```html
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@700;900&family=Noto+Sans+SC:wght@400;500;700&family=Oswald:wght@500;700&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
```

### 字号规范
| 层级 | 字号 | 属性 | 用途 |
|------|------|------|------|
| **超大标题** | 72-84px | line-height: 1.0, weight: 900, letter-spacing: -0.04em | 核心视觉钩子 |
| **大标题** | 56px | line-height: 1.1, weight: 700 | 主要章节标题 |
| **中标题** | 32px | line-height: 1.2 | 次级标题 |
| **正文** | 18-20px | line-height: 1.6, color: #1a1a1a | 主要内容 |
| **辅助信息** | 15-16px | line-height: 1.5, color: #555 | 说明文字 |
| **元数据/标签** | 13px | letter-spacing: 0.15em, weight: 700, uppercase | 分类标签 |

## 空间逻辑

- **外边距 (Container Padding)**: 40-50px
- **段落间距**: ≤ 1.5em
- **组件间距**: 30-40px
- **行高 (Line Height)**: 1.5-1.6

## 视觉装饰

- **噪点纹理**: 4% 透明度，增加纸质质感
- **重型分割线**: 4-6px 粗实线（Accent色），强化分量感
- **背景色块**: rgba(0,0,0,0.03) 浅灰色，界定空间

## 布局策略

### 内容少的情况
- 采用 **"大字符主义"**
- 标题字号撑满屏幕
- 核心数据放大至 120px+
- 作为背景视觉元素

### 内容多的情况
- 采用 **"多栏网格"**
- 参考报纸排版
- 内容分为 2-3 栏
- 垂直分割线增强结构感

## 核心样式参考

```css
.card {
  width: 900px;
  background: #f5f3ed;
  padding: 50px;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  gap: 30px;
}

.main-title {
  font-family: 'Noto Serif SC', serif;
  font-size: 80px;
  font-weight: 900;
  line-height: 1.0;
  margin: 0;
  color: #0a0a0a;
}

.content-body {
  font-family: 'Inter', 'Noto Sans SC', sans-serif;
  font-size: 19px;
  line-height: 1.6;
  color: #1a1a1a;
}

.accent-bar {
  height: 6px;
  background: var(--color-accent);
  width: 100px;
  margin: 10px 0;
}
```

## 输出流程

1. **分析**：用 1 句话分析内容的信息密度（高/中/低）
2. **代码**：输出完整的 HTML（含 CSS）
3. **自检**：确保正文文字在手机屏幕上也能一眼看清

## 使用方法

### 基本用法

提供需要转化为信息卡的内容，技能将：
1. 分析信息密度
2. 选择合适的布局策略
3. 生成完整的 HTML/CSS 代码

### 示例输入

```
创建一个关于"人工智能发展史"的信息卡，包含3个关键时期
```

### 示例输出

- 信息密度分析
- 完整的 HTML 代码
- 内联 CSS 样式
- 响应式设计

## 设计哲学

结合瑞士国际主义的严谨结构与现代杂志的视觉冲击力，在保持美感的同时，确保信息的可读性与视觉张力。

## 注意事项

- 所有生成的 HTML 代码都包含完整的内联 CSS
- 确保在移动设备上也能清晰阅读（正文 18-20px）
- 根据内容量智能选择布局策略
- 使用 Google Fonts 确保跨平台字体一致性
