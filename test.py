from secrets import SystemRandom
from itertools import combinations


def get_draw(count: int):
    draw, distribution = [], {}

    for i in range(count*10000):
        tmp_draw = sorted(SystemRandom().sample(range(1, 50), 7))
        print(i, tmp_draw)
        draw.append(tmp_draw)
        for j in tmp_draw:
            try:
                distribution[j] += 1
            except:
                distribution[j] = 1

    return SystemRandom().sample(draw, count), distribution


def get_combinations(numbers, group_size):
    return [list(i) for i in list(combinations(numbers, group_size))]


data, count = get_draw(1)

combinations = get_combinations(data[0], 6)
print(combinations)
print(data)
