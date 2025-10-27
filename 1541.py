S = input()

calculations = S.split("-")

result = 0
for i, calculation in enumerate(calculations):
    numbers = calculation.split("+")
    temp = sum(map(int, numbers))
    if i == 0:
        result += temp
    else:
        result -= temp

print(result)