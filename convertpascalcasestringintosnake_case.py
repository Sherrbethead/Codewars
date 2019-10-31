"""Complete the function/method so that it takes CamelCase string and returns
the string in snake_case notation. Lowercase characters can be numbers.
If method gets number, it should return string.
Examples:
# returns test_controller
to_underscore('TestController')
# returns movies_and_books
to_underscore('MoviesAndBooks')
# returns app7_test
to_underscore('App7Test')
# returns "1"
to_underscore(1)
"""


def to_underscore(string):
    snake = list()
    for i in str(string):
        if i.isupper():
            snake.append('_' + i.lower())
        else:
            snake.append(i)
    return ''.join(snake).lstrip('_')


print(to_underscore('TestController'))  # test_controller
print(to_underscore('App7Test'))  # app7_test
