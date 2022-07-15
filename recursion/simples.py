# 递归的一些简单例子


# 1. 阶乘
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


"""
2. 绘制标尺
给定一个最大尺寸和最大尺寸的标线长度，比如最大尺寸为2，对应的标线长度为3（即3个-）
那么中间应该是一个2个-代表的1，1和0之间又会有一个1个-代表的1/2（非整数不标注）
递归思路：
边界条件：标线长度为1时  直接画出即可
重复逻辑：
    1> 计算中央刻度的标线长度（上一次中央刻度标线长度-1）
    2> 绘制以(该中央刻度-1)为中央刻度的标尺
    3> 绘制该中央刻度线
    4> 绘制以(该中央刻度-1)为中央刻度的标尺
---0
-
--1
-
---2
"""


def draw_line(n, m=-1):
    # 画标线长度为n，尺寸为m的刻度，m默认为-1，不打印
    print('-' * n, end='')
    if m != -1:
        print(int(m), end='')
    print()


def draw_interval(n):
    # 画一个间隔
    # 中央刻度的标线长度为n
    if n == 1:
        # 中间刻度线的标线长度为1时,画出这条刻度即可
        draw_line(1)
    else:
        # 中间刻度线的标线长度大于1时
        # 1> 画出上间隔，即中间刻度为n-1的间隔
        # 1> 画出中间刻度n本身
        # 1> 画出下间隔，即中间刻度为n-1的间隔
        draw_interval(n-1)
        draw_line(n)
        draw_interval(n-1)


def draw_ruler(min, max, n):
    # 画整体尺子
    # 画出最小值和最大值两条线，递归画出中间间隔
    while min<max:
        draw_line(n, min)
        draw_interval(n-1)
        min=min+1
    draw_line(n, max)


# 二分查找
def binary_search(sorted_list: list, low: int, high: int, goal: int) -> int:
    if low>high:
        return -1
    mid = (low+high)//2
    if sorted_list[mid] == goal:
        return mid
    elif sorted_list[mid] < goal:
        return binary_search(sorted_list, mid+1, high, goal)
    else:
        return binary_search(sorted_list, low, mid-1, goal)


# 斐波那契数列
def fibonacci(n:int)-> tuple[int, int]:
    if n<=1:
        return (n, 0)
    else:
        (a, b) = fibonacci(n-1)
        return (a+b, a)

if __name__ == '__main__':
    # print(factorial(3))
    # print("*" * 20)
    # draw_ruler(0, 1, 2)
    # print("*" * 20)
    # draw_ruler(0, 3, 3)
    # sorted_list = list(range(1, 1000, 2))
    # print(len(sorted_list))
    # result = binary_search(sorted_list, 0, len(sorted_list)-1, 507)
    # print(result, sorted_list[result])
    # for i in range(10):
    #     print(fibonacci(i))

    import sys
    print(sys.getrecursionlimit())
