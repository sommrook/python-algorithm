words = list(map(str, input()))
results = []

for i in range(1, len(words)-1):
    for j in range(i+1, len(words)):
        first = words[:i]
        second = words[i:j]
        third = words[j:]

        first.reverse()
        second.reverse()
        third.reverse()

        results.append("".join(first+second+third))

print(min(results))