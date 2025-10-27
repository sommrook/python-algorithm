n, m = map(int, input().split())

painting = []
for _ in range(n):
    painting.append(list(map(int, input().split())))
search = [[0 for _ in range(m)] for _ in range(n)]

print(painting)
print(search)