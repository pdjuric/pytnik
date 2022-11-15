from abc import abstractmethod


class PathInfo:
    def __init__(self, vertices: [int], cost: int):
        self.vertices = vertices
        self.cost = cost
        self.calculate_cost()

    coin_distance = None

    @staticmethod
    def set_coin_distance(coin_distance):
        PathInfo.coin_distance = coin_distance

    def __repr__(self):
        return f'nodes: {self.vertices} cost: {self.get_cost()}'

    def __lt__(self, other):
        return self.get_cost() < other.get_cost() \
               or self.get_cost() == other.get_cost() and len(self) > len(other) \
               or self.get_cost() == other.get_cost() and len(self) == len(other) and self.get_last_node() < other.get_last_node()

    def __len__(self):
        return len(self.vertices)

    def get_last_node(self):
        return self.vertices[-1]

    def add_node(self, node):
        self.cost += PathInfo.coin_distance[self.get_last_node()][node]
        self.vertices += [node]
        self.calculate_cost()

    def contains(self, node):
        return node in self.vertices

    def get_cost(self):
        pass

    def calculate_cost(self):
        pass
