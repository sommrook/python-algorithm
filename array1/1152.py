S = input()

S = S.strip()

if S:
    words = S.split(" ")
    print(len(words))
else:
    print(0)
