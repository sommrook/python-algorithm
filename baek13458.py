N = int(input())

student = list(map(int, input().split()))

#총감독관, 부감독관
B, C = map(int, input().split())

total = 0
for number in student:
    if number-B > 0:
        if (number-B) % C == 0:
            total += ((number-B) // C) + 1
        else:
            total += ((number-B) // C) + 2
    else:
        total += 1

print(total)