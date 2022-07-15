"""
1 2 3 4 5 6 7
start:初始位置 aim:目标位置 N:位置总数 step:步数
每一步都必须移动,使位置+1或-1,但不能超过限位（即位置1时必须移动到2,7时必须移动到6）
"""
from utils import Counter

@Counter.counting_recursion
def move_to_aim(start:int, aim:int, N:int, step:int)->int:
    # 暴力递归
    # 边界：步数为0时，位于目的返回1，否则返回0
    # 递归：左右边界时，只有一个方向移动，中间时两个方向移动后的可能结果之和
    if step == 0:
        if start == aim:
            return 1
        else:
            return 0
    else:
        if start == 1:
            return move_to_aim(2, aim, N, step - 1)
        elif start == N:
            return move_to_aim(N-1, aim, N, step - 1)
        else:
            return move_to_aim(start+1, aim, N, step - 1) + move_to_aim(start-1, aim, N, step-1)

@Counter.counting_recursion
def move_to_aim2(start:int, aim:int, N:int, step:int, record:dict)->int:
    # 带记忆递归
    if record.get((start, step)) != None:
        return record[(start, step)]
    if step == 0:
        if start == aim:
            result = 1
        else:
            result = 0
    else:
        if start == 1:
            result = move_to_aim2(2, aim, N, step - 1, record)
        elif start == N:
            result = move_to_aim2(N-1, aim, N, step - 1, record)
        else:
            result = move_to_aim2(start+1, aim, N, step - 1, record) + move_to_aim2(start-1, aim, N, step-1, record)
    record[(start, step)] = result
    return result

@Counter.counting_recursion
def move_to_aim3(start:int, aim:int, N:int, step:int)->int:
    # dp使用字典
    dp = {}
    for i in range(1, N+1):
        if i==aim:
            dp[(i, 0)] = 1
        else:
            dp[(i, 0)] = 0
    for j in range(1, step+1):
        dp[(1, j)] = dp[(2, j-1)]
        for i in range(2, N):
            dp[(i, j)] = dp[(i-1, j-1)] + dp[(i+1, j-1)]
        dp[(N, j)] = dp[(N-1, j-1)]
    return dp[(start, step)]


def move_to_aim4(start:int, aim:int, N:int, step:int)->int:
    # dp使用二维列表
    dp =  [[ 0 for i in range(step+1)] for i in range(N+1)]
    dp[aim][0] = 1
    for j in range(1, step+1):
        dp[1][j] = dp[2][j-1]
        for i in range(2, N):
            dp[i][j] = dp[i-1][j-1]+dp[i+1][j-1]
        dp[N][j] = dp[N-1][j-1]
    return dp[start][step]

if __name__ == '__main__':
    # print(counter.get(fibonacci))
    start, aim, N = 2, 5, 6
    # for n in range(1, 10):
    #     print(n, ': ')
    #     result = move_to_aim(start, aim, N, n)
    #     print(result, Counter.count)
    #     Counter.count = 0
    #     record = dict()
    #     result = move_to_aim2(start, aim, N, n, {})
    #     print(result, Counter.count)
    #     Counter.count = 0
    #     result = move_to_aim3(start, aim, N, n)
    #     print(result, Counter.count)
    #     Counter.count = 0
    #     result = move_to_aim4(start, aim, N, n)
    #     print(result, Counter.count)
    # print(move_to_aim(start, aim, N, 5))
    # print(move_to_aim2(start, aim, N, 5, {}))
    # print(move_to_aim3(start, aim, N, 5))
    # print(move_to_aim4(start, aim, N, 5))
    from timeit import timeit
    tit = timeit(stmt="move_to_aim(2, 5, 6, 20)", setup="from __main__ import move_to_aim", number=1000)
    tit2 = timeit(stmt="move_to_aim2(2, 5, 6, 20, {})", setup="from __main__ import move_to_aim2", number=1000)
    tit3 = timeit(stmt="move_to_aim3(2, 5, 6, 20)", setup="from __main__ import move_to_aim3", number=1000)
    tit4 = timeit(stmt="move_to_aim4(2, 5, 6, 20)", setup="from __main__ import move_to_aim4", number=1000)

    print(tit)
    print(tit2)
    print(tit3)
    print(tit4)