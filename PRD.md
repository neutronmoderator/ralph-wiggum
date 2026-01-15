# Ralph Wiggum - Product Requirements Document

Ralph Wiggum is an automation script that uses Claude Code to work through tasks defined in this document.

---

## In Progress

(none)

---

## In Review

- Allow an argument to be passed to `ralph-wiggum` such that `ralph-wiggum 5` will run 5 iterations of the loop. Otherwise, if no argument is passed, default to 1 loop as it is now.

---

## Planned

- I currently don't see any gum spinner when running the script, I think some output is swallowed by the claude call. Can you take a look and figure out how to make the `gum spin` work:

╔════════════════╗
║ ║
║ ralph-wiggum ║
║ I'm helping! ║
║ ║
╚════════════════╝
=== Iteration 1 of 1 ===
Done. Implemented iteration count argument support:

- **Change**: `MAX_ITERATIONS=${1:-1}` - accepts optional arg, defaults to 1
- **Usage**: `ralph-wiggum` (1 iteration) or `ralph-wiggum 5` (5 iterations)
- **Committed**: `401f469`
- **PRD updated**: Feature moved to "In Review"

End (max iterations reached)

---

## Completed

- Add loop around claude call (hardcoded to 1 iteration)
- Add shell.nix file with `gum` from charm.sh and enhance ralph-wiggum script with gum features for nicer output
