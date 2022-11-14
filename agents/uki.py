from sprites import Agent


def advance(curr_path, curr_cost, new_path, new_cost):
    return new_cost > curr_cost \
           or new_cost == curr_cost and len(new_path) < len(curr_path) \
           or new_cost == curr_cost and len(new_path) == len(curr_path) and new_path[-1] > new_path[-1]


def get_pq_index(priority_queue, new_path,  new_cost):
    next_index = 0
    while next_index < len(priority_queue):
        curr_path, curr_cost = priority_queue[next_index][0:1]
        if advance(curr_path, curr_cost, new_path, new_cost):
            next_index += 1
        else:
            break
    return next_index


class Uki(Agent):
    def __init__(self, x, y, file_name):
        super().__init__(x, y, file_name)

    def get_agent_path(self, coin_distance):
        node_cnt = len(coin_distance)
        # [path, cost, visited]
        pq = [[[0], 0, [True] + [False for _ in range(1, node_cnt)]]]
        while len(pq) > 0:
            curr_path, curr_cost, curr_visited = pq.pop(0)

            if len(curr_path) == node_cnt:
                curr_cost += coin_distance[curr_path[-1]][0]
                curr_path += [0]

                idx = get_pq_index(pq, curr_path, curr_cost)
                pq.insert(idx, [curr_path, curr_cost, curr_visited])

            elif len(curr_path) == node_cnt + 1:
                return curr_path

            else:
                for i in range(node_cnt):
                    if not curr_visited[i]:
                        next_visited = curr_visited.copy()
                        next_visited[i] = True
                        next_path = curr_path + [i]
                        next_cost = curr_cost + coin_distance[curr_path[-1]][i]

                        idx = get_pq_index(pq, next_path, next_cost)
                        pq.insert(idx, [next_path, next_cost, next_visited])
