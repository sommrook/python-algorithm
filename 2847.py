N = int(input())

arr = [int(input()) for _ in range(N)]

result = 0
for i in range(N-2, -1, -1):
    if arr[i] >= arr[i+1]:
        result += arr[i]-arr[i+1]+1
        arr[i] = arr[i+1]-1

print(result)