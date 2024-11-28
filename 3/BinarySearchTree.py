import matplotlib.pyplot as plt
import networkx as nx

class Node:
    def __init__(self, data):
        self.left = self.right = None
        self.data = data

class Tree:
    def __init__(self):
        self.root = None

    def __find(self, node, parent, value):
        if node is None:
            return None, parent, False

        if value == node.data:
            return node, parent, True

        if value < node.data:
            if node.left:
                return self.__find(node.left, parent, value)

        if value > node.data:
            if node.right:
                return self.__find(node.right, parent, value)

        return node, parent, False

    def append(self, obj):
        if self.root is None:
            self.root = obj
            return obj

        new_node, new_parent, flag_find = self.__find(self.root, None, obj.data)

        if not flag_find and new_node:
            if obj.data < new_node.data:
                new_node.left = obj
            else:
                new_node.right = obj

        return obj

    def build_balanced_tree(self, values):
        def build_tree(sorted_values):
            if not sorted_values:
                return None
            mid = len(sorted_values) // 2
            root = Node(sorted_values[mid])
            root.left = build_tree(sorted_values[:mid])
            root.right = build_tree(sorted_values[mid + 1:])
            return root
        self.root = build_tree(sorted(values))


    def show_wide_tree(self, node):
        if node is None:
            return
        vertex = [node]
        while vertex:
            vertex_1 = []
            for node in vertex:
                print(node.data, end=" ")
                if node.left:
                    vertex_1 += [node.left]
                if node.right:
                    vertex_1 += [node.right]
            print()
            vertex = vertex_1

    def plot_tree(self):
        def add_edges(graph, node, pos, x=0, y=0, level=1, dx=10):
            if node is not None:
                graph.add_node(node.data, pos=(x, y))
                if node.left:
                    graph.add_edge(node.data, node.left.data)
                    add_edges(graph, node.left, pos, x - dx / (2**level), y - 2, level + 1, dx)
                if node.right:
                    graph.add_edge(node.data, node.right.data)
                    add_edges(graph, node.right, pos, x + dx /(2 ** level), y - 2, level + 1, dx)

        G = nx.DiGraph()
        pos = {}
        if self.root:
            add_edges(G, self.root, pos)

        pos = nx.get_node_attributes(G, 'pos')

        plt.figure(figsize=(12, 8))
        nx.draw(G, pos, with_labels=True, node_size=1200, node_color="pink", font_size=10, font_weight=400, arrowsize=20)
        plt.show()

x = 4
a_0 = 1

tree = Tree()
current_value = a_0
seen_values = set()

while current_value not in seen_values:
    seen_values.add(current_value)
    current_value = (current_value * (x + 5)) % 700

tree = Tree()
tree.build_balanced_tree(list(seen_values))
tree.show_wide_tree(tree.root)
tree.plot_tree()


