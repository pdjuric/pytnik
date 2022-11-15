from agents.pathinfo import PathInfo
from sprites import Agent
from heapq import heappush, heappop
from copy import deepcopy
import itertools


class Graph:
    def __init__(self, coin_distance):
        self.vertices_cnt = len(coin_distance)
        self.parent = None
        self.rank = None
        self.edges = [[u, v, coin_distance[u][v]] for u, v in itertools.product(range(self.vertices_cnt), range(self.vertices_cnt)) if u < v]
        self.edges.sort(key=lambda x: x[2])

    # A utility function to find set of an element i
    # (truly uses path compression technique)
    def find_set(self, i):
        if self.parent[i] != i:
            # Reassignment of node's parent to root node as
            # path compression requires
            self.parent[i] = self.find_set(self.parent[i])
        return self.parent[i]

    # A function that does union of two sets of x and y
    # (uses union by rank)
    def union(self, x, y):

        # Attach smaller rank tree under root of
        # high rank tree (Union by Rank)
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        elif self.rank[x] > self.rank[y]:
            self.parent[y] = x

        # If ranks are same, then make one as root
        # and increment its rank by one
        else:
            self.parent[y] = x
            self.rank[x] += 1

    # The main function to construct MST using Kruskal's
    # algorithm

    def heuristic(self, ignored_vertices):

        self.parent = [i for i in range(self.vertices_cnt)]
        self.rank = [0] * self.vertices_cnt

        # An index variable, used for sorted edges
        idx = 0
        cost = 0
        edge_cnt = 0

        # Number of edges to be taken is equal to V-1
        while edge_cnt < self.vertices_cnt - len(ignored_vertices) - 1:

            # Step 2: Pick the smallest edge and increment
            # the index for next iteration
            u, v, w = self.edges[idx]
            idx += 1

            if u in ignored_vertices or v in ignored_vertices:
                continue

            set_u = self.find_set(u)
            set_v = self.find_set(v)

            # If including this edge doesn't
            # cause cycle, then include it in result
            # and increment the index of result
            # for next edge
            if set_u == set_v:
                # Else discard the edge
                continue

            self.union(set_u, set_v)
            edge_cnt += 1
            cost += w

        return cost


class MickoPathInfo(PathInfo):
    def __init__(self, vertices: [int], cost: int):
        self.heuristic = 0
        super().__init__(vertices, cost)

    graph = None

    @staticmethod
    def set_graph():
        MickoPathInfo.graph = Graph(PathInfo.coin_distance)

    def get_cost(self):
        return self.heuristic + self.cost

    def calculate_cost(self):
        self.heuristic = MickoPathInfo.graph.heuristic(self.vertices[1:-1])


class Micko(Agent):
    def __init__(self, x, y, file_name):
        super().__init__(x, y, file_name)

    def get_agent_path(self, coin_distance):
        PathInfo.set_coin_distance(coin_distance)
        MickoPathInfo.set_graph()
        node_cnt = len(coin_distance)
        pq = [MickoPathInfo([0], 0)]
        while len(pq) > 0:
            path = heappop(pq)

            if len(path) == node_cnt + 1:
                return path.vertices

            elif len(path) == node_cnt:
                path.add_node(0)
                heappush(pq, path)

            else:
                for i in range(node_cnt):
                    if not path.contains(i):
                        next_path = deepcopy(path)
                        next_path.add_node(i)
                        heappush(pq, next_path)

        return None
