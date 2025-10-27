import heapq

N = int(input())
cards = []
result = 0

for _ in range(N):
    heapq.heappush(cards, int(input()))

total_sum = 0
while len(cards) > 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    sum_value = a + b

    total_sum += sum_value
    heapq.heappush(cards, sum_value)

print(total_sum)