'''Description

Motivation:
Natural language texts often have a very high frequency of certain letters, in German for example, almost every 5th
letter is an E, but only every 500th is a Q. It would then be clever to choose a very small representation for E.
This is exactly what the Huffman compression is about, choosing the length of the representation based on
the frequencies of the symbol in the text.
Algorithm:
Let's assume we want to encode the word "aaaabcc", then we calculate the frequencies of the letters in the text:
Symbol	Frequency
  a	       4
  b	       1
  c	       2
Now we choose a smaller representation the more often it occurs, to minimize the overall space needed.
The algorithm uses a tree for encoding and decoding:
  .
 / \
a   .
   / \
   b  c
Usually we choose 0 for the left branch and 1 for the right branch (but it might also be swapped). By traversing from
the root to the symbol leaf, we want to encode, we get the matching representation. To decode a sequence of binary
digits into a symbol, we start from the root and just follow the path in the same way, until we reach a symbol.
Considering the above tree, we would encode a with 0, b with 10 and c with 11. Therefore encoding "aaaabcc" will
result in 0000101111.
Note: As you can see the encoding is not optimal, since the code for b and c have same length, but that is topic
of another data compression Kata.
Tree construction:
To build the tree, we turn each symbol into a leaf and sort them by their frequency. In every step, we remove
2 trees with the smallest frequency and put them under a node. This node gets reinserted and has the sum of
the frequencies of both trees as new frequency. We are finished, when there is only 1 tree left.
Hint: Maybe you can do it without sorting in every step?
Goal:
Write functions frequencies, encode and decode.
Note: Frequency lists with just one or less elements should get rejected (because then there is no information we could
encode, but the length).'''


import heapq
from collections import Counter, namedtuple

class Node(namedtuple('Node', ['left', 'right'])):
    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')

class Leaf(namedtuple('Leaf', ['char'])):
    def walk(self, code, acc):
        code[self.char] = acc or '0'

def frequencies(s):
    freqs = [(ch, freq) for ch, freq in Counter(s).items()]
    return freqs

def codedict(freqs):
    h = list()
    for ch, freq in freqs:
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1
    code = dict()
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, '')
    return code

def encode(freqs, s):
    if len(freqs) > 1:
        code = codedict(freqs)
        encoded = ''.join(code[ch] for ch in s)
        return encoded

def decode(freqs, bits):
    if len(freqs) > 1:
        decoded = str()
        acc = str()
        code = codedict(freqs)
        code = {value: key for key, value in code.items()}
        for char in bits:
            acc += char
            if acc in code:
                decoded += code[acc]
                acc = str()
        return decoded

a = "aaaabcc"
fs = frequencies(a)
print(fs)  # [('a', 4), ('b', 1), ('c', 2)]
print(encode(fs, a))
b = "1111000101"
print(decode(fs, b))
c = "look, this is a string"
fs = frequencies(c)
print(fs)  # [('l', 1), ('o', 2), ('k', 1), (',', 1), (' ', 4), ('t', 2), ('h', 1), ('i', 3), ('s', 3), ('a', 1),
           # ('r', 1), ('n', 1), ('g', 1)]
print(encode(fs, c))  # 000011101110000100101101111001110010111010010111001001101011111010110001100111
d = "000011101110000100101101111001110010111010010111001001101011111010110001100111"
print(decode(fs, d))  # look, this is a string