N = int(input())
arr = [input() for _ in range(N)]

count = 0
for n in arr:
    alpha = []
    before = ""
    for i in n:
        if i not in alpha:
            before = i
            alpha.append(i)
        else:
            if before != i:
                count += 1
                break

print(N-count)