# 모두 0인경우를 고려해야한다.

arr = [list(map(int, input().split())) for _ in range(9)]

max_count = 0
position = [-1, -1]
for i in range(0, 9):
    for j in range(0, 9):
        if max_count <= arr[i][j]:
            max_count = arr[i][j]
            position = [i, j]


print(max_count)
print(f"{position[0]+1} {position[1]+1}")