rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))

if choice == 0:
  print(rock)
elif choice ==1:
  print(paper)
elif choice ==2:
  print(scissors)
else:
  print('Please type 0, 1 or 2.')

com_choice = random.randint(0,2)

print('Computer chose:')

if com_choice == 0:
  print(rock)
elif com_choice ==1:
  print(paper)
elif com_choice ==2:
  print(scissors)

if choice == 0 and com_choice == 0:
  print('You are tie!')
elif choice == 0 and com_choice == 1:
  print('You lost!')
elif choice == 0 and com_choice == 2:
  print('You won!')

if choice == 1 and com_choice == 1:
  print('You are tie!')
elif choice == 1 and com_choice == 2:
  print('You lost!')
elif choice == 1 and com_choice == 0:
  print('You won!')

if choice == 2 and com_choice == 2:
  print('You are tie!')
elif choice == 2 and com_choice == 0:
  print('You lost!')
elif choice == 2 and com_choice == 1:
  print('You won!')
