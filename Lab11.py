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
import random

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








##############################################################
##############################################################
#############         Cody Young          ####################
 
class Room:
# Class variables:
# xpos: X coordinate of the room on the map.
# ypos: Y coordinate of the room on the map.
# map_position: Overall position on map. Stores x and y coordinates as tuples for convenience.
# room_items: List of items in room. Inventory class object.
# name: Name of room.
# directions: Dictionary of valid directions for player movement in or out of room.
# visited: Tracks whether a player has visited a room previously. False by default.
# description: Room flavor text.
# hint: Hint text. 

# Class "constructor"
# Initializes room's name, x/y coordinates, and number of items.
# Note: A player object, theoretically, will always start in a room at (0,0).
  def __init__(self, name, xpos, ypos,description):
    self.xpos = xpos
    self.ypos = ypos
    self.map_position = tuple([self.xpos,self.ypos])
    self.name = name
    self.room_items = Inventory()
    self.visited = False
    self.description = description
    self.directions = ['north', 'south', 'east', 'west']
  
  # Returns the x and y coordinates of the room's position.
  def getPosition(self):
    print("%d,%d" % (self.map_position))
    return self.map_position

  # Sets a room's loation using a random coordinate within the bounds of the map.
  def randomPosition(self, name):
  # Min/max ranges for x and y axes. Can be changed as necessary (use map class function?)
    x_min = -10
    x_max = 10
    y_min = -10
    y_max = 10
	
  # X coordinate
    x_rand = random.randint(x_min, x_max + 1)
  # Y coordinate
    y_rand = random.randint(y_min, y_max + 1)

    self.xpos = x_rand
    self.ypos = y_rand

    # Returns true if room has items, else false. 
  def hasItems(self):
    if len(self.room_items.get_inventory()) > 0:
      return True
    else:
      return False

  # Checks room's valid directions for player movement.
  # Adds or removes room's valid directions (dictionary)
  # depending if player has reached x or y bound of map (a.k.a. can't move further in one direction)

##############################################################
##############################################################
#############     Nathan Warren-Acord     ####################

cmdExit = re.compile(("^(Quit|Exit){1}$"),re.I)
cmdInv = re.compile("^(Inventory){1}$",re.I)
cmdLook = re.compile(("^(Scan|Look){1}$"),re.I)
cmdHelp = re.compile(("^(Help){1}$"),re.I)
cmdExamine = re.compile(("^(?<=Examine\s)(\w+)$"),re.I)
cmdTake = re.compile(("^(?<=Take\s)(\w+)$"),re.I)
cmdDrop = re.compile(("^(?<=Drop\s)(\w+)$"),re.I)
cmdMove = re.compile(("north|n|south|s|west|w|east|e|up|down{1}"),re.I)

def user_input(cmmd):
  if cmdExit.search(cmmd):
    pass
    #Call exit function
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
  elif cmdMove.search(cmmd):
	move = cmdMove.search(cmmd).group(0)
	#If move in room connections:
		#Put player in the new room
	#Else:
		#print ("You can't go that way!")
  else:
    print "I don't know that command."

##############################################################
##############################################################
###############     Ryan Dorrity    ##########################

    
class Inventory:
  
  def __init__(self):
    self.bag = []
    
  def add_item(self, item):
    self.bag.append(item)
    
  def get_item(self, item):
    index = self.bag.index('key')
    return self.bag.pop(index)
    
  def get_inventory(self):
    return self.bag
    
  def destroy(self, item):
    self.bag.remove(item)
    
    

    
#class Room:
  
#  def __init__(self, name, room_items, description):
#    self.name = name
#    self.room_items = room_items # just testing inventory. This will be empty under final version.
#    self.description = description
#     
#  def add_item(self, item):
#    self.room_items.append(item)
#     
#  def get_item(self, item):
#    index = self.room_items.index(item)
#    return self.room_items.pop(index)
#     
#  def look(self):
#    return self.room_items
#     
#  def destroy(self, item):  
#    self.room_items.remove(item)
#   

def ryanPlay():
  
  print 'Welcome my friend. I need you to go to the north room and find me a letter and the key inside that room.'
  print 'Finding them is your only hope out of here'
  
def printWelcome():
  print "Your body aches. There is flowing water, somewhere, but you cannot tell where.\n\
Rolling over, blades of grass tickle your skin and the smell of ash brings\n\
burning tears. As you wipe your eyes, the surrounding structure comes into focus.\n\
You look around and discover you are in the ... "

def printDirections():
  print "\nWelcome to some sort of text adventure game blah blah"
  print "\nPrint directions here\n"
  raw_input("Press Enter to continue...\n")
     
def main():

  printDirections()
  printWelcome()
  #Location.print_description(main_room)

  # These following statements are for testing creating Room class objects, and returning their coordinates. - Cody

  room_0 = Room("Entrance",0,0,"You are at the entrance.")
  room_1 = Room("East Room",1,0,"You are in the east room.")
  room_2 = Room("West Room",-1,0,"You are in the west room.")
  room_3 = Room("Entrance",0,1,"You are in the north room..")
  room_4 = Room("Entrance",0,-1,"You are in the south room.")

  room_0.getPosition()
  room_1.getPosition()
  room_2.getPosition()
  room_3.getPosition()
  room_4.getPosition()



#testing
main()
#Location.remove_item(main_room, "piece of metal")
#Location.print_description(main_room)
