"""
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，
影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

示例 1：
输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
  偷窃到的最高金额 = 1 + 3 = 4 。

示例 2：
输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
    偷窃到的最高金额 = 2 + 9 + 1 = 12 。

[2, 1, 1, 2] -> 4
提示：
1 <= nums.length <= 100
0 <= nums[i] <= 400
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<2:
            return nums[0]
        return self.process(nums, len(nums)-1)

    def rob2(self, nums: List[int]) -> int:
        if len(nums)<2:
            return nums[0]
        return self.process2(nums, len(nums) - 1)

    def process(self, nums: List[int], n:int):
        # nums: 整数数组
        # n: 第几位,n-1位的视为已处理完
        if n==0:
            # n=0时,返回nums[0]
            return nums[n]
        elif n == 1:
            # n=1时,返回nums[0:1]两个数中较大的那个
            return max(nums[0], nums[1])
        else:
            # 两种可能:
            # 1. 要n, 那就不能要n-1,直接要n-2
            # 2.不要n, 那就要n-1
            return max(nums[n]+self.process(nums, n-2), self.process(nums, n-1))

    def process2(self, nums: List[int], n:int):
        dp = [0] * (n+1)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2, n+1):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])
        return dp[n]


s = Solution()
print(s.rob([1,2,3,1]))
print(s.rob2([1,2,3,1]))
print(s.rob([2,7,9,3,1]))
print(s.rob2([2,7,9,3,1]))
print(s.rob([2, 1, 1, 2]))
print(s.rob2([2, 1, 1, 2]))
print(s.rob2([0]))