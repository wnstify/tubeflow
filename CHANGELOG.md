# Changelog

All notable changes to TubeFlow will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added
- Windows PowerShell installer (`install.ps1`) for full Windows support
- GitHub issue templates (bug report, feature request)
- GitHub pull request template
- CHANGELOG.md following Keep a Changelog format
- Comprehensive USP and market position section in README.md
- Competitive analysis with existing tools (ShortGPT, text2youtube, etc.)
- "By the Numbers" quick reference section
- Author section with Simon's bio and featured content
- About Webnestify company section with ASCII logo
- Complete social links table (Website, YouTube, Discord, GitHub, LinkedIn, Twitter, Facebook, Trustpilot)
- GitHub repositories showcase
- Business contact and application links
- GitHub Actions release workflow with SHA256 checksums and build attestation

### Changed
- Updated Python requirement from 3.8+ to 3.10+ (yt-dlp compatibility)
- Updated PyYAML recommendation to 6.0.3
- Updated yt-dlp recommendation to 2025.12+
- Improved install.sh with better POSIX compatibility and version checking

### Deprecated
- Nothing yet

### Removed
- Nothing yet

### Fixed
- Nothing yet

### Security
- Nothing yet

---

## [1.0.0] - 2026-01-11

### Added

#### Core System
- Initial release of TubeFlow
- MIT License for open-source distribution
- Cross-platform support (macOS, Linux, Windows, WSL2)
- Interactive installation wizard (`install.sh` for Unix, `install.ps1` for Windows)
- Template variable processing system (`process_templates.py`)
- Example configuration for reference (`examples/webnestify/`)

#### Agents (9 total)
- `youtube-creator.md` - Creates video scripts, ideas, descriptions, full packages
- `youtube-publisher.md` - Handles post-upload workflow, metadata extraction
- `youtube-syncer.md` - Syncs published videos to public GitHub repository
- `yt-topic-gatherer.md` - Deep research into subject matter, features, docs
- `yt-competitor-gatherer.md` - Analyzes existing YouTube videos, finds gaps
- `yt-seo-gatherer.md` - Researches keywords, trends, optimal titles
- `yt-community-gatherer.md` - Researches Reddit, forums, community questions
- `yt-research-strategist.md` - Synthesizes all research into strategic recommendations
- `social-creator.md` - Creates LinkedIn, Twitter, Facebook posts

#### Commands (3 total)
- `/youtube` - Main YouTube workflow (idea, full, publish, sync)
- `/youtube-research` - Comprehensive 5-agent research workflow
- `/social` - Social media content creation (linkedin, twitter, facebook, all, video)

#### Skills (3 total)
- `youtube-workflow` - YouTube content creation skill
- `youtube-research` - Research methodology skill
- `social-workflow` - Social media posting skill

#### Scripts (5 total)
- `process_templates.py` - Variable replacement engine for templatization
- `sync_videos.py` - Public repository synchronization automation
- `create_issues.py` - GitHub roadmap issue creation
- `fetch_descriptions.py` - YouTube description fetching via yt-dlp
- `generate_videos.py` - Video catalog generation for public repo

#### Templates (8 total)
- `youtube-description.md` - SEO-optimized video description template
- `youtube-pinned-comment.md` - Engagement-focused pinned comment template
- `youtube-script.md` - Complete video script structure with visual cues
- `youtube-idea.md` - Quick video idea capture template
- `linkedin-post.md` - Professional LinkedIn post template
- `twitter-post.md` - Punchy Twitter/X post and thread template
- `facebook-post.md` - Community-focused Facebook post template
- `social-content.json` - Structured data template for social posts

#### Documentation (6 total)
- `README.md` - Comprehensive project overview with all components
- `USAGE.md` - Detailed usage guide with examples
- `GETTING_STARTED.md` - Quick start installation guide
- `CONFIGURATION.md` - Complete configuration reference
- `WORKFLOWS.md` - Workflow documentation and diagrams
- `CONTRIBUTING.md` - Contribution guidelines

#### Features
- 24 configurable template variables
- YouTube-native formatting (not Markdown)
- Platform-specific social media optimization
- Automatic open-source project acknowledgment
- FUNDING.yml sponsorship link detection
- Self-hosting topic cross-referencing
- Public GitHub repository synchronization
- Video index tracking (`youtube-index.json`)
- Social posts index tracking (`social-index.json`)
- Obsidian vault integration support
- Category-based automatic video organization

### Configuration Options
- Channel branding (name, handle, tagline, niche)
- Voice/tone settings with style guide integration
- Directory structure customization
- Social media links (Discord, LinkedIn, Facebook, Twitter)
- GitHub integration (org, voting repo, docker repo)
- Feature toggles (research, social, sync, sponsorship)

---

## Version History

| Version | Date | Description |
|---------|------|-------------|
| 1.0.0 | 2026-01-11 | Initial public release |

---

## Upgrade Guide

### Upgrading from Pre-release

If you were using TubeFlow before the official 1.0.0 release:

1. **Backup your config**:
   ```bash
   cp config.yaml config.yaml.backup
   ```

2. **Pull latest changes**:
   ```bash
   git pull origin main
   ```

3. **Compare config changes**:
   ```bash
   diff config.yaml config.example.yaml
   ```

4. **Add any new config options** from `config.example.yaml`

5. **Re-run template processing**:
   ```bash
   python3 .claude/scripts/process_templates.py config.yaml .
   ```

---

## Contributing to Changelog

When contributing to TubeFlow, please update this changelog:

1. Add your changes under `[Unreleased]`
2. Use the appropriate category:
   - **Added** - New features
   - **Changed** - Changes to existing functionality
   - **Deprecated** - Features to be removed in future
   - **Removed** - Removed features
   - **Fixed** - Bug fixes
   - **Security** - Security-related changes

3. Follow the format:
   ```markdown
   - Brief description of change ([#PR_NUMBER](link))
   ```

4. When releasing, maintainers will move unreleased items to a new version section.

---

## Links

- [GitHub Repository](https://github.com/wnstify/tubeflow)
- [Issue Tracker](https://github.com/wnstify/tubeflow/issues)
- [Discussions](https://github.com/wnstify/tubeflow/discussions)

[Unreleased]: https://github.com/wnstify/tubeflow/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/wnstify/tubeflow/releases/tag/v1.0.0
