import copy

N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

max_num = 0

def dfs(count, arr):
    global max_num

    # print(f"graph => {arr}")

    if count == 5:
        max_value = max(map(max, arr))
        max_num = max(max_num, max_value)
        return 0
    else:
        for i in ('l', 'r', 't', 'b'):
            now_graph = copy.deepcopy(arr)
            for r in range(N):
                # l => 0, 1, 2, 3
                # r => 3, 2, 1, 0
                result = []
                before = -1
                for c in range(N):
                    if i == 'l':
                        n = r
                        m = c
                    elif i == 'r':
                        n = r
                        m = N - 1 - c
                    elif i == 't':
                        n = c
                        m = r
                    else:
                        n = N - 1 - c
                        m = r

                    if arr[n][m] == 0:
                        continue
                    else:
                        if before != -1:
                            if arr[n][m] == before:
                                result.pop()
                                result.append(arr[n][m] * 2)
                                before = -1
                            else:
                                result.append(arr[n][m])
                                before = arr[n][m]
                        else:
                            result.append(arr[n][m])
                            before = arr[n][m]
                if i == 'l':
                    # graph[r] = result + [0] * (N - len(result))
                    now_graph[r] = result + [0] * (N - len(result))
                elif i == 'r':
                    result.reverse()
                    # graph[r] = [0] * (N - len(result)) + result
                    now_graph[r] = [0] * (N - len(result)) + result
                elif i == 't':
                    for num in range(N):
                        if num > len(result)-1:
                            now_graph[num][r] = 0
                            # graph[num][r] = 0
                        else:
                            now_graph[num][r] = result[num]
                            # graph[num][r] = result[num]
                else:
                    for num in range(N):
                        if num > len(result)-1:
                            now_graph[N-1-num][r] = 0
                            # graph[N-1-num][r] = 0
                        else:
                            now_graph[N-1-num][r] = result[num]
                            # graph[N-1-num][r] = result[num]
            dfs(count + 1, now_graph)
    return 0


dfs(0, graph)
print(max_num)