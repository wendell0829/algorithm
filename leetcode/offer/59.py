"""
给你一个整数数组 nums，有一个大小为k的滑动窗口从数组的最左侧移动到数组的最右侧。
你只可以看到在滑动窗口内的 k个数字。滑动窗口每次只向右移动一位。
返回 滑动窗口中的最大值 。

示例 1：
输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]

解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

示例 2：
输入：nums = [1], k = 1
输出：[1]


提示：
1 <= nums.length <= 105
-104<= nums[i] <= 104
1 <= k <= nums.length
"""

from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 初始化滑动窗口左右边界和第1个最大值
        L = 0
        R = L+k-1
        result_list = [max(nums[L:R+1])]
        # 开始循环，L，R不断右移，R移到最后一位为止
        while R<len(nums)-1:
            R += 1
            # 如果进入窗口的数比当前最大值小
            if nums[R]<result_list[L]:
                # 看离开窗口的数是否为最大值
                 if result_list[L] == nums[L]:
                     # 最大值离开只能重算最大值
                     result_list.append(max(nums[L+1:R+1]))
                 else:
                     # 最大值未离开则保留
                     result_list.append(result_list[L])
            else:
                # 否则进入窗口的数即为最大值
                result_list.append(nums[R])
            L += 1
        return result_list


s = Solution()
print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
print(s.maxSlidingWindow([1], 1))
