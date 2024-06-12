from math import sqrt, log, ceil

def foo(n):
    for i in range(ceil(n**3 - 10*n + sqrt(n))):
        for j in range(ceil(log(n**2))):
            print(i, j)
