def show_graph_properties(edges_list, m):
    adjacency_matrix = [[0] * m for _ in range(m)]
    for u, v in edges_list:
        adjacency_matrix[u - 1][v - 1] = 1

    reflexive = all(adjacency_matrix[i][i] == 1 for i in range(m))

    symmetric = True
    for i in range(m):
        for j in range(m):
            if adjacency_matrix[i][j] == 1 and adjacency_matrix[j][i] != 1:
                symmetric = False

    transitive = True
    for i in range(m):
        for j in range(m):
            for k in range(m):
                if adjacency_matrix[i][k] == 1 and adjacency_matrix[k][j] == 1 and  adjacency_matrix[i][j] != 1:
                    transitive = False

    return reflexive, symmetric, transitive



print("Введите количество рёбер и вершин:")
edges_num, vertex_num = map(int, input().split())
edges = []

print("Введите пары чисел (откуда и куда идет ребро):")
for i in range(edges_num):
    where_from, where_to = map(int, input().split())
    edges.append((where_from, where_to))

r, s, t = show_graph_properties(edges, vertex_num)
print("Рефлексивное" if r else "Не рефлексивное")
print("Симметричное" if s else "Антисимметричное")
print("Транзитивное" if t else "Не транзитивное")