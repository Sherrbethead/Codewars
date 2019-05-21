'''Description

Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid.
The function should return true if the string is valid, and false if it's invalid.
Constraints:
0 <= input.length <= 100
Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters.
Furthermore, the input string may be empty and/or not contain any parentheses at all. Do not treat other forms of
brackets as parentheses (e.g. [], {}, <>).'''


def valid_parentheses(string):
    stack = list()
    str = filter(lambda x: x == '(' or x == ')', string)
    for i in str:
        if i is '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return not stack

print(valid_parentheses("hi())("))  # False
print(valid_parentheses("hi(hi)()"))  # True