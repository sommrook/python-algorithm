N = int(input())
people = list(map(int, input().split()))
people.sort()

times = []
cnt = 0
for p in people:
    cnt += p
    times.append(cnt)

print(sum(times))