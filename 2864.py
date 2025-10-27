a, b = input().split()

max_result = int(a.replace("5", "6")) + int(b.replace("5", "6"))
min_result = int(a.replace("6", "5")) + int(b.replace("6", "5"))


print(f"{min_result} {max_result}")
