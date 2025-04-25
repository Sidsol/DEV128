class Dog:
    def __init__(self, name: str, color: str, weight: float = 10.0):
        self.name = name
        self.color = color
        self.isHungry = True
        self.weight = weight

    def bark(self):
        print(f"{self.name} : Woof Woof")

    def eat(self):
        self.isHungry = False
        self.weight = round(self.weight + 0.1, 1)
        print(f"{self.name} : Chomp Chomp")

    def walk(self):
        if self.isHungry:
            self.bark()
        else:
            self.weight = round(self.weight - 0.1, 1)
            self.isHungry = True
            print(f"{self.name} : Step Step")

    def printStatus(self):
        print(
            f"{self.name} is {self.color} in color, weighs {self.weight} kg and is {'hungry' if self.isHungry else 'not hungry'}"
        )


def command_menu():
    print(
        "Enter the command\n"
        "'S' to get Status enquiry,\t\t"
        "'F' to feed the dog,\n"
        "'W' to take it for a walk,\t\t"
        "'Q' to exit:"
    )


def main():
    willie = Dog("Willie", "brown", 15.0)

    print(f"{willie.name} welcomes you! Woof woof")

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
