n, m = map(int, input().split())

a = [input() for _ in range(n)]
b = []
for i in range(m):
    append_i = input()
    if append_i in a:
        b.append(append_i)

print(len(b))