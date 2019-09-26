from collections import defaultdict
import itertools


# This class represents a directed graph using adjacency list
# representation
class Graph:
    """
    Minimum cost to connect all the nodes of a graph
    Status: Solved by Me
    """
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        return self

    def dfs(self, v, visited):
        # Mark the current node as visited
        visited[v] = True
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] is False:
                self.dfs(i, visited)

    def connected(self):
        visited = [False] * self.V
        self.dfs(0, visited)
        visited_or_not = [False if i is False else True for i in visited]
        if False in visited_or_not:
            return False
        return True


class Utils:
    @staticmethod
    def generate_combos(input_list):
        output_list = []
        for L in range(0, len(input_list) + 1):
            for subset in itertools.combinations(input_list, L):
                output_list.append(list(subset))
        return output_list


if __name__ == '__main__':
    input_costs = [(0, 1, 8), (0, 4, 3), (1, 3, 5), (2, 4, 4), (0, 2, 1)]
    num_vertices = 5
    present_edges = [(0, 3), (3, 4), (1, 2)]

    # function
    def min_conn_graph(vertices, edges, costs):
        sorted_costs = sorted(costs, key=lambda l: l[2])
        # print('sorted graph -> ' + str(sorted_costs))
        graph = Graph(vertices)
        for edge in edges:
            graph.add_edge(edge[0], edge[1])
        # print('connectivity current -> ' + str(graph.connected()))
        costs_list = []
        output_combos = Utils.generate_combos(sorted_costs)
        for combo in output_combos:
            if len(combo) != 0:
                graph_temp = None
                temp_cost = 0
                for element in combo:
                    graph_temp = graph.add_edge(element[0], element[1])
                    temp_cost = temp_cost + element[2]
                if graph_temp.connected():
                    costs_list.append(temp_cost)
        if not costs_list:
            return None
        return min(costs_list)

    # call function
    min_cost = min_conn_graph(num_vertices, present_edges, input_costs)
    print('The min cost is -> {}'.format(str(min_cost)))



