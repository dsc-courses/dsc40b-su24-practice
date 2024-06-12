def foo(arr):
    """`arr` is a list containing n numbers."""
    for x in arr:
        if x > max(arr) / 2:
            print('large!')
        elif x < min(arr) * 2:
            print('small!')
        else:
            print('neither!')
