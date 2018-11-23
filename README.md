# Lab-11
Text based game

Plan Your Adventure

The first thing you wil need to do is plan your adventure map.  You need  at least five rooms/locations and in most of the rooms there should be multiple directions you can move (at least two).  A game with only one room and one door would be pretty boring!  You and your teammates will definitely want to draw out your map to help with the rest of the program.

Once you have a map, you'll want to think a little bit about how to organize your program into functions. You want to have multiple functions to break your code into meaningful, manageable chunks.  

The code itself for this program is not hard, you will mostly use a combination of printNow, requestString, and if statements (remember to check if two things are equal you need to use two equal signs e.g. if direction == "north" <- you will need the quotes for strings)

However, the hard part of this lab is designing the program and how the functions will work together.
Write your adventure!

Once you have done some initial planning, you are ready to get started!  In addition to having at least five rooms, your game should have the following minimum specifications

    You should display a welcome message when the game starts. 
    If the user types help at any time, you should redisplay the welcome message
    If the user types exit at any time they should be able to quit the game
    In each room, you should:
        Print a description of the room
        Give the user the directions that they are allowed to move
        Ask the user (via requestString) which direction they would like to go
        Process the answer and respond accordingly
    In this simple version of the game, you just keep prompting the user to enter a direction and moving them around until they choose to exit.

Here is a simple sample run:

*** Welcome to 205 Adventure Land! ***
In each room you will be told which directions you can go
You'll be able to go north, south, east or west by typing that direction
Type help to redisplay this introduction
Type exit to quit at any time

---------- PORCH ---------
You are on the porch of a haunted house
It is a dark and stormy night
You can go north into the house ... if you dare

[Dialog box pops up and user chooses to move north]

---------- FOYER ---------
You are in the foyer of the house. Discarded computer parts are everywhere
You feel a sense of dread
There is a passageway to the north and a door to the east
The porch is behind you to the south

[Dialog box pops up and user chooses to exit the game]

Goodbye .... chicken
