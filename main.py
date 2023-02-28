from secrets import SystemRandom
from datetime import date, timedelta


def get_all_date(start_date: str, count: int) -> list:
    yy, mm, dd = int(start_date[0:4]), int(
        start_date[4:6]), int(start_date[6:8])
    d = date(yy, mm, dd)
    assert d.isoweekday() in [2, 5], "date '{}' is not Tue or Fri.\n".format(d)

    all_date = [d.strftime("%m/%d")]
    for i in range(count-1):
        if d.isoweekday() == 2:            # Tue->Fri
            d += timedelta(3)
        else:           # Fri->Tue
            d += timedelta(4)
        all_date.append(d.strftime("%m/%d"))

    return all_date


def get_draw(count: int):
    draw, distribution = [], {}

    for i in range(count*10000):
        tmp_draw = sorted(SystemRandom().sample(range(1, 50), 6))
        draw.append(tmp_draw)
        for j in tmp_draw:
            try:
                distribution[j] += 1
            except:
                distribution[j] = 1

    return SystemRandom().sample(draw, count), distribution


ID = input("Start ID(1yy000nnn, default=1): ")
ID = int(ID) if ID else 1
count = input("Period Count(1~n, default=1): ")
count = int(count) if count else 1
all_date = input("Start Date(20yymmdd, default=None): ")
all_date = get_all_date(all_date, count) if all_date else None
print_dist = input("Print Distribution(y/n, default=y): ")
print_dist = "n" if print_dist in ["n", "N"] else "y"

winner, distribution = get_draw(count)
with open("winner.txt", "w") as w:
    w.write("draw:\n")
    for i in range(ID, ID+count):
        w.write("{0}{1}: {2}\n".format(i,
                                       ", " +
                                       all_date[i-ID] if all_date is not None else "",
                                       winner[i-ID]))
    if print_dist == "y":
        w.write("\n===\ndistribution:\n")
        for i in range(1, 50):
            w.write("{0}: {1}/{2}\n".format(i,
                                            distribution[i], round(count*6*10000/49)))
