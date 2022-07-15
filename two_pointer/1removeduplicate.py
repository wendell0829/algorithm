"""
已排序数组去重
如[1, 2, 2, 2, 3, 3, 5]
返回[1, 2, 3, 5]保持排序
在原数组上更改,不需返回
"""
"""
思路:维护双指针i,j同向前进,j检测是否重复(与j-1是否相等),i负责空位
"""

def remove_duplicate(s:list[int])->None:
    i, j = 0, 1
    while j < len(s):
        if s[j] != s[j-1]:
            i += 1
            s[i] = s[j]
        j += 1
    print(s[:i+1])

s = [1, 2, 2, 2, 3, 3, 5]
remove_duplicate(s)
# print(s[:i+1])