"""
给你一个整数数组nums，你可以对它进行一些操作。
每次操作中，选择任意一个nums[i]，删除它并获得nums[i]的点数。之后，你必须删除 所有 等于nums[i] - 1 和 nums[i] + 1的元素。
开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。

示例 1：
输入：nums = [3,4,2]
输出：6
解释：
删除 4 获得 4 个点数，因此 3 也被删除。
之后，删除 2 获得 2 个点数。总共获得 6 个点数。

示例2：
输入：nums = [2,2,3,3,3,4]
输出：9
解释：
删除 3 获得 3 个点数，接着要删除两个 2 和 4 。
之后，再次删除 3 获得 3 个点数，再次删除 3 获得 3 个点数。
总共获得 9 个点数。

提示：
1 <= nums.length <= 2 * 10^4
1 <= nums[i] <= 10^4

"""
from typing import List, Set


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        skip = set()
        return self.process1(nums, len(nums)-1, skip)

    def process1(self, nums: List[int], n:int, skip:Set[int]):
        # n：缩减条件
        # skip:需要跳过的数字，比如拿了3，skip中就要添加2和4
        if n == 0:
            # n为0时，不在skip中就拿，在skip中只能返回0
            if nums[n] in skip:
                return 0
            else:
                return nums[n]
        else:
            if nums[n] in skip:
                # nums[n] 在skip中，只能不拿
                return self.process1(nums, n-1, skip)
            else:
                # 两种情况：
                # 1. 不拿nums[n]：skip不变，直接返回f(n-1)
                # 2. 拿nums[n]：skip增加nums[n]±1，返回nums[n]+f(n-1)
                skip1 = skip.copy()
                result1 = self.process1(nums, n - 1, skip1)
                skip2 = skip.copy()
                skip2.add(nums[n] - 1)
                skip2.add(nums[n] + 1)
                result2 = nums[n]+self.process1(nums, n - 1, skip2)
                return max(result1, result2)

    def process2(self, nums: List[int], n:int):
        skip = set()
        dp = [0] * n
        dp[0] = nums[0]
        skip.add(nums[0]+1)
        skip.add(nums[0]-1)
        for i in range(1, n):
            pass

s = Solution()
print(s.deleteAndEarn([3,4,2]))
print(s.deleteAndEarn([2,2]))
print(s.deleteAndEarn([2,2,3]))
print(s.deleteAndEarn([2,2,3,3]))
print(s.deleteAndEarn([2,2,3,3,3]))
print(s.deleteAndEarn([2,2,3,3,3,4]))
print(s.deleteAndEarn([1,1]))
print(s.deleteAndEarn([1]))
print(s.deleteAndEarn([0]))