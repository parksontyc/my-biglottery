from secrets import SystemRandom
from show import show_number
from prize import winner_number


def pick_group(num):
    list_1st = list(range(1, 50))

    counts = {i: 0 for i in range(1, 50)}

    result = []
    for i in range(num):
        numbers = []
        while len(numbers) < 6:
            if not list_1st:
                list_1st = list(range(1, 50))
            SystemRandom().shuffle(list_1st)
            num = list_1st.pop(0)

            if num in numbers:
                continue
            else:
                numbers.append(num)
                counts[num] += 1
        result.append(numbers)

    return result, counts


if __name__ == "__main__":
    result, count = pick_group(9)
    print(result)
    show_number(result)
    winner_number(result)
    print(count)
