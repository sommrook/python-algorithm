N = int(input())

stairs = [int(input()) if i != 0 else 0 for i in range(N+1)]
visitedA = [0] * (N+1)
visitedB = [0] * (N+1)

visitedA[1] = stairs[1]
