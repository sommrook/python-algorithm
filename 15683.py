import copy

N, M = map(int, input().split())
cctv = []
graph = []

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]]
]


for n in range(N):
    data = list(map(int, input().split()))
    graph.append(data)
    for m in range(M):
        if data[m] in [1, 2, 3, 4, 5]:
            cctv.append([data[m], n, m])


def fill(board, mm, x, y):
    """
    :param board: 그릴 리스트
    :param mm: dx, dy를 활용할 mode의 리스트
    :param x: cctv가 있는 x좌표
    :param y: cctv가 있는 y좌표
    :return:
    """
    for i in mm:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                break
            if board[nx][ny] == 6:
                break
            elif board[nx][ny] == 0:
                board[nx][ny] = 7


def dfs(depth, arr):
    """
    :param depth: cctv를 몇개째 조사하고 있는가?
    :param arr: 그리고 있는 리스트
    :return:
    """
    global min_value

    if depth == len(cctv):
        count = 0
        for n in range(N):
            count += arr[n].count(0)
        min_value = min(min_value, count)
        return
    temp = copy.deepcopy(arr)
    cctv_num, x, y = cctv[depth]
    for i in mode[cctv_num]:
        fill(temp, i, x, y)
        dfs(depth+1, temp)
        temp = copy.deepcopy(arr)


min_value = int(1e9)
dfs(0, graph)
print(min_value)