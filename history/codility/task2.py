num = 0
def add_letter(str, self_str, other_str, self_max_cnt, other_max_cnt):
    global num
    if str.count(self_str) == self_max_cnt:
        if str.count(other_str) == other_max_cnt:
            num += 1
            return
        else:
            return
    if len(str) > 1 and str[-1] == self_str and str[-2] == self_str:
            add_letter(str+self_str, other_str, self_str, other_max_cnt, self_max_cnt)
    else:
        add_letter(str+self_str, self_str, other_str, self_max_cnt, other_max_cnt)
        add_letter(str+self_str, other_str, self_str, other_max_cnt, self_max_cnt)


def solution(A, B):
    # Implement your solution here
    global num
    add_letter("", "a", "b", A, B)
    add_letter("", "b", "a", B, A)
    return num


print(solution(5, 4))
