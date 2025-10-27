T = int(input())
coin = [25, 10, 5, 1]

qu = [int(input()) for _ in range(T)]

for q in qu:
    N = q
    result = []
    for c in coin:
        result.append(f"{N//c}")
        N = N % c
    print(" ".join(result))