# Import necessary modules
import random
import time

# Define the ranks and suits
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
suits = ("hearts", "diamonds", "clubs", "spades")

# Create a deck of cards
# deck = ...
def create_deck():
    lDeck = []
    for sSuit in suits:
        for sRank in ranks:
            lDeck.append([sRank, sSuit])
    return lDeck

# Shuffle the deck 
def shuffle_deck(lDeck):
    lShuffledDeck = []
    while len(lDeck) > 0:
        iIndex = int(random.random() * len(lDeck))
        lShuffledDeck.append(lDeck.pop(iIndex))
    while len(lShuffledDeck) > 0:
        lDeck.append(lShuffledDeck.pop(0))
    
    # To test war() then war(), force two cards are same at the beginning
    """
    lLastCards = []
    lLastCards.append(lDeck[-1])
    lLastCards.append(lDeck[-2])
    for lCard in lDeck:
        if lCard[0] == lLastCards[0][0]:
            lDeck.insert(0, lDeck.pop(lDeck.index(lCard)))
            break
    for lCard in lDeck:
        if lCard[0] == lLastCards[1][0]:
            lDeck.insert(4, lDeck.pop(lDeck.index(lCard)))
            break
    lDeck.insert(26,     lDeck.pop(lDeck.index(lLastCards[0])))
    lDeck.insert(26 + 4, lDeck.pop(lDeck.index(lLastCards[1])))
    """

# Split the deck into two hands
def split_deck(lDeck, lP1Deck, lP2Deck):
    for iIndex in range(len(lDeck)):
        if iIndex < len(lDeck) / 2:
            lP1Deck.append(lDeck[iIndex])
        else:
            lP2Deck.append(lDeck[iIndex])

# Compare two cards
def card_comparison(p1_card, p2_card):
    """This is the logic that compares two cards to find the stronger card
		Return 1 if player 1's card is strong, 2 for player 2
		if the cards are equal, return 0.

		Hint, using the index function will make this very simple (one liner)"""
    # Your code here
    print("Player 1: ", p1_card, ", Player 2:", p2_card)
    if ranks.index(p1_card[0]) > ranks.index(p2_card[0]):
        return 1
    elif ranks.index(p1_card[0]) < ranks.index(p2_card[0]):
        return 2
    else:
        return 0

def play_round(player1_hand, player2_hand):
    """Play a single round of the game.
		That is, each player flips a card, and the winner is determined using the card_comparison function
		if both players flip the same value card, call the war function
	"""
    # Your code here
    if len(player1_hand) == 0 or len(player2_hand) == 0:
        return

    iResult = card_comparison(player1_hand[0], player2_hand[0])
    if iResult == 1:
        player1_hand.append(player2_hand.pop(0))
        player1_hand.append(player1_hand.pop(0))
        print("** Player 1 has a strong card. Player 1 won 1 card")
    elif iResult == 2:
        player2_hand.append(player1_hand.pop(0))
        player2_hand.append(player2_hand.pop(0))
        print("** Player 2 has a strong card. Player 2 won 1 card")
    else:
        player1_table = []
        player2_table = []
        player1_table.append(player1_hand.pop(0))
        player2_table.append(player2_hand.pop(0))
        war(player1_hand, player2_hand, player1_table, player2_table)
    # print("player1_hand =", player1_hand)
    # print("player2_hand =", player2_hand)
    print("Player 1 has", len(player1_hand), "cards, Player 2 has", len(player2_hand), "cards.")
    # input("Press enter to continue")
    return

def war(player1_hand, player2_hand, player1_table, player2_table):
    """Handle the 'war' scenario when cards are equal.
		recall the rules of war, both players put 3 cards face down, 
		then both players flip face up a 4th card. The player with the stronger
		card takes all the cards.		
	"""
    # Your code here
    print("==== Player 1 & 2 tie. There is a war! ====")
    print("Face down 3 cards, and check the 4th card")

    # Append sequence:
    #    1. Append losing side on table cards
    #    2. Append losing side on hand cards
    #    3. Append winning side on table cards
    #    4. Append winning side on hand cards with the same amount of losing side on hand cards

    if len(player1_hand) < 4 or len(player2_hand) < 4:
        # If one player has less than 4 cards, this person loses.
        # The other player must have more than 4 cards, and that person wins.
        if len(player1_hand) > len(player2_hand):
            print("** Player 2 ran out of cards. Player 1 won all rest", len(player2_table) + len(player2_hand), "card(s)")
            iLoseHandNum = len(player2_hand)
            while len(player2_table):
                player1_hand.append(player2_table.pop(0))
            while len(player2_hand):
                player1_hand.append(player2_hand.pop(0))
            while len(player1_table):
                player1_hand.append(player1_table.pop(0))
            for iIter in range(iLoseHandNum):
                player1_hand.append(player1_hand.pop(0))
        else:
            print("** Player 1 ran out of cards. Player 2 won all rest", len(player1_table) + len(player1_hand), "card(s)")
            iLoseHandNum = len(player1_hand)
            while len(player1_table):
                player2_hand.append(player1_table.pop(0))
            while len(player1_hand):
                player2_hand.append(player1_hand.pop(0))
            while len(player2_table):
                player2_hand.append(player2_table.pop(0))
            for iIter in range(iLoseHandNum):
                player2_hand.append(player2_hand.pop(0))
        return

    # compare 4th cards as 1st cards tie (popped out), then hide 3 cards
    iResult = card_comparison(player1_hand[3], player2_hand[3])
    if iResult == 1:
        print("** Player 1 has a stronger card. Player 1 won", len(player2_table) + 4, "cards")
        while len(player2_table):
            player1_hand.append(player2_table.pop(0))
        for iIter in range(4):
            player1_hand.append(player2_hand.pop(0))
        while len(player1_table):
            player1_hand.append(player1_table.pop(0))
        for iIter in range(4):
            player1_hand.append(player1_hand.pop(0))
    elif iResult == 2:
        print("** Player 2 has a stronger card. Player 2 won", len(player1_table) + 4, "cards")
        while len(player1_table):
            player2_hand.append(player1_table.pop(0))
        for iIter in range(4):
            player2_hand.append(player1_hand.pop(0))
        while len(player2_table):
            player2_hand.append(player2_table.pop(0))
        for iIter in range(4):
            player2_hand.append(player2_hand.pop(0))
    else:
        # pop these 4 cards on each player's table
        for iIter in range(4):
            player1_table.append(player1_hand.pop(0))
        for iIter in range(4):
            player2_table.append(player2_hand.pop(0))
        war(player1_hand, player2_hand, player1_table, player2_table)
    return

def play_game():
    """Main function to run the game."""
    # Your code here
    player1_hand = []
    player2_hand = []
    print("---- Prepare for the game ----")
    print("Create deck ...")
    lDeck = create_deck()
    time.sleep(1)
    # print("********** After create deck: **********")
    # print("lDeck =", lDeck, ", len =", len(lDeck))
    # input("Press enter to continue")
    print("Shuffle deck ...")
    shuffle_deck(lDeck)
    time.sleep(1)
    # print("********** After shuffle deck: **********")
    # print("lDeck =", lDeck, ", len =", len(lDeck))
    # input("Press enter to continue")
    print("Split deck ...")
    split_deck(lDeck, player1_hand, player2_hand)
    time.sleep(1)
    # print("********** After split deck: **********")
    # print("player1_hand =", player1_hand, ", len =", len(player1_hand))
    # print("player2_hand =", player2_hand, ", len =", len(player2_hand), "total =", len(player1_hand) + len(player2_hand))
    # input("Press enter to continue")
    print("----     Game Starts      ----")
    time.sleep(1)
 
    while len(player1_hand) != 0 and len(player2_hand) != 0:
        play_round(player1_hand, player2_hand)
        time.sleep(1)
        # print("Press enter to continue")
    
    if len(player1_hand) == 0:
        print("**** Player 2 won!!! ****")
    else:
        print("**** Player 1 won!!! ****")
    print("----     Game over     ----")

# Call the main function to start the game
play_game()
