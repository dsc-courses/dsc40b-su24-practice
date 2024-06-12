def foo(n):
    for i in range(n**3):
        for j in range(n):
            print(i + j)
    for k in range(n):
        for l in range(n**2):
            print(k * l)
