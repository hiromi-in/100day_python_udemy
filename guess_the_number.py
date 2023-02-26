#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo
from replit import clear

def guess_num_game():
  print(logo)
  picked_num = random.randint(1,100)
  print("Welcome to the Number Guessing Game!\nI\'m thinking of a number between 1 and 100.")
  #print(f"The number is {picked_num}.")

  level = input("Choose a difficulty. Type \'easy\' or \'hard\': ").lower()
  life = 0
  if level == 'easy':
    life = 10
  elif level == 'hard':
    life = 5
  else:
    life = -1
  
  while life > 0:

    print(f"\nYou have {life} attempts remaining to guess the number.")
    guess_num = int(input('Make a guess: '))

    if guess_num > picked_num:
      print("Too high.")
      life -=1
    elif guess_num < picked_num:
      print('Too low.')
      life -= 1
    elif guess_num == picked_num:
      break
    if life != 0:
      print('Guess again.')
  
  if life == 0:
    print(f"\nYou lost. The answer was {picked_num}😑")
  elif life >0:
    print(f"\nYou got it! The answer was {picked_num}🥳")
  elif life == -1:
    print(f'\nYou didn\'t type the correct word. You lost. The answer was {picked_num}🤢')

  game_continue = input("\nType 'y' to play again, and 'n' to quit.")
  if game_continue == 'y':
    clear()
    guess_num_game()
  elif game_continue == 'n':
    print("\nGood bye. Please play again sometime.😙")
  else:
    print("\nInvalid answer. Game is over. Good bye!🥲")

guess_num_game()
