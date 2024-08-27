from PlayableScene import Scene


class OpeningScene(Scene):
    isLockedDoor: bool

    def __init__(self, current_player):
        super().__init__(current_player)
        self.isLockedDoor = True
        self.exit1_module = __import__("Start_Exit_Scene")
        self.exit2_module = __import__("Cage_Elevator_Shaft")

    def displayRoom(self):
        print("\nLeft of this room lies the crumbled entrance of the passageway that brought you to this room. There is"
              " no going back this way. To your right lies a rusty door shut tight,\nit looks like a key might open it."
              " Behind you there is a desecrated effigy of a god long forgotten to a time far in the past. In front of "
              "you there is a dimly lit hallway\nleading to a closed door.")

    def searchableItems(self):
        if not self.isLockedDoor:
            print("The door is unlocked and there is still nothing else to find in here.")
            return
        else:
            print("\nThere is nothing to pick up in this room, all you find is the locked door in need of a key.")
            return

    def interaction(self):
        if "rusted key" in self.player.inventory:
            print("\nWith the rusted key in hand you twist and hear the crank of the door unlocking. You can now pass "
                  "through it.")
            self.isLockedDoor = False
            return
        elif not self.isLockedDoor:
            print("\nYou have already opened the door, no need to mess with it anymore and you won't find anything else"
                  " in here.")
            return
        else:
            print("\nYou have nothing in your inventory to open the rusted door with.")
            return

    def exits(self, user_input: str):
        match user_input:
            case "forward":
                self.player.current_room = self.exit1_module.FirstHallway(self.player)
                self.player.current_room.displayRoom()
            case "right":
                if not self.isLockedDoor:
                    print("\nYou move into the room with the rusted door, pushing it open.")
                    self.player.current_room = self.exit2_module.CageElevatorShaft(self.player)
                    self.player.current_room.displayRoom()
                else:
                    print("\nThe door is still shut tight, you're missing the key to open it.")
            case _:
                print("\nYou cannot travel", user_input, "as it is inaccessible.")
