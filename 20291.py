N = int(input())

files = {}
for _ in range(N):
    s = input()
    arr = s.rsplit(".")
    if arr[1] not in files:
        files[arr[1]] = 1
    else:
        files[arr[1]] += 1


files = sorted(files.items())

for file, count in files:
    print(f"{file} {count}")