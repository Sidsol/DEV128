# Assignment: StationaryStore.py
# Class: DEV 128
# Date: 05/09/2025
# Author: Jonah Martinez
# Description: Midterm StationaryStory

# Stationery Store ordering system

def displayItemList(itemList):
    """Displays the itemList in tabular form"""
    print("Id\tName\t\tPrice\tCount")

    # Iterate over the items in the itemsList dictionary and display the values for each field
    for item, details in itemList.items():
        print(
            f"{item}:\t{details["name"]}\t{details["pricePerUnit"]}\t{details["count"]}"
        )


def calculateTotalPrice(itemList):
    """Function to calculate the total price of the currentOrder based on the
    itemList"""
    totalPrice = 0
    for items, details in itemList.items():
        totalPrice += details["count"] * details["pricePerUnit"]

    return round(totalPrice, 2)  # Implement this


def main():
    sep = "-" * 80
    print("Welcome to Bellevue Stationery")
    print(sep)
    # Dictionary to hold current order. Keys are strings representing itemIDs,
    # values are dictionaries with fields name, pricePerUnit and count
    itemList = {
        "ID001": {"name": "Notebook", "pricePerUnit": 1.79, "count": 0},
        "ID002": {"name": "Color Markers", "pricePerUnit": 2.99, "count": 0},
        "ID003": {"name": "Sticky Tape", "pricePerUnit": 3.35, "count": 0},
        "ID004": {"name": "Scissors", "pricePerUnit": 4.25, "count": 0},
        "ID005": {"name": "Pencil Box", "pricePerUnit": 4.99, "count": 0},
    }

    displayItemList(itemList)

    ans = "y"
    while ans == "y":
        #
        # prompt the user to enter ID and count of the item
        # update count in the itemList with this item
        # add error handling to take care of
        #       invalid itemID,
        #       non-integer count,
        itemId = input("Enter the Id of an item to add: ").strip().upper()
        item = itemList.get(itemId)
        if not item:
            print(f"Invalid ItemdId")
        else:
            try:
                count = int(input(f"Enter the count of the {itemList[itemId]["name"]}: "))
                if count < 0:
                    print("Something went wrong: Negative count not allowed")
                else:
                    # Update the count in the itemList
                    itemList[itemId]["count"] = count
            except ValueError:
                print("Invalid ItemId.")    
            

        print(sep)
        displayItemList(itemList)

        totalPrice = calculateTotalPrice(itemList)
        print("Total price so far: ", totalPrice)
        print(sep)
        ans = input("Order more items?(y/n) ").lower()

    print("Goodbye!")


if __name__ == "__main__":
    main()
