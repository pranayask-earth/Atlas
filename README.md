Atlas: a tool that tells you where you left off.

## Quickstart

1. Clone this repo:
```
   git clone https://github.com/pranayask-earth/Atlas.git
```
2. Run it from inside any git repository you want a summary for:
```
   python3 /path/to/Atlas/atlas.py
```

(A simpler one-command install is coming soon.)

## Optional: use `atlas` as a short command

If you'd rather type `atlas` instead of the full `python3 ...` command:

```
chmod +x atlas.py
mkdir -p ~/.local/bin
ln -s "$(pwd)/atlas.py" ~/.local/bin/atlas
```

Then add this line to `~/.bashrc` (if it's not already there):

```
export PATH="$HOME/.local/bin:$PATH"
```

Reload it:

```
source ~/.bashrc
```

This is optional — `python3 /path/to/Atlas/atlas.py` always works without it.

## What it does

Atlas reads a project's git history and answers:
- What changed since I last checked in?
- Where did I leave off — which file should I look at first?

It remembers your last checkpoint automatically, using a hidden file stored
inside the project's own `.git/` folder — no manual date entry needed.

## Example output

```
First time using Atlas here - showing your full history:
  • 6 commits
  • Most recent: "1.5.hades.c"
  • Where to start: 1.5.c (6 recent commits)
```

## Changelog highlights

- Handles running outside a git repo, or in one with zero commits, cleanly.
- Fixed commit messages containing `|` being truncated.
- Fixed pluralization ("1 commit" vs "3 commits").
- Summarizes large histories instead of dumping every commit.
- Added a `--help` flag.
- Stress-tested against spaces in filenames, empty commits, multi-line
  messages, real merge commits, emoji, and 300+ commit repos.

## Known limitations

- "Where to start" is based on raw commit frequency — it can point at a
  frequently-touched file for boring reasons, not just unfinished work.
- Nested git repositories aren't fully supported yet.
- Single-user, single-repo only — no team summaries yet.
