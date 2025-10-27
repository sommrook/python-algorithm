import sys
input = sys.stdin.readline

test_case = int(input())
for _ in range(test_case):
    n = int(input())
    calls = [input().strip() for _ in range(n)]
    calls.sort()
    for i in range(n-1):
        if calls[i] == calls[i+1][:len(calls[i])]:
            print("NO")
            break
    else:
        print("YES")