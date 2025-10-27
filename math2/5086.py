result = []
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    if n > m:
        if n % m == 0:
            result.append("multiple")
        else:
            result.append("neither")
    else:
        if m % n == 0:
            result.append("factor")
        else:
            result.append("neither")

for i in result:
    print(i)