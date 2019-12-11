"""
Description

Move the first letter of each word to the end of it, then add "ay" to the end
of the word.
Leave punctuation marks untouched.
"""


def pig_it(text):
    return ' '.join(
        [(i[1:] + i[0] + 'ay') if i.isalpha() else i for i in text.split()]
    )


print(pig_it('Pig latin is cool'))  # igPay atinlay siay oolcay
print(pig_it('This is my string'))  # hisTay siay ymay tringsay
