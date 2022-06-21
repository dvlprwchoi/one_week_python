from ast import While


p1 = input("Enter player 1's name: ")
p2 = input("Enter player 2's name: ")
player = p1
winner = None

toothpick_num = 13
while toothpick_num >= 0:
    print('|'*toothpick_num)
    print(f'There are {toothpick_num} toothpicks left')
    choice_num = int(input(f'How many do you take, {player}? '))
    while choice_num != 1 and choice_num != 2 and choice_num != 3:
        choice_num = int(input(f'You can only take 1, 2, or 3: '))

    toothpick_num -= choice_num
    if toothpick_num <= 0:
        winner = player
        print(f'{winner} wins!!!\nGAME OVER!!!')
        break
    if player == p1:
        player = p2
    else:
        player = p1


# | | | | | | | | | | | | |
# There are 13 toothpicks left
# How many do you take, Colt ?
# 3

# | | | | | | | | | |
# There are 10 toothpicks left
# How many do you take, Elton ?
# 2

# | | | | | | | |
# There are 8 toothpicks left
# How many do you take, Colt ?
# 3

# | | | | |
# There are 5 toothpicks left
# How many do you take, Elton ?
# 1

# | | | |
# There are 4 toothpicks left
# How many do you take, Colt ?
# 3

# |
# There are 1 toothpicks left
# How many do you take, Elton ?
# 1

# Elton wins!!!
# GAME OVER!!
