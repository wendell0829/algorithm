from decimal import Decimal


class LpSolver():
    # 解决状态
    # 无穷多解视为有解
    Solving = 0  # 求解中
    Solved = 1  # 已解决
    Unbounded = 9  # 无界解
    Infeasible = -1  # 无解

    def __init__(self, filename='input'):
        # 初始化规划问题，读取文件，生成标准形的约束方程的系数矩阵、目标函数的系数列表
        # 注意系数从文件中读取后需要做延拓，约束矩阵延拓一个单位阵，目标列表延拓0
        self.obj_co_list = []
        self.st_matrix = []
        self.st_co = []
        self.st_b = []
        self.load_file(filename)
        self._extend_init_matrix()
        self.state = LpSolver.Solving

    @property
    def variables_number(self):
        # 返回变量个数
        # 目标函数的系数个数减去系数为0的个数
        return len(self.obj_co_list) - self.obj_co_list.count(Decimal('0.0'))

    @property
    def constrains_number(self):
        # 返回约束条件个数
        return len(self.st_co)

    def load_file(self, filename):
        # 读取文件
        with open(filename, 'r') as f:
            obj_string = f.readline().strip()
            if obj_string:
                self.obj_co_list = [Decimal(i) for i in obj_string.split(' ')]
            for st_line in f.readlines():
                st_line = st_line.strip()
                if st_line:
                    st_line_list = [Decimal(i) for i in st_line.split(' ')]
                    self.st_b.append(st_line_list[-1])
                    self.st_co.append(st_line_list[:-1])

    def print_list(self, l):
        for i in l:
            print(f'{i:.7g}', end=' ')
        print()

    def print_problem(self):
        print('obj:', end='')
        self.print_list(self.obj_co_list)
        print('s.t.:')
        for line in self.st_matrix:
            self.print_list(line)

    def print_simplex(self):
        print('X_b:', end=' ')
        self.print_list(self.basic_variables_index)
        print('C_b:', end=' ')
        self.print_list(self.basic_variables_co)
        print('sigma:', end=' ')
        self.print_list(self.sigma_list)
        print('theta:', end=' ')
        self.print_list(self.theta_list)
        print('s.t.:')
        for line in self.st_matrix:
            self.print_list(line)
        print('solution:', end=' ')
        self.print_list(self.solution_list)
        print(f'optimal:{self.optimal:.7g}')

    def get_init_basic_variables(self):
        # 获取初始基变量，即松弛变量
        # 变量角标一律视为从0开始
        self.basic_variables_index = []
        for i in range(self.constrains_number):
            self.basic_variables_index.append(self.variables_number + i)
        self.get_basic_variables_co()

    def get_basic_variables_co(self):
        # 获取基变量的系数，按照基变量的角标在目标函数的列表中找
        self.basic_variables_co = []
        for i in self.basic_variables_index:
            co = self.obj_co_list[i]
            self.basic_variables_co.append(co)

    def _extend_init_matrix(self):

        self.obj_co_list.extend([Decimal('0.0')] * self.constrains_number)

        for i in range(self.constrains_number):
            row_vector = self.st_co[i]
            identity_vector = [Decimal('0.0')] * self.constrains_number
            identity_vector[i] = Decimal('1.0')
            row_vector.extend(identity_vector)
            row_vector.append(self.st_b[i])
            self.st_matrix.append(row_vector)

    def calculate_sigma_list(self):
        # 计算检验数
        # 对于每个变量，先获取目标函数中的系数作为初始值
        # 然后不断减去基变量的系数与约束系数的乘积
        self.sigma_list = []
        for i in range(len(self.obj_co_list)):
            sigma = self.obj_co_list[i]
            for j in range(len(self.st_matrix)):
                st_line = self.st_matrix[j]
                st_co = st_line[i]
                basic_co = self.basic_variables_co[j]
                sigma -= st_co * basic_co
            self.sigma_list.append(sigma)

    def get_in_basic_variable_index(self):
        # 获取换入基变量的角标
        # 即检验数列表中最大值的角标
        sigma_max = max(self.sigma_list)
        if sigma_max > 0:
            self.in_ = self.sigma_list.index(sigma_max)
        elif sigma_max == 0:
            self.state = LpSolver.Solved
        else:
            self.state = LpSolver.Solved

    def calculate_theta_list(self):
        # 计算θ
        # 当计算值小于0或者约束系数为0时，填充无穷大值
        self.theta_list = []
        for st_line in self.st_matrix:
            b = st_line[-1]
            co = st_line[self.in_]
            if co == 0:
                theta = Decimal('inf')
            elif b / co <= 0:
                theta = Decimal('inf')
            else:
                theta = b / co
            self.theta_list.append(theta)

    def get_out_basic_variable_index(self):
        # 获取换出基变量的角标
        # 即θ列表中最小值对应的基变量的角标
        theta_min = min(self.theta_list)
        if theta_min == Decimal('inf'):
            self.state = LpSolver.Unbounded
        else:
            self.out = self.basic_variables_index[self.theta_list.index(theta_min)]

    def change_st_matrix(self, m_row, m_col):
        # 做矩阵行变换进行高斯消元
        # 首先看m所在的行，如果m不为1，对所在行进行倍数放缩使m=1
        m = self.st_matrix[m_row][m_col]
        if m == 1:
            pass
        else:
            ratio = m / 1
            row = self.st_matrix[m_row]
            for i in range(len(row)):
                row[i] = row[i] / ratio

        # 然后看其他的每一行
        # 如果m所在列对应的元素不为0，减去相应倍数的m所在行
        row_m = self.st_matrix[m_row]
        m = row_m[m_col]

        for i, row in enumerate(self.st_matrix):
            if i == m_row:
                pass
            else:
                m_other = row[m_col]
                if m_other == 0:
                    pass
                else:
                    ratio = m_other / m
                    for i in range(len(row)):
                        row[i] = row[i] - ratio * row_m[i]

    def get_solution(self):
        # 获取最后结果
        # 最终基变量的值为原约束方程中的b值
        self.solution_list = [0] * len(self.obj_co_list)
        for row, index in enumerate(self.basic_variables_index):
            self.solution_list[index] = self.st_matrix[row][-1]

        # 如果最终基变量全部为松弛变量，则无解
        infeasible_flag = True
        for i in range(self.variables_number):
            if self.solution_list[i] > 0:
                infeasible_flag = False

        if infeasible_flag:
            self.state = LpSolver.Infeasible

        self.optimal = 0
        for i, co in enumerate(self.obj_co_list):
            self.optimal +=  self.solution_list[i] * co

    def simplex(self):
        self.get_init_basic_variables()
        while True:
            self.calculate_sigma_list()
            self.get_in_basic_variable_index()
            if self.state == LpSolver.Solved:
                break
            self.calculate_theta_list()
            self.get_out_basic_variable_index()
            if self.state == LpSolver.Unbounded:
                break
            m_row = self.basic_variables_index.index(self.out)
            m_col = self.in_
            self.basic_variables_index[m_row] = self.in_
            self.get_basic_variables_co()
            self.change_st_matrix(m_row, m_col)
        if self.state == LpSolver.Solved:
            self.get_solution()
            if self.state == LpSolver.Solved:
                result = f'optimal\n' \
                         f'{self.optimal:.7g}\n'
                for i in self.solution_list:
                    result += f'{i:.7g}  '
            else:
                result = 'infeasible'
        elif self.state == LpSolver.Unbounded:
            result = 'unbounded'
        else:
            result = 'infeasible'
        print(result)
        return result


if __name__ == '__main__':
    import sys
    filename = 'input'
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    solver = LpSolver(filename)
    solver.simplex()