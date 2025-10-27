S = input()
s = input()

i = 0
count = 0
while True:
    index = S.find(s, i)
    if index != -1:
        count += 1
        i = index + len(s)
    else:
        break


print(count)