arr = [list(input().split()) for _ in range(20)]

score = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
exclude_score = 'P'

count = 0
multiple = 0
for obj in arr:
    if obj[2] == exclude_score:
        continue
    count += float(obj[1])
    multiple += float(obj[1]) * score[obj[2]]

result = round(multiple/count, 6)
print('{:.6f}'.format(result))