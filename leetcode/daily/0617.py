"""
给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那两个整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。

示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

示例 2：
输入：nums = [3,2,4], target = 6
输出：[1,2]

"""
from typing import List
from dp.utils import Counter

class Solution:
    # @Counter.counting_recursion
    # def fun1(self, nums: List[int], target: int, L:int, R:int):
    #     # L-R之间和为target的两个数的下标
    #     if R-L == 1:
    #         if nums[L] + nums[R] == target:
    #             return [L, R]
    #         else:
    #             return None
    #     else:
    #         temp = self.fun1(nums, target, L+1, R)
    #         if temp:
    #             return temp
    #         else:
    #             rest = target - nums[L]
    #             index_rest = nums[0:].index(rest)
    #             return [L, index_rest]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            rest = target - nums[i]
            print(rest, rest in nums)
            if rest in nums[i+1:]:
                return [i, nums[i+1:].index(rest)+i+1]


if __name__ == '__main__':
    s = Solution()
    nums = [3, 1, 3]
    target = 6
    print(s.twoSum(nums, target))
    print(Counter.count)
    from timeit import timeit
    tit = timeit(stmt="s.twoSum([2,7,11,15], 26)", setup="from __main__ import Solution; s = Solution()", number=1000)
    print(tit)