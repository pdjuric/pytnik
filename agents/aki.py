from sprites import Agent


class Aki(Agent):
    def __init__(self, x, y, file_name):
        super().__init__(x, y, file_name)

    def get_agent_path(self, coin_distance):
        collected = [True] + [False] * (len(coin_distance) - 1)
        node_cnt = len(coin_distance)
        path = [0]
        while len(path) < node_cnt:
            next_coin = min([(coin_distance[path[-1]][i], i) for i in range(node_cnt) if not collected[i]])[1]
            collected[next_coin] = True
            path.append(next_coin)
        path.append(0)
        return path

