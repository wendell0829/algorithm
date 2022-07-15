'''
给你一个整数数组 nums 。如果任一值在数组中出现 至少两次 ，返回 true ；如果数组中每个元素互不相同，返回 false 。
示例 1：
输入：nums = [1,2,3,1]
输出：true
'''
from typing import List

# class Solution:
#     def containsDuplicate(nums: List[int]) -> bool:
#         s = set(nums)
#         return not(len(s)==len(nums))

'''
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
子数组 是数组中的一个连续部分。

示例 1：
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]  [4, -5, 1, 1, 1, 1, 1]
输出：6
解释：连续子数组[4,-1,2,1] 的和最大，为6 。

示例 2：
输入：nums = [1]
输出：1

示例 3：
输入：nums = [5,4,-1,7,8]
输出：23
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pres = nums[0]
        result = pres
        for i in nums[1:]:
            pres = max(i, pres+i)
            if pres>result:
                result = pres
        return result


if __name__ == '__main__':
    # nums = [1, 2, 3, 1]
    # print(Solution.containsDuplicate(nums))
    nums = [-2]
    solution = Solution()
    print(solution.maxSubArray(nums))