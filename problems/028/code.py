def foo(n):
    if n < 10:
        print("Hello world.")
        return

    for i in range(n):
        print(i)

    for i in range(6):
        foo(n//3)
