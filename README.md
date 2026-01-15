![Ralph Wiggum](header-image.jpg)

# ralph-wiggum

> "I'm helping!"

Processes GitHub issues with Claude Code, creates PRs automatically.

## What it does

1. Fetches open issues from the current repo
2. For each issue, creates a branch and runs Claude Code to implement it
3. If changes are made, commits and creates a PR

## Installation

### Using the install command (recommended)

From within your target repo, run:

```bash
curl -sL https://raw.githubusercontent.com/neutronmoderator/ralph-wiggum/main/ralph-wiggum | bash -s install
```

This will:
- Add ralph-wiggum as a git submodule at `.ralph-wiggum/`
- Create a wrapper script at the project root

Then commit and run:
```bash
git add -A && git commit -m "Add ralph-wiggum"
./ralph-wiggum
```

### Manual submodule setup

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
./ralph-wiggum          # Process open issues
./ralph-wiggum run      # Same as above
./ralph-wiggum install  # Install as submodule in current repo
./ralph-wiggum help     # Show help
```

Running without arguments processes up to 20 open issues.

## Behavior

- Skips issues that already have a branch (`issue-<number>`)
- Creates branches from your default branch
- Auto-commits with message `fix: address issue #<number>`
- Creates PRs that reference the issue with `Closes #<number>`
