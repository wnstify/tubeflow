<#
.SYNOPSIS
    TubeFlow Installer for Windows
.DESCRIPTION
    Interactive setup wizard for TubeFlow YouTube Content System
    Requires PowerShell 5.1+ (Windows PowerShell) or PowerShell 7+ (PowerShell Core)
.NOTES
    Author: TubeFlow Contributors
    License: MIT
#>

#Requires -Version 5.1

param(
    [switch]$SkipPrerequisites,
    [switch]$NonInteractive,
    [string]$ConfigFile
)

$ErrorActionPreference = "Stop"

# Colors and formatting
function Write-ColorOutput {
    param(
        [string]$Message,
        [ConsoleColor]$ForegroundColor = [ConsoleColor]::White
    )
    $fc = $host.UI.RawUI.ForegroundColor
    $host.UI.RawUI.ForegroundColor = $ForegroundColor
    Write-Output $Message
    $host.UI.RawUI.ForegroundColor = $fc
}

function Write-Success { Write-ColorOutput "  [OK] $args" Green }
function Write-Warning { Write-ColorOutput "  [!] $args" Yellow }
function Write-Error { Write-ColorOutput "  [X] $args" Red }
function Write-Info { Write-ColorOutput "  $args" Cyan }

# Script directory
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

# Banner
Write-Host ""
Write-ColorOutput @"
  ████████╗██╗   ██╗██████╗ ███████╗███████╗██╗      ██████╗ ██╗    ██╗
  ╚══██╔══╝██║   ██║██╔══██╗██╔════╝██╔════╝██║     ██╔═══██╗██║    ██║
     ██║   ██║   ██║██████╔╝█████╗  █████╗  ██║     ██║   ██║██║ █╗ ██║
     ██║   ██║   ██║██╔══██╗██╔══╝  ██╔══╝  ██║     ██║   ██║██║███╗██║
     ██║   ╚██████╔╝██████╔╝███████╗██║     ███████╗╚██████╔╝╚███╔███╔╝
     ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝╚═╝     ╚══════╝ ╚═════╝  ╚══╝╚══╝
"@ Cyan

Write-Host ""
Write-Host "  AI-Powered YouTube Content System for Claude Code" -ForegroundColor White
Write-Host ""
Write-Host "===============================================================================" -ForegroundColor Gray
Write-Host ""

# Check prerequisites
if (-not $SkipPrerequisites) {
    Write-Host "Checking prerequisites..." -ForegroundColor Blue
    Write-Host ""

    # Check Claude Code
    $claudeCmd = Get-Command claude -ErrorAction SilentlyContinue
    if ($claudeCmd) {
        try {
            $claudeVersion = & claude --version 2>&1
            Write-Success "Claude Code CLI: $claudeVersion"
        } catch {
            Write-Success "Claude Code CLI: installed"
        }
    } else {
        Write-Error "Claude Code CLI: Not found"
        Write-Host ""
        Write-Warning "Claude Code is required. Install from:"
        Write-Host "    https://claude.ai/claude-code" -ForegroundColor Yellow
        Write-Host ""
        exit 1
    }

    # Check Python
    $pythonCmd = Get-Command python -ErrorAction SilentlyContinue
    if (-not $pythonCmd) {
        $pythonCmd = Get-Command python3 -ErrorAction SilentlyContinue
    }
    if ($pythonCmd) {
        $pythonVersion = & $pythonCmd.Name --version 2>&1
        # Extract version number and check if >= 3.10
        if ($pythonVersion -match "Python (\d+)\.(\d+)") {
            $major = [int]$Matches[1]
            $minor = [int]$Matches[2]
            if ($major -ge 3 -and $minor -ge 10) {
                Write-Success "Python: $pythonVersion"
                $PythonExe = $pythonCmd.Name
            } else {
                Write-Error "Python: $pythonVersion (requires 3.10+)"
                Write-Host ""
                Write-Host "  Python 3.10+ is required. Download from:" -ForegroundColor Yellow
                Write-Host "    https://www.python.org/downloads/" -ForegroundColor Yellow
                exit 1
            }
        }
    } else {
        Write-Error "Python: Not found"
        Write-Host ""
        Write-Host "  Python 3.10+ is required. Download from:" -ForegroundColor Yellow
        Write-Host "    https://www.python.org/downloads/" -ForegroundColor Yellow
        exit 1
    }

    # Check pip
    try {
        & $PythonExe -m pip --version 2>&1 | Out-Null
        Write-Success "pip: Available"
    } catch {
        Write-Warning "pip: Not found (optional but recommended)"
    }

    # Check Git
    $gitCmd = Get-Command git -ErrorAction SilentlyContinue
    if ($gitCmd) {
        $gitVersion = & git --version 2>&1
        Write-Success "Git: $gitVersion"
    } else {
        Write-Warning "Git: Not found (required for sync features)"
    }

    # Check yt-dlp
    $ytdlpCmd = Get-Command yt-dlp -ErrorAction SilentlyContinue
    if ($ytdlpCmd) {
        $ytdlpVersion = & yt-dlp --version 2>&1
        Write-Success "yt-dlp: $ytdlpVersion"
    } else {
        Write-Warning "yt-dlp: Not found (optional, for sync features)"
        Write-Host "      Install with: pip install yt-dlp" -ForegroundColor Gray
    }

    # Check PyYAML
    try {
        & $PythonExe -c "import yaml" 2>&1 | Out-Null
        Write-Success "PyYAML: Available"
    } catch {
        Write-Warning "PyYAML: Not found"
        Write-Host "      Installing PyYAML..." -ForegroundColor Gray
        & $PythonExe -m pip install pyyaml --quiet
    }

    Write-Host ""
    Write-Host "===============================================================================" -ForegroundColor Gray
    Write-Host ""
}

Write-Host "Channel Configuration" -ForegroundColor White
Write-Host ""
Write-Host "Let's set up TubeFlow for your YouTube channel." -ForegroundColor Gray
Write-Host ""

# Channel Identity
Write-Host "Channel Identity" -ForegroundColor Cyan
Write-Host ""

do {
    $CHANNEL_NAME = Read-Host "  Channel name (e.g., TechWithTim)"
    if ([string]::IsNullOrWhiteSpace($CHANNEL_NAME)) {
        Write-Host "  Channel name is required" -ForegroundColor Red
    }
} while ([string]::IsNullOrWhiteSpace($CHANNEL_NAME))

$CHANNEL_HANDLE = Read-Host "  Channel handle (e.g., @techwithtime)"
if (-not $CHANNEL_HANDLE.StartsWith("@")) {
    $CHANNEL_HANDLE = "@$CHANNEL_HANDLE"
}

$CHANNEL_TAGLINE = Read-Host "  Channel tagline (one line)"
if ([string]::IsNullOrWhiteSpace($CHANNEL_TAGLINE)) {
    $CHANNEL_TAGLINE = "Your tagline here"
}

Write-Host ""
Write-Host "Links (Required)" -ForegroundColor Cyan
Write-Host ""

do {
    $DISCORD_URL = Read-Host "  Discord URL"
    if ([string]::IsNullOrWhiteSpace($DISCORD_URL)) {
        Write-Host "  Discord URL is required" -ForegroundColor Red
    }
} while ([string]::IsNullOrWhiteSpace($DISCORD_URL))

do {
    $BUSINESS_URL = Read-Host "  Business/Contact URL"
    if ([string]::IsNullOrWhiteSpace($BUSINESS_URL)) {
        Write-Host "  Business URL is required" -ForegroundColor Red
    }
} while ([string]::IsNullOrWhiteSpace($BUSINESS_URL))

do {
    $GITHUB_ORG = Read-Host "  GitHub Org URL (e.g., https://github.com/yourorg)"
    if ([string]::IsNullOrWhiteSpace($GITHUB_ORG)) {
        Write-Host "  GitHub Org URL is required" -ForegroundColor Red
    }
} while ([string]::IsNullOrWhiteSpace($GITHUB_ORG))

Write-Host ""
Write-Host "Links (Optional - press Enter to skip)" -ForegroundColor Cyan
Write-Host ""

$VOTING_REPO = Read-Host "  Voting Repo URL (for community voting)"
$DOCKER_REPO = Read-Host "  Docker Repo URL (for Docker content)"
$LINKEDIN_URL = Read-Host "  LinkedIn URL"
$FACEBOOK_URL = Read-Host "  Facebook URL"
$TWITTER_URL = Read-Host "  Twitter/X URL"
$REVIEWS_URL = Read-Host "  Reviews URL (Trustpilot, etc.)"
$FEATURED_VIDEO_URL = Read-Host "  Featured Video URL (your flagship video)"
$FEATURED_VIDEO_TITLE = Read-Host "  Featured Video Title"

Write-Host ""
Write-Host "Features" -ForegroundColor Cyan
Write-Host ""

$ENABLE_SYNC = Read-Host "  Enable public repo sync? [Y/n]"
if ([string]::IsNullOrWhiteSpace($ENABLE_SYNC) -or $ENABLE_SYNC -match "^[Yy]") {
    $ENABLE_SYNC = "true"
} else {
    $ENABLE_SYNC = "false"
}

$ENABLE_SOCIAL = Read-Host "  Enable social media workflow? [Y/n]"
if ([string]::IsNullOrWhiteSpace($ENABLE_SOCIAL) -or $ENABLE_SOCIAL -match "^[Yy]") {
    $ENABLE_SOCIAL = "true"
} else {
    $ENABLE_SOCIAL = "false"
}

$ENABLE_RESEARCH = Read-Host "  Enable research agents? [Y/n]"
if ([string]::IsNullOrWhiteSpace($ENABLE_RESEARCH) -or $ENABLE_RESEARCH -match "^[Yy]") {
    $ENABLE_RESEARCH = "true"
} else {
    $ENABLE_RESEARCH = "false"
}

$ENABLE_SPONSORSHIP = Read-Host "  Enable sponsorship research? [Y/n]"
if ([string]::IsNullOrWhiteSpace($ENABLE_SPONSORSHIP) -or $ENABLE_SPONSORSHIP -match "^[Yy]") {
    $ENABLE_SPONSORSHIP = "true"
} else {
    $ENABLE_SPONSORSHIP = "false"
}

$USE_OBSIDIAN = Read-Host "  Using Obsidian? [Y/n]"
if ([string]::IsNullOrWhiteSpace($USE_OBSIDIAN) -or $USE_OBSIDIAN -match "^[Yy]") {
    $USE_OBSIDIAN = "true"
    $STRUCTURE_TYPE = "obsidian"
} else {
    $USE_OBSIDIAN = "false"
    $STRUCTURE_TYPE = "markdown"
}

Write-Host ""
Write-Host "Folder Structure" -ForegroundColor Cyan
Write-Host ""

if ($USE_OBSIDIAN -eq "true") {
    $YOUTUBE_ROOT = Read-Host "  YouTube folder name [03-YouTube]"
    if ([string]::IsNullOrWhiteSpace($YOUTUBE_ROOT)) { $YOUTUBE_ROOT = "03-YouTube" }
    $SOCIAL_ROOT = Read-Host "  Social folder name [04-Social]"
    if ([string]::IsNullOrWhiteSpace($SOCIAL_ROOT)) { $SOCIAL_ROOT = "04-Social" }
    $TEMPLATES_ROOT = Read-Host "  Templates folder name [05-Templates]"
    if ([string]::IsNullOrWhiteSpace($TEMPLATES_ROOT)) { $TEMPLATES_ROOT = "05-Templates" }
} else {
    $YOUTUBE_ROOT = Read-Host "  YouTube folder name [youtube]"
    if ([string]::IsNullOrWhiteSpace($YOUTUBE_ROOT)) { $YOUTUBE_ROOT = "youtube" }
    $SOCIAL_ROOT = Read-Host "  Social folder name [social]"
    if ([string]::IsNullOrWhiteSpace($SOCIAL_ROOT)) { $SOCIAL_ROOT = "social" }
    $TEMPLATES_ROOT = Read-Host "  Templates folder name [templates]"
    if ([string]::IsNullOrWhiteSpace($TEMPLATES_ROOT)) { $TEMPLATES_ROOT = "templates" }
}

Write-Host ""
Write-Host "===============================================================================" -ForegroundColor Gray
Write-Host ""
Write-Host "Generating Configuration..." -ForegroundColor White
Write-Host ""

# Create config.yaml
$configContent = @"
# TubeFlow Configuration
# Generated by install.ps1 on $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")

version: "1.0"

channel:
  name: "$CHANNEL_NAME"
  handle: "$CHANNEL_HANDLE"
  tagline: "$CHANNEL_TAGLINE"
  niche: "self-hosting"

voice:
  style_file: "writing-style.md"
  channel_overview_file: "channel-overview.md"
  tone: "friendly"

structure:
  type: "$STRUCTURE_TYPE"
  youtube_root: "$YOUTUBE_ROOT"
  social_root: "$SOCIAL_ROOT"
  templates_root: "$TEMPLATES_ROOT"
  ideas_folder: "ideas"
  drafts_folder: "drafts"
  published_folder: "published"
  research_folder: "research"

links:
  discord: "$DISCORD_URL"
  business: "$BUSINESS_URL"
  github_org: "$GITHUB_ORG"
  voting_repo: "$VOTING_REPO"
  docker_repo: "$DOCKER_REPO"
  linkedin: "$LINKEDIN_URL"
  facebook: "$FACEBOOK_URL"
  twitter: "$TWITTER_URL"
  reviews: "$REVIEWS_URL"
  featured_video: "$FEATURED_VIDEO_URL"
  featured_video_title: "$FEATURED_VIDEO_TITLE"

features:
  public_repo_sync: $ENABLE_SYNC
  social_media: $ENABLE_SOCIAL
  research_agents: $ENABLE_RESEARCH
  sponsorship_research: $ENABLE_SPONSORSHIP
  obsidian_links: $USE_OBSIDIAN
  include_about_section: true

about:
  company_name: "$CHANNEL_NAME"
  established: "$(Get-Date -Format "yyyy")"
  location: ""
  tagline: "$CHANNEL_TAGLINE"
  application_url: ""

advanced:
  research_model: "haiku"
  strategy_model: "opus"
  content_model: "sonnet"
  parallel_research: true
  auto_publish_prompt: true
"@

$configPath = Join-Path $ScriptDir "config.yaml"
$configContent | Out-File -FilePath $configPath -Encoding UTF8
Write-Success "Created config.yaml"

# Process templates
Write-Host ""
Write-Host "Processing Templates..." -ForegroundColor White
Write-Host ""

$processScript = Join-Path $ScriptDir ".claude\scripts\process_templates.py"
try {
    & $PythonExe $processScript $configPath $ScriptDir
    Write-Success "Templates processed successfully"
} catch {
    Write-Warning "Template processing had warnings (check output above)"
}

# Create voice files if they don't exist
Write-Host ""
Write-Host "Creating Voice Files..." -ForegroundColor White
Write-Host ""

$styleFile = Join-Path $ScriptDir "writing-style.md"
if (-not (Test-Path $styleFile)) {
    $styleContent = @"
# Writing Style Guide

This file defines how content should sound. Customize this to match your voice.

## Tone
- Friendly and approachable
- Direct and clear
- Solution-focused

## Sentence Style
- Short sentences (5-15 words ideal)
- Start with action verbs
- Use questions to engage

## Phrases to Use
- "Here's the thing..."
- "Let me show you."
- "No fluff. Just what works."

## Things to Avoid
- Jargon without explanation
- Filler words
- Overly formal language

## Emoji Usage
- Strategic, not spam
- Use for visual breaks
- Keep professional
"@
    $styleContent | Out-File -FilePath $styleFile -Encoding UTF8
    Write-Success "Created writing-style.md (customize this!)"
} else {
    Write-Warning "writing-style.md already exists"
}

$overviewFile = Join-Path $ScriptDir "channel-overview.md"
if (-not (Test-Path $overviewFile)) {
    $overviewContent = @"
# Channel Overview

## About $CHANNEL_NAME

$CHANNEL_TAGLINE

## Core Values

1. **Value 1** - Description
2. **Value 2** - Description
3. **Value 3** - Description

## Content Focus

- Topic 1
- Topic 2
- Topic 3

## Target Audience

Who watches your content and what do they want to learn?
"@
    $overviewContent | Out-File -FilePath $overviewFile -Encoding UTF8
    Write-Success "Created channel-overview.md (customize this!)"
} else {
    Write-Warning "channel-overview.md already exists"
}

Write-Host ""
Write-Host "===============================================================================" -ForegroundColor Gray
Write-Host ""
Write-Host "Setup Complete!" -ForegroundColor Green
Write-Host ""
Write-Host "Next Steps:" -ForegroundColor White
Write-Host ""
Write-Host "  1. " -NoNewline; Write-Host "Customize your voice:" -ForegroundColor Cyan
Write-Host "     Edit writing-style.md and channel-overview.md"
Write-Host ""
Write-Host "  2. " -NoNewline; Write-Host "Copy to your vault:" -ForegroundColor Cyan
Write-Host "     Copy-Item -Recurse .claude\ C:\path\to\your\vault\.claude\"
Write-Host "     Copy-Item -Recurse templates\ C:\path\to\your\vault\$TEMPLATES_ROOT\"
Write-Host ""
Write-Host "  3. " -NoNewline; Write-Host "Test with a simple command:" -ForegroundColor Cyan
Write-Host "     /youtube idea `"Test Topic`""
Write-Host ""
Write-Host "  4. " -NoNewline; Write-Host "Read the docs:" -ForegroundColor Cyan
Write-Host "     Get-Content docs\GETTING_STARTED.md"
Write-Host ""
Write-Host "Commands Available:" -ForegroundColor White
Write-Host ""
Write-Host "  /youtube idea `"Topic`"      Quick idea capture"
Write-Host "  /youtube full `"Topic`"      Complete draft package"
Write-Host "  /youtube publish `"Topic`"   Move to published"
Write-Host "  /youtube sync              Sync to public repo"
Write-Host "  /youtube-research `"Topic`"  Deep research"
Write-Host "  /social all `"Topic`"        All platforms"
Write-Host ""
Write-Host "===============================================================================" -ForegroundColor Gray
Write-Host ""
