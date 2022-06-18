from random import randint
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

computer_random_number = randint(0, 2)
if computer_random_number == 0:
    computer_input = 'rock'
elif computer_random_number == 1:
    computer_input = 'paper'
elif computer_random_number == 2:
    computer_input = 'scissors'


print('*'*50)
user_input = input('Enter your move:\t').lower()
if user_input == 'rock':
    print(f'YOUR MOVE:\n {rock}')
elif user_input == 'paper':
    print(f'YOUR MOVE:\n {paper}')
elif user_input == 'scissors':
    print(f'YOUR MOVE:\n {scissors}')
else:
    print('Wrong input! Try it again!')
    # input('enter your move:\t').lower()

print('*'*50)
if computer_input == 'rock':
    print(f'COMPUTER MOVE:\n {rock}')
elif computer_input == 'paper':
    print(f'COMPUTER MOVE:\n {paper}')
elif computer_input == 'scissors':
    print(f'COMPUTER MOVE:\n {scissors}')

print('*'*50)
if user_input == computer_input:
    print("It's a tie!")
elif (user_input == 'rock' and computer_input == 'scissors'):
    print('You win!')
elif (user_input == 'scissors' and computer_input == 'paper'):
    print('You win!')
elif (user_input == 'paper' and computer_input == 'rock'):
    print('You win!')
else:
    print('You lose!')
