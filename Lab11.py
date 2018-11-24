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
 




















##############################################################
##############################################################
#############     Nathan Warren-Acord     ####################























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
    
    

    
class Room:
  
  def __init__(self, name, room_items, description):
    self.name = name
    self.room_items = room_items # just testing inventory. This will be empty under final version.
    self.description = description
     
  def add_item(self, item):
    self.room_items.append(item)
     
  def get_item(self, item):
    index = self.room_items.index(item)
    return self.room_items.pop(index)
     
  def look(self):
    return self.room_items
     
  def destroy(self, item):  
    self.room_items.remove(item)
   

    
  

def ryanPlay():
  
  print 'Welcome my friend. I need you to go to the north room and find me a letter and the key inside that room.'
  print 'Finding them is your only hope out of here'
  
     
def main():
  m = Map([[0,1,2],\
           [3,4,5],\
           [6,7,8]])
  print m.__getitem__(2,2)
  main_room = Room("Main Room", [],
                     "You wake up in a weird room. There are doors to the North, South, East, and West.")
  north_room = Room("North Room", [], "You are in the North Room")
  south_room = Room("South Room", [], "You are in the South Room")
  east_room = Room("East Room", [], "You are in the East Room")
  west_room = Room("West Room", [], "You are in the West Room")
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

