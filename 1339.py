from string import ascii_uppercase
alpha = list(ascii_uppercase)

N = int(input())
words = {}
for _ in range(N):
    word = input()
    for i in range(0, len(word)):
        if word[i] in words:
            words[word[i]] += 10 ** (len(word)-i-1)
        else:
            words[word[i]] = 10 ** (len(word)-i-1)

sorted_dict = dict(sorted(words.items(), key=lambda x: x[1], reverse=True))

count = 9
result = 0
for k, v in sorted_dict.items():
    result += (v*count)
    count -= 1

print(result)