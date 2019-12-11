"""
Description

In this Kata, you will be given a mathematical string and your task will be
to remove all braces as follows:
solve("x-(y+z)") = "x-y-z"
solve("x-(y-z)") = "x-y+z"
solve("u-(v-w-(x+y))-z") = "u-v+w+x+y-z"
solve("x-(-y-z)") = "x+y+z"
There are no spaces in the expression. Only two operators are given: "+" or "-".
"""


def solve(s):
    stack = list()
    result = list()
    for i in range(len(s)):
        if s[i] == '(':
            if i:
                if s[i - 1] == '-':
                    if stack and stack[-1]:
                        stack.append(0)
                    else:
                        stack.append(1)
                else:
                    if stack and stack[-1]:
                        stack.append(1)
                    else:
                        stack.append(0)
            else:
                stack.append(0)
        elif s[i].isalpha():
            result.append(s[i])
        elif s[i] == ')':
            stack.pop()
        elif stack and stack[-1]:
            if not result[-1].isalpha():
                result.pop()
            if s[i] == '-':
                result.append('+')
            else:
                result.append('-')
        else:
            if result and not result[-1].isalpha():
                result.pop()
            result.append(s[i])
    return (''.join(result)).lstrip('+')


print(solve("u-(v-w-(x+y))-z"))  # u-v+w+x+y-z
print(solve("(x-(-y-z))"))  # x+y+z
