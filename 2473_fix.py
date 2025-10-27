import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = float('inf')
ab = [0, 0, 0]

for i in range(N-2):
    start = i + 1
    end = N - 1

    while start < end:
        current_sum = arr[i] + arr[start] + arr[end]

        if abs(current_sum) < result:
            result = abs(current_sum)
            ab = [arr[i], arr[start], arr[end]]

        if current_sum > 0:
            end -= 1
        elif current_sum < 0:
            start += 1
        else:
            # 합이 0이면 바로 종료
            print(f"{arr[i]} {arr[start]} {arr[end]}")
            exit()

print(f"{ab[0]} {ab[1]} {ab[2]}")
