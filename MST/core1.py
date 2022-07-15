import csv
import random
import matplotlib.pyplot as plt


# 用一个字典表示图
# {
#   Node1:
#       {neighbour1: weight1, neighbour2: weight2, ...},
#   Node2: ...
# }

def load_csv(filename='test_graph.csv'):
    # 读取csv文件将图的信息保存到graph
    graph = {}

    with open(filename, 'r') as f:
        # 打开csv文件
        csv_reader = csv.reader(f)
        # 按行读取，每行为一个list，第一个元素为node，后续奇数节点为node， 偶数节点为权重
        for row in csv_reader:
            node = str(row[0])
            graph[node] = {}
            for i in range(1, len(row)):
                if i % 2 == 1:
                    neighbour = str(row[i])
                    weight = int(row[i + 1])
                    graph[node][neighbour] = weight
    return graph

def print_graph(graph:dict, info=True):
    if info:
        print('node number: ', node_number(graph))
        print('edge number: ', edge_number(graph))
        print('total weight: ', get_total_weight(graph))
    else:
        for k, v in graph.items():
            print(k, ':', v)


def is_cycling(graph:dict):
    # 判断一个图是否有环
    # 基本思路：深度优先搜索
    # 对于每个节点，考察它的子节点，若：
    #   1. 该节点是正在考察的上一级节点，跳过（因为图是无向图，两个连通节点必然互为父子节点）
    #   2. 该节点未被考察过，标记为考察过（加入visited_node)，继续考察该节点的所有子节点
    #   3. 该节点已被考察过，则有环
    # 例如从A出发，考察B的子节点：
    #   1. A，跳过
    #   2. C，未被考察过，加入考察过的列表，然后考察C的所有子节点：
    #       1. A，已被考察过，说明有环，判断结束
    # 全部遍历完毕后没有返回True则说明无环
    def dfs(node, father_node=None):
        for neighbor_node in graph.get(node).keys():
            if neighbor_node == father_node:
                continue
            elif neighbor_node in visited_node:
                return True
            else:
                visited_node.append(neighbor_node)
                if not dfs(neighbor_node, node):
                    continue
                else:
                    return True
        return False

    visited_node = [list(graph.keys())[0]]
    return dfs(visited_node[0])


def get_edge_list(graph:dict):
    # 获取图里的所有边
    # 每个边用一个三元元组表示（node1, node2, weight)
    edge_list = []
    for node1, neighbour_list in graph.items():
        for node2, weight in neighbour_list.items():
            egde = (node1, node2, weight)
            egde_reverse = (node2, node1, weight)
            # 注意同一条边只添加1次
            # 如（A, B, 7) 和 （B， A， 7）不重复添加
            if (egde not in edge_list) and (egde_reverse not in edge_list):
                edge_list.append(egde)
    return edge_list


def get_new_edge_list(graph:dict, graph_mst:dict, new_node):
    # prime算法中，获取mst里新加入的点所有对外连接的边
    # 每个边用一个三元元组表示（node1, node2, weight)
    edge_list = []
    neighbour_list = graph.get(new_node)
    # print(graph)
    # print(neighbour_list)
    for node2, weight in neighbour_list.items():
        if node2 in graph_mst.keys():
            pass
        else:
            edge = (new_node, node2, weight)
            edge_list.append(edge)
    return edge_list


def add_edge(graph:dict, edge:tuple):
    # 向图中加入一条边
    # 注意边的两个点要互相添加邻居和权重
    node1, node2, weight = edge
    if graph.get(node1):
        graph[node1].update({node2: weight})
    else:
        graph[node1] = {node2: weight}
    if graph.get(node2):
        graph[node2].update({node1: weight})
    else:
        graph[node2] = {node1: weight}


def remove_edge(graph:dict, edge:tuple):
    # 从图中去掉一条边
    # 与添加一条边相反，注意两个点都要去掉邻居
    node1, node2, weight = edge
    if graph[node1].get(node2):
        graph[node1].pop(node2)
    if graph[node2].get(node1):
        graph[node2].pop(node1)


def edge_number(graph):
    # 返回一个图的边的数量
    return len(get_edge_list(graph))


def node_number(graph):
    # 返回一个图的点的数量
    return len(graph.keys())


def get_total_weight(graph):
    # 返回一个图的总权重的数量
    total_weight = 0
    for node1, neighbour_list in graph.items():
        for node2, weight in neighbour_list.items():
            total_weight += weight
    return total_weight/2


def generate_mst_kruskal(graph):
    # 通过kruskal算法寻找mst
    # 显然mst也是一个graph
    graph_mst = {}
    # 取出图中的所有边，并按权重大小排序
    edge_list = get_edge_list(graph)
    edge_list.sort(key=lambda i:i[2])
    for edge in edge_list:
        # 按权重从小到大依次尝试加入mst中，每次加入后判断是否有环
        # 如果有环就将这条边剔除（因为mst中不可能有环）
        # 直到mst中边的数量达到原图中顶点数量-1，mst完成
        add_edge(graph_mst, edge)
        if is_cycling(graph_mst):
            remove_edge(graph_mst, edge)
        if edge_number(graph_mst) >= node_number(graph) - 1:
            break
    return graph_mst


def generate_mst_prime(graph):
    # 通过prime算法寻找mst
    # 显然mst也是一个graph
    # 首先随便找一个点作为起点，其他点作为一个整体
    # 选择起点到达其他点的最短边加入mst
    graph_mst = {}
    node = list(graph.keys())[0]
    graph_mst[node] = dict()
    edge_list = get_new_edge_list(graph, graph_mst, node)
    edge_list.sort(key=lambda i:i[2])
    while True:
        # 重复以下过程
        # 1. 确定新的起点
        # 2. 将新的起点连接剩下的点的边加入待选列表
        # 3. 待选列表按权重排序
        # 4. 选择权重最小的边加入mst，但是注意该边的两个顶点都已在mst中存在的话则跳过，避免成环
        edge_list_copy = edge_list.copy()
        for i, edge in enumerate(edge_list_copy):
            if (edge[0] in graph_mst.keys()) and (edge[1] in graph_mst.keys()):
                edge_list.remove(edge)
            else:
                edge = edge
                add_edge(graph_mst, edge)
                break
        if edge_number(graph_mst) >= node_number(graph) - 1:
            break
        new_node = edge[1]
        edge_list.extend(get_new_edge_list(graph, graph_mst, new_node))
        edge_list.sort(key=lambda i:i[2])

    return graph_mst


def generate_random_graph(node_number=100, edge_number=1000):
    # 按照输入的点的数量和边的数量生成随机图
    # 注意点的数量和边的数量要匹配，设点的数量为n，边的数量最多为n(n-1)/2
    graph = {}
    for i in range(node_number):
        node_start = str(i)
        j = 0
        if not graph.get(node_start):
            graph[node_start] = dict()
        while j < edge_number//node_number:
            node_end = str(random.randint(0, node_number-1))
            if node_start == node_end:
                continue
            else:
                weight = random.randint(5, 20)
                if graph[node_start].get(node_end):
                    continue
                else:

                    add_edge(graph, (node_start, node_end, weight))
                    j += 1
                    continue
    return graph


def compare_against_different_edges():
    # 对比不同数量的边的情况下两种算法的时间差异
    # 点的数量固定为100，边从500递增至4000
    edge_number_list = []
    kruskal_time_list = []
    prime_time_list = []

    for i in range(5, 40, 5):
        graph = generate_random_graph(100, i*100)
        import time
        time1 = time.time()
        graph_mst1 = generate_mst_kruskal(graph)
        time2 = time.time()
        graph_mst2 = generate_mst_prime(graph)
        time3 = time.time()
        edge_number_list.append(i*100)
        kruskal_time_list.append(time2-time1)
        prime_time_list.append(time3-time2)

    plt.plot(edge_number_list, kruskal_time_list, label='kruskal', color='orange', marker='o')
    plt.plot(edge_number_list, prime_time_list, label='prime', color='blue', marker='o')
    plt.xlabel("Edge number")
    plt.ylabel("time(s)")
    plt.title("Compare against different edge numbers")
    plt.legend(loc='upper left')
    plt.show()


def compare_against_different_nodes():
    # 对比不同数量的边的情况下两种算法的时间差异
    # 点的数量固定为100，边从500递增至4000
    node_number_list = []
    kruskal_time_list = []
    prime_time_list = []

    for i in range(10, 500, 50):
        graph = generate_random_graph(100, 1000)
        import time
        time1 = time.time()
        graph_mst1 = generate_mst_kruskal(graph)
        time2 = time.time()
        graph_mst2 = generate_mst_prime(graph)
        time3 = time.time()
        node_number_list.append(i)
        kruskal_time_list.append(time2-time1)
        prime_time_list.append(time3-time2)

    plt.plot(node_number_list, kruskal_time_list, label='kruskal', color='orange', marker='o')
    plt.plot(node_number_list, prime_time_list, label='prime', color='blue', marker='o')
    plt.xlabel("Node number")
    plt.ylabel("time(s)")
    plt.title("Compare against different node numbers")
    plt.legend(loc='upper left')
    plt.show()

if __name__ == '__main__':
    while True:
        print('Input the number to enter the module:\n'
              '1. import a new graph via csv files\n'
              '2. output the adjacency list as a table\n'
              '3. find MST using kruskal\n'
              '4. find MST using prime\n'
              '5. compare algorithm running times\n'
              '6. exit'
              )
        cmd = input('>>')
        try:
            cmd = int(cmd)
        except:
            print('unknown command')
            continue

        if cmd == 1:
            filename = input('please input your filename of csv file:\n>>')
            if filename:
                try:
                    graph = load_csv(filename)
                    print('Succeed.')
                except:
                    print('Failed, please check the filename')
                    continue
            else:
                continue
        elif cmd == 2:
            try:
                print_graph(graph, info=False)
                print('*' * 20)
            except:
                print('No graph here, please load one first')
                continue
        elif cmd == 3:
            try:
                graph_mst = generate_mst_kruskal(graph)
                print('*'*20)
                print('The answer of Kruskal:')
                print('The MST information:')
                print_graph(graph_mst, info=True)
                print('The MST table:')
                print_graph(graph_mst, info=False)
                print('*' * 20)
            except:
                print('No graph here, please load one first')
                continue

        elif cmd == 4:
            try:
                graph_mst = generate_mst_prime(graph)
                print('*' * 20)
                print('The answer of Prime:')
                print('The MST information:')
                print_graph(graph_mst, info=True)
                print('The MST table:')
                print_graph(graph_mst, info=False)
                print('*' * 20)
            except:
                print('No graph here, please load one first')
                continue
        elif cmd == 5:
            print('waiting...')
            compare_against_different_edges()
            compare_against_different_nodes()
            continue
        elif cmd == 6:
            print('byebye')
            break
        else:
            print('unknown command')
            continue