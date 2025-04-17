#Assignment: Dice Simulator
#Class: DEV 128
#Date: 04/09/2025
#Author: Jonah Martinez
#Description: This program simulates the rolling of a die.
 
import random

# Function to print the header. As seen in the Sample run 3 above.
def display_title():
    multiplier = 40
    
    print(f"{'='*multiplier}"
          + "\nWelcome to the Dice Roller"
          + f"\n\n{'='*multiplier}")

# Function to simulate rolling of a single 6-sided die. 
# It returns the result of the roll.
def roll():
    return random.randint(1, 6)

# Function that accepts the count of rolls to be simulated as a positive integer input parameter. 
# It then calls the roll function that many times, printing the resulting roll and adding it to a list. 
# It returns the list to the caller.
def roll_dice(count_of_rolls):    
    rolls = []
    for i in range(count_of_rolls):
        roll_result = roll()
        rolls.append(roll_result)
        print(f"Die {i+1}: {roll_result}")
        
    return rolls

# Function to prompt the user for the count of rolls to be simulated. 
# It validates that the number is greater than zero. 
# If not, gives user feedback and prompts again.
def get_positive_count():
    while True:
        try:
            number_of_dice = int(input("Enter the number of dice: "))
        except ValueError:
            print("Please enter an integer value.") 
            continue

        if int(number_of_dice) <= 0:
            print("Please enter a positive number")
            continue
        
        return int(number_of_dice)

# Function to print the outcome of the rolls.
# It checks the number of 6s rolled and prints a message based on the count.
def print_outcome(roll_array):
    count_of_six = roll_array.count(6)
    
    if count_of_six == len(roll_array):
        print(f"Yay! All rolls were the same.")
    elif count_of_six == 0:
        print(f"Sorry! No 6 found!")
    else:
        print(f"Got 6 in {count_of_six} rolls.")        
    
    
# Validate the user input for replay, ensuring it is either 'y' or 'n'.
def validate_replay_input():
    while True:
        replay = input("Enter another input? (y/n): ").lower()
        if replay in ['y', 'n']:
            return replay
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
              
def main():
    
    # Intro 
    display_title()
    
    # Loop to allow the user to roll dice multiple times.
    while True:
        
        dice_rolls = get_positive_count()
        roll_array = roll_dice(dice_rolls)
        print_outcome(roll_array)
        
        # Exit if the user enters 'n'
        replay = validate_replay_input()
        if replay == 'n':
            break   

if __name__ == "__main__":
    main()