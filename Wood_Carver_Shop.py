from PlayableScene import Scene


class WoodShop(Scene):
    def __init__(self, current_player):
        super().__init__(current_player)
        self.exit_module = __import__("Totem_Room")

    def displayRoom(self):
        print("\nBy the light of a single candle you can make out the decrepit woodcarving shop of the presumed totem"
              "maker. No other exits into the room are present and most of the sculptures\nlining the walls and "
              "scattered across the workstation were rotting. There's hardly any useful knickknacks present amongst the"
              "rotten wood.")

    def searchableItems(self):
        if "carving knife" in self.player.inventory:
            super().searchableItems()
        else:
            print("\nAnother viewing of the room reveals a faint glint from the clutter on the workstation. You can "
                  "make out the shape of a rusted carving knife.")
            self.player.addingToInventory("carving knife")

    def exits(self, user_input: str):
        match user_input:
            case "backward":
                print("\nYou step back to the light of the totem room into the spot before the statue, the wood shop"
                      " now to your left again.")
                self.player.current_room = self.exit_module.TotemRoom(self.player)
            case _:
                print("\nThere are no exits in that direction, only the way you entered behind you.")
