def foo(arr):
    """`arr` is a list containing n numbers."""
    previous = None
    n = len(arr)
    for x in arr:
        if x == previous:
            for i in range(n**2):
                print('Equal!')
            return
        previous = x
