from collections import deque

N = int(input())

# 순서가 있는 경우의 수임!
numbers = []
for _ in range(N):
    numbers.append(int(input()))


queue = deque()
count = 0
def bfs():
    global count
    while queue:
        result, target = queue.popleft()
        if result == target:
            count += 1
            continue
        if result+3 <= target:
            queue.append((result+3, target))
        if result+2 <= target:
            queue.append((result+2, target))
        queue.append((result+1, target))


if __name__ == '__main__':
    for n in numbers:
        if n == 1:
            print(1)
            continue
        if n == 2:
            print(2)
            continue
        queue.append((1, n))
        queue.append((2, n))
        queue.append((3, n))
        bfs()
        print(count)
        count = 0