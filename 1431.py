N = int(input())

def integer_sum(S):
    result = 0
    for s in S:
        if s.isdigit():
            result += int(s)
    return result


arr = []

for i in range(N):
    S = input()
    arr.append(S)

arr.sort(key=lambda x: (len(x), integer_sum(x), x))

for i in arr:
    print(i)