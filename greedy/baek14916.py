N = int(input())

#5, 2
max_c = N // 5
if N >= 5:
    if (N - max_c*5) % 2 == 0:
        charge = max_c + (N - max_c*5) // 2
    else:
        # 홀수 이면, 5를 하나 더해줘서 짝수로 만들어 줘야함
        charge = (max_c - 1) + ((N - (max_c-1)*5) // 2)
else:
    if N % 2 == 0:
        charge = N // 2
    else:
        charge = -1

print(charge)