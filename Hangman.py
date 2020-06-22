import random, time

#words to choose from.

fruits = ['pear', 'mango', 'apple', 'banana', 'apricot', 'pineapple','cantaloupe', 'grapefruit','jackfruit','papaya'] 
superHeroes = ['hawkeye', 'robin', 'Galactus', 'thor', 'mystique', 'superman', 'deadpool', 'vision', 'sandman']

randomWord = random.choice(fruits)


def game():
    print("Staring game of Hangman...")
    wrongGuesses  = input("How many incorrect attempts do you want? ")
    print("Selecting a word...")
    print("Word selected.")

    
    listOfGuesses = []

    to_guess = random.choice(fruits)
    to_guess = to_guess.lower()

    guessed  = "#"*len(to_guess) #e.g cat -> ###
    
    while(wrongGuesses != guessed):
        x = input("Word - %s . Guess a letter: "%guessed).lower()
        if x in to_guess:
            print(x,"is in the word!")
            listOfGuesses.append(x)
            # Now replace the '#' in 'guessed' to 'x' as per our word 'to_guess'
            new_guessed = ""
            for index, char in enumerate(to_guess):
                if char == x:
                    new_guessed += x
                else:
                    new_guessed += guessed[index]
            guessed = new_guessed # Change the guessed word according to new guess
            # If user has guessed full word correct, then he has won!
            if guessed == to_guess:
                print("You have guessed the word! You win!")
                print("The word was %s"%to_guess)
                return True # return true on winning
            else:
                print("Letters guessed so far:", listOfGuesses, "\n")

        else:
            print(x,"is not in the word.")
            wrongGuesses += 1
            print("Wrong guesses:", wrongGuesses)
            listOfGuesses.append(x)
            print("Letters guessed so far:", listOfGuesses, "\n")

        print("You lost the game!")
        print("The word was %s"%to_guess)
        return False # return false on loosing


def main():
    game()


main()