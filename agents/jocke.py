from sprites import Agent


def next_permutation(arr):
    # Find the largest index i such that arr[i] < arr[i + 1]. If no such
    # index exists, the permutation is the last permutation
    for i in reversed(range(len(arr) - 1)):
        if arr[i] < arr[i + 1]:
            break  # found
    else:  # no break: not found
        return False  # no next permutation

    # Find the largest index j greater than i such that arr[i] < arr[j]
    j = next(j for j in reversed(range(i + 1, len(arr))) if arr[i] < arr[j])

    # Swap the value of arr[i] with that of arr[j]
    arr[i], arr[j] = arr[j], arr[i]

    # Reverse sequence from arr[i + 1] up to and including the final element arr[n]
    arr[i + 1:] = reversed(arr[i + 1:])
    return True


class Jocke(Agent):
    def __init__(self, x, y, file_name):
        super().__init__(x, y, file_name)

    def get_agent_path(self, coin_distance):
        path = [i for i in range(1, len(coin_distance))]
        best_path = None
        min_cost = None
        while True:
            # calculate cost
            curr_cost = 0
            for i in range(1, len(path)):
                curr_cost += coin_distance[path[i - 1]][path[i]]

            # add distances from and to the 0-th node
            curr_cost += coin_distance[0][path[0]]
            curr_cost += coin_distance[path[-1]][0]

            if min_cost is None or curr_cost < min_cost:
                min_cost = curr_cost
                best_path = [0] + path + [0]

            if not next_permutation(path):
                return best_path
