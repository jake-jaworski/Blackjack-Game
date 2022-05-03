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

import random
from art import logo



def card_deal():
  '''Deal a card'''
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def score_calculation(cards):
  '''Calculate score in hand'''
  score = sum(cards)
  if score == 21:
    return 0
  elif 11 in cards and score > 21:
    cards.remove(11)
    cards.append(1)
    return sum(cards)
  else:
    return score

def winner(user_score, dealer_score):
  '''Determine the winner'''
  if user_score == dealer_score:
    return "It's a draw!"
  elif dealer_score == 0:
    return "Dealer got a blackjack. You lose."
  elif user_score == 0:
    return "You got a blackjack. You win!"
  elif user_score > 21:
    return "Bust! You lose."
  elif dealer_score > 21:
    return "Dealer bust! You win!."
  elif user_score > dealer_score:
    return "You had the better hand. You win!"
  else:
    return "Dealer had the better hand. You lose."
    
def game():
  '''Runs the blackjack game'''
  print(logo)
  user_hand = []
  dealer_hand = []
  user_finished = True
  dealer_finished = True
  
  #deals cards to players
  for c in range(2):
    user_hand.append(card_deal())
    dealer_hand.append(card_deal())
  
  #user's turn
  while user_finished == True:
    #calculates scores and displays them
    user_score = score_calculation(user_hand)
    dealer_score = score_calculation(dealer_hand)
    print(f"Your hand: {user_hand}. Your score: {user_score}")
    print(f"Dealer hand showing: {dealer_hand[0]}")
    
    #checks if there is a winner and exits
    if user_score == 0 or dealer_score == 0 or user_score > 21:
      user_finished = False
    else:
      another_card = input("Do you want to hit? Type \"y\" to hit or \"n\" to stay.\n").lower()
      if another_card == "y":
        user_hand.append(card_deal())
      else:
        user_finished = False
  
  #dealer's turn
  while dealer_finished == True:
    if dealer_score != 0 and dealer_score < 17:
      dealer_hand.append(card_deal())
      dealer_score = score_calculation(dealer_hand)
    else:
      dealer_finished = False
  
  print(f"Your final hand was {user_hand} and a score of {user_score}.")
  print(f"The dealer's final hand was {dealer_hand} and a score of {dealer_score}.")
  print(winner(user_score, dealer_score))

  play_again = input("Do you want to play again? Type \"y\" to play again or \"n\" \n").lower()

  if play_again == "y":
    game()

game()

    

  
  