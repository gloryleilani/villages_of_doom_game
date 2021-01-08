

row_1 = [1,2,3,4]
row_2 = [5,6,7,8]
row_3 = [9,10,11,12]
row_4 = [13,14,15,16]
village_map = [row_1,row_2,row_3,row_4]
#bag = {}
life_counter = 25

print("")
def show_bag_contents(bag): #function 1
  """Show the contents of your bag."""

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
  """Display the map of villages and where you are on the map."""

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
  """Ask the user which way he/she would like to move on the map."""

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
  """Allow the user to move to the next village."""

  
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
  """Ask the user whether he/she would like to explore the current village or move to a different village.""" 
  
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
  """Return the item in the dictionary containing the lists of items in the current village."""

  print("")
  print("As you look around village {}, you see:".format(current_village_number))
  print("")  

  for item in (all_village_items[current_village_number]):
    print (item)
        
  return all_village_items[current_village_number]  


def choose_item_to_pick_up(current_village_number, current_village_items):
  """Let the user select an item to pick up."""

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
  """Determine which random phrase the parrot says.""" 
  
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
  """Show what happens when an item is picked up."""

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
  """Let the user pick the village to peek into."""

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
  """Let the user see the items in another village via binoculars"""

  print("")
  print("That village contains:")
  print("")
  for item in (all_village_items[village_for_binoculars]):
    print (item)


def has_won(bag, result):
  """Tell whether the user has won or not. It takes 5 rocks in the bag to win."""
  
  if bag != {}: 
    if bag["rock"] == 5: 
      print("")
      print("Your bag starts rumbling and the rocks rise into the air and form a circle which gets larger and turns into a portal! You step through and find yourself in your own backyard again!")
      print("")
      print("CONGRATULATIONS! YOU WON!")
      print("")
      result = True
      return result


def play_game(): 
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

