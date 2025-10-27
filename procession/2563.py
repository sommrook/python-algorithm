N = int(input())

drawing = [[0 for _ in range(100)] for _ in range(100)]

for i in range(N):
    x, y = map(int, input().split())
    for xi in range(x, x+10):
        for yi in range(y, y+10):
            drawing[xi][yi] = 1

result = 0
for d in drawing:
    result += d.count(1)


print(result)