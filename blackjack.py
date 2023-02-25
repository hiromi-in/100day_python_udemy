############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

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
    if computer_sum < 17:
      computer_cards.append(random.choice(cards))
  
  def final_result():
    print(f"\n  Your final hand: {your_cards}, final score: {your_sum}")
    print(f"  Computer's final hand: {computer_cards}, final score: {computer_sum}")

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

  def hand():
    print(f'  your cards: {your_cards}, current score: {your_sum}')
    print(f'  Computer\'s first card: {computer_cards[0]}')
    
      
      
  below21 = True
  play = input('\nDo you want to play a game of Blackjack? Type \'y\' or \'n\': ')
  if play == 'y':
    clear()
    print(logo)
    one_round()
    one_round()
    your_sum = sum(your_cards)
    computer_sum = sum(computer_cards)

    if your_sum != 21 and computer_sum != 21:
      hand()
      continue_game = input("Type 'y' to get another card, type 'n' to pass: ")
    else:
      continue_game = 'y'

  
    while below21:
      if 10 in your_cards and 11 in your_cards:
        final_result()
        print("Win with a blackjack!🤑")
        break
      elif 10 in computer_cards and 11 in computer_cards:
        final_result()
        print('Lose, computer has blackjack.🫥')
        break
        
      if continue_game == 'y':
        if your_sum  > 10:
          cards[0] = 1
        one_round()
        your_sum = sum(your_cards)
        computer_sum = sum(computer_cards)
      elif continue_game == 'n':
        result()
        break
        
      if 10 in your_cards and 11 in your_cards:
        final_result()
        print("Win with a blackjack!🤑")
        break
      elif 10 in computer_cards and 11 in computer_cards:
        final_result()
        print('Lose, computer has blackjack.🫥')
        break
        
      if your_sum < 21:
        hand()
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
 


















##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

