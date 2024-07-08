alpha = str(input())

alpha_dict = {}
lower_alpha = alpha.lower()

for i in lower_alpha:
    alpha_dict[i] = alpha_dict[i] + 1 if i in alpha_dict else 1

new_list = sorted(alpha_dict, key=lambda x: alpha_dict[x], reverse=True)

if len(new_list) > 1 and alpha_dict[new_list[0]] == alpha_dict[new_list[1]]:
    print("?")
else:
    print(new_list[0].upper())