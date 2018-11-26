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
# Map class is a matrix (list of lists) that holds Room objects.
# Map looks like:
#                     --------------------
#                    |                    |
#                    |                    |
#                    |                    |                           0
#                    |     NORTH ROOM     |
#                    |                    |
#                    |                    |
#                    |                    |
# ----------------------------DOOR --------------------------
# |                  |                    |                  |
# |                  |                    |                  |
# |                  |                    |                  |
# |                  D                    D                  |
# |   WEST ROOM      O      START         O   EAST ROOM      |       1
# |                  O                    O                  |
# |                  R                    R                  |
# |                  |                    |                  |
#  ---------------------------DOOR --------------------------
#                    |                    |
#                    |                    |
#                    |                    |
#                    |                    |
#                    |    SOUTH ROOM      |
#                    |                    |                          2
#                    |                    |
#                    |                    |
#                    |                    |
#                     --------------------
#         0                     1                  2

import re

class Map:

  def __init__(self, room_list):
    self.room_list = room_list


  def add(self, room, x, y):
    self.room_list[x].insert(y, room)

  def __getitem__(self, x, y):
    return self.room_list[x][y]


##############################################################
##############################################################
#############         Cody Young          ####################
 
class Room:
# Class variables:
# xpos: X coordinate of the room on the map.
# ypos: Y coordinate of the room on the map.
# room_items: List of items in room. Inventory class object. 
# roomitem_count: Number of items in room.
# name: Name of room.
# directions: Dictionary of valid directions for player movement in or out of room.
# description: Room flavor text.
# hint: Hint text. 

# Class "constructor"
# Initializes room's name, x/y coordinates, and number of items.
# Note: A player object, theoretically, will always start in a room at (0,0).
#def __init__(self, name, xpos, ypos, item_count, description)
  def __init__(self, name, xpos, ypos, description):
    self.xpos = xpos
    self.ypos = ypos
    self.name = ""
    self.room_items = Inventory()
    #self.item_count = len(room_items)
    #self.directions = {'directions': 'north', 'south', 'east', 'west'}
    self.description = ""
    self.directions = ['north', 'south', 'east', 'west']
  
    # Returns the x and y coordinates of the room's position.
    def getPosition(self):
      return self.xpos
      return self.ypos

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
      if self.room_items > 0:
        return True
      else:
        return False 
	
# Checks room's valid directions for player movement.
# Adds or removes room's valid directions (dictionary)
# depending if player has reached x or y bound of map (a.k.a. can't move further in one direction)
	
		# X coordinate
		x_rand = random.randint(x_min, x_max + 1)
		# Y coordinate
		y_rand = random.randint(y_min, y_max + 1)
		
		self.xpos = x_rand
		self.ypos = y_rand 
	
	# Returns true if room has items, else false. 
	def hasItems(self):
		if self.room_items > 0:
			return True
		else:
			return False 
	
	# Checks room's valid directions for player movement.
	# Adds or removes room's valid directions (dictionary)
	# depending if player has reached x or y bound of map (a.k.a. can't move further in one direction)
	#def checkBounds(self):
	

	
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
  
  
     
def main():
  m = Map([[0,1,2],\
           [3,4,5],\
           [6,7,8]])
  print m.__getitem__(2,2)
  main_room = Room("Main Room", 1, 1,
                     "You wake up in a weird room. There are doors to the North, South, East, and West.")
  north_room = Room("North Room", 0, 1, "You are in the North Room")
  south_room = Room("South Room", 2, 1, "You are in the South Room")
  east_room = Room("East Room", 2, 2, "You are in the East Room")
  west_room = Room("West Room", 1, 0, "You are in the West Room")
  m.add(north_room, 0, 1)
  m.add(west_room, 1, 0)
  m.add(main_room, 1, 1)
  m.add(south_room, 2, 1)
  m.add(east_room, 2, 2)

  # Testing printing out name and description of a Room, given that the location on the map
  # IS a room. Otherwise, print YOU CANNOT GO THAT WAY.
  for x in range(0,3):
    for y in range(0,3):
      if isinstance(m.__getitem__(x,y), Room):
        print m.__getitem__(x, y).name
        print m.__getitem__(x, y).description
      else:
        print "YOU CANNOT GO THAT WAY"
                              
                                  
                                      
main()
ryanPlay()

