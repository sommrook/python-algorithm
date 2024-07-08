N, M = map(int, input().split())

arr1 = [list(map(int, input().split())) for _ in range(N)]
arr2 = [list(map(int, input().split())) for _ in range(N)]

for a, b in zip(arr1, arr2):
    temp = []
    for i, j in zip(a, b):
        temp.append(f"{i+j}")
    print(" ".join(temp))