from copy import deepcopy

# input().split() : list
# map 안의 2번째 파라미터에 list를 넣어준다. (list 뿐만 아니라 반복 가능한 객체는 다 가능 하다)
# for문을 사용 하는 반복문 대신 사용 가능 하다.
N, kim, im = map(int, input().split())

arr = [0] * N

arr[kim-1] = 1
arr[im-1] = 2

def get_round(ton):
    cnt = 1
    while ton:
        num = len(ton)//2
        temp = []
        for i in range(num):
            if ton[2*i] == 1 or ton[2*i] == 2:
                if ton[2*i+1] == 2 or ton[2*i+1] == 1:
                    return cnt
                else:
                    temp.append(ton[2*i])
            else:
                if ton[2*i+1] == 2 or ton[2*i+1] == 1:
                    temp.append(ton[2*i+1])
                else:
                    temp.append(0)
        cnt += 1
        if len(ton) % 2 == 1:
            temp.append(ton[len(ton)-1])
        ton = deepcopy(temp)

print(get_round(arr))