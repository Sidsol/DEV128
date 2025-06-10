# Assignment: Player Inheritance
# Class: DEV 128
# Date: 05/14/2025
# Author: Jonah Martinez
# Description: This program defines a base class Player and to derived classes
# Batter and Pitcher. It demonstrates the use of inheritance in python.


#  Raise ValueError if value is not a non-empty string.
def validateNotEmptyString(value, field):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field} cannot be empty.")
    return value


# Raise ValueError if value is not a positive integer.
def validatePositiveInteger(value, field):
    if not isinstance(value, int) or value <= 0:
        raise ValueError(f"{field} cannot be negative.")
    return value


# Player base class stores name and position.
class Player:
    def __init__(self, name, position):
        self.__name = validateNotEmptyString(name, "name")
        self.__position = validateNotEmptyString(position, "position")

    @property
    def name(self):
        return self.__name

    @property
    def position(self):
        return self.__position

    def getStats(self):
        return f"Name: {self.name} Position: {self.position}"


# Batter derived class inherits from Player
class Batter(Player):
    def __init__(self, name, position, at_bats, hits):
        # Call the base class constructor and pass the name and position
        super().__init__(name, position)
        self.at_bats = validatePositiveInteger(at_bats, "at_bats")
        self.hits = validatePositiveInteger(hits, "hits")

    # Return the batting average, or 0.0 if no at-bats.
    @property
    def average(self):
        return self.hits / self.at_bats if self.at_bats else 0.0

    def getStats(self):
        return f"{Player.getStats(self)}  Batting Avg: {self.average:.3f}"


# Pitcher derived class inherits from Player
class Pitcher(Player):
    # Default position for a pitcher
    POSITION = "Pitcher"
    
    def __init__(self, name, wins, loss):
        # Call the base class constructor and pass the name and position
        super().__init__(name, self.POSITION)
        self.wins = validatePositiveInteger(wins, "wins")
        self.loss = validatePositiveInteger(loss, "loss")

    def getStats(self):
        return f"{Player.getStats(self)}  {self.wins}-{self.loss} win-loss"
