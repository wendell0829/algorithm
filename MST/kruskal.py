import csv


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

    def sort_edges_by_weight(self):
        self.edge_list.sort(key=lambda edge:edge.weight)

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

    def get_edge_list(self, node):
        edge_list = []
        for edge in self.edge_list:
            if edge.start == node or edge.end == node:
                edge_list.append(edge)

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


def generate_mst(graph):
    graph_mst = Graph()
    graph.sort_edges_by_weight()
    for edge in graph.edge_list:
        graph_mst.edge_list.append(edge)
        graph_mst.generate_node_list()
        if graph_mst.is_cycling():
            graph_mst.edge_list.pop()
            graph_mst.generate_node_list()
        if graph_mst.edge_number >= graph.node_number - 1:
            break
    return graph_mst


graph = Graph()
graph.load_csv()
print(graph)
# print(graph.is_cycling())

graph_mst = generate_mst(graph)

print(graph_mst)
graph_mst.print_edge_list()

