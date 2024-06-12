import math

def foo(arr):
    """`arr` is an array with n elements."""
    n = len(arr)
    ix = 1
    s = 0

    while ix < n:
        s = s + arr[ix]
        ix = ix * 5 + 2

    return s
