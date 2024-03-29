
#  ----------
#    PART 1
#  ----------
word = "supercalifragilisticexpialidocious"

# Write a for loop that prints out each character in the above "word" variable
print('*'*50)

for char in word:
    print(char)

print('*'*50)

# Write a while loop that does the same thing!

char_index = 0
while char_index < len(word):
    print(word[char_index])
    char_index += 1

print('*'*50)

#  ----------
#    PART 2
#  ----------
# Write a while loop that prints the even numbers from 100 to 140 (including 140)
print('*'*50)

num = 100
while num <= 140:
    if(num % 2 == 0):
        print(num)
    num += 1

print('*'*50)

# Write a for loop that does the same thing (with range())

for num in range(100, 141, 1):
    if(num % 2 == 0):
        print(num)

print('*'*50)

#  ----------
#    PART 3
#  ----------
# Write a loop that asks a user to input the passphrase "sillygoose" and keeps asking them to do so until they comply:

print('*'*50)
user_input = input('Type the passphrase here:\t').lower()

while user_input != 'sillygoose':
    user_input = input('Try it again:\t').lower()

print('Great!')

print('*'*50)
