N = int(input())

n = 1
result = 1
while True:
    result += (n-1)*6
    if result >= N:
        print(n)
        break
    n += 1