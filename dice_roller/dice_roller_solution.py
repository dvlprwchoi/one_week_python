from random import randint
num_dice = int(input("how many dice are you rolling? "))
num_sides = int(input("how many sides on each die? "))

while True:
    result ="|"
    for die in range(num_dice):
        rand = randint(1,num_sides)
        result += f"{rand}|"
    print(result)
    reply = input("Roll again? (q to quit)")
    if reply == "q":
        break
