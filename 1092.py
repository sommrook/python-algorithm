import sys
input = sys.stdin.readline

N = int(input())
cranes = list(map(int, input().split()))
cranes.sort(reverse=True)

M = int(input())
boxes = list(map(int, input().split()))
boxes.sort(reverse=True)

result = 0
## 이부분 누락했었음
if boxes[0] > cranes[0]:
    result = -1
else:
    while boxes:
        result += 1
        for c in cranes:
            # crain중에 이제 더이상 box에 있는것을 옮기지 못할 경우
            ## 이부분 누락했었음
            if boxes and c < boxes[-1]:
                continue
            for b in boxes:
                if b <= c:
                    boxes.remove(b)
                    break

print(result)