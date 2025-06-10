# Assignment: martinez_jonah_Piggybank.py
# Class: DEV 128
# Date: 05/09/2025
# Author: Jonah Martinez
# Description: Midterm Piggybank

## Definition of a PiggyBank class
## It can only hold quarters and dimes with a limit on total
##   weight in grams.
##   Note: A dime weighs 2.268 grams and a quarter weighs 5.670 grams.
##
sep = "-" * 40


class PiggyBank:
    """PiggyBank class which holds only dimes and quarters with a limit on total
    weight in grams."""

    MAX_WEIGHT = 200
    DIME_WEIGHT = 2.268
    QUARTER_WEIGHT = 5.670
    DIME_VALUE = .10
    QUARTER_VALUE = .25
    
    def __init__(self, quarters: int = 0, dimes: int = 0):

        # total_weight = (quarters * PiggyBank.QUARTER_WEIGHT) + (
        #     dimes * PiggyBank.DIME_WEIGHT
        # )

        self.__quarters = quarters
        self.__dimes = dimes

        if quarters < 0 or dimes < 0:
            print(
                "Negative coint counts not accepted. Setting to 0."
            )
            self.__quarters = 0
            self.__dimes = 0
        elif self.capacity > 100:
            # elif total_weight > PiggyBank.MAX_WEIGHT:
            print("Maximum weight exceeded. Setting to 0.")
            self.__quarters = 0
            self.__dimes = 0
        else:
            self.__quarters = quarters
            self.__dimes = dimes

    @property
    def quarters(self):
        return self.__quarters

    @quarters.setter
    def quarters(self, moreQuarters):
        self.__quarters += moreQuarters
        if self.capacity > 100:
            self.__quarters -= moreQuarters
            print("Maximum weight exceeded. No update.")

    @property
    def dimes(self):
        return self.__dimes

    @dimes.setter
    def dimes(self, moreDimes: int):
        self.__dimes += moreDimes
        if self.capacity > 100:
            self.__dimes -= moreDimes
            print("Maximum weight exceeded. No update.")

    @property
    def dollarValue(self):
        return round((self.__quarters * PiggyBank.QUARTER_VALUE) + (
            self.__dimes * PiggyBank.DIME_VALUE
        ), 2)

    @property
    def capacity(self):
        total_weight = (self.__quarters * PiggyBank.QUARTER_WEIGHT) + (
            self.__dimes * PiggyBank.DIME_WEIGHT
        )
        return round((total_weight / PiggyBank.MAX_WEIGHT) * 100, 2)
    
    def transferFrom(self, transferToo: "PiggyBank"):
        if self.capacity + transferToo.capacity > 100:
            print("Cannot transfer coins as it will exceed the weight limit of the target piggy bank.")
            return

        self.__quarters += transferToo.__quarters
        self.__dimes += transferToo.__dimes

        transferToo.__quarters = 0
        transferToo.__dimes = 0

###############################################################################
##Client code. Creates PiggyBank objects and interacts with them
################################################################################


def printBank(name, bank):
    print(
        f"{name}: ${bank.dollarValue} (quarters:{bank.quarters},dimes:{bank.dimes}) {bank.capacity}% full"
    )
    print(sep)


def main():
    print(sep)

    print("Welcome!")
    print(f"MAX_WEIGHT of PiggyBank: {PiggyBank.MAX_WEIGHT}")
    print(sep)
    my_Bank1 = PiggyBank(5, 10)
    printBank("my_Bank1", my_Bank1)  # $2.25

    my_Bank2 = PiggyBank(60, 60)  # Should print maximum weight exceeded.Setting 0.
    printBank("my_Bank2", my_Bank2)  # $0.0

    my_Bank2.dimes = 20  #
    my_Bank2.quarters = 70  # Should print max weight exceeded and not update
    my_Bank2.quarters = 10
    printBank(f"my_Bank2", my_Bank2)  # $4.5

    print("Transferring..")
    my_Bank1.transferFrom(my_Bank2)  # my_Bank2 should be emptied after the transfer
    print(f"my_Bank2 capacity: {my_Bank2.capacity}%")  # should be 0%
    printBank(f"my_Bank1", my_Bank1)  # $6.75

    my_Bank3 = PiggyBank(
        -10, -10
    )  # Should print negative count not accepted. Setting to 0.
    printBank(f"my_Bank3", my_Bank3)  # 0 $0.0
    my_Bank3.quarters = 12
    printBank(f"my_Bank3", my_Bank3)  # $3.75

    my_Bank1.transferFrom(my_Bank3)  # cannot transfer since MAX_WEIGHT exceeded.
    printBank("my_Bank1", my_Bank1)  # $6.75

    my_Bank4 = PiggyBank()
    printBank("my_Bank4", my_Bank4)  #  0 $0.0

    print("Good bye!")


if __name__ == "__main__":
    main()
