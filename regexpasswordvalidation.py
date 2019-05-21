'''Description

You need to write regex that will validate a password to make sure it meets the following criteria:
- At least six characters long;
- Contains a lowercase letter;
- Contains an uppercase letter;
- Contains a number.
Valid passwords will only be alphanumeric characters.'''


from re import search

regex = '^[^_\W)]*(?=.{6,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[^_\W)]*$'

print(bool(search(regex, 'fjd3IR9')))  # True
print(bool(search(regex, 'DSJKHD23')))  # False