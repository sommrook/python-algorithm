N = int(input())
weights = [int(input()) for _ in range(N)]
weights.sort(reverse=True)

max_weight = weights[0]
for i, weight in enumerate(weights):
    if max_weight < weight * (i+1):
        max_weight = weight * (i+1)

print(max_weight)