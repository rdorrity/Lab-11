# Room Class
# Creates room objects in the adventure game, which have positions, can hold items, and valid entrances/exits.
# Cody Young
# SCSI Logic 

class Room(object):
	# Class variables:
	# xpos: X coordinate of the room on the map.
	# ypos: Y coordinate of the room on the map.
	# items: Number of items in the room.
	# name: Name of room.
	
	# Initializes room's name, x/y coordinates, and number of items.
	# Note: A player object, theoretically, will always start in a room at (0,0).
	def __init__(self, name, xpos, ypos, items):
		self.xpos = xpos
		self.ypos = ypos
		self.name = name
		self.items = items 
	
	# Returns the x and y coordinates of the room's position.
	def getPosition(self):
		return self.xpos
		return self.ypos
	
	# Sets x and y coordinates of a room.
	def setPosition(self, name):
	
	# Sets a room with random coordinates within the bounds of the map.
	def randomPosition(self, name):
		# X-axis range variable (signed)
		# Y-axis range variable (signed)
		# Generate random numbers for x and y coordinates within bounds
	
	# Returns true if room has items, else false. 
	def hasItems(self):
		if self.items > 0:
			return True
		else:
			return False 
	