import subprocess
result = subprocess.run(
["git", "log", "--pretty=format:%H|%ad|%s", "--date=short"],
capture_output=True, 
text=True
)
print(result.stdout)

