input_arr = list(map(int, input().split()))

arr = [1, 1, 2, 2, 2, 8]

for a, b in zip(input_arr, arr):
    # a: 있는 갯수 / b: 원래 기준
    print(b - a, end=' ')