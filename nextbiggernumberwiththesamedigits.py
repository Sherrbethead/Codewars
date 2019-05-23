'''Description

You have to create a function that takes a positive integer number and returns the next bigger number formed by
the same digits:
12 ==> 21
513 ==> 531
2017 ==> 2071
If no bigger number can be composed using those digits, return -1:
9 ==> -1
111 ==> -1
531 ==> -1'''


def next_bigger(n):
    dig = [i for i in str(n)]
    swapindex = int()
    for i in range(len(dig) - 1, 0, -1):
        if dig[i] > dig[i-1]:
            swapindex = dig[i:].index(min([j for j in dig[i:] if j > dig[i-1]])) + i
            dig[i-1], dig[swapindex] = dig[swapindex], dig[i-1]
            break
    return int(''.join(dig[:i] + sorted(dig[i:]))) if swapindex else -1

print(next_bigger(18887))  # 71888
print(next_bigger(21543))  # 23145