import sys

S = input()
T = input()


# def bfs(max_c):
#     # 메모리 초과
#     while queue:
#         now = queue.popleft()
#         if now == T:
#             return 1
#         if len(now) > max_c:
#             return 0
#         queue.append(f"{now}A")
#         queue.append(f"{now}B"[::-1])
#     return 0


def dfs(_s):
    """
    T에서 S로
    1. 맨뒤에 A가 있다면 맨뒤 A제거
    2. 맨앞에 B가 있으면 B제거 후 문자열 뒤집기
    """
    if _s == S:
        print(1)
        sys.exit()
    elif len(_s) <= len(S):
        return 0
    else:
        if _s.endswith('A'):
            dfs(_s[:-1])
        if _s.startswith('B'):
            dfs(_s[1:][::-1])
    return 0


dfs(T)
print(0)