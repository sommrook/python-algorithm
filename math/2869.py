A, B, V = map(int, input().split())

count = 1
high = V - A
one_night = A - B

count = count + (high//one_night)
if high % one_night != 0:
    count += 1
print(count)