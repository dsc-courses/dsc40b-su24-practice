def foo(arr, stop=None):
    if stop is None:
        stop = len(arr) - 1

    if stop < 0:
        return 1

    last = arr[stop]
    return last * foo(arr, stop - 1)
