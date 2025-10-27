N = input()

if "0"not in N:
    print("-1")
else:
    sum = 0
    for n in N:
        sum += int(n)
    if sum % 3 != 0:
        print("-1")
    else:
        sortedN = sorted(N, reverse=True)
        print("".join(sortedN))
