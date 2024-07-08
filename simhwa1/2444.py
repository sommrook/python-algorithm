N = int(input())

for i in range(0, N):
    val = ""
    val += " "*(N-1-i)
    val += "*"*(2*i+1)
    print(val)

for i in range(N-2, -1, -1):
    val = ""
    val += " " * (N - 1 - i)
    val += "*" * (2 * i + 1)
    print(val)
