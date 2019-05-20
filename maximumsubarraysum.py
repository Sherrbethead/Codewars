'''Description

The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array
or list of integers.
Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array.
If the list is made up of only negative numbers, return 0 instead.
Empty list is considered to have zero greatest sum. Note that the empty list or array is also
a valid sublist/subarray.'''


def maxSequence(arr):
    belowzero = [i for i in arr if i < 0]
    subseq = [0] * len(arr)
    if len(arr) == 0 or len(belowzero) == len(arr):
        return 0
    else:
        subseq[0] = max(0, arr[0])
        for j in range(1, len(arr)):
            subseq[j] = max(subseq[j-1] + arr[j], arr[j])
        return max(subseq)

print(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
print(maxSequence([3, 1, 6, -2, 4, -1, -7, 4, 9]))  # 17