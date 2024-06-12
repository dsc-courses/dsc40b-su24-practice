def foo(n):
    for i in range(200, n):
        for j in range(i, 2*i + n**2):
            print(i + j)
