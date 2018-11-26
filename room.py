# Room Class
# Creates room objects in the adventure game, which have positions, can hold items, and valid entrances/exits.
# Cody Young
# SCSI Logic
  
import random 
	
class Room(object):
	# Class variables:
	# xpos: X coordinate of the room on the map.
	# ypos: Y coordinate of the room on the map.
	# room_items: List of items in room.
	# roomitem_count: Number of items in room.
	# name: Name of room.
	# directions: Dictionary of valid directions for player movement in or out of room.
	# description: Room flavor text.
	# hint: Hint text. 
	
	# Class "constructor"
	# Initializes room's name, x/y coordinates, and number of items.
	# Note: A player object, theoretically, will always start in a room at (0,0).
	def __init__(self, name, xpos, ypos, item_count, description):
		self.xpos = xpos
		self.ypos = ypos
		self.name = ""
		self.room_items = Inventory()
		self.item_count = len(room_items)
		self.directions = {'directions': 'north', 'south', 'east', 'west'}
		self.description = ""
		
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
	#def checkBounds(self):
	
	