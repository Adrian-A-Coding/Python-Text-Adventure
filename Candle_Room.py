from PlayableScene import Scene


class CandleRoom(Scene):
    def __init__(self, current_player):
        super().__init__(current_player)
        self.exit_module = __import__("Totem_Room")

    def displayRoom(self):
        # Talk about some big altar with rows of candles behind it, some lit, most out
        print("\nFurther down the hall you come upon a rounded room with the center holding an altar covered in "
              "melting candles and opened tomes. All around the rooms are candles\nseated within carved out openings "
              "within the wall. The room's domed roof is adorned with constellations and a sea of stars, glimmering "
              "faintly under the candlelight.\nAs you step before the altar you notice a key atop it.")

    def searchableItems(self):
        if "rusted key" in self.player.inventory:
            print("\nThe altar is empty of anything useful now, the room has no more value to you now.")
        else:
            print("\nThe key on the altar is rusted and looking like it's ready to crumble apart.")
            self.player.addingToInventory("rusted key")

    def exits(self, user_input: str):
        match user_input:
            case "backward":
                print("\nYou step away from the altar and turn back to the totem room, facing the totem as you did "
                      "when you first entered the room.")
                self.player.current_room = self.exit_module.TotemRoom(self.player)
            case _:
                print("There are no other exits from this room beside the one behind you. You would only be stepping on"
                      " candles.")
