"""
给你一个大小为mxn的矩阵mat ，请以对角线遍历的顺序，用一个数组返回这个矩阵中的所有元素。
输入：mat = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,4,7,5,3,6,8,9]
1 2 3
4 5 6
7 8 9
"""
"""
思路：
建立平面坐标系,向右为x+,向下为y+
显然，遍历方向有两种,初始时为(1,-1),越过边界后改变为(-1,1)
越过边界时还应注意更改起点,(1,-1)方向时优先向右平移,向右平移会越界时改为向下;(-1,1)方向同理易得
过程:
初始化方向direction\起点position\边界row和column\结果列表result_list\矩阵大小size
while len(result_list) < size:
    将当前位置的元素放入result_list
    按当前方向移动position得到new_position
        判断移动后的position是否越界(上或右)
        是:
            当前方向为(1,-1)时:
                position向右平移1,如仍会越界改为向下平移
            当前方向为(-1,1)时:
                position向下平移1,如仍会越界改为向右平移
        否:
            不改变
"""

def findDiagonalOrder(mat: list[list[int]]) -> list[int]:
    direciton_x, direction_y = 1, -1
    position_x, position_y = 0, 0
    result_list = []
    max_y = len(mat)-1
    max_x = len(mat[0])-1
    size = (max_x+1)*(max_y+1)
    while True:
        result_list.append(mat[position_y][position_x])
        if len(result_list) == size:
            break

        new_x = position_x+direciton_x
        new_y = position_y+direction_y
        if (0 <= new_x <= max_x) and (0 <= new_y <= max_y):
            position_x = new_x
            position_y = new_y
        else:
            if direciton_x==1:
                if position_x+1>max_x:
                    position_y += 1
                else:
                    position_x += 1
                direciton_x, direction_y = -1, 1
            else:
                if position_y+1>max_y:
                    position_x += 1
                else:
                    position_y += 1
                direciton_x, direction_y = 1, -1
    return result_list

if __name__ == '__main__':
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    print(findDiagonalOrder(mat))

