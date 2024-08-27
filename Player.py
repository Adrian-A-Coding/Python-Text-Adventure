class Player:
    user_input: str
    isPlaying: bool
    inventory: list = []
    current_room = None  # To prevent circular dependency issue with calling Scene and not having it static

    def __init__(self, playing):
        self.isPlaying = playing

    # Method to add items to the inventory from within a scene and only needs a string item to add
    def addingToInventory(self, item_name: str):
        player_choice = input("Would you like to pick up the {}?(y/n) ".format(item_name)).lower().strip()
        if player_choice == "y":
            print("\nYou pick up the {} and place it within your pack.".format(item_name))
            self.inventory.append(item_name)
        else:
            print("\nYou decide against taking what isn't yours and leaving it be.")

    def displayInventory(self):  # Work out display for how the player gets to see their inventory
        if not self.inventory:
            print("\nThere isn't anything in your inventory!")
        else:
            print("\nThe following is what you have in your inventory currently:")
            print(", ".join(self.inventory))

    # Actions the player can take in the given room as defined
    def act(self):
        match self.user_input:
            case "left":
                self.current_room.exits(self.user_input)
            case "right":
                self.current_room.exits(self.user_input)
            case "forward":
                self.current_room.exits(self.user_input)
            case "backward":
                self.current_room.exits(self.user_input)
            case "display":
                self.current_room.displayRoom()
            case "inventory":
                self.displayInventory()
            case "search":
                self.current_room.searchableItems()
            case "interact":
                self.current_room.interaction()
            case "exit":
                print("\nThank you for playing!")
                self.isPlaying = False
            case _:
                print("\nYour input does not match any available actions, please try again.")
