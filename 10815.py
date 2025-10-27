import sys
input = sys.stdin.readline

N = int(input())
cards = sorted(list(map(int, input().split())))
M = int(input())
nums = list(map(int, input().split()))

for num in nums:
    low, high = 0, N-1
    exist = False
    while low <= high:
        mid = (low+high) // 2
        if cards[mid] > num:
            high = mid - 1
        elif cards[mid] < num:
            low = mid + 1
        else:
            exist = True
            break
    print(1 if exist else 0, end=' ')
