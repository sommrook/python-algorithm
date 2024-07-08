import re
A = input()

extract_alpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

count = len(A)
for alpha in extract_alpha:
    al_count = A.count(alpha)
    if alpha == extract_alpha[-1]:
        al_count = al_count - A.count("dz=")
    count = count - al_count * (len(alpha) - 1)


print(count)