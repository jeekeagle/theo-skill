# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a monorepo containing custom Claude Code Agent Skills. Each skill is a self-contained tool that extends Claude Code's capabilities for specific workflows.

**Repository**: https://github.com/jeekeagle/theo-skill

## Project Structure

```
theo-skill/
├── theo-card/          # Content caster - transforms text to PNG visuals
├── theo-github/        # GitHub repo analysis tool
├── theo-infocard/      # Information card design tool
├── theo-paper/         # Academic paper reading assistant
├── theo-paper-flow/    # Combined paper reading + card generation workflow
├── theo-post/          # Blog post publishing tool (AstroPaper theme)
└── theo-translate/     # Translation tool with custom glossary support
```

## Skill Architecture

Each skill follows this structure:

```
<skill-name>/
├── SKILL.md              # Skill frontmatter and documentation (required)
├── skill.json            # Parameter definitions and workflow config (optional)
├── config.md             # Skill-specific configuration (optional)
├── scripts/              # Helper scripts and validation logic
├── examples/             # Usage examples and documentation
├── references/           # Design docs, workflow steps, decision points
├── assets/               # Static assets (images, templates, etc.)
├── node_modules/         # NPM dependencies (if the skill uses Node.js)
└── package.json          # NPM package config (if applicable)
```

### SKILL.md Frontmatter

Every SKILL.md file must begin with YAML frontmatter:

```yaml
---
name: skill-name
description: Brief description of what the skill does
user_invocable: true  # If users can invoke via /skill-name
version: "1.0.0"
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, WebSearch
mcp_servers: []
---
```

### skill.json Structure

For skills with parameterized workflows, `skill.json` defines:

- `parameters`: Input validation and type checking
- `output_format`: File naming and frontmatter templates
- `workflow`: Step-by-step execution flow

Example from `theo-github`:
```json
{
  "name": "theo-github",
  "parameters": {
    "github_url": { "type": "string", "required": true, "pattern": "^https://github\\.com/[^/]+/[^/]+$" }
  },
  "workflow": {
    "steps": ["validate_url", "fetch_repo_metadata", "ai_analysis", "generate_markdown", "save_to_vault"]
  }
}
```

## Development Commands

### theo-card (Playwright dependencies)

The `theo-card` skill uses Playwright for HTML-to-PNG conversion. Install dependencies:

```bash
cd theo-card
npm install
npx playwright install chromium
```

**Screenshot tool location**: `~/.claude/skills/theo-card/assets/capture.js`

Usage: `node capture.js <html> <png> <width> <height> [fullpage]`

### theo-post Configuration

The `theo-post` skill requires environment configuration:

```bash
PROJECT_PATH=E:/Theo/theo
GIT_REPO=https://github.com/jeekeagle/theo
GIT_BRANCH=main
IMAGE_DIR=src/assets/images
BLOG_DIR=src/data/blog
```

## Skill Design Principles

1. **Self-documenting**: Each skill's SKILL.md should contain complete usage instructions
2. **Progressive disclosure**: Start with simple use cases, reveal advanced options in `references/`
3. **Shared utilities**: Common patterns (file naming, content fetching) are documented in skill SKILL.md files
4. **Trigger-based**: Skills define clear trigger words/phrases in their frontmatter

## Adding a New Skill

1. Create a new directory: `mkdir <skill-name>`
2. Create `SKILL.md` with proper frontmatter
3. Add `skill.json` if the skill has parameters
4. Create `references/` for design documentation
5. Create `examples/` for usage examples
6. If using Node.js: add `package.json` and install dependencies
7. Update root `README.md` with the new skill description

## File Naming Conventions

- **Skill names**: lowercase with hyphens (`theo-card`, `theo-post`)
- **Markdown files**: kebab-case or descriptive (`workflow-steps.md`, `basic-usage.md`)
- **PNG outputs** (theo-card): Extract title from content, ≤20 Chinese characters, remove punctuation

## Key Workflows

### theo-card Content Pipeline
1. Get content (URL → WebFetch, text → direct, file → Read)
2. Extract title/name from content
3. Generate HTML based on mold (-l/-i/-c)
4. Screenshot using Playwright
5. Output to `~/Downloads/`

### theo-github Analysis Pipeline
1. Validate GitHub URL
2. Fetch repo metadata (GitHub API)
3. AI analysis (What + Why + How)
4. Generate structured Markdown
5. Save to Obsidian Vault (`01 - Notes/`)

### theo-post Publishing Pipeline
1. Receive article content (text/URL/file)
2. Process images (upload to blog)
3. Format content (Markdown + frontmatter)
4. Commit to GitHub repo
5. Trigger deployment

## References Documentation

The `references/` directory in each skill contains:
- `workflow-steps.md`: Detailed step-by-step breakdown
- `decision-points.md`: Architecture decisions and trade-offs
- `mode-*.md`: Mode-specific documentation (e.g., theo-card molds)
- `config/*.md`: Configuration schemas and extensions

These are design documents, not user-facing documentation.
