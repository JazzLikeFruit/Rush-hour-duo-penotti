from code.classes import cars, board
from numpy import random
import csv

if __name__ == '__main__':
    datafile = "data/Rushhour6x6_1.csv"
    instance = board.Board(datafile)
    empty_board = instance.create_board(datafile)
    cardic = instance.load_cars(datafile)
    start = instance.load_board(empty_board)
    movements = 0
    times = 0
    records = []
    print(start)
    print()
    while times < 10:

        # car = input("which car? ").upper()
        # block = input("how many blocks? ")

        randomcar = random.choice(list(cardic))
        # print('Auto: ', randomcar, 'POS: ',
        #       "row", cardic[randomcar].row, "col", cardic[randomcar].col)
        ruimte = instance.check_space(randomcar)
        # print('Ruimte: ', ruimte)
        randommovement = random.choice(ruimte)
        # print('Verplaatsing: ', randommovement)

        if instance.move(randomcar, randommovement):
            movements += 1
            # print('\n\nGELUKT!!\n\n')
            # print('OUDE COORDS:', cardic[randomcar].col, cardic[randomcar].row)

            # print('NIEUWE COORDS: ',
            #       cardic[randomcar].col, cardic[randomcar].row)
            empty_board = instance.create_board(datafile)
            instance.load_board(empty_board)

            # print(randomcar, cardic[randomcar].col, cardic[randomcar].row)
            if randomcar == "X" and instance.cars[randomcar].row == 5:
                times += 1
                records.append(movements)
    records.sort()

    with open("results.csv", "a") as file:
        record = csv.writer(file, dialect="excel")
        record.writerow(records)

    # if instance.check_win() == True:
    #     print("win = true!")
    # else:
    #     print("win = false :(")

    # instance.car_output()
    # print("finit")
    # break

    # else:
    # print('\n\nerror!\n\n')
    # print(randomcar, cardic[randomcar].row, cardic[randomcar].col)
    # print('iteratie over')

    # print(instance.load_board(empty2_board))
