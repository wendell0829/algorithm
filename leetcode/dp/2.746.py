"""
给你一个整数数组 cost ，其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。一旦你支付此费用，即可选择向上爬一个或者两个台阶。
你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。
请你计算并返回达到楼梯顶部的最低花费。

示例 1：
输入：cost = [10,15,20]
输出：15
解释：你将从下标为 1 的台阶开始。
- 支付 15 ，向上爬两个台阶，到达楼梯顶部。
总花费为 15 。

示例 2：
输入：cost = [1,100,1,1,1,100,1,1,100,1]
输出：6
解释：你将从下标为 0 的台阶开始。
- 支付 1 ，向上爬两个台阶，到达下标为 2 的台阶。
- 支付 1 ，向上爬两个台阶，到达下标为 4 的台阶。
- 支付 1 ，向上爬两个台阶，到达下标为 6 的台阶。
- 支付 1 ，向上爬一个台阶，到达下标为 7 的台阶。
- 支付 1 ，向上爬两个台阶，到达下标为 9 的台阶。
- 支付 1 ，向上爬一个台阶，到达楼梯顶部。
总花费为 6

提示：
2 <= cost.length <= 1000
0 <= cost[i] <= 999
"""

"""
思路
尝试递归:
边界:距离顶部1或2时,可以支付当前cost直接跳到顶
递归:假设当前位置为current,则有两个选择:
    跳1步:current+1
    跳2步:current+2
    返回2者种的min
调用:第一步可以从0或1起跳,等价于从-1起跳,-1的cost为0
dp: 考虑从某个台阶跳到天台时需要的cost
    N-1或N-2: 该处cost
    N-3以下的n: min(f(n+1), f(n+2))+cost[n]
"""
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        return self.fun1(cost, -1)

    def fun1(self, cost: List[int], current: int) -> int:
        if current >= len(cost) - 3:
            return cost[current]
        return cost[current] + min(self.fun1(cost, current + 1), self.fun1(cost, current + 2))

    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        i = len(cost)
        result1 = cost[i - 1]
        result2 = cost[i - 2]
        i -= 3
        while i >= 0:
            result1, result2 = result2, cost[i] + min(result1, result2)
            i -= 1
        return min(result1, result2)

    def minCostClimbingStairs3(self, cost: List[int]) -> int:
        result1 = 0
        result2 = 0
        i = 0
        while i < len(cost)-1:
            result1, result2 = result2, min(result1+cost[i], result2+cost[i+1])
            # print(i, result1, result2)
            i += 1

        return result2



s = Solution()
cost = [10, 15, 20]
# s.minCostClimbingStairs(cost)
print(s.minCostClimbingStairs3(cost))
print(s.minCostClimbingStairs3(cost), s.minCostClimbingStairs3(cost))
cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(s.minCostClimbingStairs3(cost), s.minCostClimbingStairs3(cost))
cost = [10, 15]
print(s.minCostClimbingStairs3(cost), s.minCostClimbingStairs3(cost))
cost = [15, 10]
print(s.minCostClimbingStairs3(cost), s.minCostClimbingStairs3(cost))