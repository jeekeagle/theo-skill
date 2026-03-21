# Theo Infocard 使用示例

## 示例 1：低密度内容 - 大字符主义

### 输入
```
创建一个关于"设计原则"的信息卡，核心观点：少即是多
```

### 分析
信息密度：低（单一核心观点）

### 输出策略
采用"大字符主义"布局：
- 超大标题（120px+）作为视觉焦点
- 极简内容，强化视觉冲击
- 充足留白营造高级感

### 生成的 HTML 代码

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@700;900&family=Noto+Sans+SC:wght@400;500;700&family=Oswald:wght@500;700&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: 'Inter', 'Noto Sans SC', sans-serif;
      background: #e8e6e1;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      padding: 20px;
    }
    .card {
      width: 100%;
      max-width: 900px;
      background: #f5f3ed;
      padding: 60px 50px;
      position: relative;
      overflow: hidden;
    }
    .card::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%' height='100%' filter='url(%23noise)' opacity='0.04'/%3E%3C/svg%3E");
      pointer-events: none;
    }
    .main-title {
      font-family: 'Noto Serif SC', serif;
      font-size: clamp(72px, 15vw, 140px);
      font-weight: 900;
      line-height: 0.95;
      margin: 0;
      color: #0a0a0a;
      letter-spacing: -0.04em;
      position: relative;
      z-index: 1;
    }
    .accent-bar {
      height: 6px;
      background: #c9a87c;
      width: 120px;
      margin: 30px 0;
      position: relative;
      z-index: 1;
    }
    .subtitle {
      font-family: 'Inter', sans-serif;
      font-size: 20px;
      font-weight: 500;
      color: #555;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      position: relative;
      z-index: 1;
    }
  </style>
</head>
<body>
  <div class="card">
    <h1 class="main-title">少<br>即<br>是<br>多</h1>
    <div class="accent-bar"></div>
    <p class="subtitle">设计原则</p>
  </div>
</body>
</html>
```

---

## 示例 2：中密度内容 - 平衡布局

### 输入
```
创建一个关于"色彩心理学"的信息卡，包含3种颜色的心理效应
```

### 分析
信息密度：中（多个相关概念）

### 输出策略
采用平衡布局：
- 清晰的标题层次
- 结构化的内容组织
- 适度的视觉装饰

---

## 示例 3：高密度内容 - 多栏网格

### 输入
```
创建一个关于"2024科技趋势"的信息卡，包含8个主要趋势
```

### 分析
信息密度：高（大量信息点）

### 输出策略
采用"多栏网格"布局：
- 3栏报纸式排版
- 垂直分割线区分内容
- 紧凑但有序的信息排列
- 清晰的视觉层级

---

## 使用技巧

### 1. 明确内容量
在使用技能前，先估算内容量：
- **低密度**：1-2 个核心观点
- **中密度**：3-5 个相关要点
- **高密度**：6+ 个信息点

### 2. 提供关键信息
为了获得最佳效果，请提供：
- 主要标题/核心观点
- 需要包含的内容要点
- 期望的视觉风格（可选）
- 品牌色或强调色（可选）

### 3. 移动端优化
所有生成的信息卡都：
- 使用相对单位（clamp, vw）
- 最小字号 18px 确保可读性
- 响应式布局适配各种屏幕

### 4. 自定义样式
生成代码后可轻松自定义：
- 修改 `--color-accent` 变量更改强调色
- 调整 `padding` 控制留白
- 更换 `font-family` 匹配品牌字体
