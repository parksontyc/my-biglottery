from secrets import SystemRandom
from itertools import combinations
from show import show_number
from prize import winner_number


def pick_7(groups):
    list_1st = list(range(1, 50))

    counts = {i: 0 for i in range(1, 50)}

    # 取出7組, result就是用來放7組數字
    result = []
    for i in range(groups):
        # 取出7個數字, numbers放7個數字
        numbers = []
        while len(numbers) < groups:
            if not list_1st:
                list_1st = list(range(1, 50))
            SystemRandom().shuffle(list_1st)
            num = list_1st.pop(0)

            # 檢查數字是否重複, 並計數
            if num in numbers:
                continue
            else:
                numbers.append(num)
                counts[num] += 1

        result.append(numbers)

    return result, counts


def get_combinations(numbers, group_size):
    result = []
    count = 0
    for i in range(7):
        number = numbers[i]
        for sub in combinations(number, group_size):
            num = list(sub)
            count += 1
            result.append(num)
    return result, count


if __name__ == "__main__":
    group_1st, count_1st = pick_7(7)
    # print(group_1st)
    print(count_1st)
    combinations, count = get_combinations(group_1st, 6)
    # print(combinations)
    print(count)
    show_number(combinations)
    winner_number(combinations)
