# Builds manifest.csv and download scripts from jobs.txt (image index -> url).
ts = open('timestamps.txt').read().split()
rows = [("character_reference.png", "https://d8j0ntlcm91z4.cloudfront.net/user_3Jm4r4CEVOG6YwGUgkdoXfgEE27/hf_20261005_235540_093cf293-8260-46b1-a8c2-8e05c70cbf89.png")]
jobs = {}
for line in open('jobs.txt'):
    if line.strip():
        i, url = line.split()
        jobs[int(i)] = url if url.startswith("http") else "https://d8j0ntlcm91z4.cloudfront.net/user_3Jm4r4CEVOG6YwGUgkdoXfgEE27/" + url
for i in sorted(jobs):
    t = ts[(i - 1) // 2].replace(':', '-')
    rows.append((f"{t}_{(i - 1) % 2 + 1}.png", jobs[i]))
with open('manifest.csv', 'w') as f:
    f.write("filename,url\n")
    f.writelines(f"{n},{u}\n" for n, u in rows)
with open('download_images.ps1', 'w', newline='\r\n') as f:
    f.write("# Right-click > Run with PowerShell. Saves images into a 'images' folder next to this script.\n")
    f.write("$dir = Join-Path $PSScriptRoot 'images'; New-Item -ItemType Directory -Force -Path $dir | Out-Null\n")
    for n, u in rows:
        f.write(f"Invoke-WebRequest -Uri '{u}' -OutFile (Join-Path $dir '{n}')\n")
    f.write("Write-Host 'Done!'; Read-Host 'Press Enter to close'\n")
with open('download_images.sh', 'w') as f:
    f.write("#!/bin/sh\n# Mac/Linux: run 'sh download_images.sh'\nmkdir -p images\n")
    for n, u in rows:
        f.write(f"curl -sSo 'images/{n}' '{u}'\n")
    f.write("echo Done!\n")
print(len(rows) - 1, "scene images;", rows[-1][0])
