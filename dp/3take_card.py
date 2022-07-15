"""
代表不同分值的牌排列为一个数组
[10, 30, 200, 30, 50, 20]
A,B轮流拿,每次只能从最左或最右拿,目标是拿到最高分,假设AB都使用最优策略
求获胜者的分数
"""
from utils import *

# 递归
def first(cards:list[int], L:int, R:int):
    # 先手时获得的分数
    if L == R:
        return cards[L]
    return max(cards[L]+second(cards, L+1, R), cards[R]+second(cards, L, R-1))

def second(cards:list[int], L:int, R:int):
    # 后手时获得的分数
    if L == R:
        return 0
    return min(first(cards, L+1, R), first(cards, L, R-1))

def top_score(cards:list[int]):
    return max(first(cards, 0, len(cards)-1), second(cards, 0, len(cards)-1))

#记忆化搜索
def first2(cards:list[int], L:int, R:int, fdp:list[list[int]], sdp:list[list[int]]):
    # 先手时获得的分数
    if fdp[L][R] != -1:
        return fdp[L][R]
    if L == R:
        answer = cards[L]
    else:
        answer = max(cards[L]+second2(cards, L+1, R, fdp, sdp), cards[R]+second2(cards, L, R-1, fdp, sdp))
    fdp[L][R] = answer
    return answer

def second2(cards:list[int], L:int, R:int, fdp:list[list[int]], sdp:list[list[int]]):
    if sdp[L][R] != -1:
        return sdp[L][R]
    if L == R:
        answer = 0
    else:
        answer = min(first2(cards, L+1, R, fdp, sdp), first2(cards, L, R-1, fdp, sdp))
    sdp[L][R] = answer
    return answer

def top_score2(cards:list[int]):
    L, R = 0, len(cards)-1
    fdp = [[ -1 for i in range(R+1)] for i in range(R+1)]
    sdp = [[ -1 for i in range(R+1)] for i in range(R+1)]
    return max(first2(cards, L, R, fdp, sdp), second2(cards, L, R, fdp, sdp))

#dp
def first3(cards:list[int], L:int, R:int, fdp:list[list[int]], sdp:list[list[int]]):
    # 先手时获得的分数
    if fdp[L][R] != -1:
        return fdp[L][R]
    if L == R:
        answer = cards[L]
    else:
        answer = max(cards[L] + sdp[L+1][R], cards[R] + sdp[L][R-1])
    fdp[L][R] = answer
    printl(fdp)
    return answer

def second3(cards:list[int], L:int, R:int, fdp:list[list[int]], sdp:list[list[int]]):
    if sdp[L][R] != -1:
        return sdp[L][R]
    if L == R:
        answer = 0
    else:
        answer = min(fdp[L+1][R], fdp[L][R-1])
    sdp[L][R] = answer
    printl(sdp)
    return answer

def top_score3(cards:list[int]):
    L, R = 0, len(cards)-1
    fdp = [[ -1 for i in range(R+1)] for i in range(R+1)]
    sdp = [[ -1 for i in range(R+1)] for i in range(R+1)]
    for i in range(R+1):
        fdp[i][i] = cards[i]
        sdp[i][i] = 0
    return max(first3(cards, L, R, fdp, sdp), second3(cards, L, R, fdp, sdp))

if __name__ == '__main__':
    from timeit import timeit
    result = top_score([10, 2, 5, 6, 20])
    result2 = top_score2([10, 2, 5, 6, 20])
    result3 = top_score3([10, 2, 5, 6, 20])
    print(result, result2, result3)
    tit = timeit(stmt="top_score([10, 2, 5, 6, 20, 10, 20, 30])", setup="from __main__ import top_score", number=1000)
    tit2 = timeit(stmt="top_score2([10, 2, 5, 6, 20, 10, 20, 30])", setup="from __main__ import top_score2", number=1000)
    # tit3 = timeit(stmt="top_score3(2, 5, 6, 20)", setup="from __main__ import top_score3", number=1000)
    # tit4 = timeit(stmt="top_score4(2, 5, 6, 20)", setup="from __main__ import top_score4", number=1000)

    print(tit)
    print(tit2)
    # print(tit3)
    # print(tit4)