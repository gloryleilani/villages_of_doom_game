

row_1 = [1,2,3,4]
row_2 = [5,6,7,8]
row_3 = [9,10,11,12]
row_4 = [13,14,15,16]
village_map = [row_1,row_2,row_3,row_4]
#bag = {}
life_counter = 25

print("")
def show_bag_contents(bag): #function 1
  """This function shows the contents of your bag."""

  #global bag
  print("")
  if "rock" in bag:
    bag["rock"] +=1 
    print("Your bag contains: " + str(bag["rock"]) + " rocks")
  else: 
    bag["rock"] =1
    print("Your bag contains: " + str(bag["rock"]) + " rock")  

  return bag


def show_map_of_villages(current_village_number): 
  """This function displays the map of villages and where you are on the map."""

  print("")
  print("Here's the map of the villages: ")
  print("")
  print(" {}  |  {}  |  {}  |  {} ".format(row_1[0], row_1[1], row_1[2], row_1[3]))
  print("--- + --- + --- + ----")
  print(" {}  |  {}  |  {}  |  {} ".format(row_2[0], row_2[1], row_2[2], row_2[3]))
  print("--- + --- + --- + ----")
  print(" {}  |  {} |  {} |  {} ".format(row_3[0], row_3[1], row_3[2], row_3[3]))
  print("--- + --- + --- + ----")
  print(" {} |  {} |  {} |  {} ".format(row_4[0], row_4[1], row_4[2], row_4[3]))

  if current_village_number in row_1 or row_2 or row_3 or row_4:
    print("")
    #print("You are currently in village {}.".format(current_village_number))


def choose_direction(): 
  """This function asks the user which way he/she would like to move on the map."""

  while True:
    print("")
    print("Which direction would you like to move? Enter north, south, east, or west.")
    user_direction_chosen = input("> ") 
    user_direction_chosen = user_direction_chosen.lower()
    
    if not (user_direction_chosen == "north" or user_direction_chosen == "south" or user_direction_chosen == "east" or user_direction_chosen == "west"): 
      print ("I'm sorry, I didn't understand that.") 

    else: 
      print("")
      print("Ok, {} it is!".format(user_direction_chosen))
      return user_direction_chosen


def move_villages (user_direction_chosen, current_village_number):
  """This function allows the user to move to the next village."""

  
  if user_direction_chosen == "north" and current_village_number-4 > 0:
      current_village_number = current_village_number - 4 

  elif user_direction_chosen == "south" and current_village_number+4 < 17:
      current_village_number = current_village_number+ 4
    
  elif user_direction_chosen == "east" and current_village_number != 4 and current_village_number != 8 and current_village_number != 12 and current_village_number != 16:
      current_village_number = current_village_number+1

  elif user_direction_chosen == "west" and current_village_number != 1 and current_village_number != 5 and current_village_number != 9 and current_village_number != 13:
      current_village_number = current_village_number-1
  
  else:
    print("")
    print("...You look around over there, but you don't see anything interesting. You're back in village {}.".format(current_village_number))
    return current_village_number  


  print("")
  #print("First current village number:", current_village_number)
      
  transit = ["You crawl through thorny bushes and got very scratched up", 
            "You bat away a swarm of bugs which start to bite you", 
            "You accidentally set off some wild hog traps and they nearly scared you to death", 
            "You get chased by an angry mama orangutan", 
            "You climb over large rocks and slip and fall on some moss"]
      
  import random
  random_transit = random.choice(transit)

  print("{}, but you make it to village {}.".format(random_transit, current_village_number))

  global life_counter
  life_counter = life_counter -1
  print("")
  print("Your remaining life units: ", life_counter)
  print("")
  #print("Second current village number:",current_village_number)
  #print("")
  return current_village_number


def explore_or_choose_direction(current_village_number): 
  """This function asks the user whether he/she would like to explore the current village or move to a different village.""" 
  
  while True:
    print("")
    print("Would you like to explore village {} or move to a different village? Enter explore or move.".format(current_village_number)) 
    
    user_explore_or_move_chosen = input("> ")
    user_explore_or_move_chosen = user_explore_or_move_chosen.lower()

    if user_explore_or_move_chosen == "explore" or user_explore_or_move_chosen == "move":
      return user_explore_or_move_chosen

    else: 
      print("")
      print("I'm sorry, I didn't understand that.")
  

def show_items_in_current_village(current_village_number, all_village_items):
  """This function returns the item in the dictionary containing the lists of items in the current village."""

  print("")
  print("As you look around village {}, you see:".format(current_village_number))
  print("")  

  for item in (all_village_items[current_village_number]):
    print (item)
        
  return all_village_items[current_village_number]  


def choose_item_to_pick_up(current_village_number, current_village_items):
  """This function lets the user select an item to pick up."""

  while True:
    print("")
    print("Which item would you like to pick up? (Or enter skip).")
  
    item_selected = input("> ")
    item_selected = item_selected.lower()
  
    if not item_selected in current_village_items:
    
      if item_selected == "skip":
        return "none"

      else:
        print("")
        print("I'm sorry, I didn't understand that.")
     
    else: 
      return item_selected


def hear_parrot_response(): 
  """This function determines which random phrase the parrot says.""" 
  
  import random
  possible_parrot_phrases = [
    "You need to collect the rocks", 
    "All of the gnomes are scared of humans", 
    "If you're hungry, eat the food you find",
    "You can't keep anything except for the rocks!"
    ]

  final_parrot_response = random.choice(possible_parrot_phrases)
  
  return final_parrot_response 


def show_items_after_picked_up_item(current_village_number, village_items, item_selected, bag, parrot_response): 
  """This function shows what happens when an item is picked up."""

  global life_counter
  print("")
  if item_selected == "apple":
    print("You eat the delicious apple and it added 2 units to your life!")
    life_counter = life_counter + 2
    print("")
    print("Your remaining life units:", life_counter)
    village_items.remove("apple")
    #print("remaining", village_items)

  if item_selected == "rock":
    print("It's a beautiful, sparkly rock. It seems to have magnetic properties. You put it into your bag in case it's valuable.")
    #print ("BAG:", bag)
    village_items.remove("rock")

  if item_selected == "gnome":
    print("You picked up the gnome, but she got scared and bit you and ran off. The bite cost you 5 units of your life.")
    life_counter = life_counter - 5
    print("")
    print("Your remaining life units:", life_counter)
    village_items.remove("gnome")
    #print("remaining", village_items)


  if item_selected == "parrot":
    print("You picked up the parrot and it said, \"{}\" and then the parrot flew away.".format(parrot_response))
    village_items.remove("parrot")
    #print("remaining", village_items)

  if item_selected == "binoculars":
    print("You can view the items in another village with the binoculars.") 
    

  if village_items == {}:
    print("There are no remaining items in this village.")
    
  return village_items

has_won_result = False

def collect_village_number_for_binoculars():
  """This function lets the user pick the village to peek into."""

  while True:
    print("")
    village_for_binoculars = input("Which village would you like to peek into? Enter the village number. >")
    #print(type(village_for_binoculars))
    
    village_for_binoculars = int(village_for_binoculars)
    
    if (village_for_binoculars>0) and (village_for_binoculars <17):
        return village_for_binoculars
    elif (village_for_binoculars<0) or (village_for_binoculars >16):
      print("")
      print("Please enter a village number between 1 and 16.")  
    else:
      print("")
      print("I'm sorry, I didn't understand that.")


def peek_into_village_with_binoculars(village_for_binoculars, all_village_items):
  """This function let's the user see the items in another village via binoculars"""

  print("")
  print("That village contains:")
  print("")
  for item in (all_village_items[village_for_binoculars]):
    print (item)


def has_won(bag, result):
  """This function tells whether the user has won or not. It takes 5 rocks in the bag to win."""
  #print("Bag",bag)
  
  if bag != {}: 
    if bag["rock"] == 5: 
      print("")
      print("Your bag starts rumbling and the rocks rise into the air and form a circle which gets larger and turns into a portal! You step through and find yourself in your own backyard again!")
      print("")
      print("CONGRATULATIONS! YOU WON!")
      print("")
      result = True
      return result


def play_game(): #function 13
  """This is the main function to decide whether to play the game"""

  bag = {}
  current_village_number = 6

  while True:
    print("Would you like to play Villages of doom? Enter yes or no.")
  
    user_play_or_not_chosen = input("> ")
    user_play_or_not_chosen = user_play_or_not_chosen.lower()

    if user_play_or_not_chosen == "yes":
      global life_counter
      print("")
      print("Great; the game is starting!")
      
      #print("")
      #import time
      # counter = 3
      # while counter>0:
      #   print(counter)
      #   time.sleep(1)
      #   counter = counter-1

      print("")
      print("You accidentally stepped through a portal while playing with rocks in your backyard--you've found yourself in a forested area containing villages. You are searching for the portal to get home.")  
      print("")
      print("You have {} units of life and you are in village 6. Your goal is to find the portal before your life expires.".format(life_counter))
      
      all_village_items = {
        1:["rock", "gnome", "parrot"], 
        2:["rock", "apple", "binoculars"],
        3:["gnome", "parrot", "binoculars"],
        4:["rock", "gnome"],
        5:["apple", "parrot", "binoculars"],
        6:["rock", "gnome", "binoculars"],
        7:["rock", "apple", "binoculars"],
        8:["gnome", "parrot"],
        9:["apple", "binoculars"],
        10:["rock", "gnome", "parrot", "binoculars"],
        11:["apple", "rock", "binoculars"],
        12:["parrot", "binoculars"],
        13:["apple", "gnome", "parrot"],
        14:["parrot", "binoculars"],
        15:["apple", "parrot", "binoculars"],
        16:["rock", "gnome", "parrot"]
    }

      show_map_of_villages(current_village_number)
      
      while True:
        while True:
          while True:
            direction = choose_direction()
            current_village_number = move_villages(direction, current_village_number)
            show_map_of_villages(current_village_number)
            explore_or_move_decision = explore_or_choose_direction(current_village_number)

            if explore_or_move_decision == "explore":
              break
      
          this_village_items = show_items_in_current_village(current_village_number, all_village_items)
          item_picked_up = choose_item_to_pick_up(current_village_number, this_village_items)
          
          if item_picked_up == "none":
            break

          if item_picked_up == "rock":
            bag = show_bag_contents(bag)
          
          if item_picked_up == "binoculars":
            village_for_binoculars = collect_village_number_for_binoculars()
            peek_into_village_with_binoculars(village_for_binoculars, all_village_items)
          
          parrot_response = hear_parrot_response()
          
          items_left = show_items_after_picked_up_item(current_village_number, this_village_items, item_picked_up, bag, parrot_response)
          #print("Items left:", items_left)
          
          all_village_items[current_village_number] = items_left

          won_or_not = has_won(bag, has_won_result)      
          if won_or_not == True:
            break    
        if won_or_not == True:
          break 
      

    elif user_play_or_not_chosen == "no":
      print("I'm sorry; maybe next time.")
      break
    else:
      print("I didn't understand that.")


play_game()



#"Villages of doom" game


#-------------INSTRUCTIONS ---------------------

# STEP 0: REQUIREMENTS: 
#1) Error tracker, 2) Reflection, 3) Min code components

# Maintain an Error Tracker: For every error you encounter, record the error message. When you solve the error, record what solves the error. 

# Reflection: Create a 5-minute video or 500-word reflection essay on 
# The most difficult parts of learning fundamental Python
# An interesting bug or error you encountered during the course, and how you overcame it
# Your favorite part about programming
# What you plan to do next to continue your learning

# Minimum Required Components for Adventure Game:
# Ask for user input to capture the following datatypes:
# At least one integer value
# At least 2 string values
# Use a while loop to continuously ask for user input
# Loop end should be determined by the user
# Use at least 4 if statements create dynamic action in your game based on user input. Using elif/else is optional, but encouraged. For example
# Present a red and a blue button, and ask the user which button they'd like to press. Make something happen depending on red vs. blue press.
# Present two paths-- one to the right and one to the left.
# Define a list that's empty, and add items to it
# Loop over a list and print each item using a for-loop
# Define and call at least 5 functions
# At least 2 of the 5 functions must have return values, for example
# Function to calculate a mathematical value, such as a sum or average
# Function to format user input with correct capitalization, punctuation, or length
# Function to determine whether a given value is valid or not, depending on certain requirements

# Extra Credit 
# Use a dictionary to associate and use a collection of data. You must access the keys and values in the dictionary-- not just define it as a variable. For example:
# Questions and answers
# Letters and words that start with that letter
# Choice and outcomes based on those choices
# Use a tuple to keep together a collection of values that won't change over the course of a program. You must use the tuple (perhaps loop over it, or check if a given value is inside it)- don't just define a variable. For example:
# Days of the week
# Choices in a decision
# Colors in the rainbow


#STEP 1: PSEUDOCODE 
# Draft out your User Flow:
# What steps need to happen
# What data do we need to keep track of
# What the user experience will be
# Write the code without writing the proper syntax


#STEP 2: OUTLINE CODE
# Use your Pseudocode & User Flow to outline functions and logic
# What data do you need to give to each function and what do you want each function to return?
# Then you can work on each function’s code


#STEP 3: DRAFT CODE
#Turn your pseudocode into python code.


#STEP 4: REFACTOR CODE
# Re-read your code and edit it to make it:
# Easier to read
# Consistent
# D.R.Y. (Don’t repeat yourself)
# Contain docstrings!
# Remember, refactoring is not about changing the functionality.

# Naming:
# Variable names
# Function names

# #sad name
# num = input("What is your guess? ")
# #good name
# guessed_number = input("What is your guess? ")

# Comments:
# Everywhere!
# # Game will continue to run until the player types
# # anything other than 'y'
# while game_state.lower() == "y":
#   guessing(player_name)
#   game_state = input("Would you like to play again?")

# Functions:
# Docstrings
# Does the docstring accurately describe the function?
# def checks_number(number, guesses_taken, guess, player_name):
#   """Checks if the guessed number is correct, prints to user winning status"""


#------MY PLANNING FOR STEP 0: REQUIREMENTS---------------

#Objective of adventure game: Escape from the villages. Find the rocks in the village that together create a portal to escape. 


# Minimum Required Components for Adventure Game:
# Ask for user input to capture the following datatypes:
# At least one integer value
#--see what's in a village, for the 16 villages. Enter a number, 1-16.

# At least 2 string values 
#--move north/south/east/west 
#--which item or items do you want to pick up?

# Use a while loop to continuously ask for user input
# Loop end should be determined by the user
#--Would you like to explore this village or move villages?
#--Would you like to pick up another item or would you like to move villages?

# Use at least 4 if statements create dynamic action in your game based on user input. Using elif/else is optional, but encouraged. For example: Present a red and a blue button, and ask the user which button they'd like to press. Make something happen depending on red vs. blue press. Or: Present two paths-- one to the right and one to the left.
#--if explore village, show the non-picked up items 
#--if north,south,east,west, move to that next village
#--if pick up particular item or items, show what happens for each
#--if same key and box are in bag, the box magically opens and a piece of the statue is inside. It doesn't do anything on its own.
#--if all 5 keys and boxes are open, the status comes together and the portal opens to escape. 
#--if no other items to pick up, don't offer that option 
#--if no items remaining to explore, say, "you've already picked up all items"

# Define a list that's empty, and add items to it
#--bag starts empty

# Loop over a list and print each item using a for-loop
#--Inventory of bag as enter each village.

# Define and call at least 5 functions
# At least 2 of the 5 functions must have return values, for example
#--Move between villages
#--Explore room; show remaining items. Ask user what they want to pick up (pass in remaininmlg items)
#--Pick up item and tell the user what happens once item(s) is/are picked up(pass in item response dictionary, pass in remaining items dictionary)

# Function to calculate a mathematical value, such as a sum or average
#--After picking up items, the game offers to tell what items are in other villages when the user inputs the village number.  (pass in remaining items dictionary)

# Function to format user input with correct capitalization, punctuation, or length
# Function to determine whether a given value is valid or not, depending on certain requirements

# Extra Credit 
# Use a dictionary to associate and use a collection of data. You must access the keys and values in the dictionary-- not just define it as a variable. For example:
# Questions and answers
# Letters and words that start with that letter
# Choice and outcomes based on those choices
#--Each of 5 items and the outcome if they are picked up
#--The 5 items and the counts of each one remaining 

# Use a tuple to keep together a collection of values that won't change over the course of a program. You must use the tuple (perhaps loop over it, or check if a given value is inside it)- don't just define a variable. For example:
# Days of the week
# Choices in a decision
# Colors in the rainbow
#--North, South, East, west


#print instructions

#Empty list, bag starts empty
#Function to tell the inventory of your bag FOR loop
#This function should be within the function to explore the village. 

#Function to show map of villages and where you are in it e.g. "1. You are here"


#Function to move between villages while LOOP
#move_between_villages = input("Would you like to move north, south, east or west? > ")
#--if north,south,east,west, move to that next village

#action_in_village = input("You're now in village number {}. Would you like to skip this village or explore it? Enter skip or explore > ")
#--if explore village, show the non-picked up items 

#Function to explore village
#five_item_choice = input("In this village, you can see {} items. Would you like to pick up the {box}, {key}, {apple}, {gnome}, or {parrot}? > ")
#--if pick up particular item or items, show what happens for each
#--if no items remaining to explore, say, "you've already picked up all items"

#Function to pick up item, while loop

#parrot response list, random clues. ["You need to collect the box and the key.", "All of the gnomes are scared of humans." "If you're hungry, feel free to eat food you find."]
#--if binoculars selected, call function to collect user input about village number to see items in.
#--if same key and box are in bag, the box magically opens and a piece of the statue is inside. It doesn't do anything on its own.
#--if all 5 keys and boxes are open, the status comes together and the portal opens to escape. 
#Sum the keys


#Function to tell which items are in other villages when the user inputs the village number.  (pass in remaining items dictionary)



#---------MY PLANNING FOR STEP 1: PSEUDOCODE-------------

#print info to user about how to play

#def Function to tell the inventory of your bag FOR loop
#--Empty list, bag starts empty

#def Function to show map of villages and where you are in it 

#def Function to ask user which way they would like to move.
#--if north,south,east,west, call function to move to that next village

#def Function to move between villages while LOOP

#def Function to ask user whether they'd like to explore village or skip  
#--if explore village, call function to explore village

#def Function to show the non-picked up items in each village
#--Pass in the village number and items in that village
#--if no items remaining to explore, say, "you've already picked up all items"

#def Function to explore village
#--call function to show inventory of bag.
#--call function to show the non-picked up items
#--if pick up particular item or items, call function to pick up item.

#def Function to pick up item, while loop, pass in item selected, pass in inventory of bag
#--Show response for each
#--if parrot, call function to see parrot response
#--if binoculars, call function to collect user input about which village to see the items in from afar.
#--if now same key and box are in bag, the box magically opens and a piece of the statue is inside. It doesn't do anything on its own.


#def Function to determine what the parrot says. 
#--it should be a new answer each time until 5 clues and then repeat. 
#--parrot response list, random clues. ["You need to collect the box and the key.", "All of the gnomes are scared of humans." "If you're hungry, feel free to eat food you find."]

#def Function to check if has won
#--Should be called within the pick up item function.
#--if all 5 keys and boxes are open, the status comes together and the portal opens to escape.  Return true or false.
#Sum the keys and boxes.


#def Main function to play game. 
#--Call the function to tell inventory of bag

#while True loop 

#--Call the function show_map_of_villages() to show map of villages and where you are in it. Pass in village number.

#--Call the function user_choose_direction() to ask user which way they would like to move. Return user selection.

#--Call function move_to_selected_village (pass in result of user_choose_direction) to move to the selected village (pass in user's choice). Return village number of present location. 

#--Call function user_explore_or_move() to ask user whether they would like to explore village or move again. This is a loop back to call function user_choose_direction. Return result explore or not?

#--Call function explore_village_items(pass in user_explore_or_move) to explore village.  

#--Within the function to explore village:

#--Call funtion show_my_bag_contents() to tell inventory of bag. Return bag contents dictionary.

#--Call function items_in_current_village() to tell remaining items in village. Return list of current items.

#--Call function user_item_to_pick_up () to ask user which item to pick up. Return item picked up.

#--if Parrot picked up, 
#call the function parrot_responses (item picked up is parrot)for parrot responses.

#--if binoculars picked up,
#call the function to view another village's items 

#--if key or box picked up, call function check_if_won (item picked up is key or box). Return True or False.


#---------MY PLANNING FOR STEP 2: OUTLINE CODE-------------


#print info to user about how to play

#Empty my_bag_dictionary, bag starts empty

#life_counter = 50

#row_1 = [1,2,3,4]
#row_2 = [5,6,7,8]
#row_3 = [9,10,11,12]
#row_4 = [13,14,15,16]

#village_map = [row_1,row_2,row_3,row_4]
#current_village_number = 6

#col_1 = [row_1[0], row_2[0], row_3[0], row_4[0]]
#col_2 = [row_1[1], row_2[1], row_3[1], row_4[1]]
#col_3 = [row_1[2], row_2[2], row_3[2], row_4[2]]
#col_4 = [row_1[3], row_2[3], row_3[3], row_4[3]]

#1 def Function show_bag_contents() to tell the inventory of your bag FOR loop (pull in the empty list) to tell inventory of bag. Return bag contents dictionary.
  #print("Here's the contents of your bag: ")
  #for i, item in enumerate(my_bag)
    #print(i, item)


#3 def Function show_map_of_villages(current_village_number) to show map of villages and where you are in it 
  #if my location matches a number below? my location should appear with an x.

  #print("Here's the map of the vilages: ")
  #print(" {}  |  {}  |  {}  |  {} ".format(row_1[0], row_1[1], row_1[2], row_1[3]))
  #print("--- + --- + --- + ----")
  #print(" {}  |  {}  |  {}  |  {} ".format(row_2[0], row_2[1], row_2[2], row_2[3]))
  #print("--- + --- + --- + ----")
  #print(" {}  |  {} |  {} |  {} ".format(row_3[0], row_3[1], row_3[2], row_3[3]))
  #print("--- + --- + --- + ----")
  #print(" {}  |  {} |  {} |  {} ".format(row_4[0], row_4[1], row_4[2], row_4[3]))
  #if current_village_number in row_1 or row_2 or row_3 or row_4:
  #print("You are in village {}".format(current_village_number))

#4 def Function choose_direction() to ask user which way they would like to move.
  #while True:
    #--print("Which direction would you like to move? Enter north, south, east, or west.")
    #user_direction_chosen = input("> ") 
    #user_direction_chosen = user_direction_choice.lower()
    #if not north, south, east, west:
      #print "I'm sorry, I didn't understand that" Loop again.
    #return user_direction_chosen


#5 def Function move_villages (user_direction_chosen, current_village_number) to move between villages while LOOP

#if user_direction_chosen == "north",
  #if current_village_number-4 <= 0:
    #print ("There's nothing to the north. Try another village.")
  #else: current_village_number = current_village_number -4 
#if user_direction_chosen == "south", 
  #if current_village_number+4 >= 17:
    #print ("There's nothing to the south. Try another village.")
  #else: current_village_number = current_village_number+4
#if user_direction_chosen == "east",
  #if current_village_number == 4,8,12, 16:
    #print ("There's nothing to the east. Try another village.")
  #else: current_village_number = current_village_number+1
#if user_direction_chosen == "west", 
  #if current_village_number == 1,5,9,13:
    #print ("There's nothing to the west. Try another village.")
  #else: current_village_number = current_village_number-1

#life_counter = life_counter -1
#return village_number


#6 def Function explore_or_choose_direction() to ask user whether they'd like to explore village or skip 
  #while true:
    #print("Would you like to explore village {} or move to a different village? Enter explore or move".format(village_number)) 
    #user_explore_or_move_choice = input("> ")

    #if user_explore_or_move_choice == "explore:
      # explore = explore_village_items()
    #if user_explore_or_move_choice == "move":
      # move = user_choose_direction()
    #else: 
      #print("I didn't understand that.")
    #return explore_or_move_chosen


#7 def Function show_items_in_current_village(current_village_number)

  #v1 = [rock, gnome, parrot]
  #v2 = [apple, binoculars]
  #v3 = [gnome, parrot, binoculars]
  #v4 = [rock, gnome]
  #v5 = [apple, parrot, binoculars]
  #v6 = [rock, gnome, binoculars]
  #v7 = [apple, binoculars]
  #v8 = [gnome, parrot]
  #v9 = [apple, binoculars]
  #v10 = [gnome, parrot, binoculars]
  #v11 = [apple, rock, binoculars]
  #v12 = [parrot, binoculars]
  #v13 = [apple, gnome, parrot]
  #v14 = [parrot, binoculars]
  #v15 = [apple, parrot, binoculars]
  #v16 = [rock, gnome, parrot]

  #items = [v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16]

  #print("As you look around village {}, you see:")
    
  #for i, item in enumerate(items): 
    #if i+1 = current_village_number:
      #if not i+1:
        #print("nothing.")
      #else:
        #for i in item:
          #print(i)  
        #return item  


#8 def Function choose_item_to_pick_up(village_number, show_items_in_current_village()) to select an item to pick up.

  #print("Which item would you like to pick up? You can only pick up one at a time. If you don't want to pick up any items, enter none.")
  #item_selected = input("> ")
  #item_selected = item_selected.lower()
  #if not item_selected in item list:
    #print("I'm sorry, I didn't understand that. Please enter the name of an item. Your choices are: {},{},{}, {} or "none."" format(xxx))
  #elif item_selected == "none":
    #move = move_between_villages().
  #else: 
    #pick_up = function to pick up item.
    #return item_selected


#9 def collect_village_number_for_binoculars()

#print("Which village would you like to peek into? Enter the village number. >")
#village_for_binoculars = input("> ")
#print village_number [village_items] 
#return village_for_binoculars

#10 def pick_up_item_or_move
#print("Would you like to pick up another item or move villages? Enter move or pick up item")
#move_or_pick_up_choice_made = input("> ")
#move_or_pick_up_choice_made = #move_or_pick_up_choice_made.lower()

#11 def Function pick_up_this_item (item_selected): 
#to pick up item, while loop, pass in item selected
  #if item_selected == apple:
    #print("You eat the apple and it added 2 units to your life.")
    #life_counter = life_counter + 2
  #if item_selected == rock:
    #print("It's a beautiful, sparkly rock. It seems like it's a broken off piece of a larger rock. You put it into your bag in case it's valuable.")
  #if item_selected == gnome:
    #print("You picked up the gnome, and it got scared and bit you before running away. The bite cost you 5 units of your life.")
    #life_counter = life_counter - 5.
  #if item_selected == parrot:
    #print("You picked up the parrot and it said {} before flying off.".format(call parrot_response))
  #if item_selected == binoculars:
    #print("You can explore the items in another village before you make a move.")
    #call collect_village_number ()

  #if items_in_current_village > 0:
    #call pick_up_item_or_move() 
  
  #else: 
    #print("There are no remaining items in this village." 
    #call choose_direction()
  #return


#12 def Function hear_parrot_responses() to determine what the parrot says. 
#--it should be a new answer each time until 5 clues and then repeat. 
#parrot_response = random.choice(["You need to collect the box and the key.", "All of the gnomes are scared of humans." "If you're hungry, feel free to eat food you find."])
#return parrot_response 

#13 def Function to has_won()

#--if my_bag_dictionary[rock] ==5, all 5 pieces of rock are in bag (use sum), the rock formation magically puts itself together and the portal opens to escape.
#Return true or false.


#14 def Main function to play game. 

#--1 call show_bag_contents()
#Return dictionary 

#while loop 

#--2 call calculate_my_location()

#--3 call show_map_of_villages(village_number) to show map of villages and where you are in it. Pass in your location/village number.

#--4 call user_choose_direction() to ask user which way they would like to move. Return user selection.

#--5 call move_villages(user_direction_chosen) to move to the selected village. Return village_number of present location. 

#--6 call explore_or_choose_direction() to ask user whether they would like to explore village or move again. This is a loop back to call function user_choose_direction. Return explore_or_move_chosen.

#--1 call my_items = show_bag_contents()


#--7 call show_items_in_current_village(village_number) to tell remaining items in village. Return list of current items.

#--8 call choose_item_to_pick_up(village_number) to explore village.  Return item_selected

#--10 call pick_up_item_or_move()
#move_or_pick_up_choice_made

#--11 Call pick_up_this_item (item_selected) to show what happens when item is picked up.

#--if item_selected == binoculars:
#--7 call collect_village_number_for_binoculars
#call explore_this_villages_item(village_number)

#--if item_selected == parrot:
#--11 call give_parrot_responses ()
#return parrot_response


#--if item_picked_up == rock:
#--13 call function has_won (item picked up is rock). Return True or False.

