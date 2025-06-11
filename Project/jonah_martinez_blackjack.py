# Assignment: Blackjack
# Class: DEV 128
# Date: 06/10/2025
# Author: Jonah Martinez
# Description: Blackjack game implementation using Card, Deck, and Hand classes.

#!/usr/bin/env python3

from jonah_martinez_objects import Card, Deck, Hand


class Blackjack:
    def __init__(self, startingBalance):
        """Initialize the Blackjack game with a starting balance."""
        self.money = startingBalance
        self.bet = 0
        self.deck = None
        self.dealerHand = None
        self.playerHand = None

    def displayCards(self, hand, title):
        """Print the title, print the cards and the points of the hand"""
        print(f"{title}:")
        for card in hand:
            print(card)

        print(f"Points: {hand.points}\n")

    def getBet(self):
        """Method to update self.bet by prompting the user for the bet amount,
        making sure bet is less than self.money.
        """
        # Prompt the user for a bet amount until a valid bet is entered
        while True:
            try:
                bet = int(input(f"Bet amount: "))
                if 0 < bet <= self.money:
                    self.bet = bet
                    break
                else:
                    print(
                        f"Invalid bet. Please enter a value between 1 and {self.money}."
                    )
            except ValueError:
                print("Invalid input. Please enter a valid integer for the bet.")

    def setupRound(self):
        """Setup the round by doing these steps:
        initialize self.deck to a new Deck object and shuffle it
        initialize self.dealerHand and self.playerHand to new Hand objects
        deal two cards to the playerHand, and one card to the dealerHand
        finally, print dealerHand and playerHand using displayCards method
        """
        self.deck = Deck()
        self.deck.shuffle()
        self.dealerHand = Hand()
        self.playerHand = Hand()

        # Deal two cards to the player and one to the dealer
        for _ in range(2):
            self.playerHand.addCard(self.deck.dealCard())

        self.dealerHand.addCard(self.deck.dealCard())

        # Display the hands
        self.displayCards(self.dealerHand, "DEALER'S SHOW CARDS")
        print()
        self.displayCards(self.playerHand, "YOUR CARDS")

    def takePlayerTurn(self):
        """Method to simulate player playing one turn by dealing a card
        to the player."""
        print()
        # Deal a card to the player
        card = self.deck.dealCard()
        # Check if the card is valid
        if card:
            self.playerHand.addCard(card)
            self.displayCards(self.playerHand, "YOUR CARDS")
        else:
            print("No more cards in the deck.")


def main():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")

    # initialize starting money
    money = 100
    print("Starting Balance:", money)

    # instantiate object of Blackjack class
    blackjack = Blackjack(money)

    print("Setting up a round...")
    # Call the getBet() and setupRound() methods of blackjack object
    # To be implemented in Phase 2
    blackjack.getBet()
    print()
    blackjack.setupRound()

    print("\nPlaying Player Hand...")
    # To be implemented in Phase 2
    # Add code to play the player hand
    # Prompt the user to whether to Hit (h) or Stand (s)
    # If player says stand,
    #      print player's points and exit
    # else
    #    call takePlayerTurn method to deal a card to the player
    #    Check if the hand is busted, if so print player's points and exit
    #    otherwise prompt again

    # Game loop for player actions
    # Loop until the player stands or busts
    while True:
        action = input("Do you want to Hit (h) or Stand (s)? ").strip().lower()
        if action == "s":
            print(f"\nPlayer's points: {blackjack.playerHand.points}")
            break
        elif action == "h":
            blackjack.takePlayerTurn()
            if blackjack.playerHand.points > 21:
                print(f"Busted! Player's points: {blackjack.playerHand.points}")
                break
        else:
            print("Invalid input. Please enter 'h' to hit or 's' to stand.")

    print("Good bye!")


# if started as the main module, call the main function
if __name__ == "__main__":
    main()
