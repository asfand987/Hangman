import random, time

#words to choose from.

fruits = ['pear', 'mango', 'apple', 'banana', 'apricot', 'pineapple','cantaloupe', 'grapefruit','jackfruit','papaya'] 
superHeroes = ['hawkeye', 'robin', 'Galactus', 'thor', 'mystique', 'superman', 'deadpool', 'vision', 'sandman']

randomWord = random.choice(fruits)


def setUp():
    print("Staring game of Hangman...")
    attempts = input("How many incorrect attempts do you want? ")
    print("Selecting a word")


def game():
    setUp()
    
    wrongGuesses  = 0
    listOfGuesses = []

    to_guess = random.choice(fruits)
    to_guess = to_guess.lower()

    guessed  = "#"*len(to_guess)
    
    print(guessed)

def main():
    game()

main()