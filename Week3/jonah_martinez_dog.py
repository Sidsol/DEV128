# Assignment: dog.py
# Class: DEV 128
# Date: 04/26/2025
# Author: Jonah Martinez
# Description: Program to simulate a dog object with attributes and methods.

class Dog:
    def __init__(self, name: str, color: str, weight: float = 10.0):
        self.name = name
        self.color = color
        self.isHungry = True
        self.weight = weight

    def bark(self):
        print(f"{self.name} : Woof Woof")

    # Simulates the dog eating food.
    # It sets the isHungry attribute to False and increases the weight by 0.1 kg.
    def eat(self):
        self.isHungry = False
        self.weight = round(self.weight + 0.1, 1)
        print(f"{self.name} : Chomp Chomp")

    # Simulates the dog going for a walk.
    # If the dog is hungry, it barks. Otherwise, it decreases the weight by 0.1 kg and sets isHungry to True.
    def walk(self):
        # If the dog is hungry, it barks.
        if self.isHungry:
            self.bark()
        # If the dog is not hungry, it decreases the weight and sets isHungry to True.
        else:
            self.weight = round(self.weight - 0.1, 1)
            self.isHungry = True
            print(f"{self.name} : Step Step")

    # Prints the dog's status, including its name, color, weight, and hunger status.
    def printStatus(self):
        print(
            f"{self.name} is {self.color} in color, weighs {self.weight} kg and is {'hungry' if self.isHungry else 'not hungry'}"
        )


# Prints the command menu for the program.
def command_menu():
    print(
        "Enter the command\n"
        "'S' to get Status enquiry,\t\t"
        "'F' to feed the dog,\n"
        "'W' to take it for a walk,\t\t"
        "'Q' to exit:"
    )


def main():
    # Create a Dog object names Willie.
    willie = Dog("Willie", "brown", 15.0)

    print(f"{willie.name} welcomes you! Woof woof")

    # Main loop for the program.
    # The loop continues until the user enters 'Q' to quit.
    command = ""
    while command != "Q":
        print("-" * 40)
        command_menu()
        while True:
            command = input().upper().strip()
            if command in ["S", "F", "W", "Q"]:
                break
            else:
                print("Invalid command")

        match command:
            case "S":
                willie.printStatus()
            case "F":
                willie.eat()
            case "W":
                willie.walk()

    print("Good bye! Woof woof")


if __name__ == "__main__":
    main()
