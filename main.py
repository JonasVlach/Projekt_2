# Import of module random
import random


# Function for check random number conditions
def check_num(number):
    if len(str(number)) == len(set(str(number))) and str(number)[0] != 0:
        return True
    else:
        return False


# Function for generating number in range
def gen_num():
    while True:
        number = random.randint(1000, 9999)
        if check_num(number):
            return number


# Intro
print('''
Hi there!
--------------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
--------------------------------------------------
Enter a number:
--------------------------------------------------''')

# Generating of secret number
G_number = gen_num()

# Set the counter attempts
counter = 0

# Main
while True:
    cow, bull, i = 0, 0, -1
    text_b, text_c = 'bull', 'cow'
    guess = input()
    # Check conditions of user input
    if not guess.isdigit() or not len(guess) == 4 or not len(guess) == len(set(guess)) or guess[0] == '0':
        print('Incorrect entry. Enter a four-digit number without the same digits that does not begin with a zero.')

        continue
    else:
        counter += 1
        for num in guess:
            i += 1
            if str(num) == str(G_number)[i]:
                bull += 1
            elif str(num) in str(G_number):
                cow += 1

# Adding s when count is 1
    if bull != 1:
        text_b += 's'
    if cow != 1:
        text_c += 's'

# Print of result
    print(f'{bull} {text_b}, {cow} {text_c}')
    print(50 * '-')
    if bull == 4:
        break

# Rating of players result
rating = ['amazing', 'pretty good', 'average', 'not so good', 'terrible']
if counter < 6:
    rating = rating[0]
elif 5 < counter < 10:
    rating = rating[1]
elif 9 < counter < 13:
    rating = rating[2]
elif 12 < counter < 16:
    rating = rating[3]
else:
    rating = rating[4]

# Print of result and rating
print(f'Correct, you\'ve guessed the right number in {counter} guesses!')
print(f'That\'s {rating}!')
