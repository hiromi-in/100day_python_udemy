from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
secret_bid = {}
bidding_cycle = True

def bidding(bidder_name, bidded_amount):
  secret_bid[bidder_name] = bidded_amount

while bidding_cycle:

  name = input('What is your name?: ')
  bid = int(input('What is your bid?:  $'))

  bidding(bidder_name = name, bidded_amount = bid)

  other_bidders = input('Are there any other bidders? Type "Yes" or "No": ').lower()

  if other_bidders == 'yes':
    clear()
  elif other_bidders == 'no':
    bid = 0
    for key in secret_bid:
      if secret_bid[key] > bid:
        bid = secret_bid[key]
        winner = key
    print(f'The winner is {winner} with a bid of ${bid}!')
    bidding_cycle = False
