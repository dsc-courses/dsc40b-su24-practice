import random

def foo(n):
    x = random.randrange(n)

    if x < 8:
        for j in range(n**3):
            print(j)
    else:
        for j in range(n):
            print(j)
