T = int(input())

for _ in range(T):
    S = input()
    flag = 0
    score = 0
    for s in S:
        if s == "O":
            flag += 1
        else:
            flag = 0
        score += flag
    print(score)