# Contributing to TubeFlow

Thank you for your interest in contributing to TubeFlow. This document provides guidelines and information for contributors.

---

## Table of Contents

- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Code Style](#code-style)
- [Areas for Contribution](#areas-for-contribution)
- [Pull Request Guidelines](#pull-request-guidelines)
- [Issue Reporting](#issue-reporting)
- [Code of Conduct](#code-of-conduct)

---

## How to Contribute

### Fork and Clone

1. **Fork the repository** on GitHub

2. **Clone your fork**:
   ```bash
   git clone https://github.com/YOUR-USERNAME/tubeflow.git
   cd tubeflow
   ```

3. **Add upstream remote**:
   ```bash
   git remote add upstream https://github.com/yourorg/tubeflow.git
   ```

### Create a Feature Branch

Always create a branch for your changes:

```bash
git checkout -b feature/your-feature-name
```

Branch naming conventions:
- `feature/` - New features
- `fix/` - Bug fixes
- `docs/` - Documentation updates
- `refactor/` - Code refactoring

### Make Your Changes

1. Make your changes in the feature branch
2. Test your changes locally
3. Commit with clear messages

### Submit a Pull Request

1. Push your branch to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

2. Open a Pull Request on GitHub

3. Fill out the PR template

4. Wait for review

---

## Development Setup

### Prerequisites

- Git
- Claude Code CLI (for testing workflows)
- Obsidian (optional, for vault testing)
- Python 3.8+ (for yt-dlp integration)
- yt-dlp (`pip install yt-dlp`)

### Clone and Configure

```bash
# Clone your fork
git clone https://github.com/YOUR-USERNAME/tubeflow.git
cd tubeflow

# Copy example config
cp config.example.yaml config.yaml
```

### Set Up Test Vault

Create a test vault structure for development:

```bash
mkdir -p test-vault/03-YouTube/{ideas,drafts,published,research}
mkdir -p test-vault/04-Social/{linkedin,twitter,facebook,cross-post}
mkdir -p test-vault/05-Templates
```

### Testing Changes Locally

1. **For workflow changes** (`.claude/commands/`):
   - Copy modified files to `~/.claude/commands/`
   - Run the command in a test vault
   - Verify output matches expectations

2. **For agent changes** (`.claude/agents/`):
   - Copy modified files to `~/.claude/agents/`
   - Test agent functionality
   - Check output format and quality

3. **For template changes** (`templates/`):
   - Test template rendering
   - Verify placeholders work correctly
   - Check formatting on target platform

### Running Tests

```bash
# Validate YAML syntax
python -c "import yaml; yaml.safe_load(open('config.example.yaml'))"

# Check markdown formatting
# (Install markdownlint-cli if needed: npm install -g markdownlint-cli)
markdownlint docs/*.md
```

---

## Code Style

### Markdown Formatting

- Use ATX-style headers (`#`, `##`, `###`)
- One blank line before and after headers
- Use fenced code blocks with language identifiers
- Maximum line length: 100 characters (soft limit)
- Use tables for structured data
- Consistent list formatting (use `-` for unordered lists)

```markdown
# Good Example

## Section Header

This is a paragraph with a [link](https://example.com).

- List item one
- List item two

| Column 1 | Column 2 |
|----------|----------|
| Data     | Data     |
```

### YAML Style

- 2-space indentation
- Use quotes for strings with special characters
- Include comments for non-obvious settings
- Group related settings together

```yaml
# Good Example
section:
  # Description of setting
  setting_name: "value"
  another_setting: true
```

### Agent and Command Files

- Clear header with agent/command purpose
- Structured sections with headers
- Include example usage
- Document all parameters
- Use consistent terminology

### Variable and File Naming

| Type | Convention | Example |
|------|------------|---------|
| Folders | lowercase-with-hyphens | `youtube-research` |
| Files | lowercase-with-hyphens.md | `research-pack.md` |
| Config keys | snake_case | `research_model` |
| Commands | lowercase | `/youtube-research` |
| Agents | @lowercase-name | `@yt-topic-gatherer` |

---

## Areas for Contribution

We welcome contributions in these areas:

### New Platform Integrations

- **TikTok** workflow
- **Instagram** Reels workflow
- **Threads** integration
- **Mastodon** support

Requirements:
- Platform-specific formatting rules
- Character limits and best practices
- Template for content creation
- Integration with existing `/social` workflow

### Additional Research Agents

- **Trend Analyzer** - Identify trending topics in niche
- **Monetization Researcher** - Sponsorship opportunities
- **Accessibility Checker** - Ensure content is accessible
- **Localization Helper** - Multi-language considerations

Requirements:
- Clear agent responsibility
- Defined output format
- Integration with research workflow
- Appropriate model selection

### Documentation Improvements

- Tutorial videos/guides
- More examples
- Translations
- Troubleshooting guides
- FAQ sections

### Bug Fixes

- Formatting issues
- Edge case handling
- Error messages
- Performance improvements

### Template Enhancements

- New template types
- Template customization options
- Platform-specific templates
- Template validation

---

## Pull Request Guidelines

### PR Checklist

Before submitting:

- [ ] Code follows the style guidelines
- [ ] Changes are tested locally
- [ ] Documentation is updated (if applicable)
- [ ] Commit messages are clear and descriptive
- [ ] PR description explains the changes

### PR Description Template

```markdown
## Summary

Brief description of changes.

## Type of Change

- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Refactoring

## Changes Made

- Change 1
- Change 2

## Testing

How did you test these changes?

## Related Issues

Fixes #123
```

### Review Process

1. A maintainer will review your PR
2. Changes may be requested
3. Once approved, PR will be merged
4. Your contribution will be acknowledged

### Commit Message Guidelines

Use clear, descriptive commit messages:

```
feat: add TikTok platform support

- Add TikTok template
- Integrate with /social workflow
- Update documentation
```

Prefixes:
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation only
- `refactor:` - Code refactoring
- `test:` - Test additions/changes
- `chore:` - Maintenance tasks

---

## Issue Reporting

### Bug Reports

Use this template when reporting bugs:

```markdown
## Bug Description

Clear description of the bug.

## Steps to Reproduce

1. Step one
2. Step two
3. Step three

## Expected Behavior

What should happen.

## Actual Behavior

What actually happens.

## Environment

- OS: [e.g., macOS 14.0]
- Claude Code version: [e.g., 1.2.0]
- TubeFlow version: [e.g., 1.0.0]

## Additional Context

Any other relevant information.
```

### Feature Requests

Use this template for feature requests:

```markdown
## Feature Description

Clear description of the proposed feature.

## Use Case

Why is this feature needed? What problem does it solve?

## Proposed Solution

How should this feature work?

## Alternatives Considered

Other approaches you've thought about.

## Additional Context

Any other relevant information.
```

### Good Issue Practices

- Search existing issues before creating new ones
- Use descriptive titles
- Provide as much context as possible
- Be responsive to follow-up questions
- Keep discussions on-topic

---

## Code of Conduct

### Our Standards

We are committed to providing a welcoming and inclusive environment. We expect all contributors to:

- **Be respectful**: Treat everyone with respect and consideration
- **Be constructive**: Provide helpful feedback and suggestions
- **Be collaborative**: Work together toward common goals
- **Be patient**: Remember that everyone has different skill levels
- **Be professional**: Keep discussions focused and productive

### Unacceptable Behavior

- Harassment or discrimination of any kind
- Trolling, insulting, or derogatory comments
- Personal or political attacks
- Publishing others' private information
- Other conduct inappropriate for a professional setting

### Enforcement

Violations of the code of conduct may result in:
1. Warning from maintainers
2. Temporary ban from the project
3. Permanent ban from the project

### Reporting

If you experience or witness unacceptable behavior, please contact the maintainers through:
- Email: your-email@example.com
- GitHub: Open a private issue

All reports will be handled confidentially.

---

## Questions?

If you have questions about contributing:

1. Check existing documentation
2. Search closed issues
3. Open a new issue with the `question` label
4. Join our Discord community

---

## Recognition

Contributors are recognized in:
- The project README
- Release notes
- Our Hall of Fame (coming soon)

Thank you for helping make TubeFlow better.
