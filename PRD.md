# Ralph Wiggum - Product Requirements Document

Ralph Wiggum is an automation script that uses Claude Code to work through tasks defined in this document.

---

## In Progress

(none)

---

## In Review

- build a small python script that uses inline uv dependencies for def fibonacci(n) which returns the nth fibonacci number, 0-indexed

---

## Planned

- I currently never see this conditional in ralph-wiggum execute: if [["$result" == *"<promise>COMPLETE</promise>"*]]; then. Look into why that might be.

---

## Completed

- Add loop around claude call (hardcoded to 1 iteration)
- Add shell.nix file with `gum` from charm.sh and enhance ralph-wiggum script with gum features for nicer output
- Allow an argument to be passed to `ralph-wiggum` such that `ralph-wiggum 5` will run 5 iterations of the loop. Otherwise, if no argument is passed, default to 1 loop as it is now.
