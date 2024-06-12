import math

def most_common(arr, start, stop):
    """Attempts to compute the most common element in arr[start:stop]."""
    if stop - start == 1:
        return (arr[start], 1)

    middle = math.floor((start + stop) / 2)

    left_value, left_count = most_common(arr, start, middle)
    right_value, right_count = most_common(arr, middle, stop)

    if left_count > right_count:
        return (left_value, left_count)
    else:
        return (right_value, right_count)
