"""
fibonacci: f(n) = f(n-2)+f(n-1)
"""

# 动态规划
from functools import wraps


class CountTimes:
    count = 0

    def __init__(self):
        pass

    @classmethod
    def counting_recursion(cls, fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            cls.count += 1
            return fn(*args, **kwargs)
        return wrapper


@CountTimes.counting_recursion
# 1. 斐波那契数列
def fibonacci(n:int):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

@CountTimes.counting_recursion
# 1. 斐波那契数列优化(带记忆)
def fibonacci2(n:int, record:dict):
    if record.get(n) != None:
        return record.get(n)
    else:
        if n == 1:
            result = 0
        elif n == 2:
            result = 1
        else:
            result = fibonacci2(n-1, record)+fibonacci2(n-2, record)
        record[n] = result
        return result

@CountTimes.counting_recursion
# 1. 斐波那契数列优化(dp)
def fibonacci3(n:int):
    result = {
        1:0,
        2:1,
    }
    i = 3
    while i<=n:
        result[i] = result[i-1] + result[i-2]
        i += 1
    return result[n]

# 1. 斐波那契数列优化(只存2个)
def fibonacci4(n:int):
    n1 = 0
    n2 = 1
    i = 1
    while i<=n:
        n1, n2 = n2, n1+n2
        i += 1
    return n1


if __name__ == '__main__':
    for n in range(1, 20):
        print(n)
        result = fibonacci(n)
        print(result, CountTimes.count)
        CountTimes.count = 0
        record = dict()
        result = fibonacci2(n, record)
        print(result, CountTimes.count)
        # print(record)
        CountTimes.count = 0
        result = fibonacci3(n)
        print(result, CountTimes.count)
        CountTimes.count = 0
        result = fibonacci4(n)
        print(result, CountTimes.count)
    from timeit import timeit

    tit = timeit(stmt="fibonacci(10)", setup="from __main__ import fibonacci", number=1000)
    tit2 = timeit(stmt="fibonacci2(10, {})", setup="from __main__ import fibonacci2", number=1000)
    tit3 = timeit(stmt="fibonacci3(10)", setup="from __main__ import fibonacci3", number=1000)
    tit4 = timeit(stmt="fibonacci4(10)", setup="from __main__ import fibonacci4", number=1000)

    print(tit)
    print(tit2)
    print(tit3)
    print(tit4)





