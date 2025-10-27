N = int(input())

count = 0
while True:
    if N % 5 == 0:
        count += N//5
        break
    if N - 3 >= 0:
        N -= 3
        count += 1
    else:
        count = -1
        break


print(count)