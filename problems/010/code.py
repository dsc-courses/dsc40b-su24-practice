import random

def foo(n):
    # draw a number uniformly at random from 0, 1, 2, ..., n-1
    # in constant time
    x = random.randrange(n)
    if x < 100:
        for j in range(n**2):
            print(j)
