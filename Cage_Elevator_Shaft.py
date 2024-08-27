from PlayableScene import Scene


class CageElevatorShaft(Scene):
    def __init__(self, current_player):
        super().__init__(current_player)
        self.elevatorPresent = False
        self.exit1_module = __import__("Start_Scene")

    def displayRoom(self):
        if not self.elevatorPresent:
            print(
                "\nBeyond the creaking door you step forward before a short hallway into a large room, a deep chasm in "
                "the center. From above there is faint natural light guiding a chain down into the darkness of the pit."
                " There appears to be a small\nswitch on the right most wall, covered in cobweb and layered with dust. "
                "Nothing besides the button is prominent within this room.")
        else:
            print("\nThe room once housing an empty chasm with a single chain descending into it now contains a cage "
                  "in the center of the it. It holds steady connected to the chain ready for use and anyone brave "
                  "enough\nto step within it. The door on the cage is shut tight and within you can make out some sort "
                  "of control console.")

    def searchableItems(self):
        print("\nLooking to your right you can make out the cobweb covered button built into the wall. You may be able"
              " to press it and see what comes next.")
        if self.elevatorPresent:
            print("\nIt would seem that your curiosity has allowed you some sort of ride.")

    def interaction(self):
        if not self.elevatorPresent:
            call_elevator = input("\nThe button is jutted out looking like it can be pressed, would you like to?(y/n) ")
            call_elevator.strip().lower()
            if call_elevator == "n":
                self.elevatorPresent = True
                print("\nWith the button pressed a screech followed by a throbbing creak echo from below in the shaft "
                      "while the chain begins to shift upward. After a long moment you notice curved bars peering from"
                      " the darkness as\na large bird cage breaks from the veil and levels it self with the room.")
            else:
                print("It feels like it would be best to step away and not gamble with this outcome.")
        else:
            print("\nThe button is flat to it's case and cannot be pushed any further with the elevator here.")

    def exits(self, user_input: str):
        match user_input:
            case "backward":
                print("\nYou turn around and make your way to the rusted door and begin to pull it open to exit.")
                self.player.current_room = self.exit1_module.OpeningScene(self.player)
            case "forward":
                if self.elevatorPresent:
                    print("\nWith the elevator present you pull it's door open and step into it. Here you can see your"
                          " next choice to go up or down.")
                    while True:
                        up_or_down = input("Which direction would you like to travel to?(up/down): ").lower().strip()
                        match up_or_down:
                            case "up":
                                print("\nThe elevator lets out a groan as it begins to move upward shuttering on its "
                                      "climb to freedom. It takes a few minutes before the light at the surface grows "
                                      "brighter and\nreaches out to greet you. By the time you're enveloped in sunlight"
                                      " you can smell the forest you traveled through to reach the labyrinth's entrance"
                                      " and descended. The time since has been long and now you've made your way out.\n"
                                      "There's no reason to leave this elevator accessible so you must condemn it as "
                                      "unsafe for future explorers. You certainly must do your due diligence as a "
                                      "skilled adventurer!")
                                self.player.isPlaying = False
                                print("You've made the right choices and are free, congratulations!")
                                break
                            case "down":
                                print("\nThe elevator squeals as it begins slowly to descend into the chasm feeding you"
                                      " to the darkness as all light begins to evaporate. It starts slow but you can "
                                      "feel the\nelevator speed up as it rapidly begins to speed up its descent. It's "
                                      "as if the labyrinth wants you to quickly find out its secrets, but it's nothing"
                                      " but a ruse. There's a creaking as the elevator screams and the chain holding it"
                                      " snaps and you can\nfeel your stomach floating as you accelerate. Its all sudden"
                                      " until you hear the crash before nothing. Your journey has ended prematurely "
                                      "before you can explore further or remember why you stepped foot into this place "
                                      "and what you need from it.")
                                print("But there won't be any answers for you, and the labyrinth will be able to invite"
                                      " others to find that answer.")
                                self.player.isPlaying = False
                                print("You are now one with this labyrinth, there is no freedom for you.")
                                break
                            case _:
                                print("That didn't match with either up or down as valid directions.")
                else:
                    print("\nThere is no elevator present to take you anywhere, maybe you can find a call button.")
            case _:
                print("There is only going back behind the rusted door or forward, wherever the elevator may take you.")
