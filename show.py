

def show_number(result):
    # pass

    print('=========== Hit_Number ============')
    for i, sublist in enumerate([[str(num).zfill(2) for num in sublist] for sublist in result]):
        print(f'{str(i + 1).zfill(2)} : 1st : {sublist[0]} {sublist[1]} {sublist[2]} {sublist[3]} \
{sublist[4]} {sublist[5]} ')
