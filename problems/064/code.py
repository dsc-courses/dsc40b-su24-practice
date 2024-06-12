import random
import math

def foo(n):
    # draw a number uniformly at random from 0, 1, 2, ..., n-1 in Theta(1)
    x = random.randrange(n)

    if x < math.log(n):
        for j in range(n**2):
            print(j)
    elif x < math.sqrt(n):
        print('Ok!')
    else:
        for i in range(n):
            print(i)
