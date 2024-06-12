import math

def foo(n):
    for i in range(math.floor(math.sqrt(n))):
        for j in range(i):
            print(i + j)
