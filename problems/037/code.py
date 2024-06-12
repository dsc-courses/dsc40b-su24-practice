import random

def foo(n):
    # draw a number uniformly at random from 0, 1, 2, ..., n-1 in Theta(1)
    x = random.randrange(n)
    if x < math.sqrt(n):
        for j in range(n):
            print(j)
