import subprocess
import datetime
try:
    with open(".git/atlas_checkpoint", "r") as f:
        cutoff_date = f.read().strip()
except FileNotFoundError:
     cutoff_date = "2000-01-01"

result = subprocess.run(
    ["git", "log", "--pretty=format:==COMMIT==%n%H|%ad|%s", "--name-only", "--date=short"],
    capture_output=True,
    text=True
)

blocks = result.stdout.strip().split("==COMMIT==")

commits = []
for block in blocks:
    block = block.strip()
    if block == "":
         continue
    block_lines = block.split("\n")
    header = block_lines[0]
    parts = header.split("|")

    files = block_lines[1:]

    commit = {
        "hash": parts[0],
        "date": parts[1],
        "message": parts[2],
        "files": files
    }
    commits.append(commit)

recent_commits = []
for commit in commits:
    if commit["date"] >= cutoff_date:
        recent_commits.append(commit)

commit_count = len(recent_commits)

print(f"Since {cutoff_date}:")
print(f"  • {commit_count} commits")

if commit_count > 0:
   most_recent = recent_commits[0]
   print(f"  • Most recent: \"{most_recent['message']}\"")
else:
    print(f"  • Nothing new. You're all caught up!")

today = datetime.date.today().isoformat()
with open(".git/atlas_checkpoint", "w") as f:
     f.write(today)
