def foo(arr):
    """`arr` is a list containing n numbers."""
    for x in arr:
        n = len(arr)
        if x > sum(arr) / n:
            print('large!')
        elif x < sum(arr) / n:
            print('small!')
        else:
            print('neither!')
