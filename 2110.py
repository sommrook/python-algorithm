N, C = map(int, input().split())

house = []
for _ in range(N):
    house.append(int(input()))
house.sort()

start = 1
end = house[-1] - house[0]
middle = (end - start) // 2