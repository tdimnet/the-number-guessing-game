"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():

    random_number = random.randint(1, 10)
    number_proposal = 0
    number_of_attempts = 0

    print("======")
    print("random_number", random_number)
    print("======")
    print("======")
    print("number_proposal", number_proposal)
    print("======")
    
    while random_number != number_proposal:
      number_proposal = int(input("Pick a number between 1 and 10: "))

      if number_proposal < 1 or number_proposal > 10:
        print("Please pick a number between 1 and 10")
      else:
        if number_proposal < random_number:
          print("It is higher")
        elif number_proposal > random_number:
          print("It is lower")

        number_of_attempts += 1
    
    print("Got it! It took you {} tries to find out the correct answer".format(number_of_attempts))


def main():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player: DONE
    2. Store a random number as the answer/solution: DONE
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower": DONE
      b. If the guess is less than the solution, display to the player "It's higher": DONE
    
    4. Once the guess is correct, stop looping, inform the user they "Got it": DONE
         and show how many attempts it took them to get the correct number: DONE
    5. Let the player know the game is ending, or something that indicates the game is over: DONE
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    print("------------------------------------")
    print("Welcome to the Number Guessing Game!")
    print("------------------------------------")

    start_game()


# Kick off the program by calling the start_game function.
main()
