from PlayableScene import Scene


class FirstHallway(Scene):
    def __init__(self, current_player):
        super().__init__(current_player)
        # import start scene dynamically
        self.exit1_module = __import__("Start_Scene")
        self.exit2_module = __import__("Totem_Room")

    def displayRoom(self):
        print("\nYou're greeted with a dark, foul hallway that as you walk further feels more claustrophobic. At the en"
              "d of the hallway is a rusted door slightly ajar with a soft yellow glow\nemanating from beyond.")

    def exits(self, user_input: str):
        match user_input:
            case "forward":
                print("\nYou push the door open further with all your might and step into the room before you.")
                self.player.current_room = self.exit2_module.TotemRoom(self.player)
                self.player.current_room.displayRoom()
            case "backward":
                print("\nYou make your way into the room where your adventure started now at its center once more.")
                self.player.current_room = self.exit1_module.OpeningScene(self.player)
            case _:
                print("\nYou cannot travel", user_input, "as it is an impassible wall. You only have behind you where "
                      "your journey began and forward to the totem room.")
