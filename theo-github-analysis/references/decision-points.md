# 决策点

本文档描述 Theo Github 技能中的关键决策点。

---

## 决策点 1: 分析深度选择

**条件**: 用户未指定 `--depth` 参数

**选项**:
- **quick**: 快速模式（仅基础信息）
- **standard**: 标准模式（What + Why + How）
- **deep**: 深度模式（+ 架构分析）

**决策依据**:
```python
if 用户未指定:
    depth = "standard"  # 默认使用标准模式
else:
    depth = 用户指定的值
```

**推荐**: 大多数情况下使用 `standard` 模式，既能获取有价值的信息，又不会过于冗长。

---

## 决策点 2: Subjects 自动推断

**条件**: 生成 YAML frontmatter 时需要确定 subjects

**选项**:
- `[[Productivity]]`: 工具类项目
- `[[Creativity]]`: 创意工具
- `[[Business]]`: 商业应用
- `[[Philosophy]]`: 哲学思考
- `[[Health]]`: 健康相关
- `[[Relationships]]`: 关系管理
- 多个 subjects: 组合分类

**决策依据**:
```python
subjects = []

# 根据编程语言推断
lang = metadata.get('language', '').lower()
if lang in ['typescript', 'javascript', 'python', 'go', 'rust']:
    subjects.append("[[Productivity]]")

# 根据 topics 推断
topics = metadata.get('topics', [])
topic_str = ' '.join(topics).lower()

if any(word in topic_str for word in ['ai', 'ml', 'machine-learning']):
    subjects.append("[[Productivity]]")

# 默认值
if not subjects:
    subjects.append("[[Productivity]]")
```

**推荐**: 如果不确定，默认使用 `[[Productivity]]`

---

## 决策点 3: 文件名冲突处理

**条件**: 目标文件已存在

**选项**:
- **覆盖**: 直接覆盖已有文件
- **重命名**: 生成带时间戳的新文件名
- **跳过**: 不保存，退出流程

**决策依据**:
```python
if filepath.exists():
    print(f"⚠️ 文件已存在: {filepath}")
    choice = input("是否覆盖？(y/n): ").lower()

    if choice == 'y':
        # 覆盖文件
        pass
    else:
        # 生成新文件名
        counter = 1
        while True:
            new_filename = f"{date_str}-{repo_name}-github-analysis-{counter}.md"
            new_filepath = output_dir / new_filename
            if not new_filepath.exists():
                filepath = new_filepath
                break
            counter += 1
```

**推荐**: 询问用户是否覆盖，给用户选择权

---

## 决策点 4: GitHub API 使用方式

**条件**: 需要获取仓库信息

**选项**:
- **GitHub CLI**: 使用 `gh` 命令行工具
- **GitHub REST API**: 直接调用 API
- **GitHub GraphQL API**: 使用 GraphQL 查询
- **网页爬取**: 解析 GitHub 页面（不推荐）

**决策依据**:
```python
# 优先使用 GitHub CLI
if has_gh_cli():
    return fetch_via_gh_cli()
# 其次使用 REST API
elif has_github_token():
    return fetch_via_rest_api()
# 最后尝试网页解析（可能不准确）
else:
    return fetch_via_web_scraping()
```

**推荐**: 优先使用 GitHub CLI（如果已安装），因为配置简单且无需 API token

---

## 决策点 5: AI 分析 Prompt 策略

**条件**: 需要对项目进行深度分析

**选项**:
- **单次分析**: 一次性生成所有内容
- **分步分析**: 分别分析 What/Why/How
- **交互式分析**: 逐步生成并确认

**决策依据**:
```python
if depth == "quick":
    prompt = generate_quick_prompt(metadata)
elif depth == "standard":
    prompt = generate_standard_prompt(metadata)
elif depth == "deep":
    # 分步分析，每次聚焦一个方面
    what_analysis = analyze_what(metadata)
    why_analysis = analyze_why(metadata, what_analysis)
    how_analysis = analyze_how(metadata, what_analysis, why_analysis)
    return combine_analyses(what_analysis, why_analysis, how_analysis)
```

**推荐**:
- Quick/Standard: 单次分析
- Deep: 分步分析，保证质量

---

## 决策点 6: 输出格式选择

**条件**: 生成分析报告

**选项**:
- **Markdown**: 默认，兼容 Obsidian
- **HTML**: 用于分享
- **PDF**: 用于打印
- **JSON**: 用于程序处理

**决策依据**:
```python
output_format = args.format or "markdown"

if output_format == "markdown":
    return generate_markdown(content)
elif output_format == "html":
    return generate_html(content)
elif output_format == "pdf":
    return generate_pdf(content)
elif output_format == "json":
    return generate_json(content)
```

**推荐**: 默认使用 Markdown，确保与 Obsidian Vault 完美集成

---

## 决策点 7: 错误恢复策略

**条件**: 分析过程中出现错误

**选项**:
- **立即失败**: 遇到错误立即停止
- **部分保存**: 保存已获取的信息
- **重试机制**: 自动重试失败的步骤
- **降级处理**: 使用简化策略

**决策依据**:
```python
try:
    metadata = fetch_metadata()
except APIError as e:
    if allow_degraded:
        # 降级处理：使用基础信息
        metadata = get_basic_metadata(url)
        logger.warning(f"API失败，使用降级模式: {e}")
    else:
        raise

try:
    analysis = ai_analyze(metadata)
except AIServiceError as e:
    if retry_count < max_retries:
        retry_count += 1
        time.sleep(2 ** retry_count)  # 指数退避
        return ai_analyze(metadata)  # 重试
    else:
        # 保存部分结果
        return save_partial_analysis(metadata)
```

**推荐**:
- API 错误：降级处理
- AI 服务错误：重试 3 次
- 其他错误：保存部分结果

---

## 决策点 8: 批量处理策略

**条件**: 用户输入多个 URL

**选项**:
- **串行处理**: 依次处理每个 URL
- **并行处理**: 同时处理多个 URL
- **限流处理**: 控制并发数

**决策依据**:
```python
if len(urls) == 1:
    return analyze_single(urls[0])

# 多个 URL
if allow_parallel:
    # 并行处理，但限制并发数
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(analyze, url) for url in urls]
        results = [f.result() for f in futures]
    return results
else:
    # 串行处理
    results = [analyze(url) for url in urls]
    return results
```

**推荐**:
- 2-3 个 URL: 并行处理
- 更多 URL: 限流并行（最多 3 个并发）
- 避免 GitHub API 限流

---

## 决策点 9: 缓存策略

**条件**: 用户重复分析同一仓库

**选项**:
- **不缓存**: 每次都重新分析
- **内存缓存**: 仅当前会话缓存
- **磁盘缓存**: 持久化缓存
- **智能缓存**: 根据仓库更新时间决定

**决策依据**:
```python
cache_dir = Path(".cache/theo-github")
cache_file = cache_dir / f"{repo_name}.json"

if use_smart_cache and cache_file.exists():
    cached = load_cache(cache_file)
    # 检查缓存是否过期（7天）
    if datetime.now() - cached['date'] < timedelta(days=7):
        # 检查仓库是否有更新
        if cached['last_updated'] == current_last_updated:
            return cached['analysis']

# 重新分析
result = perform_analysis(metadata)
save_cache(cache_file, result)
return result
```

**推荐**: 使用智能缓存，7天内未更新的仓库直接使用缓存

---

## 决策点 10: 学习要点提取策略

**条件**: Deep 模式下需要提取学习要点

**选项**:
- **模式识别**: 识别设计模式
- **最佳实践**: 提取最佳实践
- **代码片段**: 提取关键代码片段
- **架构图**: 生成架构可视化

**决策依据**:
```python
learning_points = {
    'design_patterns': extract_design_patterns(codebase),
    'best_practices': extract_best_practices(codebase),
    'code_snippets': extract_key_snippets(codebase, limit=5),
    'architecture': generate_architecture_diagram(codebase)
}

# 优先级排序
learning_points = prioritize_by_relevance(learning_points)
```

**推荐**:
- 提取前 3-5 个最重要的设计模式
- 选取 3-5 个最具代表性的代码片段
- 生成简化的架构图

---

## 决策总结

| 决策点 | 推荐方案 | 灵活性 |
|--------|---------|--------|
| 分析深度 | standard (可配置) | ⭐⭐⭐ |
| Subjects | 自动推断 + 手动调整 | ⭐⭐ |
| 文件冲突 | 询问用户 | ⭐⭐⭐ |
| API 方式 | GitHub CLI 优先 | ⭐⭐ |
| Prompt 策略 | 根据深度选择 | ⭐⭐⭐ |
| 输出格式 | Markdown 默认 | ⭐⭐ |
| 错误恢复 | 降级 + 重试 | ⭐⭐⭐ |
| 批量处理 | 限流并行 | ⭐⭐ |
| 缓存策略 | 智能缓存 | ⭐⭐⭐ |
| 学习要点 | Top 3-5 | ⭐⭐ |