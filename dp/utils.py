from functools import wraps
from timeit import timeit
from typing import Optional


class Counter:
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

# tit = timeit(stmt="move_to_aim(2, 6, 8, 18)", setup="from practice import move_to_aim", number=1000)
# tit2 = timeit(stmt="move_to_aim2(2, 6, 8, 18, {})", setup="from practice import move_to_aim2", number=1000)
#
# print(tit)
# print(tit2)
def printl(l:list[list[Optional]]):
    for i in l:
        print(i)