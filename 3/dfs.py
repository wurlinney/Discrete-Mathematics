def dfs(graph, start, visited):
    visited.add(start)
    print(f"Посетили: {start}")
    for next in graph[start]:
        if next not in visited:
            dfs(graph, next, visited)


print("Необходимо задать граф с 10 вершинами и 20 ребрами.")
edges_num, vertex_num = 20, 10
edges = []
print("Введите пары чисел (откуда и куда идет ребро):")
for i in range(edges_num):
    where_from, where_to = map(int, input().split())
    edges.append((where_from, where_to))

graph = {}
for i in range(1, vertex_num + 1):
    graph[i] = []

for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

print("Алгоритм dfs для заданного графа:")
start_vertex = 1
dfs(graph, start_vertex, visited=set())