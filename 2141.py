N = int(input())

graph = []
people = 0
for _ in range(N):
    x, a = map(int, input().split())
    people += a
    graph.append((x, a))

graph.sort(key=lambda x: x[0])

current_people = 0
for index, peo in graph:
    current_people += peo
    if current_people >= people / 2:
        print(index)
        break