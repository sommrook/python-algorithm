N, B = map(int, input().split())

arr = []

share = N
while True:
    share, remainder = share // B, share % B
    arr.append(remainder)
    if share == 0:
        break
arr.reverse()

for a in arr:
    if a >= 10:
        print(chr(a+55), end="")
    else:
        print(a, end="")