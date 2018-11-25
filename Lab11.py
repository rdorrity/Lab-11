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
  
  def __init__(self):
    self.room_items = ['candle', 'key', 'book', 'letter'] # just testing inventory. This will be empty under final version.
     
  def add_item(self, item):
    self.room_items.append(item)
     
  def get_item(self, item):
    index = self.room_items.index(item)
    return self.room_items.pop(index)
     
  def look(self):
    return self.room_items
     
  def destroy(self, item):  
    self.room_items.remove(item)
   
     
   
class Map:
  
  main_room = Room()
  north_room = Room()
  south_room = Room()
  east_room = Room()
  west_room = Room()
  
  def __init__(self):
    self.map = [north_room]
    
  

def ryanPlay():
  
  print 'Welcome my friend. I need you to go to the north room and find me a letter and the key inside that room.'
  print 'Finding them is your only hope out of here'
  
  
     
              
                  
                      
                          
                              
                                  
                                      
                                          
                                                  
    
