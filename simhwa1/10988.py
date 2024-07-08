S = input()

# 몫 구하기
count = len(S) // 2

temp = 1
for i in range(0, count):
    if S[i] != S[-i-1]:
        temp = 0
        break

print(temp)
