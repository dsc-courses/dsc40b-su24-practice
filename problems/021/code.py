import math

def foo(n):
    for i in range(math.floor(math.sqrt(n))):
        for j in range(math.floor(5*n**2 - math.sqrt(n)/1_000_000 + 100)):
            print(n * n)
