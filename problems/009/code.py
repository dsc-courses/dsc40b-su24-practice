import random

def foo(n):
    # draw a random number uniformly from 0, 1, 2, ..., 99
    # in constant time
    x = random.randrange(100)
    for i in range(x):
        for j in range(n):
            print("Here!")
