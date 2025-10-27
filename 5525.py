N = int(input())
M = int(input())
S = input()

P = f"I" + f"OI" * N

cnt = 0
temp_s = S
while True:
    index = temp_s.find(P)
    if index == -1:
        break
    cnt += 1
    if index + 1 == len(temp_s):
        break
    temp_s = temp_s[index+1:]


print(cnt)

