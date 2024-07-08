from queue import PriorityQueue

N = int(input())

# rooms = deque(sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: (x[1], x[0])))

queue = PriorityQueue(maxsize=200000)

rooms = list(map(int, input().split()))

start = 0
end = 0

room_c = 0

"""
시간 초과
"""
while rooms:
    time = rooms.popleft()
    if end > time[1]:
        start = end = 0
    if start == end == 0:
        start, end = time[0], time[1]
        room_c += 1
    else:
        if end <= time[0]:
            start, end = time[0], time[1]
        else:
            rooms.append(time)

print(room_c)