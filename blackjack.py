# Import local library with art
import art

# Import external library for math calculations
import random

'''
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

# Create a function to finish the game
def finish_game(status):
    # Print the outcome of the game
    
    # Blackjack (Blackjack is only when you have a 10 and a Ace, otherwise if it's 21, it's simply you win)
    if status == 'blackjack':
	    print("You have a Blackjack! You win! 🎉")
     
    # You win
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
    else:
        print("It's a draw!")
    
    if status == 'blackjack':
        # Don't show the final hands
        return
    else : 
        # Print the final hands of the player and the computer
        print(f"Your final hand: {cards_player}, final score: {sum(cards_player)}")
        print(f"Computer's final hand: {cards_computer}, final score: {sum(cards_computer)}")
    
    # Ask the player if they want to play another game
    check_play_game = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ")
   
   
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
    
    
# Create a function to check who won the game
def game_mechanics():
    
    # - Blackjack
    if sum(cards_player) == 21:
        finish_game('blackjack')
        
    # - Player wins
    elif calculate_player_score() > calculate_computer_score():
        finish_game('player_wins')

    # - Player bust
    elif calculate_player_score() > 21:
        finish_game('player_bust')
        
    # - Computer wins
    elif calculate_player_score() < calculate_computer_score():
        finish_game('computer_wins')
        
    # - Computer bust
    elif calculate_computer_score() > 21:
        finish_game('computer_bust')
        
    # - Draw
    else:
        finish_game('draw')
    
    
def blackjack_game():
    
    # Create a variable to check if the player wants to play a game
    check_play_game = ''
    
    while check_play_game != 'n':
        
        # Print the logo of the game
        print(art.logo)

        # Assign two cards to the player at the start of the game
        for car in range(2):
            cards_player.append(random.choice(cards))
            
        # Assign one card to the computer at the start of the game
        cards_computer.append(random.choice(cards))

        # Print the cards of the player and the computer
        print(f"Your cards: {cards_player}, current score: {sum(cards_player)}")
        print(f"Computer's first card: {cards_computer}")

        # Check if the player has a blackjack right away
        if sum(cards_player) == 21:
            finish_game('blackjack')

        else:
            # Ask the player if they want to draw another card
            draw_card = input("Type 'y' to get another card, type 'n' to pass: ")
            
            # Als de speler een kaart wilt, geef hem een extra kaart en check de score
            cards_player.append(random.choice(cards)) # Geef extra kaart
            
            # Check if the player has 21
            if sum(cards_player) == 21:
                --> player_has_21
                --> calculate_computer_score
                --> check_winner
                
            # Check if the player went over 21
            elif sum(cards_player) > 21:
                --> player_is_busted
                --> calculate_computer_score
                --> computer_wins
            
            else:
                print(f"Your cards: {cards_player}, current score: {sum(cards_player)}")
                print(f"Computer's first card: {cards_computer}")
                draw_card = input("Type 'y' to get another card, type 'n' to pass: ")
            
            
            # Draw a card if the player wants to
            while draw_card == 'y':
                cards_player.append(random.choice(cards))
                print(f"Your cards: {cards_player}, current score: {sum(cards_player)}")
                print(f"Computer's first card: {cards_computer}")
                
                # Check the game mechanics and see who won
                game_mechanics()
                
        
            
        
        
        # create variable to check if user wants to play a game
        check_play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        
        
# Call the function to start the game
blackjack_game()