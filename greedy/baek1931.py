N = int(input())
rooms = [list(map(int, input().split())) for _ in range(N)]

rooms.sort(key=lambda x: (x[1], x[0]))

start = 0
end = 0
count = 0

for room in rooms:
    if count == 0:
        count += 1
        start = room[0]
        end = room[1]
    else:
        if room[0] >= end:
            count += 1
            start = room[0]
            end = room[1]
print(count)
