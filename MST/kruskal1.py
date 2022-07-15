import csv
import random


class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

    def is_same(self, edge):
        if self.start == edge.start and self.end == edge.end:
            return True
        elif self.start == edge.end and self.end == edge.start:
            return True
        return False

    def get_another_node(self, node):
        print(self, node)
        if node == self.start:
            return self.end
        elif node == self.end:
            return self.start
        else:
            return None

    def __eq__(self, other):
        return self.is_same(other)

    def __repr__(self):
        return f'{self.start.name}-{self.end.name}:{self.weight}'


class Node:
    def __init__(self, name, neighbor_list=None):
        self.name = name
        if neighbor_list:
            self.neighbor_list = neighbor_list
        else:
            self.neighbor_list = []

    def add_neighbor(self, node):
        if node not in self.neighbor_list:
            self.neighbor_list.append(node)

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
        neighbor_names = ' '.join([node.name for node in self.neighbor_list])
        return f'name: {self.name}  ' \
               f'neighbors: {neighbor_names}'


class Graph:
    def __init__(self):
        self.node_list = []
        self.edge_list = []

    @property
    def node_number(self):
        return len(self.node_list)

    @property
    def edge_number(self):
        return len(self.edge_list)

    @property
    def total_weight(self):
        total_weight = 0
        for edge in self.edge_list:
            total_weight += edge.weight
        return total_weight

    def load_csv(self, filename='test_graph.csv'):
        with open(filename, 'r') as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                node_start = Node(row[0])
                for i in range(1, len(row)):
                    if i % 2 == 1:
                        node_end = Node(row[i])
                        weight = int(row[i + 1])
                        self.add_edge(node_start, node_end, weight)
        self.generate_node_list()

    def generate_random_edges(self, node_number=100, edge_number=1000):
        print(node_number, edge_number, edge_number//node_number)
        for i in range(node_number):
            node_start = Node(str(i))
            j = 0
            while j < edge_number//node_number:
                node_end = Node(str(random.randint(0, node_number)))
                if node_start == node_end:
                    continue
                else:
                    weight = random.randint(5, 20)
                    if self.add_edge(node_start, node_end, weight):
                        j += 1
                    else:
                        continue
        self.generate_node_list()

    def is_cycling(self):
        self.visited_node = [self.node_list[0]]
        return self.dfs(self.node_list[0], Node(''))

    def dfs(self, node, father_node):
        for neighbor_node in node.neighbor_list:
            # print(neighbor_node)
            # print(node)
            # print(father_node)
            # print(self.visited_node)
            if neighbor_node == father_node:
                continue
            elif neighbor_node in self.visited_node:
                return True
            else:
                self.visited_node.append(neighbor_node)
                if not self.dfs(neighbor_node, node):
                    continue
                else:
                    return True
        return False

    def sort_edges_by_weight(self, edge_list:list):
        edge_list.sort(key=lambda edge:edge.weight)
        return edge_list

    def add_node(self, name):
        node = Node(name)
        if node in self.node_list:
            node = self.node_list[self.node_list.index(node)]
        else:
            self.node_list.append(node)
        return node

    def add_edge(self, node_start, node_end, weight):
        edge = Edge(node_start, node_end, weight)
        if edge not in self.edge_list:
            self.edge_list.append(edge)
            return True
        else:
            return False

    def get_edge_list(self, node):
        edge_list = []
        for edge in self.edge_list:
            if edge.start == node or edge.end == node:
                edge_list.append(edge)
        return edge_list

    def generate_node_list(self):
        self.node_list = []
        for edge in self.edge_list:
            node_start = self.add_node(edge.start.name)
            node_end = self.add_node(edge.end.name)
            node_start.add_neighbor(node_end)
            node_end.add_neighbor(node_start)

    def print_edge_list(self):
        for edge in self.edge_list:
            print(edge)

    def __repr__(self):
        return f'node number: {self.node_number}\n' \
               f'edge number: {self.edge_number}\n' \
               f'total weight: {self.total_weight}'

    def generate_mst_kruskal(self):
        graph_mst = Graph()
        self.edge_list = self.sort_edges_by_weight(self.edge_list)
        for edge in self.edge_list:
            graph_mst.edge_list.append(edge)
            graph_mst.generate_node_list()
            if graph_mst.is_cycling():
                graph_mst.edge_list.pop()
                graph_mst.generate_node_list()
            if graph_mst.edge_number >= self.node_number - 1:
                break
        return graph_mst

    def generate_mst_prime(self):
        graph_mst = Graph()
        node = self.node_list[0]
        edge_list = self.get_edge_list(node)
        edge_list = self.sort_edges_by_weight(edge_list)
        while True:
            for edge in edge_list:
                if edge in graph_mst.edge_list:
                    pass
                elif (edge.start in graph_mst.node_list) and (edge.end in graph_mst.node_list):
                    pass
                else:
                    graph_mst.add_edge(edge.start, edge.end, edge.weight)
                    graph_mst.generate_node_list()
                    if edge.start in graph_mst.node_list:
                        node = edge.end
                    else:
                        node= edge.start
                    break
            if graph_mst.edge_number >= self.node_number - 1:
                break
            edge_list.extend(self.get_edge_list(node))
            edge_list = self.sort_edges_by_weight(edge_list)
        return graph_mst


# graph.load_csv()
# graph.generate_random_edges()
# print(graph)
# print(graph.is_cycling())
# node_number_list = []
# edge_number_list = []
# kruskal_time_list = []
# prime_time_list = []
#
# for i in range(49, 510, 50):
#     graph = Graph()
#     graph.generate_random_edges(i, (i+input)*10)
#     import time
#
#     time1 = time.time()
#     graph_mst1 = graph.generate_mst_kruskal()
#     time2 = time.time()
#     graph_mst2 = graph.generate_mst_prime()
#     time3 = time.time()
#
#     node_number_list.append(i)
#     kruskal_time_list.append(time2-time1)
#     prime_time_list.append(time3-time2)
#
#     print(graph)
#     print(time2-time1)
#     print(time3-time2)
#
# import matplotlib.pyplot as plt
#
# plt.plot(node_number_list, kruskal_time_list, label='kruskal', color='orange', marker='o')
# plt.plot(node_number_list, prime_time_list, label='prime', color='blue', marker='o')
# plt.xlabel("Node number")
# plt.ylabel("time(s)")
# plt.title("Compare against different node numbers")
# plt.legend(loc='upper left')
# plt.show()

# graph_mst2.print_edge_list()

node_number_list = []
edge_number_list = []
kruskal_time_list = []
prime_time_list = []

for i in range(5, 40, 5):
    graph = Graph()
    graph.generate_random_edges(100, i*100)
    import time

    time1 = time.time()
    graph_mst1 = graph.generate_mst_kruskal()
    time2 = time.time()
    graph_mst2 = graph.generate_mst_prime()
    time3 = time.time()

    edge_number_list.append(i*100)
    kruskal_time_list.append(time2-time1)
    prime_time_list.append(time3-time2)

    print(graph)
    print(time2-time1)
    print(time3-time2)

import matplotlib.pyplot as plt

plt.plot(edge_number_list, kruskal_time_list, label='kruskal', color='orange', marker='o')
plt.plot(edge_number_list, prime_time_list, label='prime', color='blue', marker='o')
plt.xlabel("Edge number")
plt.ylabel("time(s)")
plt.title("Compare against different edge numbers")
plt.legend(loc='upper left')
plt.show()
