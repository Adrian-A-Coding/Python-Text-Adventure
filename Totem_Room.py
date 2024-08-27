from PlayableScene import Scene


class TotemRoom(Scene):
    def __init__(self, current_player):
        super().__init__(current_player)
        self.exit1_module = __import__("Start_Exit_Scene")
        self.exit2_module = __import__("Wood_Carver_Shop")
        self.exit3_module = __import__("Candle_Room")

    def displayRoom(self):
        print("\nWithin the warm glow of candlelight a large, rotting, wooden totem stood over you with its air of sick"
              "ly superiority. The stale air of the hallway you came from lingers\nfaintly behind you while you observe"
              " behind the totem a solid wall. The only openings are to your left and right, both gaping maws of darkne"
              "ss inviting you to venture within.")

    def exits(self, user_input: str):
        match user_input:
            case "left":
                print("\nLeaving the candlelit room you venture left into a much dimmer room.")
                self.player.current_room = self.exit2_module.WoodShop(self.player)
                self.player.current_room.displayRoom()
            case "right":
                print("\nYou take a step into the dark and walk further away from the light of the totem room.")
                self.player.current_room = self.exit3_module.CandleRoom(self.player)
                self.player.current_room.displayRoom()
            case "backward":
                print("\nYou venture back into the foul stale air of the hallway leading to where you awoke in.")
                self.player.current_room = self.exit1_module.FirstHallway(self.player)
            case _:
                print("\nThere is no way forward, only the other paths are available.")
