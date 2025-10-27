N, M = map(int, input().split())

package = 1000
one = 1000
for _ in range(M):
    a, b = map(int, input().split())
    package = min(a, package)
    one = min(b, one)

if package >= one * 6:
    print(one*N)
else:
    a, b = divmod(N, 6)
    print(min(a*package+b*one, (a+1)*package))