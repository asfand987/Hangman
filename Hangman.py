import random

#list of words for game
hangmanWords = ("Halloween","Hockey","Minnesota","Vikings","Twins","Timberwolves","Wild","Playstation","Achievement","Minecraft","Metallica","Portal","Xbox","Guitar")

#assigns radomized word to variable
randomWord = random.choice(hangmanWords)
3
def menu():
   print("""
Welcome to Hangman!

Select a difficulty:
1. Easy (9 Misses)
2. Medium (7 Misses)
3. Advanced (5 Misses)

4. Exit Game
""")
   selection = int(input("What difficulty do you pick (1-4)?: "))
   return selection

def game(mode):
   
    modes = {1:9, 2:7, 3:5} # Matches mode to guesses
    guesses = modes[mode]
    wrongGuesses = 0
    listOfGuesses = []
    # print(randomWord) Dont't print the solution!!

    # Get a random word which would be guessed by the user
    to_guess = random.choice(hangmanWords)
    to_guess = to_guess.lower()

    # The correctly guessed part of the word that we print after every guess
    guessed  = "#"*len(to_guess) # e.g. "Hangman" --> "#######"
    while(wrongGuesses != guesses):
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
   select = menu()
   while(select != 4):
      game(select)
      select = menu()

   print("You don't want to play today? :'(")

main()