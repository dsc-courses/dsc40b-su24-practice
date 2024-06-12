import random

def foo(n):
    for i in range(n):
        # draw a number uniformly at random from 0, 1, 2, ..., n-1 in Theta(1)
        x = random.randrange(n)
        for j in range(x):
            print(j)
