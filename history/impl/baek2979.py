A, B, C = map(int, input().split())

arr = []
for _ in range(3):
    arr.append(list(map(int, input().split())))

minS = min(arr[0][0], arr[1][0], arr[2][0])
maxE = max(arr[0][1], arr[1][1], arr[2][1])


price = 0
for current in range(minS, maxE):
    count = 0
    for truck in arr:
        if truck[0] <= current < truck[1]:
            count += 1

    if count == 1:
        price += A
    elif count == 2:
        price += 2*B
    elif count == 3:
        price += 3*C

print(price)
