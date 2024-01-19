import random
import os
from PIL import Image


items = ["diamond ring", "key", "knife", "trap", "russian tank", "rose"]

inventory = []

description = {
    "Entrance": "You are in the house entrance. There is a King Charles III painting, a (stolen) Banksy, a selfie stick, and doors to the north and east",
    "Garage": "You are in a garage. Theres a new Tesla, a Benz and a Russian Tank. Also a door to the west and north.",
    "Hallway": "You are in a hallway. There are doors to the north, east, west and south.",
    "Garden": "You are in a Garden. There are roses fertilizer and a corpse, and a door to the west and south,",
    "Master Bedroom": "You are in a bedroom. There is a bed, a dresser and a key. There's a door to the south and a door to the west.",
    "Bathroom": "You are in a bathroom. There is a sink, a toilet and a diamond ring, and a door to the south and east.",
    "Kitchen":"You are in the kitchen there is a knife, a ham leg and fish and chips. There is a door to the east and to the north."
}

rooms = {
    "Entrance": {"east": "Garage", "north": "Hallway"},
    "Garage": {"west": "Entrance", "north": "Garden"},
    "Hallway": {"north": "Master Bedroom", "south": "Entrance", "east": "Garden", "west": "Kitchen"},
    "Garden": {"west": "Hallway", "south": "Garage"},
    "Master Bedroom": {"south": "Hallway", "west": "Bathroom"},
    "Bathroom": {"south": "Kitchen", "east": "Master Bedroom"},
    "Kitchen": {"east": "Hallway", "north": "Bathroom"}
}

options = ["Move to a different room", "Find item", "quit", "Open door"]


class Player:

    def __init__(self, position: str):
        self.position = position

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position


#Instantiate player object
player = Player("Entrance")


# clears the terminal to make game more readable
def clear():
    os.system("cls" if os.name == "nt" else "clear")


# first menu player sees when starting the game. Gives option to show map or not
def map():
    print("Welcome to the Mansion!\n")
    print("Rules - To win the game you need to pick up 4 or more items and reach the 'Master Bedroom' to win the game.\n      - Be careful to not step on any traps or its game over!")
    main_menu = input("\nMap or no map? (y/n): ")

    while True:

        if main_menu == "y":
            img = Image.open('map2.PNG')
            img.show()
            break

        elif main_menu == "n":
            break

        else:
            print("Invalid input.")
            continue
    print("")


# displays the options the player has after every move
def prompt():
    print(f"Location: {player.get_position()}\n{description[player.get_position()]}\n")
    print(f"Inventory: {inventory}")
    print("-------------------------")
    if len(inventory) >= 4 and player.get_position() == "Master Bedroom":
        for i in range(len(options)):
            print(f"{i + 1}. {options[i]}")
        print("-------------------------")
        print("")

    else:
        for i in range(len(options) - 1):
            print(f"{i + 1}. {options[i]}")
        print("-------------------------")
        print("")


# main game loop
def game_loop():

    # Randomizes item locations except for the item in the first room so the player doesn't get a trap instantly
    random.shuffle(items)
    item_location = {
    "Entrance": "",
    "Garage": items[0], 
    "Hallway": items[1],
    "Garden": items[2],
    "Master Bedroom": items[3],
    "Bathroom": items[4],
    "Kitchen": items[5]
    }


    while True:

        prompt()
        next_move = (input("Next move (Type 1, 2 or 3): "))

        match(next_move):

            # movement of player in specific direction
            case "1":

                while True:

                    direction = input("where to you want to move? (Type: north, west, east or south)\n")

                    if direction in ["north", "west", "east", "south"]:
                        clear()

                        try: 
                            player.set_position(rooms[player.get_position()][direction])
                            break

                        except KeyError:
                            print("Can't move in that direction.")
                    
                    elif direction == "back":
                        break

                    else:
                        clear()
                        print("Invalid Input. Please enter 'north, west, east or south'.\n")
                        continue

            # Picking up item
            case "2":

                clear()

                if item_location[player.get_position()] == "trap":
                    print("you have died.")
                    return False
                
                elif item_location[player.get_position()]:
                    print(f"you have found {item_location.get(player.get_position())}")
                    inventory.append(item_location.get(player.get_position()))
                    item_location[player.get_position()] = ""

                elif item_location[player.get_position()] == "":
                    print("You find nothing")
                    continue

            # Quitting the game
            case "3":
                break

            # Beating the game
            case "4":
                print("you have beaten the game!")
                break

            # Validating user input
            case _:
                clear()
                print("Please enter a valid input.\n")
                continue


def main():
    clear()
    map()
    game_loop()

if __name__ == "__main__":
    main()