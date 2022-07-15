"""
爬楼梯
假设你正在爬楼梯。需要 n阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

示例 1：
输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶
示例 2：
输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶
"""

"""
思路
首先考虑尝试递归,显然有:
边界: n==1时,return 1, n==0时,return 1
递归:选择爬1格,则有climbStairs(n-1)种,选择爬2格,则有climbStairs(n-2),二者之和即为所求
递归写完之后显然这是一个fibonacci数列
尝试一下矩阵快速幂
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        elif n == 1:
            return 1
        else:
            return self.climbStairs(n-1)+self.climbStairs(n-2)

    def climbStairs1(self, n: int) -> int:
        n0 = 1
        n1 = 1
        i = 1
        while i<=n:
            n0, n1 = n1, n0+n1
            i += 1
        return n0

    def climbStairs2(self, n: int) -> int:
        a0 = [[1],
              [1]]
        M = [[0, 1],
             [1, 1]]
        M0 = [[1, 0],
             [0, 1]]
        while n>0:
            if n%2==1:
                 M0 = self.matrixMulti(M0, M)
            n //= 2
            M = self.matrixMulti(M, M)
        return M0[0][0]*a0[0][0] + M0[0][1]*a0[1][0]

    def matrixMulti(self, m1:list[list[int]], m2:list[list[int]])->list[list[int]]:
        return [[m1[0][0]*m2[0][0]+m1[0][1]*m2[1][0], m1[0][0]*m2[0][1]+m1[0][1]*m2[1][1]],
                [m1[1][0]*m2[0][0]+m1[1][1]*m2[1][0], m1[1][0]*m2[0][1]+m1[1][1]*m2[1][1]]]


s = Solution()
for i in range(10):
    print(s.climbStairs(i), s.climbStairs1(i), s.climbStairs2(i))
