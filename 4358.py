import sys
input = sys.stdin.readline

tree_dict = {}

cnt = 0
while True:
    tree = str(input().rstrip())

    if not tree:
        break

    if tree in tree_dict:
        tree_dict[tree] += 1
    else:
        tree_dict[tree] = 1

    cnt += 1

for tree, t_cnt in sorted(tree_dict.items()):
    percentage = round(t_cnt / cnt * 100, 4)
    print("%s %.4f" % (tree, percentage))