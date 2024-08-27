"""
Name: Adrian Aguilar
Assignment: Final Project
Last Updated:8/17/24
Planned Improvements: Adding Textual for UI and making the story much longer with more time and options to interact. I
may want to include characters later on or even a basic fighting system.
"""
# import textual
# lightweight gui option for later
from Player import Player
from Start_Scene import OpeningScene


def main():
    print("Welcome traveler to the labyrinth of Confusion! Navigate out after observing your surroundings.")
    print("Feel free to grab as much as you can carry into your backpack!")
    # Create a new player object and the first opening scene
    p = Player(True)
    p.current_room = OpeningScene(p)
    p.current_room.displayRoom()

    while p.isPlaying:
        print("Enter DISPLAY to view the room description again.")
        print("Enter SEARCH to see if a room has any items to pick up or interactable objects within. You can also type"
              " in INTERACT to mess with certain objects.")
        print("Enter INVENTORY to view the objects you're carrying.")
        print("If you would like to stop playing type in EXIT.")
        p.user_input = input("Now you may enter a direction to travel: LEFT/RIGHT/FORWARD/BACKWARD ").lower()
        p.act()


if __name__ == "__main__":
    main()
