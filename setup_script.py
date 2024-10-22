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


# Add empty variable for scores of player and computer
score_player = 0
score_computer = 0

# Check if player wants an extra card
check_for_extra_card = input("Type 'y' to get another card, type 'n' to pass: ")

# Pick cards until players says stop
while check_for_extra_card == 'y':

	# Create a list with all the cards
	cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

	# Pick a random card from the list
	random_pick = random.randint(0, len(cards))

	# Add random card to score player
	score_player += cards[random_pick]

	print(score_player)

	# Check if player wants an extra card
	check_for_extra_card = input("Type 'y' to get another card, type 'n' to pass: ")