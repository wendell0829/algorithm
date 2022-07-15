"""
给定一个非负整数数组nums ，你最初位于数组的 第一个下标 。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个下标。


示例1：
输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。

示例2：
输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。

提示：
1 <= nums.length <= 3 * 104
0 <= nums[i] <= 105
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return self.recursion1(nums, 0, len(nums)-1)

    def recursion1(self, nums: List[int], i:int, n:int) -> bool:
        # nums：即给定数组
        # n: 数组最后位置
        # i: 当前所处位置，i到n时结束，能跳到
        if i == n:
            return True
        else:
            for j in range(1, nums[i]+1):
                # 对于所有能跳的步数j（1到nums[i]），尝试继续跳，如果能到终点，返回true
                if self.recursion1(nums, i+j, n):
                    return True
            # 所有j都试过了都不能跳到终点，返回false
            return False

    def dp1(self, nums: List[int]):
        dp = [0] * (len(nums)-1)
        dp[0] = True
        for i in range(len(nums)):
            dp[1] =

s = Solution()
print(s.canJump([2,3,1,1,4]))
print(s.canJump([3,2,1,0,4]))