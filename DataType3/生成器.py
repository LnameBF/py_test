import sys


def function_create(n):
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        else:
            yield a
            a, b = b, a + b
            counter += 1


f = function_create(10)

while True:
    try:
        x = (next(f))
        print(x)
    except StopIteration:
        sys.exit()
