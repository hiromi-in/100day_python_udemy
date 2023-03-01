import art
from game_data import data
from random import randint
import os

score = 0
choice_a = randint(0, len(data)-1)
game_continue = True
print(art.logo)

while game_continue:
  choice_b = randint(0, len(data)-1)
  while choice_a == choice_b:
    choice_b = randint(0, len(data)-1)

  print(f"\nCompare A: {data[choice_a]['name']}, a {data[choice_a]['description']}, from {data[choice_a]['country']}.")
  print(art.vs)
  print(f"\nAgainst B: {data[choice_b]['name']}, a {data[choice_b]['description']}, from {data[choice_b]['country']}.")
  
  a_or_b = input("\nWho has more followers? Type 'A' or 'B': ").upper()

  follower_count_a = data[choice_a]['follower_count']
  follower_count_b = data[choice_b]['follower_count']

  def judge(input_a_or_b):
    if input_a_or_b == 'A':
      if follower_count_a > follower_count_b:
         return 'right'
      elif follower_count_a < follower_count_b:
         return 'wrong'
    elif input_a_or_b == 'B':
      if follower_count_a > follower_count_b:
         return 'wrong'
      elif follower_count_a < follower_count_b:
         return 'right'

  guess = judge(input_a_or_b = a_or_b)
 
  if guess == 'right':
    score += 1
    choice_b = choice_a
    os.system('clear')
    print(art.logo)
    print(f"You're right! Current score: {score}")
  elif guess == 'wrong':
    os.system('clear')
    print(art.logo)
    print(f"Sorry, that's wrong. Final score: {score}")
    if input("\nWhould you like to play again? Type 'y' to play again, or 'no' to quit.: ").lower() == 'n':
      print("Have a good day!🤗")
      game_continue = False
    
    

