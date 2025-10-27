N = int(input())

# 다 5만 사용하거나, 다 3만 사용하거나, 5와 3을 섞어서 사용
def pack_calculation(n):
    pack_count = 0
    while True:
        if n < 0:
            print(-1)
            break
        if n % 5 == 0:
            pack_count += (n//5)
            print(pack_count)
            break
        n -= 3
        pack_count += 1


if __name__ == '__main__':
    pack_calculation(N)