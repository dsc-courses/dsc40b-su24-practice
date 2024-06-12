import random

def foo(n):
    # draw a random number uniformly from 0, 1, 2, ..., n-1
    # in constant time
    x = random.randrange(n)
    for i in range(x):
        for j in range(n):
            print("Here!")
