import random

while True:

    uNum = input("ENTER rock, paper, scissors or quit : ")
    rNum = random.randint(0,9)

    print("PLAYER CHOSE : ", uNum)

    if uNum == 'quit':
        break
    elif rNum <= 3:
        result = 'rock'
    elif rNum > 3 and rNum <= 6:
        result = 'paper'
    elif rNum > 6 and rNum <=9:
        result = 'scissors'

    print('')

    value1 = 'rock'
    value2 = 'paper'
    value3 = 'scissors'

    #sol1 = value2 > value1
    #sol2 = value3 > value2
    #sol3 = value1 > value3

   
    print("COMPUTER CHOSE : ", result)

    if uNum == result:
        print("DRAW")
    elif uNum == value2 and result == value1:
        print("PLAYER WINS...")
    elif uNum == value3 and result == value2:
        print("PLAYER WINS...")
    elif uNum == value1 and result == value3:
        print("PLAYER WINS...")
    elif result == value2 and uNum == value1:
        print("COMPUTER WINS...  :)")
    elif result == value3 and uNum == value2:
        print("COMPUTER WINS...  :)")
    elif result == value1 and uNum == value3:
        print("COMPUTER WINS...  :)")
    else:
        continue
