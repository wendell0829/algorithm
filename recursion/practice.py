"""
1. 最大值
"""
import copy


def find_max(s:list, n:int):
    if n==0:
        return s[0]
    else:
        if s[n] > find_max(s, n-1):
            return s[n]
        else:
            return find_max(s, n-1)

"""
10. 计算logN(2为底)
"""
def calculate_log(n):
    if n<=3:
        return 1
    else:
        return calculate_log(int(n/2))+1

"""
14. 汉诺塔
"""
def hanoi(n, t1, t2, t3):
    if n==1:
        print(t1+"->"+t2)
    else:
        hanoi(n-1, t1, t3, t2)
        print(t1 + "->" + t2)
        hanoi(n-1, t3, t2, t1)

"""
15. 含有n个元素的集合的所有子集（即n个元素的全组合）
思路： 
初始条件：集合为空，则输出空集
重复：函数主体是求某个集合的所有子集，每次移除一个元素
"""
def find_all_subset(s:set, result_list):
    if len(s)==0:
        result_list.append(s)
    else:
        n = s.pop()
        find_all_subset(s, result_list)
        copy_list = copy.deepcopy(result_list)
        for i in copy_list:
            i.add(n)
            result_list.append(i)


if __name__ == '__main__':
    # s = [1, 3, 5, 8, 2]
    # print(find_max(s, len(s)-1))
    # for i in range(4, 18):
    #     print(calculate_log(i))
    # hanoi(3, 'a', 'b', 'c')
    a = {1, 2, 3}
    # b = a.pop()
    # print(a, b)
    k = []
    find_all_subset(a, k)
    print(k)