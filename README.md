![Ralph Wiggum](header-image.jpg)

# ralph-wiggum

> "I'm helping!"

Processes GitHub issues with Claude Code, creates PRs automatically.

## What it does

1. Fetches open issues from the current repo
2. For each issue, creates a branch and runs Claude Code to implement it
3. If changes are made, commits and creates a PR

## Installation

### As a git submodule (recommended)

```bash
git submodule add https://github.com/neutronmoderator/ralph-wiggum.git .ralph-wiggum
```

Then run with:
```bash
./.ralph-wiggum/ralph-wiggum
```

### Direct copy

```bash
curl -O https://raw.githubusercontent.com/neutronmoderator/ralph-wiggum/main/ralph-wiggum
chmod +x ralph-wiggum
```

## Requirements

- `gh` (GitHub CLI) - authenticated
- `claude` (Claude Code CLI)
- `jq`
- Clean git working directory

## Usage

```bash
./ralph-wiggum
```

That's it. It will process up to 20 open issues.

## Behavior

- Skips issues that already have a branch (`issue-<number>`)
- Creates branches from your default branch
- Auto-commits with message `fix: address issue #<number>`
- Creates PRs that reference the issue with `Closes #<number>`
