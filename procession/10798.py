arr = [list(input()) for _ in range(5)]

j = 0
result = ""
while True:
    count = 0
    for i in range(5):
        try:
            result += arr[i][j]
            count += 1
        except IndexError:
            continue
    j += 1
    if count == 0:
        break

print(result)