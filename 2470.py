N = int(input())
arr = list(map(int, input().split()))
arr.sort()

end = N-1
start = 0
result = float('inf')
ab = [arr[start], arr[end]]

while start < end:
    sum_num = abs(arr[start]+arr[end])
    if result > sum_num:
        ab = [arr[start], arr[end]]
        result = sum_num

    if sum_num == 0:
        break

    # 양수이면
    if arr[start]+arr[end] > 0:
        end -= 1

    # 음수이면
    elif arr[start]+arr[end] < 0:
        start += 1


print(f"{ab[0]} {ab[1]}")