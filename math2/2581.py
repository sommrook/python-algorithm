M = int(input())
N = int(input())

min_prime = -1
sum_prime = 0
for i in range(M, N+1):
    temp = 0
    for j in range(1, i+1):
        if i % j == 0:
            temp += 1
    if temp == 2:
        sum_prime += i
        if min_prime == -1:
            min_prime = i

if min_prime == -1:
    print(-1)
else:
    print(sum_prime)
    print(min_prime)


# prime = []
# for i in range(M, N + 1):
#     check = 0
#     for j in range(2, int(i ** 0.5) + 1):
#         if i % j == 0:
#             check = 1
#             break
#     if check == 0:
#         prime.append(i)
#
# if prime and prime[0] == 1:
#     prime.pop(0)
# print(sum(prime)) if prime else print(-1)
# if prime:
#     print(prime[0])


"""
소수는 나자신과 1만 약수로 가지는것
2부터 (나 자신의 1/2 + 1)에 어떠한 약수도 가지고 있지 않으면 소수로 판단할 수 있다.
2를 약수로 가지고 있다면 나 자신의 1/2가 약수가 된다.
3을 약수로 가지고 있다면 나 자신의 1/3가 약수가 된다.
이처럼 2를 약수로 가지고 있을 때 상대 약수값(나 자신의 1/2)가 가장 큰 값이 된다.
"""