S = input()

zero = 0
one = 0

before = ""
for s in S:
    if before == s:
        continue
    if s == "0":
        zero += 1
    else:
        one += 1
    before = s

print(min(zero, one))