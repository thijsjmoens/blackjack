#!/usr/bin/env python

# Import local and external libraries
import art
import random
import os

# Credits
__author__ = "Thijs Moens"
__copyright__ = "Copyright 2025, Thijs Moens"
__credits__ = ["Thijs Moens"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Thijs Moens"
__email__ = "thijsmoens@email.com"
__status__ = "Production"

# Information about the game
'''
This is a game of Blackjack. The rules are as follows:
- The deck is unlimited in size.
- There are no jokers.
- The Jack/Queen/King all count as 10.
- The Ace can count as 11 or 1.
- Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
- The cards in the list have equal probability of being drawn.
- Cards are not removed from the deck as they are drawn.
- The computer is the dealer.
- The computer stops at 17
'''

# The main function of the game
def main():
    
    check_play_game = '' 
    
    # Ask the player if they want to play another game
    check_play_game = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ")
    
    # Check if player wants to play a game
    while check_play_game != 'n':
            
        # This is where the game starts
        start_game()
  
  
# Function for the card deck
def card_deck():
    
    # Show the complete list of cards
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  
    
    # Remove the card from the deck
    # cards.remove(interaction)
    
    # If new game, reset the original card deck
    
    # Return the cards
    return cards

  
# Function to pick a random card from the card deck
def pick_random_card():
    
    # Pick a random card from the card deck
    card = random.choice(card_deck())
    
    # print(f"Pick random card: {card}")
    # remove_random_card(card)
    
    return card


# Function to remove random picked card from the card deck
def remove_random_card(card):
    
    print(f"Remove random card: {card}")

    # Remove the card from the card deck
    card_deck(card)
    
    return card
   

# Function to calculate the score of the player
def calculate_score_player(cards_player):

    # Sum the cards of the player
    return sum(cards_player)


# Function to calculate the score of the computer
def calculate_score_computer(cards_computer):

    # Sum the cards of the computer
    return sum(cards_computer)


# Function with the cards of the player
def cards_player(card = ''):
    
    # List with the cards of the player
    cards_player= []
    
    # Append the card to the list of the player
    cards_player.append(card)
    
    # Return the cards of the player
    return cards_player


# Function with the cards of the computer
def cards_computer():
    
    # List with the cards of the computer
    cards_computer = []
    
    # Return the cards of the computer
    return cards_computer
    
  
# Function to start the game
def start_game():
    
        
    # Clear the screen
    os.system('cls||clear')
    
    # Print the logo of the game
    print(art.logo)
    
    # Assign two cards to the player at the start of the game
    for cards in range(2):
        cards_player(pick_random_card())
    
    # Assign one card to the computer at the start of the game
    cards_computer = pick_random_card()
    
    # Check if the player has a blackjack
    if calculate_score_player(cards_player) == 21:
        print("You have a Blackjack! You win! 🎉")
        end_of_game(byline=False)
    
    # If the player does not have a blackjack, show the cards and continue the game
    
    # Print the cards of the player and the computer


# Function to end the game
def end_of_game(byline=True):
    
    # Display the final score of the player and the computer
    if byline:
        print(f"Your final hand: {cards_player}, final score: {calculate_score_player}")
        print(f"Computer's final hand: {cards_computer}, final score: {calculate_score_computer}")
        
    # Ask the player if they want to play another game
    check_play_game = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ")
    
    # If player want to play another game, start the game again
    if check_play_game == 'y':
        return check_play_game
    else:   
        exit()
        
        
# Start the game
if __name__ == "__main__":
    main()