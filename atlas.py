import subprocess
result = subprocess.run(
["git", "log", "--pretty=format:%H|%ad|%s", "--date=short"],
capture_output=True, 
text=True
)
lines = result.stdout.strip().split("\n")
commits = []
for line in lines:
    parts = line.split("|")
    commit = {
        "hash": parts[0],
        "date": parts[1],
        "message": parts[2]
    }
    commits.append(commit)
print(commits)
