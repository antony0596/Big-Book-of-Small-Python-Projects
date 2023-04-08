import random
'''
 In Bagels, a deductive logic game, you must guess a secret three-digit number based on clues. The game offers one of the following hints in response to your guess: "Pico" when your guess has a correct digit in the wrong place, "Fermi" when your guess has a correct digit in the correct place, and "Bagels" if your guess has no correct digits. You have 10 tries to guess the secret number. 
'''

game_credits = '''Bagels: A Deductive Logic Game

By Al Sweigart al@inventwithpython.com
Code solution by Antony Fuentes me@tonyfweb.com'''
game_prompt = '''I am thinking of a 3-digit number.
Try to guess what it is.
Here are some clues:

"Pico" means the digit is
correct but in the wrong
position.

"Fermi" means that the digit
is correct and in the right
position.

"Bagel" means that the digit
is not correct.

I have thought of a number.
You have 10 guesses to get it.
'''
lost_game = 'Sorry, you did not guess correctly in 10 tries.'
random_number = None
guess = None

def start_game():
    print(f'{game_credits}\n\n{game_prompt}\n\n')
    random_number = str(random.randint(100, 999))

    # Show the number to guess for testing purposes
    #print(random_number)

    for i in range(10):
        guess = get_user_guess()
        check_chars(guess, random_number)
    
    print(lost_game)
    play_again()

def get_user_guess():
    '''
    Gets user input and checks if it's a valid guess
    '''
    while True:
        try:
            guess = int(input('Guess a three digit number: '))
            if guess < 100 or guess > 999:
                print(f'{guess} is not a three digit number.')
            else:
                guess = str(guess)
                return guess
        except ValueError:
            print('Invalid input.')

def check_chars(guess, random_number):
    if guess == random_number:
        print('Congratulations! Your guess is correct!')
        play_again()

    # Pico:  right number in wrong place
    # Fermi: right number in right place
    # Bagel: wrong number
    for char in guess:
        char_index = guess.index(char)
        if char not in random_number:
            print('Bagel')
        else:
            if char == random_number[char_index]:
                print('Fermi')
            else:
                print('Pico')

def play_again():
    while True:
        play_again = input('Do you want to play again? (yes or no): ')
        if play_again == 'yes' or play_again == 'y':
            start_game()
        elif play_again == 'no' or play_again == 'n':
            print('Thank you for playing!')
            exit()
        else:
            print('Invalid input.')

start_game()