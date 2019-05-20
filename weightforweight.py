'''Description

My friend John and I are members of the "Fat to Fit Club (FFC)". John is worried because each month a list with
the weights of members is published and each month he is the last on the list which means he is the heaviest.
I am the one who establishes the list so I told him: "Don't worry any more, I will modify the order of the list".
It was decided to attribute a "weight" to numbers. The weight of a number will be from now on the sum of its digits.
For example 99 will have "weight" 18, 100 will have "weight" 1 so in the list 100 will come before 99. Given a string
with the weights of FFC members in normal order can you give this string ordered by "weights" of these numbers?
All numbers in the list are positive numbers and the list can be empty.
Notes:
- It may happen that the input string have leading, trailing whitespaces and more than a unique whitespace between
two consecutive numbers;
- Don't modify the input.'''


def digitsum(a):
    digitlist = list()
    for i in a.split():
        sum = 0
        for j in range(len(i)):
            sum += int(i[j])
        digitlist.append(sum)
    return digitlist

def order_weight(strng):
    return ' '.join(sorted(sorted(strng.split()), key = digitsum))

print(order_weight("103 123 4444 99 2000"))  # 2000 103 123 4444 99
print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"))  # 11 11 2000 10003 22 123 1234000 44444444 9999