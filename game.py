#!/usr/bin/env python

# Import local and external libraries
import art
import random
import os

__author__ = "Thijs Moens"
__copyright__ = "Copyright 2025, Thijs Moens"
__credits__ = ["Thijs Moens"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Thijs Moens"
__email__ = "thijsmoens@email.com"
__status__ = "Production"


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

# Create a list for the player
cards_player = []

# Create a list for the computer
cards_computer = []

# Create a variable to draw a card
check_draw_card = ''

# Create a variable to check if the player wants to play a game
check_play_game = ''

# Create a function to calculate the score of the computer
def calculate_computer_score():
    
    # Draw a card for the computer until the score is 17 or higher
    while sum(cards_computer) < 17:
        cards_computer.append(random.choice(cards))
    
    # Return the score of the computer
    return sum(cards_computer)


# Create a function to calculate the score of the player
def calculate_player_score():
    return sum(cards_player) 

# Create a function for text output
def text_output(status):
    
    # Blackjack
    if status == 'blackjack':
        print("You have a Blackjack! You win! 🎉")
    
    # If player has 21
    elif status == '21':
        
        print("You have 21! You win! 🎉")
              
    # Player wins
    elif status == 'player_wins':
        print("You win! 🎉")
     
    # You Bust (over)
    elif status == 'player_bust':
        print("You went over. You lose...")

    # Opponent (computer) bust
    elif status == 'computer_bust':
        print("Opponent went over. You win! 🎉")

    # Computer has more points
    elif status == 'computer_wins':
        print("You lose...")
        
    # Draw
    elif status == 'draw':
        print("It's a draw, so you lose...")


# Check if player wants to play a game
while check_play_game != 'n':
    
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
    
    # Print the cards of the player and the computer
    print(f"Your cards: {cards_player}, current score: {sum(cards_player)}")
    print(f"Computer's first card: {cards_computer}")

    # Check if the player has a blackjack right away
    if sum(cards_player) == 21:
        text_output('blackjack')
        break
    else:
        
        # Ask the player if they want to draw another card
        check_draw_card = input("Type 'y' to get another card, type 'n' to pass: ")
        
        while check_draw_card != 'n':
        
            # Als de speler een kaart wilt, geef hem een extra kaart en check de score
            temp_card_player = random.choice(cards)
            cards_player.append(temp_card_player)
            cards.remove(temp_card_player)        
            
            # Show the cards of the player and the computer
            print(f"Your cards: {cards_player}, current score: {sum(cards_player)}")
            print(f"Computer's first card: {cards_computer}")
                
                
            # Check if the player has 21
            if sum(cards_player) == 21:
                
                text_output('21')  
                                
                # Show the final hands and the outcome of the game
                print(f"Your final hand: {cards_player}, final score: {sum(cards_player)}")
                print(f"Computer's final hand: {cards_computer}, final score: {sum(cards_computer)}")
                
                break
                
            elif sum(cards_player) > 21:
                
                text_output('player_bust')
                
                # Show the final hands and the outcome of the game
                print(f"Your final hand: {cards_player}, final score: {sum(cards_player)}")
                print(f"Computer's final hand: {cards_computer}, final score: {sum(cards_computer)}")
                
                break
                
            elif sum(cards_player) < 21:
                
                check_draw_card = input("Type 'y' to get another card, type 'n' to pass: ")
                
                
                
                
                
            
                    
            # # Check if Player wins
            # elif calculate_player_score() > calculate_computer_score() and calculate_player_score() <= 21:
            
            #     print("You win! 🎉")
                
            #     # Show the final hands and the outcome of the game
            #     print(f"Your final hand: {cards_player}, final score: {sum(cards_player)}")
            #     print(f"Computer's final hand: {cards_computer}, final score: {sum(cards_computer)}")

            # # Check if Player is busted
            # elif calculate_player_score() > 21:
                
            #     print("You went over. You lose...")
                
            #     # Show the final hands and the outcome of the game
            #     print(f"Your final hand: {cards_player}, final score: {sum(cards_player)}")
            #     print(f"Computer's final hand: {cards_computer}, final score: {sum(cards_computer)}")
                    
            # # Check if Computer wins
            # elif calculate_player_score() < calculate_computer_score():
            
            #     print("You lose...")
                
            #     # Show the final hands and the outcome of the game
            #     print(f"Your final hand: {cards_player}, final score: {sum(cards_player)}")
            #     print(f"Computer's final hand: {cards_computer}, final score: {sum(cards_computer)}")
                    
            # # Check if computer is busted
            # elif calculate_computer_score() > 21:
            
            #     print("Opponent went over. You win! 🎉.")
                
            #     # Show the final hands and the outcome of the game
            #     print(f"Your final hand: {cards_player}, final score: {sum(cards_player)}")
            #     print(f"Computer's final hand: {cards_computer}, final score: {sum(cards_computer)}")
                    
            # # Check if it is a draw
            # else:
                            
            #     print("It's a draw!")
                
            #     # Show the final hands and the outcome of the game
            #     print(f"Your final hand: {cards_player}, final score: {sum(cards_player)}")
            #     print(f"Computer's final hand: {cards_computer}, final score: {sum(cards_computer)}")
                
            
            # # Ask the player if they want to draw another card
            # check_draw_card = input("Type 'y' to get another card, type 'n' to pass: ")
                
        # If the player pass
        # Calculate the total score of the player
        calculate_player_score()
        
        # Calculate the total score of the computer
        calculate_computer_score()
        
        # Check who won the game
        if calculate_player_score() > calculate_computer_score():
        
            text_output('player_wins')
            
        elif calculate_player_score() == calculate_computer_score():
            
            text_output('draw')
             
        elif calculate_computer_score() > 21:
            
            text_output('computer_bust')
             
        else : 
            
            text_output('computer_wins')
            
        # Show the final hands and the outcome of the game
        print(f"Your final hand: {cards_player}, final score: {sum(cards_player)}")
        print(f"Computer's final hand: {cards_computer}, final score: {sum(cards_computer)}")
    
    # Ask the player if they want to play another game
    check_play_game = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ")