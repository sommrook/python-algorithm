N = int(input())
arr = [int(input()) for _ in range(N)]

def fibonacci(_fibo):
    for _i in range(3, len(_fibo)):
        _fibo[_i] = (_fibo[_i - 1][0] + _fibo[_i - 2][0], _fibo[_i - 1][1] + _fibo[_i - 2][1])


if __name__ == "__main__":
    for i in arr:
        fibo = [(0, 0)] * (i + 1)
        if i == 0:
            print(f"1 0")
        elif i == 1:
            print(f"0 1")
        elif i == 2:
            print(f"1 1")
        else:
            fibo[1] = (0, 1)
            fibo[2] = (1, 1)
            fibonacci(fibo)

            print(f"{fibo[i][0]} {fibo[i][1]}")
