print('WELCOME TO OUR USELESS STORE!')
print('*'*30)
item = input('What item are you purchasing?\t')
price = input(f'What is the price of {item}?\t')
number = input(f'How many {item} are you buying?\t')

print(f'Added {number} {item}(s) to shopping cart\nSubtotal: ${float(price)*float(number)}')
