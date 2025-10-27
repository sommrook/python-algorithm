N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]

meetings.sort(key=lambda x: (x[1], x[0]))


count = 0
last_start = 0
last_end = 0

for meeting in meetings:
    if last_end <= meeting[0]:
        count += 1
        last_start = meeting[0]
        last_end = meeting[1]

print(count)