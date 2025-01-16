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

# # Pick a card from the deck, assign it to player/computer and remove it from the deck
# def pick_a_random_card():
    
#     temp_card = random.choice(cards)
#     player_cards.append(temp_card)
#     cards.remove(temp_card)

cards = []

# A list with all the removed cards, to store them back when a new game starts
temp_cards = []

# Variable for checking if a player want another game
check_play_game = '' 

# Create a variable to draw a card
check_draw_card = ''

# Ask the player if they want to play another game
check_play_game = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ")

# Check if player wants to play a game
while check_play_game != 'n':
    
    # Clear the screen
    os.system('cls||clear')
    
    # Print the logo of the game
    print(art.logo)
    
    # Show the complete list of cards
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  
    
    # Store all cards of the player and computer
    player_cards = []
    computer_cards = []
        
    # Assign two cards to the player at the start of the game
    for card in range(2):
        temp_card = random.choice(cards) # pick a random card from the deck
        player_cards.append(temp_card) # assign card to player
        cards.remove(temp_card) # remove card from the deck
        temp_cards.append(temp_card) # add removed card to temp list
        
    # Assign one card to the computer at the start of the game
    temp_card_comp = random.choice(cards) # pick a random card from the deck
    computer_cards.append(temp_card_comp) # assign card to player
    cards.remove(temp_card_comp) # remove card from the deck
    temp_cards.append(temp_card_comp) # add removed card to temp list  
        
    # Check if the player has a blackjack
    if sum(player_cards) == 21:
        print("You have a Blackjack! You win! 🎉") 
        break
    
    # Check if the player wants a card
    while check_draw_card != 'n':
        
        # Show the cards of the player and the computer
        print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
        print(f"Computer's first card: {computer_cards}")

        # Check if the player has 21
        if sum(player_cards) == 21:
            check_draw_card = 'n'
            print("You have 21! You win! 🎉")
            break
        
        # Check if the player has more than 21
        elif sum(player_cards) > 21:
            check_draw_card = 'n'
            print("You went over. You lose...")
            break
        
        # Check if the player has less than 21
        elif sum(player_cards) < 21:
                        
            # Ask the player if they want to draw another card
            check_draw_card = input("Type 'y' to get another card, type 'n' to pass: ")
            
            # Assign a card to the player
            if check_draw_card == 'y':
                temp_card_player = random.choice(cards) # pick a random card from the deck
                player_cards.append(temp_card_player) # assign card to player
                cards.remove(temp_card_player) # remove card from the deck
                temp_cards.append(temp_card_player) # add removed card to temp list
            # elif check_draw_card == 
            #     break
                            
                
    # Draw a card for the computer until the score is 17 or higher
    if sum(player_cards) < 21:
    
        while sum(computer_cards) < 17:
            temp_card_computer = random.choice(cards)
            computer_cards.append(temp_card_computer)
            cards.remove(temp_card_computer)
            
        # If computer is bust
        if sum(computer_cards) > 21:
            print("Opponent went over. You win! 🎉.") 
        
        # If the player has more points
        elif sum(player_cards) > sum(computer_cards):
            print("You win! 🎉")
        
        # If the computer has more points
        elif sum(computer_cards) > sum(player_cards) or sum(computer_cards) == sum(player_cards) :
            print("You lose...")           
        
    # Print the final hand of player and computer
    print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
    print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")

    # Ask the player if they want to play another game
    check_play_game = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ")


    
exit()
    
