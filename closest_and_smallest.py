"""
Description

Input:
- a string strng of n positive numbers (n = 0 or n >= 2).
Let us call weight of a number the sum of its digits. For example 99 will have
"weight" 18, 100 will have "weight" 1.
Two numbers are "close" if the difference of their weights is small.
Task:
For each number in strng calculate its "weight" and then find two numbers
of strng that have:
- the smallest difference of weights ie that are the closest;
- with the smallest weights;
- and with the smallest indices (or ranks, numbered from 0) in strng;
Output:
- an array of two arrays, each subarray in the following format:
[number-weight, index in strng of the corresponding number, original
corresponding number instrng] or a pair of two subarrays (Haskell, Clojure,
FSharp) or an array of tuples (Elixir, C++) or a (char*) in C mimicking an
array of two subarrays or a string or a matrix in R (2 rows, 3 columns, no
columns names).
The two subarrays are sorted in ascending order by their number weights if
these weights are different, by their indexes in the string if they have the
same weights.
"""


def closest(strng):
    if strng:
        numbers = strng.split()
        weights = list()
        for i in numbers:
            weight = 0
            for j in i:
                weight += int(j)
            weights.append(weight)
        order = sorted(weights)
        m = float('inf')
        x, y = 0, 0
        for k in range(len(order) - 1):
            if abs(order[k] - order[k + 1]) < m:
                x, y = order[k], order[k + 1]
            m = min(abs(order[k] - order[k + 1]), m)
        x_index = weights.index(x)
        y_index = weights.index(y)
        if y_index >= x_index:
            del weights[x_index]
            y_index = weights.index(y) + 1
            weights.insert(x_index, x)
        return [
            [x, x_index, int(numbers[x_index])],
            [y, y_index, int(numbers[y_index])]
        ]
    return []


print(closest(
    "239382 162 254765 182 485944 468751 49780 108 54"
))  # [[9, 1, 162], [9, 7, 108]]
print(closest(
    "79257 160 44641 146 386224 147 313622 117 259947 155 58"
))  # [[11, 3, 146], [11, 9, 155]]
