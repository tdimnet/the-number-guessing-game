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
  
  while random_number != number_proposal:

    try:
      number_proposal = int(input("Pick a number between 1 and 10: "))
      
      if number_proposal < 1 or number_proposal > 10:
        print("Please pick a number between 1 and 10")
      else:
        if number_proposal < random_number:
          print("It is higher")
        elif number_proposal > random_number:
          print("It is lower")

        number_of_attempts += 1

    except ValueError:
      print("Incorrect value type, this program needs a number to work")
  
  print("Got it! It took you {} tries to find out the correct answer".format(number_of_attempts))
  return number_of_attempts


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

    is_playing = True
    high_score = start_game()

    while is_playing:
      is_playing = input('Do you want to play again?  [y]es/[n]o:  ')

      if is_playing == 'y':
        if high_score != 0:
          print("High score {}".format(high_score))
          game_score = start_game()
          if game_score < high_score:
            high_score = game_score
        is_playing = True
      elif is_playing == 'n':
        is_playing = False
      else:
        print("Incorrect input")

    print("Closing game, see you next time!")

# Kick off the program by calling the start_game function.
main()