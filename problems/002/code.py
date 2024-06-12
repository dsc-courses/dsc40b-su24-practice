def foo(n):
    for i in range(n**2):

        for j in range(i):
            print(i+j)

        for k in range(n):
            print(i+k)

        for x in range(n - i):
            print(x)
