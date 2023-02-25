import random
from art import logo
import os

def clear():
   os.system('clear')



def blackjack():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  your_cards = []
  computer_cards = []

  your_sum = sum(your_cards)
  computer_sum = sum(computer_cards)

  def one_round():
    your_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards)) 
  
  def final_result():
    print(f"\nYour final hand: {your_cards}, final score: {your_sum}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_sum}")

  def result():
    if your_sum <= 21 and your_sum > computer_sum:
             final_result()
             print("You are closer to 21. You win!🥳")
    elif your_sum <= 21 and computer_sum > 21:
             final_result()
             print("Opponent went over. You win!🥳")
    elif your_sum == computer_sum:
             final_result()
             print("Draw! Why don't you try again?😗")
    elif your_sum > 21:
             final_result()
             print("You went over. You lose.😭")
    elif your_sum < computer_sum:
             final_result()
             print("Opponent is closer to 21. You lose.😭")
    below21 = False 
    
  
  below21 = True
  play = input('\nDo you want to play a game of Blackjack? Type \'y\' or \'no\': ')
  if play == 'y':
    clear()
    print(logo)
    one_round()
    one_round()
    your_sum = sum(your_cards)
    computer_sum = sum(computer_cards)
    
    print(f'your cards: {your_cards}, current score: {your_sum}')
    print(f'Computer\'s first card: {computer_cards[0]}')
    continue_game = input("Type 'y' to get another card, type 'n' to pass: ")
  
    while below21:
      if continue_game == 'y':
        one_round()
        your_sum = sum(your_cards)
        computer_sum = sum(computer_cards)
      elif continue_game == 'n':
        result()
        
      
      if your_sum <= 21:
        print(f'\nyour cards: {your_cards}, current score: {your_sum}')
        print(f'Computer\'s first card: {computer_cards[0]}')
        continue_game = input("Type 'y' to get another card, type 'n' to pass: ")
        if continue_game == 'n':
          result()
          break
  
      elif your_sum > 21:
        final_result()
        print("You went over. You lose.😭")
        below21 = False
     
    blackjack()
  
  elif play == 'n':
    print("Good bye.🤗")
     
blackjack()
 
