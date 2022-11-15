from agents.pathinfo import PathInfo
from sprites import Agent
from heapq import heappush, heappop
from copy import deepcopy


class UkiPathInfo(PathInfo):
    def __init__(self, vertices: [int], cost: int):
        super().__init__(vertices, cost)

    def get_cost(self):
        return self.cost


class Uki(Agent):
    def __init__(self, x, y, file_name):
        super().__init__(x, y, file_name)

    def get_agent_path(self, coin_distance):
        PathInfo.set_coin_distance(coin_distance)
        node_cnt = len(coin_distance)
        pq = [UkiPathInfo([0], 0)]
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
