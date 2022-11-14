
from sprites import Agent


class Aki(Agent):
    def __init__(self, x, y, file_name):
        super().__init__(x, y, file_name)

    def get_agent_path(self, coin_distance):
        collected = [True] + [False for i in range(1, len(coin_distance))]
        path = [0]
        curr_coin = 0
        while len(path) < len(coin_distance):
            next_coin = None
            for i in range(len(coin_distance)):
                if not collected[i] and (next_coin is None or coin_distance[curr_coin][i] < coin_distance[curr_coin][next_coin]):
                    next_coin = i
            collected[next_coin] = True
            path.append(next_coin)
        path.append(0)
        return path

