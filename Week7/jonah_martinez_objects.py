# Assignment: Objects
# Class: DEV 128
# Date: 5/29/2025
# Author: Jonah Martinez
# Description: This program defines a Card, Deck, and Hand class to serve as the basis for a card game.

#!/usr/bin/env python3
import random
CARDS_CHARACTERS = {"Spades": "♠", "Hearts": "♥", "Diamonds": "♦", "Clubs": "♣"}
# Set of allowed Suits and Ranks used for validation
ALLOWED_SUITES = {"Spades", "Hearts", "Diamonds", "Clubs" }
ALLOWED_RANKS = {"Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"}

##########################################################################
## Definitions for the classes: Card, Deck and Hand
##########################################################################
class Card():
    def __init__(self, rank, suit):
        if suit not in ALLOWED_SUITES:
            raise ValueError(f"Invalid suit: {suit}. Allowed suits are: {ALLOWED_SUITES}")
        if rank not in ALLOWED_RANKS:
            raise ValueError(f"Invalid rank: {rank}. Allowed ranks are: {ALLOWED_RANKS}")
        
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
    def displayCard(self):
        return f"{self.rank} of {self.suit} ({CARDS_CHARACTERS[self.suit]})"
        
class Deck():
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

class Hand():
    def __init__(self):
        # Private attribute to store the cards in the hand.
        # Initialized as an empty list.
        self.__cards = []

    # Returns the number of cards in the hand.
    @property
    def count(self):
        return len(self.__cards)
    
    # Returns the total points of the hand by summing the values of all cards.
    @property
    def points(self):
        return sum(card.value for card in self.__cards)
    
    # Adds a card to the hand.
    def addCard(self, card):
        self.__cards.append(card)
    
    # Displays all cards in the hand.
    def displayHand(self):
        for card in self.__cards:
            print(card.displayCard())
        
def main():
    print("Cards - Tester")
    print()
    
    # test deck
    print("DECK")
    deck = Deck()
    print("Deck created.")
    deck.shuffle()    
    print("Deck shuffled.")
    print("Deck count:", deck.count)
    print()

    # test hand
    print("HAND")
    hand = Hand()
    for i in range(4):
        hand.addCard(deck.dealCard())

    hand.displayHand()
    print()

    print("Hand points:", hand.points)
    print("Hand count:", hand.count)
    print("Deck count:", deck.count)

if __name__ == "__main__":
    main()
