N = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(arr)

end = N-1
start = 0
middle = (start+end)//2

result = float('inf')
ab = [arr[start], arr[middle], arr[end]]
before_middle = None

while start < middle < end:
    print('=================')
    print(arr[start], arr[middle], arr[end])
    print(result)

    if arr[start] + arr[middle] + arr[end] > 0:
        print("PP")
        before_sum = float('inf')
        while start < middle < end:

            current_sum = arr[start] + arr[middle] + arr[end]

            if before_sum < abs(arr[start] + arr[middle] + arr[end]):
                break

            if abs(current_sum) < result:
                result = abs(current_sum)
                ab = [arr[start], arr[middle], arr[end]]

            before_sum = current_sum
            middle -= 1

        if before_sum == 0:
            break

        end -= 1
        middle = (start + end) // 2

    elif arr[start] + arr[middle] + arr[end] < 0:
        print("MM")
        before_sum = float('inf')
        while start < middle < end:
            current_sum = abs(arr[start] + arr[middle] + arr[end])
            if before_sum < abs(arr[start] + arr[middle] + arr[end]):
                break

            if abs(current_sum) < result:
                result = abs(current_sum)
                ab = [arr[start], arr[middle], arr[end]]

            before_sum = current_sum
            middle += 1

        if before_sum == 0:
            break

        start += 1
        middle = (start + end) // 2

    # 0일 때
    else:
        result = 0
        ab = [arr[start], arr[middle], arr[end]]
        break


print(f"{ab[0]} {ab[1]} {ab[2]}")