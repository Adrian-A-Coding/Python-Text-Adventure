from Player import Player


class Scene:
    player: Player

    def __init__(self, current_player: Player):
        self.player = current_player

    def displayRoom(self):  # Print out the room's description
        pass

    def searchableItems(self):  # Handle searching for and picking up items for the player object
        print("\nThere is nothing of note here, you're better off searching another room.")

    def interaction(self):  # This is what should handle operating certain objects like levers or doors
        print("\nThere isn't anything in this room for you to meaningfully interact with.")

    def exits(self, user_input: str):  # Want the scene to have exits which refer to valid scene objects or files
        pass
