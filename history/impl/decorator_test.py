glo_cnt = [0]
def deco_cnt(func):
    def wrapper(*args):
        return func(*args, glo_cnt)
    return wrapper

@deco_cnt
def DFS(numbers, idx, value, target, cnt):
    if len(numbers)-1 == idx:
        if value == target:
            cnt[0] += 1
        return
    DFS(numbers, idx + 1, value + numbers[idx + 1], target)
    DFS(numbers, idx + 1, value + numbers[idx + 1] * -1, target)


@deco_cnt
def solution(numbers, target, cnt):
    DFS(numbers, 0, numbers[0], target)
    DFS(numbers, 0, numbers[0] * -1, target)
    return cnt[0]


print(solution([1, 1, 1, 1, 1], 3))