N = int(input())

count = 1
while True:
    if N - count <= 0:
        break
    N = N - count
    count += 1

if count % 2 == 0:
    print(f"{N}/{count+1-N}")
else:
    print(f"{count+1-N}/{N}")
