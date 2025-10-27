n = int(input())
arr = list(map(int, input().split()))
x = int(input())
arr.sort()

start = 0
end = n-1

answer = 0
while 0 <= start < end < n:
    result = arr[start] + arr[end]
    if result >= x:
        end -= 1
        if result == x:
            answer += 1
    else:
        start += 1

print(answer)