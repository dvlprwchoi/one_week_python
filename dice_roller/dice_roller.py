from random import randint

dice_num = int(input('How many dice are we rolling?'))
side_num = int(input('How many sides on each die?'))

while True:
    result = '|'
    for dice in range(1, dice_num+1):
        rand = str(randint(1, side_num))
        result += f'{rand}|'
    print(result)
    user_action = input("Roll again? ('q' to quit)")
    if user_action == 'q':
        quit()
