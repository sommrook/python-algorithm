N = int(input())

arr = []
while True:
    if N == 1:
        break
    temp = 0
    for i in range(2, N):
        if N % i == 0:
            N = int(N / i)
            temp = 1
            arr.append(i)
            break
    if temp == 0:
        arr.append(N)
        break

for i in arr:
    print(i)