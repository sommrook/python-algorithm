T = int(input())

result = 0
arr = []

"""
재귀의 자식이 끝나면 그 전 재귀의 for문으로 (나 말고 다른 자식으로) 돌아간다고 생각하면 된다.
"""

def search(x, _n):
    global result
    for i in (1, 2, 3):
        if i + x == _n:
            result += 1
        elif i + x < _n:
            search(i + x, _n)


for _ in range(T):
    n = int(input())
    result = 0
    search(0, n)
    arr.append(result)


for a in arr:
    print(a)
