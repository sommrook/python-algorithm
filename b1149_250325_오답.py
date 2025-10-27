"""
오답인 이유
해당 문제 풀이를 하려면, 각 색별로 이전 가격의 최솟값 + 각 색 (총3개)의 경우의수를 구한 후 3개중 최솟값을 구해야한다.

하지만 내가 푼 풀이는, 현재의 값에 다음값들의 최솟값을 구하는식으로 했는데, 그렇게 하게되면 최솟값을 구할수가 없다.
반례)
현재: 30 (빨)
다음: 빨 20 / 파 10 / 초 40
다다음: 빨 50 / 파 5 / 초 90

내 방식: 30 + 10 + 50 = 90
답: 30 + 40 + 5 = 75

최솟값의 기준을 다음으로 두는게 아니라 이전값에 두어야한다. (어차피 지금 나 자신은 고정이기 때문)

점화식
i) n-1 가 빨간색
f(n) = min(f(n-1)+초 가격, f(n-1)+파 가격)
"""

from collections import deque

N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

dx = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1]
}
queue = deque()
min_price = N * 1000
def bfs():
    global queue, min_price
    while queue:
        i, j, price = queue.popleft()
        if i == N - 1:
            min_price = min(min_price, price)
            continue
        if i < N-1:
            # for x in dx[j]:
            #     queue.append((i+1, x, price+arr[i+1][x]))
            if arr[i+1][dx[j][0]] > arr[i+1][dx[j][1]]:
                queue.append((i + 1, dx[j][1], price + arr[i+1][dx[j][1]]))
            else:
                queue.append((i + 1, dx[j][0], price + arr[i + 1][dx[j][0]]))


if __name__ == '__main__':
    queue.append((0, 0, arr[0][0]))
    queue.append((0, 1, arr[0][1]))
    queue.append((0, 2, arr[0][2]))
    bfs()
    print(min_price)