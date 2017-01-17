"""
Import functions
"""
from adventure import intro, StartingRoom, RoomInfo, HelpCommands, GoForward, GoBack
"""
Import functions
"""
from adventure import RoomLook, RoomClue, RoomObjects, LookObject, OpenObject, KickObject
"""
Import functions
"""
from adventure import UnlockDoor, MoveObject, CheckChestLock, CheckInv, AddInv, RemoveInv
"""
Import functions
"""
from adventure import currentRoom, useItem
"""
Import getopt and sys
"""
import getopt, sys

def main():
    """
    Listen
    """
    intro()
    room = StartingRoom()
    RoomInfo()
    while True:
        choice = input("--> ")

        if choice == "quit":
            return
        elif choice == "h" or choice == "help":
            HelpCommands()
        elif choice == "i" or choice == "info":
            RoomInfo()
        elif choice == "fw" or choice == "forward":
            room = GoForward()
        elif choice == "ba" or choice == "back":
            GoBack()
        elif choice == "look":
            RoomLook()
        elif choice == "c" or choice == "clue":
            RoomClue()
        elif choice == "o" or choice == "objects":
            RoomObjects()
        elif "l " in choice or "look" in choice and len(choice) > 4 and "open" not in \
        choice and "kick" not in choice and "move" not in choice:
            theObject = choice.split(" ", 1)[1]
            theObject = theObject.lower()
            LookObject(theObject)
        elif "op " in choice and "drop" not in choice or "open" in choice and "look" not in choice and "kick" not \
        in choice and "move" not in choice:
            theObject = choice.split(" ", 1)[1]
            theObject = theObject.lower()
            OpenObject(theObject)
        elif "k " in choice or "kick" in choice and "open" not in choice and "look" not \
        in choice and "move" not in choice:
            theObject = choice.split(" ", 1)[1]
            theObject = theObject.lower()
            KickObject(theObject)
            room = currentRoom()
            if "button" in theObject and room == "5":
                UnlockDoor()
        elif "m " in choice or "move" in choice and "open" not in choice and "kick" not \
        in choice and "look" not in choice:
            theObject = choice.split(" ", 1)[1]
            theObject = theObject.lower()
            MoveObject(theObject)
            room = currentRoom()
            if "shrine" in theObject and room == "1":
                CheckChestLock()
        elif choice == "inv" or choice == "inventory":
            CheckInv()
        elif "take" in choice:
            theObject = choice.split(" ", 1)[1]
            theObject = theObject.lower()
            AddInv(theObject)
        elif "dr " in choice or "drop" in choice:
            theObject = choice.split(" ", 1)[1]
            theObject = theObject.lower()
            RemoveInv(theObject)
        elif "u " in choice or "use" in choice:
            theObject = choice.split(" ", 1)[1]
            theObject = theObject.lower()
            useItem(theObject)
        else:
            print("Unknown command", choice)
            HelpCommands()


        #input("\nPress enter to continue...")

#------------------------------------------------------------------------------

def usage():
    """
    Print help
    """
    print("""
    Usage:
        ./adventure.py command

    Commands:
        -h --help                                   Show this help message
        -i --info                                   Show game info
        -v --version                                Game version
        -a --about                                  About the creator
        -c --cheat                                  Cheat for game
        """)

def info():
    """
    Print info
    """
    print("""
    This is a text-based game which is about solving small puzzles to move
    forward. In the game are seven rooms, and in each room you have to do
    a tast or series of tasks to unlock the next room.

    In an attempt to make it a little more interesting I have chosen to do this
    in a fictional world based on The Elder Scrolls video game series.

    The game is written in Python.
    """)

def version():
    """
    Print version
    """
    versionnr = "0.21"
    print("\nVERSION: " + versionnr)

def about():
    """
    Print about
    """
    print("""
    The game was created by me, André Johansson, a student at Blekinge
    Institute of Technology in Karlskrona. I'm 22 years old, living currently
    in Karlshamn.

    I like games, coding, tv series, cars, planes, space, art, design and many
    other things. But coding for the web is what I can see myself doing as a
    job, which is the reason I'm studying web programming. It's good fun.
    """)

def cheat():
    """
    Print cheat
    """
    print("""
    The following shows the quickest path you can take through the game. If
    you type the commands below in the order shown, you will complete the game.

    move left shrine
    move middle shrine
    move middle shrine
    move right shrine
    move right shrine
    open chest
    take key
    use key
    forward
    move skull
    move sword
    forward
    move right torch
    forward
    kick wooden box
    take fishing rod
    use fishing rod
    use dirty key
    forward
    kick serpent button
    kick warrior button
    forward
    kick the wall
    kick the wall
    kick the wall
    forward
    kick the keeper
    use staff
    open grate
    kick the keeper
    kick crystal
    """)

def clmain():
    """
    Listen to parameters
    """
    try:
        opts = getopt.getopt(sys.argv[1], "hivac", ["help", "info", "version", "about", "cheat"])
    except getopt.GetoptError:
        print("\nCommand", sys.argv[1:], "not found\n")
        usage()
        sys.exit(1)
    for opt in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit(0)
        elif opt in ("-i", "--info"):
            info()
            sys.exit(0)
        elif opt in ("-v", "--version"):
            version()
            sys.exit(0)
        elif opt in ("-a", "--about"):
            about()
            sys.exit(0)
        elif opt in ("-c", "--cheat"):
            cheat()
            sys.exit(0)
