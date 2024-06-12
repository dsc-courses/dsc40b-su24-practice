def foo(n):
    if n < 1:
        return 0

    for i in range(n**2):
        print("here")

    foo(n/2)
