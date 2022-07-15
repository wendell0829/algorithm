"""
tribonacci: f(n) = f(n-3)+f(n-2)+f(n-1)
"""

def tribonacci(n:int)->int:
    n1 = 0
    n2 = 1
    n3 = 1
    i = 0
    while i<n-2:
        o = n2
        n2 = n1 + n2 + n3
        n1 = n3
        n3 = n1+o+n2
        i += 2
    if n == i:
        return n1
    elif n == i+1:
        return n2
    elif n == i+2:
        return n3

from functools import lru_cache

@lru_cache(maxsize=None)
def tribonacci1(n:int)->int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return tribonacci(n-3)+tribonacci(n-2)+tribonacci(n-1)

for i in range(8):
    print(i, tribonacci(i), tribonacci1(i))

from timeit import timeit

tit = timeit(stmt="tribonacci(30)", setup="from __main__ import tribonacci", number=1000)
tit2 = timeit(stmt="tribonacci1(30)", setup="from __main__ import tribonacci1", number=1000)

print(tit)
print(tit2)
