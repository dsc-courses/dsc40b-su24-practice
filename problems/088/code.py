import random
import math

def foo(n):
    # draw a number uniformly at random from 0, 1, 2, ..., n-1 in Theta(1)
    x = random.randrange(n)

    if x < math.sqrt(n):
        for j in range(n):
            print(j)
    elif x < n//2:
        print('Ok!')
    else:
        for i in range(n**2):
            print(i)
