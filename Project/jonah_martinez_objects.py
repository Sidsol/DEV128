# Assignment: Objects V2
# Class: DEV 128
# Date: 06/10/2025
# Author: Jonah Martinez
# Description: This program defines a Card, Deck, and Hand class to serve as the basis for a card game.

#!/usr/bin/env python3
import random

CARDS_CHARACTERS = {"Spades": "♠", "Hearts": "♥", "Diamonds": "♦", "Clubs": "♣"}
# Set of allowed Suits and Ranks used for validation
ALLOWED_SUITES = ["Spades", "Hearts", "Diamonds", "Clubs"]
ALLOWED_RANKS = [
    "Ace",
    "King",
    "Queen",
    "Jack",
    "10",
    "9",
    "8",
    "7",
    "6",
    "5",
    "4",
    "3",
    "2",
]


##########################################################################
## Definitions for the classes: Card, Deck and Hand
##########################################################################
class Card:
    def __init__(self, rank, suit):
        if suit not in ALLOWED_SUITES:
            raise ValueError(
                f"Invalid suit: {suit}. Allowed suits are: {ALLOWED_SUITES}"
            )
        if rank not in ALLOWED_RANKS:
            raise ValueError(
                f"Invalid rank: {rank}. Allowed ranks are: {ALLOWED_RANKS}"
            )

        # public attributes
        self.suit = suit
        self.rank = rank

    # Returns the value of the card based on its rank.
    @property
    def value(self):
        if self.rank in {"Jack", "Queen", "King"}:
            return 10
        elif self.rank == "Ace":
            return 11
        else:
            return int(self.rank)

    # Returns a string representation of the card.
    # The string includes the rank, suit, and a character representation of the suit.
    # For example: "Ace of Spades (♠)".
    def __str__(self):
        return f"{self.rank} of {self.suit} {CARDS_CHARACTERS[self.suit]}"

    # Compares two Card objects based on their suit and rank.
    def __lt__(self, other):
        if self.suit == other.suit:
            return ALLOWED_RANKS.index(self.rank) > ALLOWED_RANKS.index(other.rank)
        return ALLOWED_SUITES.index(self.suit) > ALLOWED_SUITES.index(other.suit)


class Deck:
    def __init__(self):
        self.__deck = []

        # Initialize the deck with all possible cards.
        for suit in ALLOWED_SUITES:
            for rank in ALLOWED_RANKS:
                self.__deck.append(Card(rank, suit))

    # Returns the number of cards in the deck.
    @property
    def count(self):
        return len(self.__deck)

    # Shuffles the deck in place using random.shuffle.
    def shuffle(self):
        random.shuffle(self.__deck)

    # Deals a card from the deck and removes it from the deck.
    def dealCard(self):
        if not self.__deck:
            return None
        return self.__deck.pop()

    def __iter__(self):
        for cards in self.__deck:
            yield cards

    def __len__(self):
        return len(self.__deck)


class Hand:
    def __init__(self):
        # Private attribute to store the cards in the hand.
        # Initialized as an empty list.
        self.__cards = []

    # Returns the number of cards in the hand.
    @property
    def count(self):
        return len(
            self.__cards
        )  # Returns the total points of the hand by summing the values of all cards.

    # Handles Aces as 1 or 11 to avoid going over 21.
    @property
    def points(self):
        total = 0
        aces = 0

        # First, calculate total treating all aces as 11 and count aces
        for card in self.__cards:
            if card.rank == "Ace":
                aces += 1
                total += 11
            else:
                total += card.value

        # Convert aces from 11 to 1 as needed to stay under or at 21
        while total > 21 and aces > 0:
            total -= 10  # Convert an ace from 11 to 1 (subtract 10)
            aces -= 1

        return total

    # Returns True if the hand points are greater than 21 (busted).
    @property
    def isBusted(self):
        return self.points > 21

    # Returns True if the hand has exactly 2 cards and the points are 21 (blackjack).
    @property
    def hasBlackjack(self):
        return len(self.__cards) == 2 and self.points == 21

    # Adds a card to the hand.
    def addCard(self, card):
        self.__cards.append(card)

    def shortDisplay(self):
        """Returns a short display of the hand, showing only the rank and suit symbol of each sorted card."""
        sorted_cards = sorted(self.__cards)
        return " ".join(
            f"{card.rank}{CARDS_CHARACTERS[card.suit]}" for card in sorted_cards
        )  # Displays all cards in the hand.

    def __str__(self):
        if not self.__cards:
            return "Empty hand"
        card_strings = [str(card) for card in self.__cards]
        return "\n" + "\n".join(card_strings)

    # Make Hand iterable by yielding cards one by one
    def __iter__(self):
        for card in self.__cards:
            yield card

    def __len__(self):
        return len(self.__cards)


def main():
    print("Cards - Tester")
    print()

    # test sorting of the cards
    testcardsList = [
        Card("Ace", "Spades"),
        Card("Queen", "Hearts"),
        Card("10", "Clubs"),
        Card("3", "Diamonds"),
        Card("Jack", "Hearts"),
        Card("7", "Spades"),
    ]
    testcardsList.sort()
    print("TEST CARDS LIST AFTER SORTING.")
    for c in testcardsList:
        print(c)
    print()

    # test deck
    print("DECK")
    deck = Deck()
    print("Deck created.")
    deck.shuffle()
    print("Deck shuffled.")
    print("Deck count:", len(deck))

    # test hand
    hand = Hand()
    for i in range(10):
        hand.addCard(deck.dealCard())

    print("HAND")
    print(hand)

    print("\nShort Display of Hand:")
    print(hand.shortDisplay())

    print()
    print("Hand points:", hand.points)
    print("Hand count:", len(hand))
    print("Deck count:", len(deck))


if __name__ == "__main__":
    main()
