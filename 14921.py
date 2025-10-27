N = int(input())
arr = list(map(int, input().split()))
arr.sort()

end = N-1
start = 0
result = float('inf')
ab = [arr[start], arr[end]]

while start < end:
    sum_num = arr[start]+arr[end]
    if abs(sum_num) < abs(result):
        result = sum_num
        ab = [arr[start], arr[end]]

    if sum_num == 0:
        break

    if arr[start] + arr[end] > 0:
        end -= 1

    elif arr[start] + arr[end] < 0:
        start += 1


print(result)
