N = int(input())
arr = []

for i in range(N):
    age, name = input().split()
    temp = [i, int(age), name]
    arr.append(temp)


arr.sort(key=lambda x: (x[1], x[0]))

for i, age, name in arr:
    print(age, name)