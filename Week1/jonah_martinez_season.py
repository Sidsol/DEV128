#Assignment: Seasons
#Class: DEV 128
#Date: 04/09/2025
#Author: Jonah Martinez
#Description: This program determines the season based on the month and day chosen by the user.

# Validate the user input for month and day, ensuring they are within the correct range.
def validate_user_input(string, lower_bound, upper_bound):
    while True:
        valid_input = input(f"Please enter the {string} (Between {lower_bound} and {upper_bound}): ")
        if not valid_input.isdigit() or not (lower_bound <= int(valid_input) <= upper_bound):
            print(f"Invalid {string} entered.")
            continue
        return int(valid_input)

# Validate the user input for replay, ensuring it is either 'y' or 'n'.
def validate_replay_input():
    while True:
        replay = input("Enter another input? (y/n): ").lower()
        if replay in ['y', 'n']:
            return replay
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

# Determine the upper bound for the day based on the month.
def determin_upper_bound_day(month):
    match month:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            upper_bound = 31
        case 4 | 6 | 9 | 11:
            upper_bound = 30
        case 2:
            upper_bound = 28
    return upper_bound

# Determine the season based on the month and day.
def determine_season(month, day):
    # For dates from 12/16 to 3/15, the season should be declared "Winter"
    if (month, day) >= (12, 16) or (month, day) <= (3, 15):
        season = "Winter"
    # For dates from 3/16 to 6/15, the season should be declared "Spring"
    elif (month, day) >= (3, 16) and (month, day) <= (6, 15):
        season = "Spring"
    # For dates from 6/16 to 9/15, the season should be declared "Summer".
    elif (month, day) >= (6, 16) and (month, day) <= (9, 15):
        season = "Summer"
    # For dates from 9/16 to 12/15, the season should be declared "Fall"
    else:
        season = "Fall"
    
    print("Season = ", season)
            
def main():
    #Intro
    print("Welcom to the Seasons program")
    while True:
        
        lower_bound = 1
        total_months = 12
        
        # Get user input for month
        month = validate_user_input("month", lower_bound, total_months)

        # Determine the upper bound for the day based on the month
        upper_bound_day = determin_upper_bound_day(month)

        # Get user input for day
        day = validate_user_input("day", lower_bound, upper_bound_day)

        # Determine the season based on the month and day
        determine_season(month, day)
        
        # Ask user to replay or exit
        # Exit if the user enters 'n'
        replay = validate_replay_input()
        if replay == 'n':
            break   
    
if __name__ == "__main__":
    main()