def foo(arr):
    """`arr` is an array with n elements."""
    x = max(arr) * min(arr)
    if sum(arr) > 10:
        return x
    else:
        return 0
