# Team SCSI Logic
# Sara Kazemi, Cody Young, Nathan Warren-Acord, Ryan Dorrity
# Lab 11
# 11/22/2018
# ###########################################################

# Welcome everyone! This is just a template I started for the lab.
# Please feel free to change anything. I thought this might help 
# keep us organized, but please share any ideas you have for 
# this lab.



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