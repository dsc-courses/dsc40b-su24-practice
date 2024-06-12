def foo(n):
    i = 0
    while i < n**2:
        i = i + 2
        j = 0
        while j < n:
            for k in range(n):
                print(i + j + k)
            j = j + 10
