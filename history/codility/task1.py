def solution(N):
    # Implement your solution here
    # binarys = []
    before = -1
    current = 0
    max_n = 0
    while N >= 2:
        n, d = divmod(N, 2)
        if d == 1:
            if before == -1:
                before = current
            else:
                max_n = max(max_n, current-before-1)
                before = current
        current += 1
        if n==1:
            max_n = 0 if before == -1 else max(max_n, current-before-1)
            break
        N = n
    return max_n


print(solution(32))