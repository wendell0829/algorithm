"""
位运算的使用技巧（异或 ^）

注意以下性质，对任意一个整数n：
n^n = 0
n^0 = n

由此可知，对于任意2个整数a和b
a^a = 0  a^a^b = b
b^b = 0  b^b^a = a
由于^运算满足结合律和交换律，可以得到
a^b^a = b     b^a^b = a
利用这个性质，可以不使用额外空间（1）交换两个数，而且可以避免溢出问题

再进一步，对于任意n个数
N1^N2^....^Nn
如果有相等的数出现偶数次，会消除掉
如果有相等的数出现奇数次，效果等同于出现1次

利用这个性质，可以轻易解决一些数组中独特数的问题，比如：
（2）给定一个数组，其中只有1个数出现奇数次，其余数出现偶数次，找到这个数
（3）给定一个数组，其中只有2个数出现奇数次，其余数出现偶数次，找到这2个数

"""

# （1）
from typing import List

a = 2000000000000000000000
b = 3000000000000000000000

a = a^b
b = a^b
a = a^b

print(a, b)


# （2）
def onlyOdd(nums:List[int]):
    result = 0
    for i in nums:
        result ^= i
    return result

# (3)
def doubleOdd(nums:List[int]):
    # 假设为a和b
    # 首先我们得到a^b
    result = 0
    for i in nums:
        result ^= i
    # 注意接下来我们要做的就是在整体异或中屏蔽a和b中一个的影响
    # 在a^b中随便取一个值为1的位，我们注意到a^b中为1的位就是a和b值不同的位
    # 那么我们留下这个1，其他位置0，得到一个数n，那么显然有 n&a 和 n&b 必然有一个为0（a和b在这一位上不同）
    # 别的数无所谓了，异或到最后都是消掉的
    aOne = result & (~result+1)  # 为了方便，取最右边的1
    result2 = 0
    for i in nums:
        if i&aOne == 0:
            result2 ^= i
    return result2, result^result2


if __name__ == '__main__':

    nums = [1, 2, 5, 2, 7, 1, 7, 2, 2]
    nums2 = [1, 2, 5, 2, 7, 1, 7, 2, 2, 6, 7, 7]
    nums3 = [1, 2, 5, 2, 7, 1, 7, 2, 2, 6, 7, 7, 6, 8]
    print(onlyOdd(nums))
    print(doubleOdd(nums2))
    print(doubleOdd(nums3))
