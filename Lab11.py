# Team SCSI Logic
# Sara Kazemi, Cody Young, Nathan Warren-Acord, Ryan Dorrity
# Lab 11
# 11/22/2018
# ###########################################################

# Welcome everyone! This is just a template I started for the lab.
# Please feel free to change anything. I thought this might help 
# keep us organized, but please share any ideas you have for 
# this lab.

# Please note that any code you see in my section is mostly just
# for my own practice and not meant as a basis for how we should 
# code this project together.



##############################################################
##############################################################
#############          Sara Kazemi        ####################
# Game map:
#
#                     --------------------
#                    |                    |
#                    |                    |
#                    |                    |
#                    |     NORTH ROOM     |
#                    |                    |
#                    |                    |
#                    |                    |
# ----------------------------DOOR --------------------------
# |                  |                    |                  |
# |                  |                    |                  |
# |                  |                    |                  |
# |                  D                    D                  |
# |   WEST ROOM      O      START         O   EAST ROOM      |
# |                  O                    O                  |
# |                  R                    R                  |
# |                  |                    |                  |
#  ---------------------------DOOR --------------------------
#                    |                    |
#                    |                    |
#                    |                    |
#                    |                    |
#                    |    SOUTH ROOM      |
#                    |                    |
#                    |                    |
#                    |                    |
#                    |                    |
#                     --------------------
#

import re

class Location:

  def __init__(self, name, description, interactions, connections):
    self.name = name
    self.description = description
    self.interactions = interactions
    self.connections = connections
    self.visited = False

  def print_description(self):
    print("\n\t~~"+self.name+"~~\n")
    if not self.visited:
      print(self.description)

  def remove_item(self, item):
    if item in itemTable:
      self.description = self.description.replace(itemTable[item][2], "")

  def __getitem__(self):
    return self.name


# Room Definitions
main_room = Location("","",[], {})
north_room = Location("","",[], {})
south_room = Location("","",[], {})
east_room = Location("","",[], {})
west_room = Location("","",[], {})

# Items in the world
itemTable = {
  "piece of metal": ["\nRadiates with a strange glow. Smooth to the touch.", main_room, "\nA shiny piece of\
 metal catches your eye on the west wall."]
}

# Room Initializations

# Main Room
main_room.name ="Main Room"
main_room.interactions = []
main_room.description = " Lit with a flickering torchlight, the room darkens at the corners. \
The walls are\nCyclopean stone and painted with moss. \
Motes of flora drift lightly and your feet\nsettle on soft grass. \
Four doors face you in each cardinal direction." + itemTable["piece of metal"][2]
main_room.connections = {"north": north_room, "south": south_room,\
                         "east": east_room, "west": west_room }

# North Room
north_room.name = "North Room"
north_room.description = "This is the North Room"
north_room.interactions = []
north_room.connectors = {"south": main_room}

# South Room
south_room.name = "South Room"
south_room.description = "This is the South Room"
south_room.interactions = []
south_room.connectors = {"north": main_room}

# East Room
east_room.name = "East Room"
east_room.description = "This is the East Room"
east_room.interactions = []
east_room.connectors = {"west": main_room}

# West Room
west_room.name = "West Room"
west_room.description = "This is the West Room"
west_room.interactions = []
west_room.connectors = {"east": main_room}


cmdMove = re.compile(("(north|n|south|s|west|w|east|e|up|down)"),re.I)
cmdExit = re.compile(("^(Quit|Exit){1}$"),re.I)
cmdInv = re.compile("^(Inventory){1}$",re.I)
cmdLook = re.compile(("^(Scan|Look){1}$"),re.I)
cmdHelp = re.compile(("^(Help){1}$"),re.I)
cmdExamine = re.compile(("^(?<=Examine\s)(\w+)$"),re.I)
cmdTake = re.compile(("^(?<=Take\s)(\w+)$"),re.I)
cmdDrop = re.compile(("^(?<=Drop\s)(\w+)$"),re.I)

def user_input(cmmd):
  if cmdExit.search(cmmd):
    pass
    #Call exit function
  elif cmdMove.search(cmmd):
   pass
   #player_move(cmdMove.search(cmmd).group(0))
  elif cmdHelp.search(cmmd):
    pass
    #Print out commands
  elif cmdInv.search(cmmd): 
    pass
    #Print out contents of the inventory
  elif cmdLook.search(cmmd):
    pass
    #Print out description for current room
  elif cmdExamine.search(cmmd):
    examine = cmdExamine.search(cmmd).group(0)
    #if examine in (player inv) or examine in (room inv):
      #Print out that object description
    #else:
      #Print that player can't do that
  elif cmdTake.search(cmmd):
    take = cmdTake.search(cmmd).group(0)
    #If take in room inv and is obtainable:
      #Add to player's inv and remove from room's inv
    #else:
      #Tell player that it failed
  elif cmdDrop.search(cmmd):
    dropped = cmdDrop.search(cmmd).group(0)
    #If in player's inv:
      #Remove from player's inv and add to room inv
    #Else:
      #Tell player it failed
  else:
    print "I don't know that command."

    
class Player():
  def __init__(self):
    self.location = main_room

  def take_item(self, item):
    self.location.remove_item(item)
    if item in itemTable:
      itemTable[item][1] = self

  def move(self, direction):
    possibilities = ["north", "south", "east", "west", "up", "down"]
    for possibility in possibilities:
      if direction == possibility[0] or direction == possibility:
        if possibility in self.location.connections:
          self.location.visited = True
          self.location = self.location.connections[possibility]
        print "There's nowhere to go to the " + direction


  
def print_welcome():
  print "Your body aches. There is flowing water, somewhere, but you cannot tell where.\n\
Rolling over, blades of grass tickle your skin and the smell of ash brings\n\
burning tears. As you wipe your eyes, the surrounding structure comes into focus.\n\
You look around and discover you are in the ... "

def print_directions():
  print "\nWelcome to some sort of text adventure game blah blah"
  print "\nPrint directions here\n"
  raw_input("Press Enter to continue...\n")
     
def main():

  print_directions()
  print_welcome()
  Location.print_description(main_room)


#testing
main()
p = Player()
Player.take_item(p, "piece of metal")
Location.print_description(main_room)
p.move("north")
print p.location.name



                                  
                                      



