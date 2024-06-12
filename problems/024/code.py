def foo(n):
    i = 0
    while i < n:
        j = 0
        while j < i:
            print(i + j)
            j += 1
        i += 5
