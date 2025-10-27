import sys

input = sys.stdin.readline

N = int(input())

# 무게
W = []
# 내구성
S = []
for _ in range(N):
    s, w = map(int, input().split())
    S.append(s)
    W.append(w)

max_cnt = 0
def dfs(idx):
    global max_cnt

    if idx == N:
        cnt = 0
        for s in S:
            if s <= 0:
                cnt += 1
        max_cnt = max(cnt, max_cnt)
        return

    if S[idx] <= 0:
        dfs(idx+1)
        return

    broken = False

    for i in range(N):
        if i != idx and S[i] > 0:
            # 계란 부딪히기
            S[idx] = S[idx] - W[i]
            S[i] = S[i] - W[idx]

            broken = True
            dfs(idx+1)

            # 원상 복구
            S[idx] = S[idx] + W[i]
            S[i] = S[i] + W[idx]

    if not broken:
        dfs(idx+1)


dfs(0)
print(max_cnt)