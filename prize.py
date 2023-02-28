import random


def winner_number(num_picker):

    winner_num = list(random.sample(range(1, 50), 6)) + [random.randint(1, 50)]
    # special_num = [random.randint(1, 50)]
    print()
    print(f'----本局獎號 : 1st : {winner_num[0:6]}  2nd : [{winner_num[6]}] ----')

    count = 0
    money_list = []
    for i, sublist in enumerate(num_picker):

        hit_count = len(set(sublist[:6]).intersection(set(winner_num[:6])))
        hit_number = list(set(sublist[:6]).intersection(set(winner_num[:6])))

        special_prize = hit_count == 6
        grand_prize = hit_count == 5 and winner_num[6] in sublist
        first_prize = hit_count == 5
        second_prize = hit_count == 4 and winner_num[6] in sublist
        if special_prize:
            money = 2000000000
            prize = '頭獎'
        elif grand_prize:
            money = 20000000
            prize = '貳獎'
        elif first_prize:
            money = 15000
            prize = '參獎'
        elif second_prize:
            money = 20000
            prize = '肆獎'
        elif hit_count == 4:
            money = 2000
            prize = '伍獎'
        elif hit_count == 3 and winner_num[6] in sublist:
            money = 1000
            prize = '陸獎'
        elif hit_count == 2 and winner_num[6] in sublist:
            money = 400
            prize = '柒獎'
        elif hit_count == 3:
            money = 400
            prize = '普獎'
        else:
            print(f"{i + 1}.都沒中!Q.Q")
            continue
        count += 1
        money_list.append(money)
        print(
            f'{i + 1}.{sublist}, 中獎號碼 {hit_number}  [{winner_num[6]}], 這注得到 {prize}, 獎金 {money} 元。')

    total_money = sum(money_list)
    print(f'共中獎 {count} 注, 獎金合計 {total_money} 元！')

    return num_picker
