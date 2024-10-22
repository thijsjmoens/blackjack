import art

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


# Create the main function of the game
def blackjack():






# Call the main function
blackjack()



# Function for all inputs and displays
def opening_sentences():

	# create variable to check if user wants to play a game
	check_play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

	while check_play_game == 'y':

		print(art.logo)

		print(f"Your cards: {cards_player}, current score: {current_score}\n")
		print(f"Computer's first card: {computer_card}")

		input("Type 'y' to get another card, type 'n' to pass: ")


		# Display final hand
		print(f"Your final hand: {final_hand}, final score: {final_score}")
		print(f"Computer's final hand: {computer_final_hand}, final score: {computer_final_score}")

		# Display the outcome

		# Blackjack
		# Blackjack is only when you have a 10 and a Ace, otherwise if it's 21, it's simply you win
		print("Win with a Blackjack!")

		# You win
		print("You win!")

		# You Bust (over)
		print("You went over. You lose...")

		# Opponent (computer) bust
		print("Opponent went over. You win!")

		# Computer has more points
		print("You lose...")


	





def game_mechanics():

	# Create a list with all the cards
	cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

	# Step 1
	# Pick two random cards for player and add them together

	# Pick a random card for computer (dealer)


	# Step 2
	# Check if player wants an extra card
	# If so, add to the total of the two previous cards 
		# Check if there is an ace. If third card goes above 21, make it 1, otherwise keep it 11

	# Step 3 
	# Repeat asking player for more cards, unless player get bust

	# Step 4
	# If player passed or get busted, draw cards for dealer
		# Stop if total hits 17 or more
		# Stop if player gets busted


















