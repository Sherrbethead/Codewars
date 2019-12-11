"""
Description

What is an anagram? Well, two words are anagrams of each other if they both
contain the same letters.
Write a function that will find all the anagrams of a word from a list.
You will be given two inputs a word and an array with words. You should return
an array of all the anagrams or an empty array if there are none.
"""


from collections import Counter


def anagrams(word, words):
    anagram_list = list()
    for i in words:
        if Counter(word) == Counter(i):
            anagram_list.append(i)
    return anagram_list


print(anagrams(
    'abba', ['aabb', 'abcd', 'bbaa', 'dada']
))  # ['aabb', 'bbaa']
print(anagrams(
    'racer', ['crazer', 'carer', 'racar', 'caers', 'racer']
))  # ['carer', 'racer']
