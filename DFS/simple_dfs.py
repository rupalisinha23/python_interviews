# non-recursive
def dfs_nonrecur(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


# recursive
def dfs_recur(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs_recur(graph, next, visited)
    return visited


graph = {'A': {'B', 'C'},
         'B': {'A', 'D', 'E'},
         'C': {'A', 'F'},
         'D': {'B'},
         'E': {'B', 'F'},
         'F': {'C', 'E'}}

dfs_nonrecur(graph, 'C') # {'E', 'D', 'F', 'A', 'C', 'B'}
dfs_recur(graph, 'A') # {'E', 'D', 'F', 'A', 'C', 'B'}
