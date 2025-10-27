A, B = input().split()

answer = []
for i in range(len(B) - len(A) + 1):
    count = 0
    for j in range(len(A)):
        if A[j] != B[i+j]:
            count += 1
    answer.append(count)

print(min(answer))