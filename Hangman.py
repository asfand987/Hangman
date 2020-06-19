import random, time

#words to choose from.

fruits = ['pear', 'mango', 'apple', 'banana', 'apricot', 'pineapple','cantaloupe', 'grapefruit','jackfruit','papaya'] 
superHeroes = ['hawkeye', 'robin', 'Galactus', 'thor', 'mystique', 'superman', 'deadpool', 'vision', 'sandman']

userGuesslist = []
userGuesses = []
playGame = True
attempts = 0

def setUp():
    print("Staring game of Hangman...")
    attempts = input("How many incorrect attempts do you want? ")
    print("Selecting a word")


setUp()

