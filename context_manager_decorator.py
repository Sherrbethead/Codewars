"""
Description

Your task in this kata is to implement simple version of
contextlib.contextmanager.
The decorator will be used on a generator functions and use the part of
function before yield as context manager's "enter section" and the part after
the yield as "exit section".
If exception occurs inside the context of the with statement, the exception
should be passed to the generator via its throw method.
"""


class ContextManager(object):

    def __init__(self, f, args, kwargs):
        self.gen = f(*args, **kwargs)
        self.f, self.args, self.kwargs = f, args, kwargs

    def __enter__(self):
        return next(self.gen)

    def __exit__(self, err_type, err_value, traceback):
        return


def contextmanager(f):
    def wrapper(*args, **kwargs):
        return ContextManager(f, args, kwargs)
    return wrapper


if __name__ == '__main__':
    results = []

    @contextmanager
    def foo():
        global results
        results.append(0)
        try:
            yield
        finally:
            results.append(2)

    try:
        with foo():
            results.append(1)
            raise ValueError('a')
    except ValueError as ex:
        results.append(ex)

    print(len(results))  # 4
    print(results[3])  # a
