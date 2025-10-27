N = int(input())
K = int(input())
sensor = list(map(int, input().split()))
sensor.sort()

interval = []
for i in range(N-1):
    interval += [sensor[i+1] - sensor[i]]
interval.sort()

print(sum(interval[:N-K]))