result = {}
while True:
    n = int(input())
    if n == -1:
        break
    temp = []
    for i in range(1, n):
        if n % i == 0:
            temp.append(i)
    result[n] = temp

for i in result:
    if sum(result[i]) == i:
        transform = " + ".join(map(str, result[i]))
        print(f"{i} = {transform}")
    else:
        print(f"{i} is NOT perfect.")