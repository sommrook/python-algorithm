B, N = input().split()
N = int(N)

maxL = len(B)-1
output = 0
for b in B:
    result = (ord(b) - 55) if ord(b) >= 65 else int(b)
    output += N**maxL*result
    maxL -= 1

print(output)