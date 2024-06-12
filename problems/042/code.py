import math
def maximum(arr, start=0, stop=None):
    """Find the maximum of arr[start:stop]."""
    if stop is None:
        stop = len(arr)
    if stop - start == 0:
        return -float('inf')

    middle = math.floor((start + stop) / 2)
    left = maximum(arr, start, middle)
    right = maximum(arr, middle, stop)
    if left > right:
        return left
    else:
        return right
