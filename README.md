Atlas: a tool that tells you where you left off.

## What it does

Atlas is a command-line tool that reads a project's git history and answers:
- What changed since I last checked in?
- Where did I leave off — which file should I look at first?
- Detects and handles running outside a git repository, or in one with
  zero commits — clear message instead of a crash or false "nothing new."
- Fixed a bug where commit messages containing `|` were silently truncated.
- Fixed pluralization ("1 commit" vs "3 commits").
- Atlas can now be run as a plain `atlas` command instead of `python3 atlas.py`.
- Stress-tested against: filenames with spaces, empty commits, multi-line
  commit messages, real merge commits, emoji in commit messages, and
  300+ commits in one repo (all handled correctly, sub-second speed).

It remembers your last checkpoint automatically (no manual date entry needed),
using a hidden checkpoint file stored inside the project's own `.git/` folder.

## Example output

First time using Atlas here - showing your full history:
  • 6 commits
  • Most recent: "1.5.hades.c"
  • Where to start: 1.5.c (6 recent commits)

## Known limitations

- "Where to start" is based on raw commit frequency per file — it can point
  at a frequently-touched file for boring reasons, not just unfinished work.
- Nested git repositories (a `.git` folder inside another tracked folder)
  aren't fully supported yet — Atlas should be run from inside the actual
  repo you want a summary for.
- Only tracks a single user's own commits in a single repo — no
  multi-contributor / team summary support yet (planned future work).

