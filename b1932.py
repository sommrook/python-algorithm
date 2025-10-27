N = int(input())

triangle = []
for i in range(N):
    lines = list(map(int, input().split()))
    triangle.append(lines)

sum_drawing = [[0] * N for _ in range(N)]
sum_drawing[0][0] = triangle[0][0]

for i in range(1, N):
    for j in range(0, i+1):
        if j == 0:
            sum_drawing[i][j] = triangle[i][j] + sum_drawing[i-1][j]
        elif j == N-1:
            sum_drawing[i][j] = triangle[i][j] + sum_drawing[i-1][j-1]
        else:
            sum_drawing[i][j] = triangle[i][j] + max(sum_drawing[i-1][j-1], sum_drawing[i-1][j])

print(max(sum_drawing[N-1]))