import subprocess
result = subprocess.run(["git", "log"], capture_output=True, text=True)
print(result.stdout)

