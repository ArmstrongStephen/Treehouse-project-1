"""
Project 1 - Number Guessing Game
--------------------------------

For this first project you can use Workspaces. 

NOTE: If you prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random
import statistics

saved_attempts = []
high_score = []

# ask user if they want to play again, in N display median, mean, and mode or saved_attempts
def play_again():
    play_again = input("Would you like to play again? Y/N \n").lower()
    while play_again != 'y' and play_again != 'n':
        play_again = input("Would you like to play again? Y/N \n").lower()
    if play_again == 'y':
        start_game()
    elif play_again == 'n':
        median_guesses = statistics.median(saved_attempts)
        mode_guesses = statistics.mode(saved_attempts)
        average_guesses = round(sum(saved_attempts) / len(saved_attempts))

        print(f"The median of all guesses is {median_guesses}")
        print(f"The mode of all guesses is {mode_guesses}")
        print(f"The average number of guesses is {average_guesses}\n")
        print("****************************")
        print("***Thank you for playing!***")
        print("****************************")
        return True
        
    
# check is users guess is less than, equal to or higher than the hidden number
def check_guess(guess, winning_number, guess_count):
    if guess < winning_number:
        print("I'ts Higher")
    elif guess > winning_number:
        print("I'ts Lower")
    else:
        print("You Win!")
        saved_attempts.append(guess_count)
        return True
    if guess_count == 1:
        print(f"You have guessed {guess_count} time.\n")
    else: 
        print(f"You have guessed {guess_count} times.\n")
  

def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Save their attempt number to a list.
    6. At the end of the game, show the player, 1) their number of attempts, 2) the mean, median, and mode of the saved attempts list.
    7. Ask the player if they want to play again.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.

    number_of_guesses = 0
    winning_number = random.randint(1, 100)

    print("\n-----------------------------------------------")
    print("----- Welcome to the Number Guessing Game -----")
    print("-----------------------------------------------\n")
    if high_score == []:
        print(f"Current High Score: No current high score.")
    else:
        print(f"Current High Score: {min(high_score)}")
    

    while True:
      try:
          # verify guess is between 1 and 100. also checks that guess is a number
        guess = int(input("Pleas enter a number between 1 and 100: "))
        if guess < 1 or guess > 100:
          raise(ValueError)
      except ValueError:
        print("Invalid Input. Please enter a number between 1 and 100.")
      else:
        number_of_guesses += 1
        win = check_guess(guess, winning_number, number_of_guesses)
        if win == True:
            high_score.append(number_of_guesses)
            exit = play_again()
            if exit == True:
                break
    



# Kick off the program by calling the start_game function.
start_game()