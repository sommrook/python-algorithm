N, S = map(int, input().split())
arr = list(map(int, input().split()))

current_sum = 0
start = 0
end = 0
min_length = N+1

while end <= N:
    if current_sum >= S:
        min_length = min(min_length, end - start)
        current_sum = current_sum - arr[start]
        start = start+1
    else:
        if end+1 > N:
            break
        current_sum = current_sum + arr[end]
        end = end+1

print(0 if min_length == N+1 else min_length)
