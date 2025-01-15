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

# Create a list of cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def start_game(cards_player, score_player, cards_computer, score_computer):
    
    score_player = sum(cards_player)
    score_computer = sum(cards_computer)
    
    # Clear the cards for player and computer
    cards_player = []
    cards_computer = []
    
    # Clear the screen
    os.system('cls||clear')
    
    # Print the logo of the game
    print(art.logo)

     # Assign two cards to the player at the start of the game
    for car in range(2):
        temp_card_player = random.choice(cards)
        cards_player.append(temp_card_player)
        cards.remove(temp_card_player)        
            
    # Assign one card to the computer at the start of the game
    temp_card_computer = random.choice(cards)
    cards_computer.append(temp_card_computer)
    cards.remove(temp_card_computer)
    score_player = sum(cards_player)
    
    # Print the cards of the player and the computer
    print(f"Your cards: {cards_player}, current score: {score_player}")
    print(f"Computer's first card: {cards_computer}")
    
    # Check if the player has a blackjack
    if sum(cards_player) == 21:
        print("You have a Blackjack! You win!")
        end_game(cards_player, score_player, cards_computer, score_computer)
    else :
        player_logic(cards_player, score_player, cards_computer, score_computer)
    
    
    
def player_logic(cards_player, score_player, cards_computer, score_computer):
    
    check_draw_card = '' # Create a variable to draw a card
    
    while check_draw_card != 'n':

        # Check if the player has 21
        if sum(cards_player) == 21:
            check_draw_card = 'n'
            print("You have 21! You win! 🎉")
            end_game(cards_player, score_player, cards_computer, score_computer)
        
        # Check if the player has more than 21
        elif sum(cards_player) > 21:
            check_draw_card = 'n'
            print("You went over. You lose...")
            end_game(cards_player, score_player, cards_computer, score_computer)
        
        # Check if the player has less than 21
        elif sum(cards_player) < 21:
            
            # Ask the player if they want to draw another card
            check_draw_card = input("Type 'y' to get another card, type 'n' to pass: ")
            
            # Assign a card to the player
            if check_draw_card == 'y':
                temp_card_player = random.choice(cards)
                cards_player.append(temp_card_player)
                cards.remove(temp_card_player)        
                score_player = sum(cards_player)
            
                # Show the cards of the player and the computer
                print(f"Your cards: {cards_player}, current score: {score_player}")
                print(f"Computer's first card: {cards_computer}")
                
            # If the player doesn't want to draw a card, the computer will play
            else:
                computer_logic(cards_player, score_player, cards_computer, score_computer)
            
    
    
def computer_logic(cards_player, score_player, cards_computer, score_computer):
    
    # Draw a card for the computer until the score is 17 or higher
    while sum(cards_computer) < 17:
        temp_card_computer = random.choice(cards)
        cards_computer.append(temp_card_computer)
        cards.remove(temp_card_computer)
        score_computer = sum(cards_computer)
    
    check_winner(cards_player, score_player, cards_computer, score_computer)
    
    
def check_winner(cards_player, score_player, cards_computer, score_computer):
    
    # If computer is bust
    if score_computer > 21:
        print("Opponent went over. You win! 🎉.") 
        end_game(cards_player, score_player, cards_computer, score_computer)
    
    # If the player has more points
    elif score_player > score_computer:
        print("You win! 🎉")
        end_game(cards_player, score_player, cards_computer, score_computer)
    
    # If the computer has more points
    elif score_computer > score_player:
        print("You lose...")
        end_game(cards_player, score_player, cards_computer, score_computer)
    
    
def end_game(cards_player, score_player, cards_computer, score_computer):
    
    print(f"Your final hand: {cards_player}, final score: {score_player}")
    print(f"Computer's final hand: {cards_computer}, final score: {score_computer}")
    
    
def main():
    
    cards_player = []
    score_player = 0
    cards_computer = []
    score_computer = 0
    check_play_game = '' 
    
    # Ask the player if they want to play another game
    check_play_game = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ")
    
    # Check if player wants to play a game
    while check_play_game != 'n':
    
        # This is where the main function is called
        start_game(cards_player, score_player, cards_computer, score_computer)
        player_logic(cards_player, score_player, cards_computer, score_computer)
        computer_logic(cards_player, score_player, cards_computer, score_computer)
        check_winner(cards_player, score_player, cards_computer, score_computer)
        end_game(cards_player, score_player, cards_computer, score_computer)
        
# Start the game
if __name__ == "__main__":
    main()