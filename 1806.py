N, S = map(int, input().split())
arr = list(map(int, input().split()))

current_sum = 0
start = 0
end = -1

for n in range(0, N):
    if current_sum + arr[n] >= S:
        current_sum += arr[n]
        end = n
        break
    else:
        current_sum += arr[n]

if end == -1:
    print(0)
else:
    min_length = end - start + 1

    # print("========while===========")
    while end < N:
        # print("start, end position: ", start, end)
        # print("min_length: ", min_length)
        # print("current_sum: ", current_sum)

        if current_sum - arr[start] >= S:
            current_sum = current_sum - arr[start]
            start += 1
        else:
            if end + 1 < N:
                current_sum = current_sum + arr[end+1]
                end += 1
            else:
                break
        min_length = min(min_length, end - start + 1)

    print(min_length)