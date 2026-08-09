import subprocess
import datetime
try:
    with open(".git/atlas_checkpoint", "r") as f:
        cutoff_date = f.read().strip()
    first_run = False
except FileNotFoundError:
     cutoff_date = "2000-01-01"
     first_run = True

result = subprocess.run(
    ["git", "log", "--pretty=format:==COMMIT==%n%H|%ad|%s", "--name-only", "--date=short"],
    capture_output=True,
    text=True
)

if result.returncode !=0:
    print("Couldn't read git history here. Make sure this is a git repository with at least one commit.")
    exit()

blocks = result.stdout.strip().split("==COMMIT==")

commits = []
for block in blocks:
    block = block.strip()
    if block == "":
         continue
    block_lines = block.split("\n")
    header = block_lines[0]
    parts = header.split("|", 2)

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

file_counts = {}
for commit in recent_commits:
    for filename in commit["files"]:
        if filename in file_counts:
            file_counts[filename] = file_counts[filename] + 1
        else:
            file_counts[filename] = 1

if file_counts:
    top_file = max(file_counts, key=file_counts.get)
    top_count = file_counts[top_file]

commit_count = len(recent_commits)

if first_run:
    print("First time using Atlas here - showing your full history:")
else:
    print(f"Since {cutoff_date}:")
if commit_count == 1:
    word = "commit"
else:
    word = "commits"

print(f"  • {commit_count} {word}")

if commit_count > 0:
   most_recent = recent_commits[0]
   print(f"  • Most recent: \"{most_recent['message']}\"")
   print(f"  • Where to start: {top_file} ({top_count} recent commits)")
else:
    print(f"  • Nothing new. You're all caught up!")

today = datetime.date.today().isoformat()
with open(".git/atlas_checkpoint", "w") as f:
     f.write(today)
