def index_of_maximum(arr):
    """`arr` is an array with n elements."""
    for i, x in enumerate(arr):
        if x == max(arr):
            return i
