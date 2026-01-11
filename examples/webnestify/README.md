# Webnestify Example

This is a production configuration from the [@webnestify](https://youtube.com/@webnestify) YouTube channel.

## About This Example

Webnestify is a YouTube channel focused on:
- Self-hosting tutorials
- Docker guides
- Cloud solutions
- Security and privacy

This configuration demonstrates a mature TubeFlow setup with:
- All features enabled
- Complete link configuration
- Custom video categories
- Obsidian-style folder structure

## What's Included

| File | Description |
|------|-------------|
| `config.yaml` | Complete production configuration |

## Key Features Used

### Community Voting
The `voting_repo` is set to a public GitHub repository where viewers can:
- Vote on upcoming video topics via GitHub Issues
- See the video roadmap
- Request new content

### Public Repo Sync
With `public_repo_sync: true`, published videos are automatically synced to a public repository with:
- README files for each video (full YouTube description)
- VIDEOS.md catalog organized by category
- Automatic roadmap issue closing

### Research Agents
All 5 research agents are enabled for comprehensive topic research before content creation.

### Sponsorship Research
Automatically finds and includes:
- FUNDING.yml links
- GitHub Sponsors pages
- Open Collective links

## Using This Example

1. **Copy the config:**
   ```bash
   cp examples/webnestify/config.yaml config.yaml
   ```

2. **Edit for your channel:**
   - Replace all URLs with your own
   - Update channel name and handle
   - Customize the about section

3. **Process templates:**
   ```bash
   python .claude/scripts/process_templates.py config.yaml .
   ```

## Live Channel

- YouTube: https://youtube.com/@webnestify
- GitHub: https://github.com/wnstify
- Video Repository: https://github.com/wnstify/wn-youtube

## Statistics

As of January 2026:
- 129 published videos
- 119 roadmap ideas
- 118 voting issues
- Active community engagement
