import math

T = int(input())

test_cases = []

for _ in range(T):
    test_cases.append(list(map(int, input().split())))


for test_case in test_cases:
    print(math.comb(test_case[1], test_case[0]))