#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Importing stuff and things
"""
import sys, random, json

rooms = ["1", "2", "3", "4", "5", "6", "7"]
room = "0"
unlocked = {"1": "unlocked", "2": "locked", "3": "locked", "4": "locked", "5": "locked", "6": "locked", "7": "locked", }
shrines = {"Left Shrine": "blue", "Middle Shrine": "yellow", "Right Shrine": "red"}
#shrines = {"Left Shrine": "blue", "Middle Shrine": "blue", "Right Shrine": "yellow"}
plates = {"Skull Plate": "inactive", "Sword Plate": "inactive"}
torches = {"Left Torch": "placed", "Middle Torch": "placed", "Right Torch": "placed"}
ObjectState = {"Chest": "intact", "Wooden Box": "intact"}
buttons = {"Serpent": "inactive", "Warrior": "inactive", "Theif": "inactive", "Mage": "inactive"}
roomSeven = {"KeeperStaff": "False", "KeeperLocked": "False", "GrateLocked": "True", "GrateOpen": "False"}
chestLocked = True
keyObtainable = False
FishedKey = False
kickCounter = 0
room1key = False
fishingrod = False
room4key = False

open("inv.data", "w").close()
inventory = [line.strip() for line in open("inv.data", 'r')]

def HelpCommands():
    """
    Print available commands
    """
    print("""
    i, info                                         Description of the room
    h, help                                         Show this help message
    fw, forward                                     Go to next room if unlocked
    ba, back                                        Go back to previous room
    look                                            Look around the room
    c, clue                                         Gives you a clue
    o, objects                                      Shows all objects in room
    l [object], look [object]                       Get description of an object
    op [object], open [object]                      Open object (if possible)
    k [object], kick [object]                       Break object (if breakable)
    m [object], move [object]                       Move object (if moveable)
    inv, inventory                                  Get contents of inventory
    take [object]                                   Add object to inventory
    drop [object]                                   Drop object from inventory
    use [object]                                    Use object from inventory
    quit                                            Exit the game
    """)

def intro():
    """
    Game intro - description
    """
    print("""
    You are a hero warrior in the world of Tamriel. But you've just entered a
    big, scary dungeon in hopes to find many treasures after defeating the evil
    that resides there. Just beyond the entrance sits a man in thick, golden
    armor - he seems broken.

    As you approach the man he slowly stands to his feet.

    "This place is teeming with Undead. You should leave if you value your
    life."

    Naturally, instead of leaving, you offer to help the man cleanse the dungeon
    of evil. He agrees and tells you that deep in the dungeon is a crystal, the
    source of the necromantic power that keeps the undead standing. All you need
    to do is get there and get past the keeper.

    "The keeper is strong but if I hold him off you can get to the crystal. We
    just need to get to the final room. And I know a secret passage past all the
    undead. Though it is blocked by a series of puzzles."

    The man has spent some time studying the puzzles, and is confident he knows
    the solution to all of them. Together, you walk further into the dungeon.

    ---------------------------------------------------------------------------
    """)

    input("\nPress enter to continue...")

    StartingRoom()

def theEnd():
    """
    Game ending
    """
    print("""
    ---------------------------------------------------------------------------

    And so, you've successfully cleared the dungeon of the undead. Before you
    leave you find a big treasure chest with all kinds of legendary items. And
    you didn't even have to do much fighting at all. In fact, this was probably
    the easiest dungeon ever.

    The man, whose name you learn is Asgan, is very grateful for your help, and
    as you leave the dugeon, he gives you a little bit of gold and informs you
    of a similar dungeon in another region.

    So after you've said your farewells, you get on your horse and head towards
    the next dungeon. It probably won't be as easy as this one, but it'll have
    loot. and you love loot. The End.
    """)
    sys.exit(0)

# ROOMS

def RoomInfo():
    """
    Description of the room
    """
    global room
    room = room
    # FIRST ROOM ------------------------------------------------------------
    if room == "1":
        print(r"""

                                   |     |
                                   |     |
                                   |     |
                   |     |         |     |         |     |
                   |     |         |     |         |     |
                   |     |         -------         |     |
                   |     |         _______         |     |
                   |     |       /         \       |     |
                   -------       |         |       -------
                                 |         |
                                 |         |
                                 |         |
                                 |         |
                                 |         |
                                 |         |
                                 |         |
    ---------------------------------------------------------------------------




                  \  ___  /       \  ___  /       \  ___  /
                    /   \           /   \           /   \
                    \___/           \___/           \___/
                  /  | |  \      ___________      /  | |  \
                     | |        /           \        | |
                     | |        |           |        | |
                     | |        |           |        | |
                                |           |
                                |___________|



    You enter the first room. On the floor sits a chest and behind it are three
    shrines with some kind of glowing light coming out of them. From left to
    right they glow """ + shrines["Left Shrine"] + """, """ + shrines["Middle Shrine"] + """, """ \
    + shrines["Right Shrine"] + """.

    Behind the shrines is the door to the next room. Above it hangs three
    banners. From left to right, they are yellow, blue, yellow.
        """)
    # END FIRST ROOM --------------------------------------------------------
    # SECOND ROOM -----------------------------------------------------------
    elif room == "2":
        print(r"""

                                  _________
                                 /         \
                                 |         |
                                 |         |
                                 |         |
                                 |         |
                                 |         |
                                 |         |
                                 |         |
                                 |         |
    ---------------------------------------------------------------------------

     ____
    |    |
    |    |                   ___             ___
    |    |                  |___|           |___|
    |____|



    As you enter the second room you spot what looks like two pressure plates
    in front of the next door. On the left is a stone table with some objects.

    You might have to inspect the objects further to realise what's going on.
        """)
    # END SECOND ROOM -------------------------------------------------------
    # THIRD ROOM ------------------------------------------------------------
    elif room == "3":
        print(r"""


                                       __
                                      /~~\
                    __               /~~~~\               __
                   /~~\              \    /              /~~\
                  /~~~~\              \  /              /~~~~\
                  \    /               \/               \    /
                   \  /                                  \  /
                    \/                                    \/





    ---------------------------------------------------------------------------


    The third room you enter is quite smaller than the previous ones. All you
    see in front of you are three burning torches. There is nothing else.
        """)
    # END THIRD ROOM --------------------------------------------------------
    # FOURTH ROOM -----------------------------------------------------------
    elif room == "4":
        print(r"""

                                  _________
                                 /         \
                                 |         |
                                 |         |
                                 |         |
                                 |         |
                                 |         |
                                 |         |
                                 |         |
                                 |         |
    ---------------------------------------------------------------------------



                         _________________
                        |                 |
                        |                 |
                        |_________________|             _________
                                                       /         \
                                                       \_________/



    When you enter the fourth room you see a big wooden box and a hole in the
    ground.

    At the end is a door.
        """)
    # END FOURTH ROOM -------------------------------------------------------
    # FIFTH ROOM ------------------------------------------------------------
    elif room == "5":
        print(r"""


            |           |         _________         |           |
            |           |        /         \        |           |
            |           |        |         |        |           |
            |           |        |         |        |           |
            |           |        |         |        |           |
            |  _______  |        |         |        |  _______  |
            | |       | |        |         |        | |       | |
            | |       | |        |         |        | |       | |
            | |_______| |        |         |        | |_______| |
            |           |        |         |        |           |
    --------|           |---------------------------|           |--------------
            |           |                           |           |
            |           |                           |           |

                              ___             ___
                             |___|           |___|
                              ___             ___
                             |___|           |___|


    In the fifth room you see two large pillars and between them is the door
    at the end. In front of them, in the middle, are what looks like four
    buttons or pressure plates.

    On the left pillar is a symbol of a serpent. On the right is a symbol of a
    warrior.

    The buttons seems to have similar symbols.
        """)
    # END FIFTH ROOM --------------------------------------------------------
    # SIXTH ROOM ------------------------------------------------------------
    elif room == "6":
        print(r"""


                                 _,.-------.,_
                             ,;~'             '~;,
                           ,;                     ;,
                          ;                         ;
                         ,'                         ',
                        ,;                           ;,
                        ; ;      .           .      ; ;
                        | ;   ______       ______   ; |
                        |  `/~"     ~" . "~     "~\'  |
                        |  ~  ,-~~~^~, | ,~^~~~-,  ~  |
                         |   |        }:{        |   |
                         |   l       / | \       !   |
                         .~  (__,.--" .^. "--.,__)  ~.
                         |     ---;' / | \ `;---     |
                          \__.       \/^\/       .__/
                           V| \                 / |V
                            | |T~\___!___!___/~T| |
                            | |`IIII_I_I_I_IIII'| |
                            |  \,III I I I III,/  |
                             \   `~~~~~~~~~~'    /
                               \   .       .   /
                                 \.    ^    ./
                                   ^~~~^~~~^

    --------------------------------------------------------------------------



    The sixth room seems odd. In front of you is a wall with a skull on it.
    There is no door. There is nothing else.
        """)
    # END SIXTH ROOM --------------------------------------------------------
    # SEVENTH ROOM ----------------------------------------------------------
    elif room == "7":
        print(r"""

             ____________________________________________________
            |                                                    |
            |____________________________________________________|
            |  |        |  |                     |  |         |  |
            |  |        |  |                     |  |         |  |
            |  |        |  |                     |  |         |  |
            |  |        |  |                     |  |         |  |
            |  |        |  |         /\          |  |         |  |
            |  |        |  |         ||          |  |         |  |
            |__|________|__|_________||__________|__|_________|__|
            |               ---------------------                |
            |               ---------------------                |
            |               ---------------------                |
            ------------------------------------------------------


    You take a step through the broken wall. In front of you, you see the
    crystal in some kind of circular structure with pillars. But before you
    have time to react, something wakes up from a stone coffin.

    The Keeper. A big skeleton with glowing blue eyes and a staff.

    Quickly, you have to decide what to do. You draw your sword and prepare to
    fight the beast. But before you can swing it, the Keeper shatters it to
    pieces with its staff and throws you across the room.

    You land on some sort of grate in the floor. The man runs over to help you,
    and as you stand to your feet you see the Keeper coming right for you.
        """)
    # END SEVENTH ROOM ------------------------------------------------------

def StartingRoom():
    """
    First room
    """
    global room
    room = "1"
    return room

def RoomLook():
    """
    Look around first room
    """
    # FIRST ROOM ------------------------------------------------------------
    if room == "1":
        print("\nLooking at the door, you see that it requires some form of key to open.")
        print("\nFrom left to right the shrines glow " + shrines["Left Shrine"] + \
        ", " + shrines["Middle Shrine"] + ", " + shrines["Right Shrine"] + ".")
        print("\nThe door is " + unlocked["2"] + ".\n")
    # END FIRST ROOM --------------------------------------------------------
    # SECOND ROOM -----------------------------------------------------------
    if room == "2":
        print("\nUpon further inspection you see that the pressure plates have symbols on them." + \
        " One is a skull and the other is a sword.")
        print("\nThe skull plate is " + plates["Skull Plate"] + " and the sword plate is " + \
        plates["Sword Plate"] + ".")
        print("\nThe door is " + unlocked["3"] + ".\n")
    # END SECOND ROOM -------------------------------------------------------
    # THIRD ROOM ------------------------------------------------------------
    if room == "3":
        print("\nSince there is no actual door, that must mean you have to go through the wall." + \
        " All you have to do is open it.")
    # END THIRD ROOM --------------------------------------------------------
    # FOURTH ROOM -----------------------------------------------------------
    if room == "4":
        print("\nThe wooden box is " + ObjectState["Wooden Box"] + \
        ". You take a look down the well and you see a glowing object at the bottom.")
        print("\nThe door is " + unlocked["5"] + ".\n")
    # END FOURTH ROOM -------------------------------------------------------
    # FIFTH ROOM ------------------------------------------------------------
    if room == "5":
        print("\nOn the pillar on the left is a serpent. On the pillar on the right is a warrior.")
        print("\nOn the floor are four buttons. They show symbols of Serpent, Warrior, Theif and Mage.")
        print("\nThe serpent is " + buttons["Serpent"] + ". The warrior is " + buttons["Warrior"] + \
        ". The Theif is " + buttons["Theif"] + " . And the Mage is " + buttons["Mage"] + ".")
        print("\nThe door is " + unlocked["6"] + ".\n")
    # END FIFTH ROOM --------------------------------------------------------
    # SIXTH ROOM ------------------------------------------------------------
    if room == "6":
        print("\nThe wall appears to be made out of stone. But it doesn't seem properly solid.\n")
    # END SIXTH ROOM --------------------------------------------------------
    # SEVENTH ROOM ----------------------------------------------------------
    global roomSeven
    roomSeven = roomSeven
    if room == "7":
        if roomSeven["KeeperLocked"] == "True":
            print("\nYou locked him in! You can get to the crystal!\n")
        elif roomSeven["KeeperStaff"] == "True":
            print("\nYou took the staff from the Keeper. Now use it!\n")
        else:
            print("\nYou have no sword and the keeper is coming towards you. " + \
            " There is a locked grate below you. Find some way to open it!\n")
    # END SEVENTH ROOM ------------------------------------------------------

def RoomClue():
    """
    Room clues
    """
    global room
    global rooms
    room = room
    rooms = rooms
    clueFile = "room_clues.txt"
    clues = open(clueFile, "r")
    jsonobject = json.load(clues)
    theClue = random.randint(1, len(jsonobject[room]))
    for r in rooms:
        if r == room:
            for clue in jsonobject[room]:
                try:
                    print("\n" + clue['clue' + str(theClue)] + "\n")
                except KeyError:
                    continue

def RoomObjects():
    """
    Print objects in the room
    """
    # FIRST ROOM ------------------------------------------------------------
    global keyObtainable
    keyObtainable = keyObtainable
    print("\n")
    if room == "1":
        if keyObtainable == True:
            objs = ["Chest", "Left Shrine", "Middle Shrine", "Right Shrine", "Door", "Banners", "Key"]
        else:
            objs = ["Chest", "Left Shrine", "Middle Shrine", "Right Shrine", "Door", "Banners"]
    # END FIRST ROOM --------------------------------------------------------
    # SECOND ROOM -----------------------------------------------------------
    if room == "2":
        objs = ["Skull Plate", "Sword Plate", "Skull", "Sword", "Candle", "Helmet", "Door"]
    # END SECOND ROOM -------------------------------------------------------
    # THIRD ROOM ------------------------------------------------------------
    if room == "3":
        objs = ["Left Torch", "Middle Torch", "Right Torch"]
    # END THIRD ROOM --------------------------------------------------------
    # FOURTH ROOM -----------------------------------------------------------
    global ObjectState
    ObjectState = ObjectState
    if room == "4":
        if ObjectState["Wooden Box"] == "intact":
            objs = ["Hole", "Wooden Box", "Door"]
        else:
            objs = ["Hole", "Wooden Box", "Door", "Fishing Rod"]
    # END FOURTH ROOM -------------------------------------------------------
    # FIFTH ROOM ------------------------------------------------------------
    if room == "5":
        objs = ["Serpent Button", "Warrior Button", "Theif Button", "Mage Button", "Door"]
    # END FIFTH ROOM --------------------------------------------------------
    # SIXTH ROOM ------------------------------------------------------------
    if room == "6":
        objs = ["The Wall"]
    # END SIXTH ROOM --------------------------------------------------------
    # SEVENTH ROOM ----------------------------------------------------------
    global roomSeven
    roomSeven = roomSeven
    if room == "7":
        objs = ["Grate", "The Keeper", "Crystal", "Staff"]
    for obj in objs:
        print(obj)
    print("\n")
    # END SEVENTH ROOM ------------------------------------------------------

# MOVING

def GoForward():
    """
    Check if door unlocked then move forward if it is
    """
    global room
    global unlocked
    unlocked = unlocked
    nextRoom = str(int(room) + 1)
    if unlocked[nextRoom] == "unlocked":
        room = nextRoom
        if room != "8":
            RoomInfo()
        else:
            print("\nYou have destroyed the crystal.")
    else:
        if room == "8":
            print("\nYou have not destroyed the crystal!")
        else:
            print("\nYou have not unlocked the door!")
        return room

def GoBack():
    """
    Go to previous room
    """
    global room
    global rooms
    rooms = rooms
    for roomNum in rooms:
        if room == "1":
            print("\nYou go back out of the dungeon. Never to return. The end.")
            sys.exit(0)
        elif roomNum == room:
            room = str(int(room) - 1)
            print("\nYou go back to room " + room + ".")
            RoomInfo()
            break

#------------------------------------------------------------------------------

def CheckChestLock():
    """
    Check if puzzle is solved.
    """
    global shrines
    global chestLocked
    global keyObtainable
    shrines = shrines
    if shrines["Left Shrine"] == "yellow" and shrines["Middle Shrine"] == "blue" and \
    shrines["Right Shrine"] == "yellow":
        chestLocked = False
        keyObtainable = True
        print("\nThe magical protections seems to have disappeared.\n")

def UnlockDoor():
    """
    Check if puzzle is solved.
    """
    global buttons
    buttons = buttons
    if buttons["Serpent"] == "active" and buttons["Warrior"] == "active" and \
    buttons["Theif"] == "inactive" and buttons["Mage"] == "inactive":
        unlocked["6"] = "unlocked"
        print("\nThe door starts opening. You solved it!\n")
    else:
        unlocked["6"] = "locked"
        print("\nThe door is locked.\n")


def LookObject(theObject):
    """
    Inspect object
    """
    stringsFile = "object_strings.txt"
    strings = open(stringsFile, "r")
    jsonobject = json.load(strings)

    # FIRST ROOM ------------------------------------------------------------


    global shrines
    global unlocked
    shrines = shrines
    unlocked = unlocked
    if room == "1":
        if theObject == "chest":
            if chestLocked == True and ObjectState["Chest"] == "intact":
                print(jsonobject["look_1"][0]["Chest1"])
            elif chestLocked == False and ObjectState["Chest"] == "intact":
                print(jsonobject["look_1"][0]["Chest2"])
            elif ObjectState["Chest"] == "broken":
                print(jsonobject["look_1"][0]["Chest3"])
        elif theObject == "left shrine":
            print(jsonobject["look_1"][1]["LeftShrine"].format(color=shrines["Left Shrine"]))
        elif theObject == "middle shrine":
            print(jsonobject["look_1"][2]["MiddleShrine"].format(color=shrines["Middle Shrine"]))
        elif theObject == "right shrine":
            print(jsonobject["look_1"][3]["RightShrine"].format(color=shrines["Right Shrine"]))
        elif theObject == "door":
            print(jsonobject["look_1"][4]["Door"])
        elif theObject == "banners":
            print(jsonobject["look_1"][5]["Banners"])
        elif theObject == "key":
            if room1key == True:
                print(jsonobject["look_1"][6]["Key1"])
            else:
                print(jsonobject["look_1"][6]["Key2"])
        else:
            print("\nNo such object\n")


    # END FIRST ROOM --------------------------------------------------------


    # SECOND ROOM -----------------------------------------------------------


    global plates
    plates = plates
    if room == "2":
        if theObject == "skull plate":
            print(jsonobject["look_2"][1]["SkullPlate"].format(state=plates["Skull Plate"]))
        elif theObject == "sword plate":
            print(jsonobject["look_2"][2]["SwordPlate"].format(state=plates["Sword Plate"]))
        elif theObject == "skull":
            print(jsonobject["look_2"][3]["Skull"])
        elif theObject == "sword":
            print(jsonobject["look_2"][4]["Sword"])
        elif theObject == "candle":
            print(jsonobject["look_2"][5]["Candle"])
        elif theObject == "helmet":
            print(jsonobject["look_2"][6]["Helmet"])
        elif theObject == "door":
            print(jsonobject["look_2"][7]["Door"])
        else:
            print("\nNo such object\n")


    # END SECOND ROOM -------------------------------------------------------


    # THIRD ROOM ------------------------------------------------------------


    if room == "3":
        if theObject == "left torch" or theObject == "middle torch" or theObject == "right torch":
            print(jsonobject["look_3"][0]["Torches"])
        else:
            print("\nNo such object\n")


    # END THIRD ROOM --------------------------------------------------------


    # FOURTH ROOM -----------------------------------------------------------


    global FishedKey
    FishedKey = FishedKey
    if room == "4":
        if theObject == "hole":
            if FishedKey == False:
                print(jsonobject["look_4"][0]["Hole1"])
            else:
                print(jsonobject["look_4"][0]["Hole2"])
        elif theObject == "wooden box":
            if ObjectState["Wooden Box"] == "intact":
                print(jsonobject["look_4"][1]["WoodenBox1"])
            else:
                print(jsonobject["look_4"][1]["WoodenBox2"])
        elif theObject == "door":
            print(jsonobject["look_4"][2]["Door"].format(lock=unlocked["5"]))
        elif theObject == "fishing rod":
            if ObjectState["Wooden Box"] == "broken":
                print(jsonobject["look_4"][3]["FishingRod1"])
            else:
                print(jsonobject["look_4"][3]["FishingRod2"])
        else:
            print("\nNo such object\n")


    # END FOURTH ROOM --------------------------------------------------------


    # FIFTH ROOM -------------------------------------------------------------


    if room == "5":
        if theObject == "serpent button":
            print(jsonobject["look_5"][0]["Buttons"].format(state=buttons["Serpent"]))
        elif theObject == "warrior button":
            print(jsonobject["look_5"][0]["Buttons"].format(state=buttons["Warrior"]))
        elif theObject == "theif button":
            print(jsonobject["look_5"][0]["Buttons"].format(state=buttons["Theif"]))
        elif theObject == "mage button":
            print(jsonobject["look_5"][0]["Buttons"].format(state=buttons["Mage"]))
        elif theObject == "door":
            print(jsonobject["look_4"][2]["Door"].format(state=unlocked["6"]))
        else:
            print("\nNo such object\n")


    # END FIFTH ROOM ---------------------------------------------------------


    # SIXTH ROOM -------------------------------------------------------------


    if room == "6":
        if theObject == "the wall" or theObject == "wall":
            if unlocked["7"] == "unlocked":
                print(jsonobject["look_6"][0]["Wall1"])
            else:
                print(jsonobject["look_6"][0]["Wall2"])
        else:
            print("\nNo such object\n")


    # END SIXTH ROOM ---------------------------------------------------------


    # SEVENTH ROOM -----------------------------------------------------------


    global roomSeven
    roomSeven = roomSeven
    if room == "7":
        if theObject == "grate":
            if roomSeven["KeeperLocked"] == "True":
                print(jsonobject["look_7"][0]["Grate1"])
            elif roomSeven["GrateOpen"] == "True":
                print(jsonobject["look_7"][0]["Grate2"])
            else:
                print(jsonobject["look_7"][0]["Grate3"])
        elif theObject == "the keeper" or theObject == "keeper":
            if roomSeven["KeeperLocked"] == "True":
                print(jsonobject["look_7"][1]["Keeper1"])
            elif roomSeven["KeeperStaff"] == "True":
                print(jsonobject["look_7"][1]["Keeper2"])
            else:
                print(jsonobject["look_7"][1]["Keeper3"])
        elif theObject == "crystal":
            if roomSeven["KeeperLocked"] == "True":
                print(jsonobject["look_7"][2]["Crystal1"])
            elif roomSeven["KeeperStaff"] == "True":
                print(jsonobject["look_7"][2]["Crystal2"])
            else:
                print(jsonobject["look_7"][2]["Crystal3"])
        elif theObject == "staff":
            if roomSeven["KeeperStaff"] == "True":
                print(jsonobject["look_7"][3]["Staff1"])
            else:
                print(jsonobject["look_7"][3]["Staff2"])
        else:
            print("\nNo such object\n")


    # END SEVENTH ROOM -------------------------------------------------------


def OpenObject(theObject):
    """
    Attempt to open object
    """
    stringsFile = "object_strings.txt"
    strings = open(stringsFile, "r")
    jsonobject = json.load(strings)

    # FIRST ROOM ------------------------------------------------------------

    global shrines
    global chestLocked
    global keyObtainable
    shrines = shrines
    chestLocked = chestLocked
    keyObtainable = keyObtainable
    if room == "1":
        if theObject == "chest":
            if chestLocked == False:
                print(jsonobject["open_1"][0]["Chest1"])
            else:
                print(jsonobject["open_1"][0]["Chest2"])
        elif theObject == "left shrine":
            print(jsonobject["open_1"][1]["Shrines"])
        elif theObject == "middle shrine":
            print(jsonobject["open_1"][1]["Shrines"])
        elif theObject == "right shrine":
            print(jsonobject["open_1"][1]["Shrines"])
        elif theObject == "door":
            if keyObtainable == True and unlocked["2"] == "locked":
                unlocked["2"] = "unlocked"
                print(jsonobject["open_1"][2]["Door1"])
            elif unlocked["2"] == "unlocked":
                print(jsonobject["open_1"][2]["Door2"])
            else:
                print(jsonobject["open_1"][2]["Door3"])
        elif theObject == "banners":
            print(jsonobject["open_1"][3]["Banners"])
        elif theObject == "key":
            if room1key == True:
                print(jsonobject["open_1"][4]["Key"])
            else:
                print(jsonobject["look_1"][6]["Key2"])
        else:
            print("\nNo such object\n")


    # END FIRST ROOM --------------------------------------------------------


    # SECOND ROOM -----------------------------------------------------------


    global plates
    plates = plates
    if room == "2":
        if theObject == "skull plate":
            print(jsonobject["open_2"][0]["Plates"])
        elif theObject == "sword plate":
            print(jsonobject["open_2"][0]["Plates"])
        elif theObject == "skull":
            print(jsonobject["open_2"][1]["Skull"])
        elif theObject == "sword":
            print(jsonobject["open_2"][2]["Sword"])
        elif theObject == "candle":
            print(jsonobject["open_2"][3]["Candle"])
        elif theObject == "helmet":
            print(jsonobject["open_2"][4]["Helmet"])
        elif theObject == "door":
            if plates["Skull Plate"] == "active" and plates["Sword Plate"] == "active":
                print(jsonobject["open_1"][2]["Door2"])
            else:
                print(jsonobject["open_2"][5]["Door"])
        else:
            print("\nNo such object\n")


    # END SECOND ROOM -------------------------------------------------------


    # THIRD ROOM ------------------------------------------------------------


    if room == "3":
        if theObject == "left torch":
            print(jsonobject["open_3"][0]["Torches"])
        elif theObject == "middle torch":
            print(jsonobject["open_3"][0]["Torches"])
        elif theObject == "right torch":
            print(jsonobject["open_3"][0]["Torches"])
        else:
            print("\nNo such object\n")


    # END THIRD ROOM --------------------------------------------------------


    # FOURTH ROOM -----------------------------------------------------------


    global FishedKey
    FishedKey = FishedKey
    if room == "4":
        if theObject == "hole":
            print(jsonobject["open_4"][0]["Hole"])
        elif theObject == "wooden box":
            if ObjectState["Wooden Box"] == "intact":
                print(jsonobject["open_4"][1]["WoodenBox1"])
            else:
                print(jsonobject["open_4"][1]["WoodenBox2"])
        elif theObject == "door":
            if FishedKey == True and unlocked["5"] == "locked":
                print(jsonobject["open_4"][2]["Door1"])
            else:
                print(jsonobject["open_4"][2]["Door2"].format(lock=unlocked["5"]))
        elif theObject == "fishing rod":
            if ObjectState["Wooden Box"] == "broken":
                print(jsonobject["open_4"][3]["FishingRod"])
            else:
                print(jsonobject["look_4"][3]["FishingRod2"])
        else:
            print("\nNo such object\n")


    # END FOURTH ROOM --------------------------------------------------------


    # FIFTH ROOM -------------------------------------------------------------


    if room == "5":
        if theObject == "serpent button":
            print(jsonobject["open_5"][0]["Buttons"])
        elif theObject == "warrior button":
            print(jsonobject["open_5"][0]["Buttons"])
        elif theObject == "theif button":
            print(jsonobject["open_5"][0]["Buttons"])
        elif theObject == "mage button":
            print(jsonobject["open_5"][0]["Buttons"])
        elif theObject == "door":
            if unlocked["6"] == "locked":
                print(jsonobject["look_4"][2]["Door"].format(lock=unlocked["6"]))
            else:
                print(jsonobject["open_1"][2]["Door2"])
        else:
            print("\nNo such object\n")


    # END FIFTH ROOM ---------------------------------------------------------


    # SIXTH ROOM -------------------------------------------------------------


    if room == "6":
        if theObject == "the wall" or theObject == "wall":
            if unlocked["7"] == "unlocked":
                print(jsonobject["look_6"][0]["Wall1"])
            else:
                print(jsonobject["open_6"][0]["Wall"])
        else:
            print("\nNo such object\n")


    # END SIXTH ROOM ---------------------------------------------------------


    # SEVENTH ROOM -----------------------------------------------------------


    global roomSeven
    roomSeven = roomSeven
    if room == "7":
        if theObject == "grate":
            if roomSeven["KeeperLocked"] == "True":
                print(jsonobject["open_7"][0]["Grate1"])
            elif roomSeven["GrateOpen"] == "True":
                print(jsonobject["open_7"][0]["Grate2"])
            elif roomSeven["GrateLocked"] == "False":
                roomSeven["GrateOpen"] = "True"
                print(jsonobject["open_7"][0]["Grate3"])
            else:
                print(jsonobject["open_7"][0]["Grate4"])
        elif theObject == "the keeper" or theObject == "keeper":
            print(jsonobject["open_7"][1]["Keeper"])
        elif theObject == "crystal":
            if roomSeven["KeeperLocked"] == "True":
                print(jsonobject["open_7"][2]["Crystal1"])
            else:
                print(jsonobject["open_7"][2]["Crystal2"])
        elif theObject == "staff":
            if roomSeven["KeeperStaff"] == "True":
                print(jsonobject["open_7"][3]["Staff"])
            else:
                print(jsonobject["look_7"][3]["Staff2"])
        else:
            print("\nNo such object\n")


    # END SEVENTH ROOM -------------------------------------------------------

def MoveObject(theObject):
    """
    Move the objects
    """
    stringsFile = "object_strings.txt"
    strings = open(stringsFile, "r")
    jsonobject = json.load(strings)

    # FIRST ROOM ------------------------------------------------------------


    global shrines
    shrines = shrines
    if room == "1":
        if theObject == "chest":
            print(jsonobject["move_1"][0]["Chest"])
        elif theObject == "left shrine":
            if shrines["Left Shrine"] == "blue":
                shrines["Left Shrine"] = "yellow"
            elif shrines["Left Shrine"] == "yellow":
                shrines["Left Shrine"] = "red"
            elif shrines["Left Shrine"] == "red":
                shrines["Left Shrine"] = "blue"
            print(jsonobject["move_1"][1]["Shrines"].format(color=shrines["Left Shrine"]))
        elif theObject == "middle shrine":
            if shrines["Middle Shrine"] == "blue":
                shrines["Middle Shrine"] = "yellow"
            elif shrines["Middle Shrine"] == "yellow":
                shrines["Middle Shrine"] = "red"
            elif shrines["Middle Shrine"] == "red":
                shrines["Middle Shrine"] = "blue"
            print(jsonobject["move_1"][1]["Shrines"].format(color=shrines["Middle Shrine"]))
        elif theObject == "right shrine":
            if shrines["Right Shrine"] == "blue":
                shrines["Right Shrine"] = "yellow"
            elif shrines["Right Shrine"] == "yellow":
                shrines["Right Shrine"] = "red"
            elif shrines["Right Shrine"] == "red":
                shrines["Right Shrine"] = "blue"
            print(jsonobject["move_1"][1]["Shrines"].format(color=shrines["Right Shrine"]))
        elif theObject == "door":
            print(jsonobject["move_1"][2]["Door"])
        elif theObject == "banners":
            print(jsonobject["move_1"][3]["Banners"])
        elif theObject == "key":
            if room1key == True:
                print(jsonobject["move_1"][4]["Key"])
            else:
                print(jsonobject["look_1"][6]["Key2"])
        else:
            print("\nNo such object\n")



    # END FIRST ROOM --------------------------------------------------------


    # SECOND ROOM -----------------------------------------------------------


    global plates
    plates = plates
    if room == "2":
        if theObject == "skull plate":
            print(jsonobject["move_2"][0]["Plates"])
        elif theObject == "sword plate":
            print(jsonobject["move_2"][0]["Plates"])
        elif theObject == "skull":
            if plates["Skull Plate"] == "inactive":
                plates["Skull Plate"] = "active"
                if plates["Sword Plate"] == "active":
                    unlocked["3"] = "unlocked"
                    print(jsonobject["move_2"][1]["Skull1"])
                else:
                    print(jsonobject["move_2"][1]["Skull2"])
            else:
                plates["Skull Plate"] = "inactive"
                unlocked["3"] = "locked"
                print(jsonobject["move_2"][1]["Skull3"])
        elif theObject == "sword":
            if plates["Sword Plate"] == "inactive":
                plates["Sword Plate"] = "active"
                if plates["Sword Plate"] == "active":
                    unlocked["3"] = "unlocked"
                    print(jsonobject["move_2"][2]["Sword1"])
                else:
                    print(jsonobject["move_2"][2]["Sword2"])
            else:
                plates["Sword Plate"] = "inactive"
                unlocked["3"] = "locked"
                print(jsonobject["move_2"][2]["Sword3"])
        elif theObject == "candle":
            print(jsonobject["move_2"][3]["Candle"])
        elif theObject == "helmet":
            print(jsonobject["move_2"][4]["Helmet"])
        elif theObject == "door":
            print(jsonobject["move_2"][5]["Door"])
        else:
            print("\nNo such object\n")


    # END SECOND ROOM -------------------------------------------------------


    # THIRD ROOM ------------------------------------------------------------


    if room == "3":
        if theObject == "left torch":
            if torches["Left Torch"] == "placed":
                torches["Left Torch"] = "removed"
                print(jsonobject["move_3"][0]["Torches1"])
            else:
                torches["Left Torch"] = "placed"
                print(jsonobject["move_3"][0]["Torches2"])
        elif theObject == "middle torch":
            if torches["Middle Torch"] == "placed":
                torches["Middle Torch"] = "removed"
                print(jsonobject["move_3"][0]["Torches1"])
            else:
                torches["Middle Torch"] = "placed"
                print(jsonobject["move_3"][0]["Torches2"])
        elif theObject == "right torch":
            if torches["Right Torch"] == "placed":
                torches["Right Torch"] = "removed"
                unlocked["4"] = "unlocked"
                print(jsonobject["move_3"][1]["RightTorch1"])
            else:
                torches["Right Torch"] = "placed"
                unlocked["4"] = "locked"
                print(jsonobject["move_3"][1]["RightTorch2"])
        else:
            print("\nNo such object\n")


    # END THIRD ROOM --------------------------------------------------------


    # FOURTH ROOM -----------------------------------------------------------


    if room == "4":
        if theObject == "hole":
            print(jsonobject["move_4"][0]["Hole"])
        elif theObject == "Wooden Box" or theObject == "Wooden box" or theObject == "wooden box":
            if ObjectState["Wooden Box"] == "intact":
                print(jsonobject["move_4"][1]["WoodenBox1"])
            else:
                print(jsonobject["move_4"][1]["WoodenBox2"])
        elif theObject == "door":
            print(jsonobject["move_4"][2]["Door"])
        elif theObject == "fishing rod":
            if ObjectState["Wooden Box"] == "broken":
                print(jsonobject["move_4"][3]["FishingRod"])
            else:
                print(jsonobject["look_4"][3]["FishingRod2"])
        else:
            print("\nNo such object\n")


    # END FOURTH ROOM --------------------------------------------------------


    # FIFTH ROOM -------------------------------------------------------------


    if room == "5":
        if theObject == "serpent button":
            print(jsonobject["move_5"][0]["Buttons"])
        elif theObject == "warrior button":
            print(jsonobject["move_5"][0]["Buttons"])
        elif theObject == "theif button":
            print(jsonobject["move_5"][0]["Buttons"])
        elif theObject == "mage button":
            print(jsonobject["move_5"][0]["Buttons"])
        elif theObject == "door":
            print(jsonobject["move_4"][2]["Door"])
        else:
            print("\nNo such object\n")


    # END FIFTH ROOM ---------------------------------------------------------


    # SIXTH ROOM -------------------------------------------------------------


    if room == "6":
        if theObject == "the wall" or theObject == "wall":
            if unlocked["7"] == "unlocked":
                print(jsonobject["look_6"][0]["Wall1"])
            else:
                print(jsonobject["move_6"][0]["Wall"])
        else:
            print("\nNo such object\n")


    # END SIXTH ROOM ---------------------------------------------------------


    # SEVENTH ROOM -----------------------------------------------------------


    global roomSeven
    roomSeven = roomSeven
    if room == "7":
        if theObject == "grate":
            if roomSeven["GrateLocked"] == "True":
                print(jsonobject["move_7"][0]["Grate1"])
            elif roomSeven["GrateOpen"] == "True":
                print(jsonobject["move_7"][0]["Grate2"])
        elif theObject == "the keeper" or theObject == "keeper":
            print(jsonobject["move_7"][1]["Keeper"])
        elif theObject == "crystal":
            if roomSeven["KeeperLocked"] == "True":
                print(jsonobject["move_7"][2]["Crytal1"])
            else:
                print(jsonobject["move_7"][2]["Crytal1"])
        elif theObject == "staff":
            if roomSeven["KeeperStaff"] == "True":
                print(jsonobject["move_7"][3]["Staff"])
            else:
                print(jsonobject["look_7"][3]["Staff2"])
        else:
            print("\nNo such object\n")


    # END SEVENTH ROOM -------------------------------------------------------


def KickObject(theObject):
    """
    Kick the objects
    """
    stringsFile = "object_strings.txt"
    strings = open(stringsFile, "r")
    jsonobject = json.load(strings)

    # FIRST ROOM ------------------------------------------------------------

    global shrines
    global chestLocked
    shrines = shrines
    chestLocked = chestLocked
    if room == "1":
        if theObject == "chest":
            if chestLocked == False:
                ObjectState["Chest"] = "broken"
                print(jsonobject["kick_1"][0]["Chest1"])
            else:
                print(jsonobject["kick_1"][0]["Chest2"])
        elif theObject == "left shrine":
            print(jsonobject["kick_1"][1]["Shrines"])
        elif theObject == "middle shrine":
            print(jsonobject["kick_1"][1]["Shrines"])
        elif theObject == "right shrine":
            print(jsonobject["kick_1"][1]["Shrines"])
        elif theObject == "door":
            print(jsonobject["kick_1"][2]["Door"])
        elif theObject == "banners":
            print(jsonobject["kick_1"][3]["Banners"])
        elif theObject == "key":
            if room1key == True:
                print(jsonobject["kick_1"][4]["Key"])
            else:
                print(jsonobject["look_1"][6]["Key2"])
        else:
            print("\nNo such object\n")


    # END FIRST ROOM --------------------------------------------------------


    # SECOND ROOM -----------------------------------------------------------


    if room == "2":
        if theObject == "skull plate":
            print(jsonobject["kick_2"][0]["Plates"])
        elif theObject == "sword plate":
            print(jsonobject["kick_2"][0]["Plates"])
        elif theObject == "skull":
            print(jsonobject["kick_2"][1]["Skull"])
        elif theObject == "sword":
            print(jsonobject["kick_2"][2]["Sword"])
        elif theObject == "candle":
            print(jsonobject["kick_2"][3]["Candle"])
        elif theObject == "helmet":
            print(jsonobject["kick_2"][4]["Helmet"])
        elif theObject == "door":
            print(jsonobject["kick_2"][5]["Door"])
        else:
            print("\nNo such object\n")


    # END SECOND ROOM -------------------------------------------------------


    # THIRD ROOM ------------------------------------------------------------


    if room == "3":
        if theObject == "left torch":
            print(jsonobject["kick_3"][0]["Torches"])
        elif theObject == "middle torch":
            print(jsonobject["kick_3"][0]["Torches"])
        elif theObject == "right torch":
            print(jsonobject["kick_3"][0]["Torches"])
        else:
            print("\nNo such object\n")


    # END THIRD ROOM --------------------------------------------------------


    # FOURTH ROOM -----------------------------------------------------------


    if room == "4":
        if theObject == "hole":
            print(jsonobject["kick_4"][0]["Hole"])
        elif theObject == "wooden box":
            if ObjectState["Wooden Box"] == "intact":
                ObjectState["Wooden Box"] = "broken"
                print(jsonobject["kick_4"][1]["WoodenBox1"])
            else:
                print(jsonobject["kick_4"][1]["WoodenBox2"])
        elif theObject == "door":
            print(jsonobject["kick_4"][2]["Door"])
        elif theObject == "fishing rod":
            if ObjectState["Wooden Box"] == "broken":
                print(jsonobject["kick_4"][3]["FishingRod"])
            else:
                print(jsonobject["look_4"][3]["FishingRod2"])
        else:
            print("\nNo such object\n")


    # END FOURTH ROOM --------------------------------------------------------


    # FIFTH ROOM -------------------------------------------------------------


    global buttons
    buttons = buttons
    if room == "5":
        if theObject == "serpent button":
            if buttons["Serpent"] == "inactive":
                buttons["Serpent"] = "active"
                print(jsonobject["kick_5"][0]["Buttons1"])
            else:
                buttons["Serpent"] = "inactive"
                print(jsonobject["kick_5"][0]["Buttons2"])
        elif theObject == "warrior button":
            if buttons["Warrior"] == "inactive":
                buttons["Warrior"] = "active"
                print(jsonobject["kick_5"][0]["Buttons1"])
            else:
                buttons["Warrior"] = "inactive"
                print(jsonobject["kick_5"][0]["Buttons2"])
        elif theObject == "theif button":
            if buttons["Theif"] == "inactive":
                buttons["Theif"] = "active"
                print(jsonobject["kick_5"][0]["Buttons1"])
            else:
                buttons["Theif"] = "inactive"
                print(jsonobject["kick_5"][0]["Buttons2"])
        elif theObject == "mage button":
            if buttons["Mage"] == "inactive":
                buttons["Mage"] = "active"
                print(jsonobject["kick_5"][0]["Buttons1"])
            else:
                buttons["Mage"] = "inactive"
                print(jsonobject["kick_5"][0]["Buttons2"])
        elif theObject == "door":
            print(jsonobject["kick_4"][2]["Door"])
        else:
            print("\nNo such object\n")


    # END FIFTH ROOM ---------------------------------------------------------


    # SIXTH ROOM -------------------------------------------------------------


    global kickCounter
    if room == "6":
        if theObject == "the wall" or theObject == "wall":
            kickCounter = kickCounter + 1
            if unlocked["7"] == "unlocked":
                print(jsonobject["kick_6"][0]["Wall1"])
            elif kickCounter == 1:
                print(jsonobject["kick_6"][0]["Wall2"])
            elif kickCounter == 2:
                print(jsonobject["kick_6"][0]["Wall3"])
            elif kickCounter == 3:
                unlocked["7"] = "unlocked"
                print(jsonobject["kick_6"][0]["Wall4"])
            else:
                print("\nNo such object\n")


    # END SIXTH ROOM ---------------------------------------------------------


    # SEVENTH ROOM -----------------------------------------------------------


    global roomSeven
    roomSeven = roomSeven
    if room == "7":
        if theObject == "grate":
            if roomSeven["GrateLocked"] == "True":
                print(jsonobject["kick_7"][0]["Grate1"])
            else:
                print(jsonobject["kick_7"][0]["Grate2"])
        elif theObject == "the keeper" or theObject == "keeper":
            if roomSeven["KeeperStaff"] == "False":
                print(jsonobject["kick_7"][1]["Keeper1"])
                AddInv("staff")
            elif roomSeven["KeeperStaff"] == "True" and roomSeven["GrateOpen"] == "True":
                roomSeven["KeeperLocked"] = "True"
                roomSeven["GrateLocked"] = "True"
                roomSeven["GrateOpen"] = "False"
                print(jsonobject["kick_7"][1]["Keeper2"])
            elif roomSeven["KeeperLocked"] == "True":
                print(jsonobject["kick_7"][1]["Keeper3"])
            else:
                print(jsonobject["kick_7"][1]["Keeper4"])
        elif theObject == "crystal":
            if roomSeven["KeeperLocked"] == "True":
                print(jsonobject["kick_7"][2]["Crystal1"])
                input("\nPress enter to continue...")
                theEnd()
            else:
                print(jsonobject["kick_7"][2]["Crystal2"])
        elif theObject == "staff":
            if roomSeven["KeeperStaff"] == "True":
                print(jsonobject["kick_7"][3]["Staff"])
            else:
                print(jsonobject["look_7"][3]["Staff2"])
        else:
            print("\nNo such object\n")


    # END SEVENTH ROOM -------------------------------------------------------

#-----------------------------------------------------------------------------

def CheckInv():
    """
    Print contents of inventory
    """
    invFile = open("inv.data")
    firstLine = invFile.readline()
    if firstLine == "":
        print("\nMy inventory is empty\n")
    else:
        itemList = invFile.read()
        print("\nYour inventory:")
        print(firstLine.rstrip())
        print(itemList)

def AddInv(item):
    """
    Add items to inventory
    """
    global room1key
    if room == "1" and item == "key":
        if keyObtainable == True:
            if item not in inventory:
                invFile = open("inv.data", "w")
                inventory.append(item)
                for i in inventory:
                    invFile.write("%s\n" % i)
                print("\nGot " + item + "\n")
                room1key = True
            elif item in inventory:
                print("\nYou already have the key.\n")
        else:
            print("\nYou can't get the key.")
    global fishingrod
    if room == "4" and item == "fishing rod":
        if ObjectState["Wooden Box"] == "broken":
            if item not in inventory:
                invFile = open("inv.data", "w")
                inventory.append(item)
                for i in inventory:
                    invFile.write("%s\n" % i)
                print("\nGot " + item + "\n")
                fishingrod = True
            elif item in inventory:
                print("\nYou already have the fishing rod.\n")
    if room == "7" and item == "staff":
        if item not in inventory:
            roomSeven["KeeperStaff"] = "True"
            invFile = open("inv.data", "w")
            inventory.append(item)
            for i in inventory:
                invFile.write("%s\n" % i)
            print("\nGot " + item + "\n")
        elif item in inventory:
            print("\nYou already have the staff!\n")

def RemoveInv(item):
    """
    Remove items from inventory
    """
    if item in inventory:
        invFile = open("inv.data", "w")
        inventory.remove(item)
        print("\nDropping " + item + "\n")
        for i in inventory:
            invFile.write("%s\n" % i)
    else:
        print("\nYou don't even have that item.\n")

def useItem(item):
    """
    Use items
    """
    stringsFile = "object_strings.txt"
    strings = open(stringsFile, "r")
    jsonobject = json.load(strings)
    if room == "1":
        if item == "key" and item in inventory:
            if room1key == True:
                unlocked["2"] = "unlocked"
                print(jsonobject["open_1"][2]["Door1"])
            else:
                print("\nYou don't have the key.")
        else:
            print("\nYou don't even have that item.\n")
    if room == "4":
        if item == "fishing rod" and item in inventory:
            global FishedKey
            FishedKey = True
            print("\nClever, using the fishing rod. And it's a key!")
            print("\nGot dirty key\n")
            invFile = open("inv.data", "w")
            inventory.append("dirty key")
            for i in inventory:
                invFile.write("%s\n" % i)
        elif item == "dirty key" and item in inventory:
            unlocked["5"] = "unlocked"
            print("\nYet another room solved. Let's move forward!\n")
    if room == "7":
        if item == "staff" and item in inventory:
            roomSeven["GrateLocked"] = "False"
            print("\nGood! The staff broke the look on the grate! " + \
            " We can use that since the staff doesn't seem to affect him. \n")

def currentRoom():
    """
    Return current room
    """
    global room
    room = room
    return room

#------------------------------------------------------------------------------

if __name__ == "__main__":
    try:
        from main import clmain
        clmain()
    except IndexError:
        from main import main
        main()
