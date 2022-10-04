"""Exercises with simple functions"""


from math import sqrt


def prod(a, b, c):
    """
    Compute the product of three numbers.

    >>> prod(1, 2, 3)
    6
    """
    return a * b * c

a = 2
def prod2(b):
    """
    Get a global a and write to a local c before computing prod(a, b, c)

    >>> prod2(42)
    168
    """
    if not 'a' in globals():
        raise ValueError("Global a wasn't found")
    c = a
    return prod(a, b, c)
    ...


def longest(x, y):
    """
    Returning the longest of two lists.

    >>> longest([1, 2, 3], [4, 5])
    [1, 2, 3]
    """
    if len(x) > len(y): return x
    else: return y


def dist(p1, p2):
    """
    Compute the distance between p1 and p2.

    >>> dist((1,1), (1,1))
    0.0
    """
    x1, y1 = p1
    x2, y2 = p2
    return sqrt((x1-x2)**2 + (y1 - y2)**2)
