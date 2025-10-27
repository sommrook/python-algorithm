N = int(input())
distances = list(map(int, input().split()))
city_prices = list(map(int, input().split()))

i = 0
min_distance = 0
while i < N-1:
    sum_distance = 0
    temp = 0
    sum_distance += distances[i]
    for j in range(i+1, N-1):
        if city_prices[i] >= city_prices[j]:
            break
        else:
            temp += 1
            sum_distance += distances[j]
    min_distance += (sum_distance * city_prices[i])
    i += (temp + 1)

print(min_distance)