import sys
import os
import time
import random
import subprocess
from getpass import getpass
import json

# Open the JSON file and read its contents
with open("pokemon.json", "r") as json_file:
    json_data = json_file.read()

# Convert the JSON data to a dictionary
pokemon_data = json.loads(json_data)


trainer_name = ""

item = ""
mum_items = ""

brody_fight = False
global met_lucy
met_lucy = False

pokemon = ""
pokemon_health = ""
choice = ""

inventory = {

}

pokemon_inv = {

}

location = ""

global mode
mode = ""

# Brody = cyan, Lucy = purple, Professor Avalon = yellow
RED = "\033[0;31m"
GREEN = "\033[0;32m"
ORANGE = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
WHITE = "\033[0;37m"
BLACK = "\033[0;30m"
RED = "\033[0;91m"
GREEN = "\033[0;92m"
YELLOW = "\033[0;93m"
BLUE = "\033[0;94m"
MAGENTA = "\033[0;95m"
CYAN = "\033[0;96m"
BRIGHT_BLACK = "\033[0;90m"
BRIGHT_RED = "\033[0;91m"
BRIGHT_GREEN = "\033[0;92m"
BRIGHT_YELLOW = "\033[0;93m"
BRIGHT_BLUE = "\033[0;94m"
BRIGHT_MAGENTA = "\033[0;95m"
BRIGHT_CYAN = "\033[0;96m"
BRIGHT_WHITE = "\033[0;97m"
CYAN_BACK = "\033[0;46m"
PURPLE_BACK = "\033[0;45m"
WHITE_BACK = "\033[0;47m"
BLUE_BACK = "\033[0;44m"
ORANGE_BACK = "\033[0;43m"
GREEN_BACK = "\033[0;42m"
PINK_BACK = "\033[0;41m"
GREY_BACK = "\033[0;40m"
GREY = '\033[38;4;236m'
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
ITALIC = "\033[3m"
DARKEN = "\033[2m"
INVISIBLE='\033[08m'
REVERSE='\033[07m'
END='\033[0m'
GREY = "\x1b[90m"

# Brody's introduction
brody_introduction = "STRANGER: Hey there, new trainer! I'm Brody, the Gym Leader of Bro Town, and I'm the best there is. No one can defeat me, and I'm ready to take on any challenger who's brave enough to try."

brody_introduction_2 = BOLD + UNDERLINE + CYAN + "BRODY: " + END + "Come on by and test your skills against me and my unbeatable Pokemon team. I'll be waiting for you at the Gym, ready to prove my superiority. Let's see if you've got what it takes to become the ultimate champion."

brody_advice = BOLD + UNDERLINE + CYAN + "BRODY: " + END + "Catching Pokemon is key, so be sure to explore and catch as many as you can. Feed your Pokémon berries to increase their level."

brody_advice_2 = BOLD + UNDERLINE + CYAN + "BRODY: " + END + "And also dont forget to visit the shop every once in a while to refill your Pokéball stock."

# Lucy's introduction

lucy_intro_2 = "GIRL: Hey there handsome, my name is " + PURPLE + "Lucy" + END + ". I'm the town's resident quest giver, so if you're looking for some adventure and a chance to prove your worth, come see me. Who knows, maybe we'll even have a little fun along the way ;)"

# Brody Quest 1
brody_quest_1 = BOLD + UNDERLINE + CYAN + "BRODY: " + END + "Hey, trainer! I've got a bit of a problem, and I could use your help. There's a group of wild Pokemon that have been causing trouble at the beach lately, and I'm worried they might start attacking people. I was wondering if you could help me clear them out? If you're successful, I'll give you a reward of your choice - it could be a TM, an item, or even a battle against one of my strongest Pokemon. What do you say?"

# Lucy Quest 1
lucy_quest_1 = PURPLE + "LUCY:" + END + " Scavenger hunt: Lucy has lost a valuable item and needs the player's help to find it. She will provide clues and riddles to guide the player through the search, and will reward them with a special item or battle opportunity when they are successful."

# Lucy Quest 2
lucy_quest_2 = PURPLE + "LUCY:" + END + " Pokemon contest: Lucy is preparing to enter a Pokemon contest and needs some help practicing and perfecting her routines. She will ask the player to help her and her Pokemon train and prepare for the contest, and will give them a reward if they are able to help her place in the top three."

# Lucy accept quest
lucy_accept_quest = PURPLE + "LUCY:" + END + " Great! I knew I could count on you!"

# Lucy decline quest
lucy_decline_quest = PURPLE + "LUCY:" + END + " Oh, well that's okay. If you change your mind, just let me know."

# Lucy quest completed
lucy_quest_completed = PURPLE + "LUCY:" + END + " Wow, you really came through for me! Thank you so much. Here's your reward, just as promised."

# Lucy defeated
lucy_defeated = PURPLE + "LUCY:" + END + " Wow, you really gave me a run for my money! I'm impressed. Good job, trainer."

# Lucy Quest 3
lucy_quest_3 = PURPLE + "LUCY:" + END + " Research project: Lucy is working on a research project for the local Pokemon research lab, and needs the player's help collecting data and samples from various locations around Bro Town. She will provide the player with a list of tasks to complete, and will reward them with a special item or battle opportunity when they are finished."

# Brody gives pokeballs
brody_gift_text = BOLD + UNDERLINE + CYAN + "BRODY: " + END + "Oh I almost forgot, I want to help you get off to a good start. Here, take these 15 Pokeballs aswell as 50 Bro Coins (Bro Town currency ¥)"

brody_gift_text_2 = "\n" + BOLD + UNDERLINE + CYAN + "BRODY: " + END + "They'll come in handy when you're trying to catch all the cool Pokemon out there. And don't forget - come back and challenge me when you're feeling like a real champion."

# Introduction Text
introduction_text = "Welcome to " + BOLD + UNDERLINE + BLUE + "Pokemon Bros 2!" + END + "\nExplore Bro Town, capture new " + BOLD + UNDERLINE + GREEN + "Pokemon" + END + ", and become a " + BOLD + UNDERLINE + BRIGHT_RED + "Master Trainer." + END

# Bro Town intro
bro_town_intro = "\nYou take your first steps into Bro Town, taking in the sights and sounds of the bustling city. The sun is shining and the air is filled with the cries of Pokemon."

bro_town_intro_2 = "\nIn front of you stands a tall friendly-looking trainer. Hes wearing sunglasses and seems to be from around here. He waves for you to come to him."

shop_owner = GREEN + "SHOP OWNER: " + END + "Welcome to my shop. What can I get for ya?"

town_text = "As you walk through the streets of Bro Town, you come across the town plaza. You've heard that this is the center of the town and a popular gathering place for trainers."

town1 = "You decide to take a look around and see what the plaza has to offer. You wander through the crowds of people, taking in the sights and sounds of the bustling marketplace."

sees_lucy = "Suddenly, you spot a girl standing off to the side, her arms crossed and a curious expression on her face. You've never seen her before, but something about her draws you in."

brody_fight_1 = ""

def exit_game():
  choice = input("Are you sure?" + RED + " ALL PROGRESS FROM THIS PLAYTROUGH WILL BE LOST!" + END + " (y/n)")

  if choice == "y" or choice == "Y" or choice == "yes" or choice == "Yes":
    print("\nThank you for playing! Goodbye!")
    time.sleep(1)
    sys.exit()

  else: 
    print("Ok, not exiting...")
    time.sleep(3)
    main(met_lucy)

  return

def add_item(item, num_items):
  if item in inventory:
    # If the item is already in the inventory, update the quantity
    if item == "GOLDEN BRO COIN":
      inventory[item] += num_items
      print(str(num_items) + " " + YELLOW + BOLD + UNDERLINE + item + "S" + END + " WAS ADDED TO YOUR INVENTORY")
      return

    inventory[item] += num_items
    print(str(num_items) + " " + BRIGHT_RED + BOLD + UNDERLINE + item + "S" + END + " WAS ADDED TO YOUR INVENTORY")
    return
  
  else:
    # If the item is not in the inventory, add it
    if item == "GOLDEN BRO COIN":
      inventory[item] = num_items
      print(str(num_items) + " " + YELLOW + BOLD + UNDERLINE + item + END + " WAS ADDED TO YOUR INVENTORY")
      return
       
    inventory[item] = num_items
    print(str(num_items) + " " + BRIGHT_RED + BOLD + UNDERLINE + item + "S" + END + " WAS ADDED TO YOUR INVENTORY")
    return

def clear_screen():
  # Clear the screen using the appropriate command for the operating system
  subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

def add_pokemon(pokemon):
    if pokemon in pokemon_inv:
      # If the Pokémon is already in the inventory
      print("YOU ALREADY HAVE A " + pokemon + " IN YOUR INVENTORY")
      return
    else:
      # If the pokemon is not in the inventory, add it
      pokemon_health = pokemon_data.get(pokemon, {}).get("max_health", 0)
      pokemon_type = pokemon_data.get(pokemon, {}).get("type", "")
      pokedex = pokemon_data.get(pokemon, {}).get("found", 0)
      pokemon_inv[pokemon] = (pokemon_health, pokemon_type)
      pokemon_data[pokemon]["found"] = 1
      
      if pokemon_type == "Fire" or pokemon_type == "Fighting":
        print(BRIGHT_RED + pokemon + END + " WAS ADDED TO YOUR INVENTORY")

      elif pokemon_type == "Water":
        print(BLUE + pokemon + END + " WAS ADDED TO YOUR INVENTORY")

      elif pokemon_type == "Normal" or pokemon_type == "Ground" or pokemon_type == "Rock":
        print(BOLD + pokemon + END + " WAS ADDED TO YOUR INVENTORY")

      elif pokemon_type == "Bug" or pokemon_type == "Grass":
        print(GREEN + pokemon + END + " WAS ADDED TO YOUR INVENTORY")

      elif pokemon_type == "Poison" or pokemon_type == "Ghost" or pokemon_type == "Phsycic":
        print(PURPLE + pokemon + END + " WAS ADDED TO YOUR INVENTORY")

      elif pokemon_type == "Electric":
        print(YELLOW + pokemon + END + " WAS ADDED TO YOUR INVENTORY")

      add_item("BRO COIN", 5)
      return

def stats(location):

  print("LOCATION: " + location)
  print("POKEBALLS: " + str(inventory.get("POKEBALL", 0)))
  print("BRO COINS: " + YELLOW + str(inventory.get("BRO COIN", 0)) + "¥" + END)

  if not pokemon_inv:
    pokemon_list = "POKÈMON: None"
    print(pokemon_list)
    print("\n")

  else:
    
    # Print the names of all the Pokémon in the player's inventory on the same line, separated by a comma
    pokemon_list = "POKÉMON: "
    for pokemon in pokemon_inv:
        pokemon_list += pokemon + ", "
    
    # Remove the final comma and space from the list
    pokemon_list = pokemon_list[:-2]
    print(pokemon_list)
    print("\n")


  return

def spawn_pokemon():
  # Get a list of all the Pokémon in the Pokémon data
  pokemon_list = list(pokemon_data.keys())
  # Shuffle the list
  random.shuffle(pokemon_list)
  
  # Choose a random number between 0 and 1
  rand_num = random.uniform(0, 1)
  
  # Loop through the Pokémon list
  for pokemon in pokemon_list:
    # Get the spawn rate of the current Pokémon
    data = pokemon_data[pokemon]
    spawn_rate = data.get("spawn_rate", 0)
  
    # Check if the random number is less than the spawn rate
    if rand_num < spawn_rate:
      # Add the Pokémon to the player's inventory
      # Exit the loop
      return pokemon

  return

def moves(p_pokemon, p_pokemon_hp, p_pokemon_type):
    p_pokemon_dmg = pokemon_data[p_pokemon]["attack_damage"]

    while True:
      move = input("\nChoose your action:\n(1)" + BRIGHT_RED + " Attack" + END + " - DEAL " + str(p_pokemon_dmg) + "\n")

      if move == "1":
          move = "Attack"
          return move, p_pokemon_dmg
    
      else:
         print("\nUnrecognised input.")

def battle(npc_name):

    # Define a variable to store the number of the current Pokémon in the list
    pokemon_number = 1

    print("\n\nChoose your battling Pokémon!\n")
    for pokemon in pokemon_inv:
        pokemon_health = pokemon_inv[pokemon][0]
        pokemon_max_health = pokemon_data[pokemon]["max_health"]
        print("(" + str(pokemon_number) + ") " + pokemon + " " + str(pokemon_health) + "/" + str(pokemon_max_health) + " HP")
        pokemon_number += 1

    choice = input("")
    choice = int(choice)

    # p = player
    p_pokemon = list(pokemon_inv.keys())[choice - 1]
    print("\nYou brought " + p_pokemon + " into battle!")

    # get player pokemon health and type for the battle
    p_pokemon_hp = pokemon_health
    p_pokemon_type = pokemon_data[p_pokemon]["type"]
    p_pokemon_dmg = pokemon_data[p_pokemon]["attack_damage"]

    # get npc random pokemon and corresponding health and type for the battle

    # Get a list of all the Pokémon in the Pokémon data
    pokemon_list = list(pokemon_data.keys())
    # Shuffle the list
    random.shuffle(pokemon_list)

    # Choose a random number between 0 and 1
    rand_num = random.uniform(0, 1)

    # Loop through the Pokémon list
    for pokemon in pokemon_list:
        # Get the spawn rate of the current Pokémon
        data = pokemon_data[pokemon]
        spawn_rate = data.get("spawn_rate", 0)
    
        # Check if the random number is less than the spawn rate
        if rand_num < spawn_rate:
            npc_pokemon = pokemon


    npc_name = npc_name

    npc_pokemon_hp = pokemon_data[npc_pokemon]["max_health"]
    npc_pokemon_type = pokemon_data[npc_pokemon]["type"]
    npc_pokemon_dmg = pokemon_data[npc_pokemon]["attack_damage"]


    if npc_name == "Brody":
        npc_pokemon = BOLD + UNDERLINE + "Brody's Special Growlithe" + END
        npc_pokemon_dmg = 17
        npc_pokemon_type = "Fire"
        npc_pokemon_hp = 75
        print("\nYour opponent is " + BOLD + UNDERLINE + CYAN + npc_name + END + " using "  + npc_pokemon + " with " + str(npc_pokemon_hp) + " HP. " +"It is " + npc_pokemon_type + " type and has an attack damage of " + str(npc_pokemon_dmg) + "!")
        time.sleep(7)
        print("\n\nBattle begins in...")
        time.sleep(1)
        print("\n3...")
        time.sleep(1)
        print("\n2...")
        time.sleep(1)
        print("\n1...")
        time.sleep(1)
        print("\n\nBegin Battle!!\n\n")
        while(npc_pokemon_dmg >= 0 and p_pokemon_hp >= 0):
            move, p_pokemon_dmg = moves(p_pokemon, p_pokemon_hp, p_pokemon_type)
            

            if move == "Attack":
                print("\n" + p_pokemon + " used " + BRIGHT_RED + "Attack!" + END)
                npc_pokemon_hp -= p_pokemon_dmg
                time.sleep(1)
                npc_pokemon_hp = max(0, npc_pokemon_hp)
                print("-" + str(p_pokemon_dmg) + "HP for " + npc_pokemon + "! Now " + str(npc_pokemon_hp) + " HP!" )
                time.sleep(3)

                if npc_pokemon_hp > 0:
                    random_number1 = random.randint(1, 100)
                    if random_number1 in range(1, 26):
                        print("\n" + BOLD + UNDERLINE + CYAN + "BRODY: " + END + "Hah! You'll never beat me with that feeble " + p_pokemon + "!\n")
                    elif random_number1 in range(27, 61):
                        print("\n" + BOLD + UNDERLINE + CYAN + "BRODY: " + END + "You really think you can beat me, huh?\n")
                    else:
                        print("\n" + BOLD + UNDERLINE + CYAN + "BRODY: " + END + "Augh, come on!\n")
                    time.sleep(3)
                    print("\n" + npc_pokemon + " used " + BRIGHT_RED + "Attack!" + END)
                    p_pokemon_hp -= npc_pokemon_dmg
                    time.sleep(1)
                    print("-" + str(npc_pokemon_dmg) + "HP for " + p_pokemon + "! Now " + str(p_pokemon_hp) + " HP!" )

            if npc_pokemon_hp <= 0:
                print("\n" + npc_pokemon + " has been defeated!")
                time.sleep(1) 
                time.sleep(5)
                return "win"

            elif p_pokemon_hp <= 0:
                print("\n" + "Your " + p_pokemon + " has been defeated.")
                time.sleep(5)
                return "lose"

    if npc_name == "Lucy":
        npc_pokemon = BOLD + UNDERLINE + "Lucy's Special Jigglypuff" + END
        npc_pokemon_dmg = 20
        npc_pokemon_type = "Normal"
        npc_pokemon_hp = 115
        print("\nYour opponent is " + npc_name + " using "  + npc_pokemon + " with " + str(npc_pokemon_hp) + " HP. " + "It is " + npc_pokemon_type + " type and has an attack damage of " + str(npc_pokemon_dmg) + "!")
        time.sleep(7)
        print("\n\nBattle begins in...")
        time.sleep(1)
        print("\n3...")
        time.sleep(1)
        print("\n2...")
        time.sleep(1)
        print("\n1...")
        time.sleep(1)
        print("\n\nBegin Battle!!\n\n")
        while(npc_pokemon_dmg >= 0 and p_pokemon_hp >= 0):
            move, p_pokemon_dmg = moves(p_pokemon, p_pokemon_hp, p_pokemon_type)

            if move == "Attack":
                print("\n" + p_pokemon + " used " + BRIGHT_RED + "Attack!" + END)
                npc_pokemon_hp -= p_pokemon_dmg
                time.sleep(1)
                npc_pokemon_hp = max(0, npc_pokemon_hp)
                print("-" + str(p_pokemon_dmg) + "HP for " + npc_pokemon + "! Now " + str(npc_pokemon_hp) + " HP!" )
                time.sleep(3)

                if npc_pokemon_hp > 0:
                    random_number1 = random.randint(1, 100)
                    if random_number1 in range(1, 26):
                        print("\n" + PURPLE + "LUCY:" + END + " I won't go down that easily! " + "\n")
                    elif random_number1 in range(27, 61):
                        print("\n" + PURPLE + "LUCY:" + END + "I've got a few tricks up my sleeve!\n")
                    else:
                        print("\n" + PURPLE + "LUCY:" + END + " I'm not feeling very strong today... (◞╭╮◟)\n")
                    time.sleep(3)
                    print("\n" + npc_pokemon + " used " + BRIGHT_RED + "Attack!" + END)
                    p_pokemon_hp -= npc_pokemon_dmg
                    time.sleep(1)
                    print("-" + str(npc_pokemon_dmg) + "HP for " + p_pokemon + "! Now " + str(p_pokemon_hp) + " HP!" )

            if npc_pokemon_hp <= 0:
                print("\n" + npc_name + "'s " + npc_pokemon + " has been defeated!")
                time.sleep(1) 
                add_item("BRO COIN", 100)
                time.sleep(5)
                return "win"

            elif p_pokemon_hp <= 0:
                print("\n" + "Your " + p_pokemon + " has been defeated.")
                time.sleep(5)
                return "lose"

    print("\nYour opponent is " + npc_name + " using "  + npc_pokemon + " with " + str(npc_pokemon_hp) + " HP. " + npc_pokemon + " is " + npc_pokemon_type + " type and has an attack damage of " + str(npc_pokemon_dmg) + "!")
    time.sleep(7)
    print("\n\nBattle begins in...")
    time.sleep(1)
    print("\n3...")
    time.sleep(1)
    print("\n2...")
    time.sleep(1)
    print("\n1...")
    time.sleep(1)
    print("\n\nBegin Battle!!\n\n")

    while(npc_pokemon_dmg >= 0 and p_pokemon_hp >= 0):
        move, p_pokemon_dmg = moves(p_pokemon, p_pokemon_hp, p_pokemon_type)

        if move == "Attack":
            print("\n" + p_pokemon + " used " + BRIGHT_RED + "Attack!" + END)
            npc_pokemon_hp -= p_pokemon_dmg
            time.sleep(1)
            npc_pokemon_hp = max(0, npc_pokemon_hp)
            print("-" + str(p_pokemon_dmg) + "HP for " + npc_pokemon + "! Now " + str(npc_pokemon_hp) + " HP!" )
            time.sleep(3)
            # Generate random number from 1-100
            random_number = random.randint(1, 100)

            if random_number in range(1, 96) and npc_pokemon_hp > 0:
                print("\n" + npc_pokemon + BRIGHT_RED + " used Attack!" + END)
                p_pokemon_hp -= npc_pokemon_dmg
                time.sleep(1)
                print("-" + str(npc_pokemon_dmg) + "HP for " + p_pokemon + "! Now " + str(p_pokemon_hp) + " HP!" )
            
            elif random_number not in range(1, 96) and npc_pokemon_hp > 0:
                print("\n" + npc_pokemon + " fled the battle!")
                time.sleep(1) 
                add_item("BRO COIN", 50)
                time.sleep(4)
                return "win"

        if npc_pokemon_hp <= 0:
            print("\n" + npc_name + "'s " + npc_pokemon + " has been defeated!")
            time.sleep(1) 
            add_item("BRO COIN", 50)
            time.sleep(5)
            return "win"
        elif p_pokemon_hp <= 0:
            print("\n" + "Your " + p_pokemon + " has been defeated.")
            time.sleep(5)
            return "lose"

def choose_starter():
  clear_screen()
  choice = input("Choose your starter Pokémon! \n\n(1) " + RED + "Charmander!" + END + "\n(2) " + BLUE + "Squirtle!" + END + "\n(3) " + GREEN + "Bulbasaur!\n" + END)

  if choice == "1":
    print("\n" + YELLOW + "PROFESSOR AVALON:" + END + " Congratulations! Take good care of " + RED + "Charmander!\n" + END)
    time.sleep(3)
    add_pokemon("Charmander")
    time.sleep(2)
    print("\n\nYou put " + RED + "Charmander" + END + " on your shoulder and begin to walk home...")
    time.sleep(3)
    met_lucy = True
    main(met_lucy)
    
  elif choice == "2":
    print("\n" + YELLOW + "PROFESSOR AVALON:" + END + " Congratulations! Take good care of " + BLUE + "Squirtle!\n" + END)
    time.sleep(3)
    add_pokemon("Squirtle")
    time.sleep(2)
    print("\n\nYou put " + BLUE + "Squirtle" + END + " on your shoulder and begin to walk home...")
    time.sleep(3)
    met_lucy = True
    main(met_lucy)
    
  elif choice == "3":
    print("\n" + YELLOW + "PROFESSOR AVALON:" + END + " Congratulations! Take good care of " + GREEN + "Bulbasaur!\n" + END)
    time.sleep(3)
    add_pokemon("Bulbasaur")
    time.sleep(2)
    print("\n\nYou put " + GREEN + "Bulbasaur" + END + " on your shoulder and begin to walk home...")
    time.sleep(3)
    met_lucy = True
    main(met_lucy)
    
  else:
    print("Invalid choice.")
    clear_screen()
    choose_starter()

def town(state):
  global met_lucy
  global mode
  met_lucy = True
  print("You leave your house and head for the Town...")
  time.sleep(3)
  clear_screen()

  if state == "new" and mode == "dialogue":
    met_lucy = True
    print(town_text)
    print("\n \n")
    time.sleep(6)
    print(town1)
    time.sleep(6)
    print("\n \n")
    print(sees_lucy)
    time.sleep(4)
    print("\n \n")
    print("Say something to the girl...")
    print("\n")
    choice = input("(1) Introduce yourself \n(2) Introduce yourself romantically\n")
  
    if choice == "1":
      print("\n")
      print("You introduce yourself to the girl...")
      time.sleep(1)
      print("\n")
      print("GIRL: Hi" + trainer_name + "! I'm " + PURPLE + "Lucy" + END + ", the towns local quest giver. I have a few quests that I could use your help with. You'll get to explore new areas, catch some new Pokémon, and earn some rewards along the way. What do you say? Are you interested in helping me out?")
      time.sleep(8)
      print("\n")
      print("Unfortunately, it looks like the board is empty right now.\n\n")
      time.sleep(6)
      print("You thank " + PURPLE + "Lucy" + END + " for her time and continues walking through the Town. She will probably have some quests for you later.\n")
      time.sleep(4)
      print("As you continue on your journey, a building with a sign reading " + YELLOW + 'BTRS: Bro Town Research Institute' + END + " comes into view. It looks like a laboratory of some sort.\n \n") 
      time.sleep(5)
      print("Could this be where you obtain your starter Pokémon?\n\n")
      time.sleep(4)
      print("Suddenly, you feel a gentle tap on your shoulder, and as you turn around, you see a towering figure standing before you.\n\n")
      time.sleep(4)
      print("BIG GUY: Ah, hello there! Welcome to the Bro Town Research Institute. My name is " + YELLOW + "Professor Avalon." + END + " I specialize in the study of Pokémon and their behaviors. What brings you here today?\n\n")
      choice = input("(1) Ask him about starter pokémons\n(2) Ask about nearby Pokémon catching spots.\n")

      if choice == "1":
        print("\n")
        print(YELLOW + "PROFESSOR AVALON:" + END + " Well, as a professor at the BTRS, it is my duty to assist trainers like yourself in their journey to becoming the very best. As such, I have three starter Pokémon that I can offer to you. I have a Charmander, a Squirtle, and a Bulbasaur. They are all very capable and strong Pokémon, and I have no doubt that they will serve you well on your journey. So, which one do you choose?")
        time.sleep(10)
        choose_starter()

      if choice == "2":
        
        print("\n" + YELLOW + "PROFESSOR AVALON:" + END + " Well, there are a lot of great places to catch Pokémon around Bro Town. One of them is The Redwood Forest, it's great for grass and ground type. Anyway, what can I do for you?\n")
        choice2 = input("(1) Ask him about starter pokémons\n")

        if choice2 == "1":
          print("\n")
          print(YELLOW + "PROFESSOR AVALON:" + END + " Well, as a professor at the BTRS, it is my duty to assist trainers like yourself in their journey to becoming the very best. As such, I have three starter Pokémon that I can offer to you. I have a " + RED + "Charmander" + END + "," + " a " + BLUE + "Squirtle" + END + ", and a " + GREEN + "Bulbasaur" + END + ". They are all very capable and strong Pokémon, and I have no doubt that they will serve you well on your journey. So, which one do you choose?")
        time.sleep(10)
        choose_starter()

      else:
       print("\nUnrecognised input.")
       input("Press enter...")

    elif choice == "2":
      print("\n")
      print("You romantically introduce yourself to the girl...")
      time.sleep(1)
      print("\n")
      print(lucy_intro_2)
      time.sleep(8)
      print("\n")
      print("Unfortunately, it looks like the board is empty right now.\n\n")
      time.sleep(6)
      print("You thank " + PURPLE + "LUCY:" + END + " for her time and continues walking through the Town. She will probably have some quests for you later.")
      time.sleep(4)
      print("As you continue on your journey, a building with a sign reading " + YELLOW + 'BTRS: Bro Town Research Institute' + END + " comes into view. It looks like a laboratory of some sort.\n \n") 
      time.sleep(5)
      print("Could this be where you obtain your starter Pokémon?\n\n")
      time.sleep(4)
      print("Suddenly, you feel a gentle tap on your shoulder, and as you turn around, you see a towering figure standing before you.\n\n")
      time.sleep(4)
      print("BIG GUY: Ah, hello there! Welcome to the Bro Town Research Institute. My name is " + YELLOW + "Professor Avalon." + END + " I specialize in the study of Pokémon and their behaviors. What brings you here today?\n\n")
      choice = input("(1) Ask him about starter pokémons.\n(2) Ask about nearby Pokémon catching spots.\n")

      if choice == "1":
        print("\n")
        efeg = input(YELLOW + "PROFESSOR AVALON:" + END + " Well, as a professor at the BTRS, it is my duty to assist trainers like yourself in their journey to becoming the very best. As such, I have three starter Pokémon that I can offer to you. I have a Charmander, a Squirtle, and a Bulbasaur. They are all very capable and strong Pokémon, and I have no doubt that they will serve you well on your journey. So, which one do you choose?\n")
        time.sleep(10)
        print("\nPRESS ENTER TO CONTINUE...")
        if efeg == " ":
            choose_starter()
        else: 
            print("Unknown command, try again!")
            time.sleep(3)
            clear_screen()
            town("new")

      if choice == "2":
        print(YELLOW + "PROFESSOR AVALON:" + END + "  Well, there are a lot of great places to catch Pokémon around Bro Town. One of them is The Redwood Forest, it's great for grass and ground type. Anyway, what can I do for you?")
        choice2 = input("(1) Ask him about starter pokémons\n")

        if choice2 == "1":
            print("\n")
            efeg = input(YELLOW + "PROFESSOR AVALON:" + END + "  Well, as a professor at the BTRS, it is my duty to assist trainers like yourself in their journey to becoming the very best. As such, I have three starter Pokémon that I can offer to you. I have a Charmander, a Squirtle, and a Bulbasaur. They are all very capable and strong Pokémon, and I have no doubt that they will serve you well on your journey. So, which one do you choose?\n")
            time.sleep(10)
            print("\nPRESS ENTER TO CONTINUE...")
            if efeg == " ":
                choose_starter()
            else: 
                print("Unknown command, try again!")
                time.sleep(3)
                clear_screen()
                town("new")
  
  elif state == "new" and mode == "normal":
    met_lucy = True
    print("\n In the town you can get quests from Lucy for rewards and also visit the Bro Town Research Institute.")
    time.sleep(3)
    print("\n In front of you stands a building with a sign reading " + YELLOW + '"BTRS: Bro Town Research Institute"' + END + "\n \n") 
    time.sleep(3)
    print("Could this be where you obtain your starter Pokémon?\n\n")
    time.sleep(4)
    print("Suddenly, you feel a gentle tap on your shoulder, and as you turn around, you see a towering figure standing before you.\n\n")
    time.sleep(4)
    print("BIG GUY: Ah, hello there! Welcome to the Bro Town Research Institute. My name is " + YELLOW + "Professor Avalon." + END + " I specialize in the study of Pokémon. I have some Pokémon inside for you.\n\n")
    time.sleep(4)
    print("\nYou follow Professor Avalon into the building...")
    input("Enter to continue...")
    choose_starter()

  else:
     print(PURPLE, "LUCY: ", "Welcome back! My quest shop is now open if you wanna take a look.")
     choices("quest")          

def start():
    size = os.get_terminal_size().columns
    global mode
    if size >= 120:
      print(BLUE + r"""
██████╗  ██████╗ ██╗  ██╗███████╗███╗   ███╗ ██████╗ ███╗   ██╗    ██████╗ ██████╗  ██████╗ ███████╗    ██████╗ ██╗
██╔══██╗██╔═══██╗██║ ██╔╝██╔════╝████╗ ████║██╔═══██╗████╗  ██║    ██╔══██╗██╔══██╗██╔═══██╗██╔════╝    ╚════██╗██║
██████╔╝██║   ██║█████╔╝ █████╗  ██╔████╔██║██║   ██║██╔██╗ ██║    ██████╔╝██████╔╝██║   ██║███████╗     █████╔╝██║
██╔═══╝ ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╔╝██║██║   ██║██║╚██╗██║    ██╔══██╗██╔══██╗██║   ██║╚════██║    ██╔═══╝ ╚═╝
██║     ╚██████╔╝██║  ██╗███████╗██║ ╚═╝ ██║╚██████╔╝██║ ╚████║    ██████╔╝██║  ██║╚██████╔╝███████║    ███████╗██╗
╚═╝      ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝    ╚══════╝╚═╝                                                                                                               
      """ + END)

    elif size < 120:
      print(BLUE + r"""
██████╗  ██████╗ ██╗  ██╗███████╗███╗   ███╗ ██████╗ ███╗   ██╗    
██╔══██╗██╔═══██╗██║ ██╔╝██╔════╝████╗ ████║██╔═══██╗████╗  ██║    
██████╔╝██║   ██║█████╔╝ █████╗  ██╔████╔██║██║   ██║██╔██╗ ██║    
██╔═══╝ ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╔╝██║██║   ██║██║╚██╗██║    
██║     ╚██████╔╝██║  ██╗███████╗██║ ╚═╝ ██║╚██████╔╝██║ ╚████║    
╚═╝      ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝    
                                                                      
██████╗ ██████╗  ██████╗ ███████╗    ██████╗ ██╗                   
██╔══██╗██╔══██╗██╔═══██╗██╔════╝    ╚════██╗██║                   
██████╔╝██████╔╝██║   ██║███████╗     █████╔╝██║                   
██╔══██╗██╔══██╗██║   ██║╚════██║    ██╔═══╝ ╚═╝                   
██████╔╝██║  ██║╚██████╔╝███████║    ███████╗██╗                   
╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝    ╚══════╝╚═╝                                                                                     
    """ + END)
  
    print(introduction_text)
    time.sleep(2)
    start_input = input("\n(1) Start Game in " + BOLD + "Nomal Mode (Less dialogue and more EPIC GAMING)" + END + " \n(2) Start Game in " + BOLD + "Story Mode (More dialogue and lore)" + END + " \n(3) Exit\n")

    if start_input == "1":
      mode = "normal"
      fake_main()

    elif start_input == "2":
      mode = "dialogue"
      brody_intro()

    elif start_input == "3":
       exit_game()

    else:
       print("\nInvalid input, please try again.")
       clear_screen()
       start()

def brody_intro():
  print(bro_town_intro)
  time.sleep(5)
  print(bro_town_intro_2)
  time.sleep(3)
  ch1 = input("\n(1) Approach the stranger\n")

  if ch1 == "1":
    print("\n")
    print(brody_introduction)
    time.sleep(6)
    print("\n")
    print(brody_introduction_2)
    time.sleep(6)
    ch2 = input("\n(1) 'Im new to this whole trainer thing. Do you have any advice for how I can become the best?' \n(2) Battle Brody\n")

    if ch2 == "1":
      print("\n")
      print(brody_advice)
      time.sleep(6)
      print("\n\n")
      print(brody_advice_2)
      time.sleep(6)
      print("\nYOU: Thanks, I'll keep this in mind.")
      time.sleep(3)
      brody_gift()

    if ch2 == "2": 
      print("\n" + CYAN + BOLD + UNDERLINE + "BRODY:" + END + " Man, how are you supposed to battle me? You dont even have any Pokémons!\n")
      time.sleep(3)
      brody_gift()

    else:
      print("\nInvalid input, please try again.")
      brody_intro()

  else:
    print("\nInvalid input. Please try again.")
    brody_intro()
    
def brody_gift():
  print(brody_gift_text)
  time.sleep(4)
  print(brody_gift_text_2)
  time.sleep(3)
  print("\n")
  add_item("POKEBALL", 15)
  add_item("BRO COIN", 50)
  time.sleep(3)
  print("\n" + CYAN + BOLD + UNDERLINE + "BRODY:" + END + " Anyways, I should really get going. See you later... uhm... What was your name again?\n")
  trainer_name = input("YOUR NAME: " + PURPLE + END)
  time.sleep(3)
  fake_main()

def gym(state):
    if state == "brody":
        clear_screen()
        print("You enter the gym...")
        time.sleep(3)
        print("\n" + CYAN + BOLD + UNDERLINE + "BRODY:" + END + " Hey " + trainer_name + ", you're back already! Are you ready to take on the strongest trainer in town? I must warn you, I'm not one to go easy on my opponents. But don't worry, I'll make sure to give you a fair fight. Though you wont win ;)\n")
        time.sleep(6)
        choice = input("(1) Let's do it! \n(2) We'll se about that... \n(3) Im not ready yet.\n")
        if choice == "1" or choice == "2":
            #start battle with Brody
            print("\nAlright, see you in the battle arena!")
            time.sleep(3)
            results = battle("Brody")
            if results == "win":
                clear_screen()
                print(CYAN + BOLD + UNDERLINE + "BRODY:" + END + " Ah man, I can't believe I lost. But don't get too cocky, I'll be back to take you down next time!")
                time.sleep(5)
                print("\n\nYOU GOT REWARDED 100¥ AND 10 POKEBALLS\n\n")
                add_item("BRO COIN", 100)
                add_item("POKEBALL", 10)
                time.sleep(5)
                main(met_lucy)

            else:
                clear_screen()
                print(CYAN + BOLD + UNDERLINE + "BRODY:" + END + " Ha! I told you I was the best! Better luck next time, " + trainer_name + ".")
                time.sleep(6)
                main(met_lucy)

        elif choice == "3":
            print("\n\nYou go back home...")
            time.sleep(4)
            main(met_lucy)


    else:
        print("The gym is currently under development (Klaga på Askel), come back later!")
        time.sleep(4)
        return

def calc_pokemon_value(pokemon, rarity):
  # Get the spawn rate of the Pokémon from the pokemon_data dictionary
  spawn_rate = pokemon_data[pokemon]["spawn_rate"]

  # Use the spawn rate to determine the value of the Pokémon
  if spawn_rate < 0.1:
    # Very rare Pokémon are worth the most
    return 400, "EXTREMELY RARE"
  elif spawn_rate < 0.5:
    # Rare Pokémon are worth less than very rare ones
    return 80, "PRETTY RARE"
  elif spawn_rate < 0.7:
    # Uncommon
    return 50, "UNCOMMON"
  else:
    # Common Pokémon are worth the least
    return 20, "COMMON"

def calc_rare_pokemon_value(pokemon, rarity):
  # Get the spawn rate of the Pokémon from the pokemon_data dictionary
  spawn_rate = pokemon_data[pokemon]["spawn_rate"]
  #name = pokemon_data[pokemon]["name"]

  # Use the spawn rate to determine the value of the Pokémon
  if spawn_rate < 0.1:
    # Very rare Pokémon are worth the most
    return 1000, "VERY RARE"
  elif spawn_rate < 0.5:
    # Rare Pokémon are worth less than very rare ones
    return 400, "PRETTY RARE"
  elif spawn_rate < 0.7:
    # Uncommon
    return 200, "UNCOMMON"
  #elif name == "Mewtwo" or name == "LAPRAS!" or name == "Christians_Mom":
    #return 2000, "INSANELY RARE!"
  else:
    # Common Pokémon are worth the least
    return 100, "COMMON"

def pokemon_shop():
  clear_screen()
  print(PURPLE + "SHOP OWNER: " + END + "Ah, a seeker of the rarest, \nWelcome to my shop, where the most exclusive Pokémon of the region are sold.")
  print("\nPokémon for sale:\n")
  print("BRO COINS: " + YELLOW + str(inventory.get("BRO COIN", 0)) + "¥" + END + "\n")
  # Get a list of all the keys in the pokemon_data dictionary
  pokemon_list = list(pokemon_data.keys())

  # Shuffle the list of Pokemon
  random.shuffle(pokemon_list)

  # Filter the list of Pokemon to only include those with a spawn rate of 0.35 or lower
  pokemon_list = [p for p in pokemon_list if pokemon_data[p]["spawn_rate"] <= 0.35]

  # Get a list of 5 random Pokemon in the shuffled list
  pokemon_for_sale = random.sample(pokemon_list, 5)

  pokemon_number = 1
  value = 0
  rarity = ""

  for pokemon in pokemon_for_sale:
    value, rarity = calc_rare_pokemon_value(pokemon, rarity)
    print("(" + str(pokemon_number) + ") " + PURPLE + pokemon + END + " " + str(value) + "¥, " + rarity)
    pokemon_number += 1

  print("(e) Exit")

  choice = input("")

  try:
    choice = int(choice)

    if choice == 1:
      if inventory.get("BRO COIN", 0) >= value:
        # Accept
        inventory["BRO COIN"] -= value
        pokemon = pokemon_for_sale[0]
        add_pokemon(pokemon)
        print("")
        input("\nPress enter to continue...\n")
        pokemon_shop()
      else:
        print("\nNot enough Bro Coins!")
        input("Press enter to continue...")
        pokemon_shop()

    elif choice == 2:
      if inventory.get("BRO COIN", 0) >= value:
        # Accept
        inventory["BRO COIN"] -= value
        pokemon = pokemon_for_sale[1]
        add_pokemon(pokemon)
        print("")
        input("\nPress enter to continue...\n")
        pokemon_shop()

    elif choice == 3:
      if inventory.get("BRO COIN", 0) >= value:
        # Accept
        inventory["BRO COIN"] -= value
        pokemon = pokemon_for_sale[2]
        add_pokemon(pokemon)
        print("")
        input("\nPress enter to continue...\n")
        pokemon_shop()

    elif choice == 4:
      if inventory.get("BRO COIN", 0) >= value:
        # Accept
        inventory["BRO COIN"] -= value
        pokemon = pokemon_for_sale[3]
        add_pokemon(pokemon)
        print("")
        input("\nPress enter to continue...\n")
        pokemon_shop()
    
    elif choice == 5:
      if inventory.get("BRO COIN", 0) >= value:
        # Accept
        inventory["BRO COIN"] -= value
        pokemon = pokemon_for_sale[4]
        add_pokemon(pokemon)   
        print("")
        input("\nPress enter to continue...\n")
        pokemon_shop() 
    
    else:
      print("Unrecognised input...\nPress enter to continue...\n")
      input("")
      pokemon_shop()

  except ValueError as e:
    print(e)
    shop()

  pokemon_shop()   

def shop():
  clear_screen()
  print(shop_owner)
  print("\n")
  print("BRO COINS: " + YELLOW + str(inventory.get("BRO COIN", 0)) + "¥" + END)
  print("POKEBALLS: " + str(inventory.get("POKEBALL", 0)))

  if not pokemon_inv:
      pokemon_list = "POKÈMON: None"
      print(pokemon_list)
      print("\n")

  else:
      # Print the names of all the Pokémon in the player's inventory on the same line, separated by a comma
      pokemon_list = "POKÉMON: "
      for pokemon in pokemon_inv:
          pokemon_list += pokemon + ", "
      
      # Remove the final comma and space from the list
      pokemon_list = pokemon_list[:-2]
      print(pokemon_list)
      print("\n")

  buy_input = input("\n(1) Pokeballs " + YELLOW + "10¥" + END + "\n(2) Berries " + YELLOW + "45¥" + END + "\n(3) Sell a Pokémon \n(4) Enter the special Pokémon shop - " + PURPLE + "BUY RARE POKÉMON" + END + "\n(5) Exit Shop \n")

  if buy_input == "1":
    # check Bro Coins 10
    if inventory.get("BRO COIN", 0) >= 10:
      # Accept
      inventory["BRO COIN"] -= 10
      add_item("POKEBALL", 1)
      print("You bough 1 Pokeball")
      time.sleep(1)
      shop()
    else:
      print("You dont have enough Bro Coins!")
      time.sleep(1)
      shop()
  
  elif buy_input == "2":
    # check Bro Coins 50
    if inventory.get("BRO COIN", 0) >= 45:
      # Accept
      inventory["BRO COIN"] -= 45
      add_item("BERRIE", 1)
      print("You bough 1 Berrie")
      time.sleep(1)
      shop()
    else:
      print("You dont have enough Bro Coins!")
      time.sleep(1)
      shop()

  elif buy_input == "3":
    pokemon_number = 1
    value = 0
    rarity = ""

    print("\nWhich Pokémon do you wish to sell?\n")
    for pokemon in pokemon_inv:
        value, rarity = calc_pokemon_value(pokemon, rarity)
        pokemon_health = pokemon_inv[pokemon][0]
        pokemon_max_health = pokemon_data[pokemon]["max_health"]
        print("(" + str(pokemon_number) + ") " + pokemon + " " + str(pokemon_health) + "/" + str(pokemon_max_health) + " HP. -- ESTIMATED VALUE: " + YELLOW + str(value) + "¥" + END)
        pokemon_number += 1

    choice = input("")
    choice = int(choice)

    pokemon = list(pokemon_inv.keys())[choice - 1]
    choice = input("\nAre you sure you want to sell " + pokemon + "? (y/n)\n")

    if choice == "y" or choice == "Y" or choice == "yes" or choice == "Yes":
      # Sell pokemon
      # Get value of pokemon
      value = 0
      rarity = ""

      value, rarity = calc_pokemon_value(pokemon, rarity)
      print("\nYour " + pokemon + " was determined to be " + RED + UNDERLINE + rarity + END + ".\nEstimated value: " + str(value) + " Bro Coins.")
      time.sleep(1)
      pokemon_data[pokemon]["num_of"] -= 1
      del pokemon_inv[pokemon]
      add_item("BRO COIN", value)
      waiting = input("\nPress enter...")
      shop()

    elif choice == "n" or choice == "N" or choice == "no" or choice == "No":
      # Dont sell
      print("\n Ok, not selling Pokémon...")
      time.sleep(2)
      shop()

  elif buy_input == "4":
    pokemon_shop()

  elif buy_input == "5":
    main(met_lucy)

  else:
    print("Unrecognised input...")
    input("Press enter to continue...")
    shop()
      
def fake_main():
  
  if mode == "normal":
    add_item("POKEBALL", 15)
    add_item("BRO COIN", 50)
    trainer_name = input("Enter your name: ")

  # Clear the screen
  clear_screen()
 
  print("Welcome to your rented apartment in Bro Town! This is where you'll be keeping all of your Pokémon as you journey through the region. \nFrom here, you can access any location in the town and continue on your journey as a Pokémon trainer... \n")
  time.sleep(7)
  clear_screen()
  main(met_lucy)

def look_for_pokemon(location):
  choices("pokemon", met_lucy)

def poi(location, state):
  if state == "new":
    if location == "Redwood" or location == "redwood":
        clear_screen()
        print("After hours of searching you finally found your way to the popular Pokémon catching spot 'Redwood Forest'")
        time.sleep(5)
        look_for_pokemon(location)

    elif location == "Sapphire" or location == "sapphire":
        clear_screen()
        print("You step onto the shore of 'Sapphire Lagoon'. You are amazed by the fresh air and wonderful view. This place gotta have some rare " + BLUE + "Water type Pokémon" + END)
        time.sleep(5)
        look_for_pokemon(location)

    else:
        clear_screen()
        print("Something went wrong...")
        time.sleep(5)
        return
  else:
    if location == "Redwood" or location == "redwood":
      print("\n\nYou grab some Pokeballs and venture into the deep forest...")
      time.sleep(3)
      look_for_pokemon(location)
    
    elif location == "Sapphire" or location == "sapphire":
      print("\n\nYou grab some Pokeballs and start walking...")
      time.sleep(3)
      look_for_pokemon(location)

def pokedex():
  clear_screen()
  print(BOLD + CYAN + "Welcome to your Pokédex. Here you can view detailed information on all caught Pokemon.\n" + END)
  i = 1
  for pokemon in pokemon_data:
    # Player hasnt found pokemon
    if pokemon_data[pokemon]["found"] == 0:
      print(str(i) + ")" + "-Unkown-")
    
    # player has found pokemon
    elif pokemon_data[pokemon]["found"] == 1:
      print(str(i) + ")" + RED + pokemon + END)
    i += 1

  choice = input("\nWhich Pokemon would you like to view? (type 'e' to exit) \n")
  if choice == "e":
    main(met_lucy)
  pokemon_name = list(pokemon_data.keys())[int(choice)-1]
  pokemon_data1 = pokemon_data[pokemon_name]
  max_health = pokemon_data1["max_health"]
  pokemon_type = pokemon_data1["type"]
  spawn_rate = pokemon_data1["spawn_rate"]
  found = pokemon_data1["found"]
  attack_damage = pokemon_data1["attack_damage"]

  if found == 1:
    print(f"\nName: {pokemon_name}\nMax Health: {RED}{max_health}{END}\nType: {RED if pokemon_type in ['Fire', 'Fighting'] else BLUE if pokemon_type == 'Water' else GREEN if pokemon_type in ['Bug', 'Grass'] else PURPLE if pokemon_type in ['Poison', 'Ghost', 'Psychic'] else YELLOW if pokemon_type == 'Electric' else BOLD if pokemon_type in ['Normal', 'Ground', 'Rock'] else ''}{pokemon_type}{END}\nSpawn Rate: {RED}{spawn_rate}{END}\nHas been caught: {RED}{'Yes' if found == 1 else 'No'}{END}\nAttack Damage: {RED}{attack_damage}{END}\n")

    input("\nPress enter to continue...")
    pokedex()
  
  elif found == 0:
    print("\nYou havent discovered this Pokémon yet.")
    input("Press enter to continue...")
    pokedex()

class Quest:
    
    def __init__(self, title, description, rewards):
        self.title = title
        self.description = description
        self.rewards = rewards

    def __str__(self):
        return BOLD + CYAN + self.title + END + BOLD + "\nRewards: " + END + ', '.join(self.rewards) + "\n\n" + self.description

scavenger_hunt = Quest("Scavenger Hunt", "Lucy lost a valuable item and needs your help finding it. You will be rewarded with a special item or battle opportunity upon success.", ["Special item", "Battle Opportunity"])
pokemon_contest = Quest("Pokemon Contest", "Lucy is preparing for the yearly Pokemon contest in Bro Town. Help her perfect her skills by battling her.", ["Cash prize", "Special Item"])
trade = Quest("Trade", "Lucy is seeking exotic Pokemon and is willing to trade valuable items and Pokemon in return for your help in obtaining them.", ["Valuable Item", "Rare Pokemon"])
explore_ruins = Quest("Exploring the Ruins", "Lucy has heard rumors of ancient ruins in the nearby mountains, and she believes that there may be rare and powerful Pokemon hidden inside.", ["Exotic Pokemon"])
lost_treasure = Quest("The Lost Treasure", "Lucy has heard a legend about a legendary treasure hidden somewhere in Redwood Forest.", ["Valuables"])
pokemon_rescue = Quest("Pokemon Rescue", "Lucy has heard that a group of Pokemon are trapped in a nearby cave and need help getting out.", ["Pokemon", "Valuables"])
fairy_garden = Quest("The Fairy Garden", "Lucy has heard rumors of a secret garden where rare Fairy-type Pokemon can be found. Lucy wants you to find a list of Pokémons from there.", ["Fairy Type Pokemon"])

quests = [scavenger_hunt, pokemon_contest, trade, explore_ruins, lost_treasure, pokemon_rescue, fairy_garden]

def play_quest(quest_title):
   clear_screen()
   quest_title.lower()
   print("You are now helping Lucy with " + RED + quest_title.title() + END + "!")

   if quest_title == "scavenger hunt":
      # Scavenger Hunt

      # Define a list of potential locations where the item could be found
      locations = ["redwood forest", "sapphire lagoon", "bro town center", "the ruins", "the fairy garden"]
      locations1 = [location.upper() for location in locations]

      while True:
          # Randomly select a location for the item to be found
          item_location = random.choice(locations)

          item_locations = ["under a shiny rock.", "behind a huge tree.", "in a dark scary cave", "at the bottom of a deep lake.", "on top of a snowy mountain.", "inside an abandoned building.", "behind a waterfall.", "on a secluded island."]

          random_location = random.choice(item_locations)

          print("\nLucy lost a valuable item and needs your help finding it.")
          print("\nYou will be rewarded with a special item or battle opportunity upon success.")
          time.sleep(2.5)

          # Ask the player where they would like to search for the item
          while True:
              print(RED + "\nLocations to search: " + END + ", ".join(locations1))
              player_choice = input("\nWhere would you like to search for the item?\n")
              
              if player_choice.lower() in locations:
                  if player_choice.lower() == item_location:
                      print("\nLooking for the item...\n")
                      time.sleep(2)
                      print("Congratulations! You have found the item in " + player_choice.title() + " " + random_location)
                      time.sleep(3)
                      print("\nYou have been rewarded with a special item!")
                      add_item("GOLDEN BRO COIN", 1)
                      input("Press enter to continue...")
                      quest_shop()
                      break
                  else:
                      print("\nSorry, the item is not at that location.")
              else:
                  print("\nInvalid location. Please enter a valid location from the list")


   elif quest_title == "pokemon contest":
      # Pokemon Contest
      print("This quest is under development. (Klaga på Askel) Come back later")
      input("Press enter to continue...")
      quest_shop()

   elif quest_title == "trade":
      # Trade
        print("This quest is under development. (Klaga på Askel) Come back later")
        input("Press enter to continue...")
        quest_shop()

   elif quest_title == "exploring the ruins":
      # Exploring the Ruins
      print("This quest is under development. (Klaga på Askel) Come back later")
      input("Press enter to continue...")
      quest_shop()

   elif quest_title == "the lost treasure":
      # The lost Treasure
        print("This quest is under development. (Klaga på Askel) Come back later")
        input("Press enter to continue...")
        quest_shop()

   elif quest_title == "pokemon rescue":
      # Pokemon Rescue
        print("This quest is under development. (Klaga på Askel) Come back later")
        input("Press enter to continue...")
        quest_shop()

   elif quest_title == "the fairy garden":
      # The Fairy Garden
          print("This quest is under development. (Klaga på Askel) Come back later")
          input("Press enter to continue...")
          quest_shop()

def gen_quest():
  #Generate quests
  random_quests = random.sample(quests, 3)
  for quest in random_quests:
        quest_output = quest
        if quest_output is not None:
            print(quest_output)
            print("\n"*2)
  return random_quests

def quest_shop():
   
   clear_screen()
   print(YELLOW + BOLD + "LUCY'S QUEST BOARD\n" + END)
   lucy_talk = [CYAN, "LUCY: Welcome to my quest shop, adventurer! Are you ready for some exciting challenges and fun adventures with your Pokemon?", "LUCY: I've got all sorts of quests and tasks that will test your skills and help you become a better trainer.", "LUCY: Looking for a way to earn some rare items? I've got just the quest for you!", "LUCY: I'm always updating my quest shop with new and exciting challenges, so be sure to check back often for new quests and adventures!", END]
   # print random from lucy_talk
   print(CYAN + random.choice(lucy_talk) + END)
   input("Press enter...")
   clear_screen()
   print(YELLOW + BOLD + "LUCY'S QUEST BOARD\n" + END)
   lucy_talk = [CYAN, "LUCY: Welcome to my quest shop, adventurer! Are you ready for some exciting challenges and fun adventures with your Pokemon?", "LUCY: I've got all sorts of quests and tasks that will test your skills and help you become a better trainer.", "LUCY: Looking for a way to earn some rare items? I've got just the quest for you!", "LUCY: I'm always updating my quest shop with new and exciting challenges, so be sure to check back often for new quests and adventures!", END]
   quests = gen_quest()
   choice = input("(1) Help lucy with a quest. \n(2) Exit\n")
   if choice == "1":
    while True:
        choice2 = input("\nI want to help Lucy with [Quest Name]: ")
        for quest in quests:
            if choice2.lower() == quest.title.lower():
                print("You have selected:", quest.title)
                # Perform actions for the selected quest
                quest_title = quest.title.lower()
                play_quest(quest_title)
                break
        else:
            print("\nQuest not found. Please enter a valid quest title. (press q to exit)")
        if choice2.lower() == quest.title.lower():
            break
        if choice2.lower() == "q":
           quest_shop()
           break

   elif choice == "2": 
      main(met_lucy)
   
   else:
      input("Invalid input. Press enter...")
      quest_shop()

def btrs():
  print(YELLOW + "PROFFESOR AVALON: " + END + "Welcome to my facility! What brings you here?\n")
  input("\n\nIn the future you will be able to scan your Pokémon here and also level it up. Come back later. (Säg till Askel att skynda sig annars dör hans familj.)")

def choices(location, met_lucy):
  if location == "Apartment" and brody_fight == False and met_lucy == False:
    print("(1) Go to the Shop")
    print("(2) Open Pokédex")
    print("(3) Go to Town - " + CYAN + "CLAIM STARTER POKÉMON" + END)
    print("(4) Open Inventory")
    print("(5) Exit Game - " + BRIGHT_RED + "PROGRESS WILL BE LOST" + END)
    #print("(6) Try to seduce Lucy (make love to her)" + BRIGHT_RED + "If successfull Good feels will go up")
    choice = input("\n")

    if choice == "1":
      shop()
      
    elif choice == "2":
      pokedex()
      
    elif choice == "3":
      town("new")

    elif choice == "4":
       clear_screen()
       print("Inventory:")
       print("Item".ljust(20) + "Count".rjust(10))
       for item, count in inventory.items():
          print(item.ljust(20) + str(count).rjust(10))
       input("Press enter to continue...")  
       main(met_lucy)
      
    elif choice == "5":
      exit_game()
    #elif choice == "6":
      #lucy()
    
    else:
       print("\nUnrecognised input...")
       input("Press enter to continue...")
       main(met_lucy)

    return

  elif location == "Apartment" and brody_fight == False and met_lucy == True:
    print("(1) Go to the Shop")
    print("(2) Go to the Gym - " + CYAN + BOLD + UNDERLINE + "BRODY" + END + " BATTLE")
    print("(3) Go to Town - " + "UNDER DEVELOPMENT (Klaga på Askel)")
    print("(4) Open Inventory")
    print("(5) Open Pokédex")
    print("(6) Go to Redwood Forest - " + GREEN + "GRASS TYPE BOOST" + END)
    print("(7) Exit Game - " + BRIGHT_RED + "PROGRESS WILL BE LOST" + END)
    choice = input("\n")

    if choice == "1":
        shop()

    elif choice == "2":
        gym("brody")

    elif choice == "3":
        town("")

    elif choice == "4":
       clear_screen()
       print("Inventory:")
       print("Item".ljust(20) + "Count".rjust(10))
       for item, count in inventory.items():
          print(item.ljust(20) + str(count).rjust(10))
       input("Press enter to continue...")  
       main(met_lucy)
        

    elif choice == "5":
      pokedex()

    elif choice == "6":
        poi("Redwood", "new")

    elif choice == "7":
      exit_game()
    
    else:
       print("\nUnrecognised input...")
       input("Press enter to continue...")
       main(met_lucy)

    return

  elif location == "Apartment" and brody_fight == True and met_lucy == True:
    print("(1) Go to the Shop")
    print("(2) Go to the Gym")
    print("(3) Go to Town")
    print("(4) Open Inventory")
    print("(5) Open Pokédex")
    print("(5) Go to Redwood Forest - " + GREEN + "GRASS TYPE BOOST" + END)
    print("(6) Go to Sapphire Lagoon - " + BLUE + "WATER TYPE BOOST" + END)
    print("(7) Exit Game - " + BRIGHT_RED + "PROGRESS WILL BE LOST" + END)
    choice = input("\n")

    if choice == "1":
      shop()

    elif choice == "2":
      gym("")

    elif choice == "3":
      town("")

    elif choice == "4":
       clear_screen()
       print("Inventory:")
       print("Item".ljust(20) + "Count".rjust(10))
       for item, count in inventory.items():
          print(item.ljust(20) + str(count).rjust(10))
       input("Press enter to continue...")  
       main(met_lucy)

    elif choice == "5":
      poi("Redwood", "")

    elif choice == "6":
      poi("Sapphire", "")

    elif choice == "7":
      exit_game()
      
    return

  elif location == "pokemon":
    clear_screen()
    continue_walking = True
    pokeball_num = inventory["POKEBALL"]
    
    while(continue_walking):
      print("\nPokeballs: " + str(pokeball_num))
      choice = input("\n\n(1) Continue Walking\n(2) Leave the area\n")

      if choice == "1":
        # 40% chance to find pokemon
        random_num = random.randint(1, 100)

        if random_num in range(1, 41):
          # spawn pokemon
          strings = ["\n\nWalking...", "\n\nWalking through some bushes...", "\n\nJumping over some stones...", "\n\nEnjoying the scenery...", "\n\nWalking along the river...", "\n\nNavigating through tall grass...", "\n\nWalking along a dirt path...", "\n\nTaking in the fresh air...", "\n\nClimbing up a small hill for a better view...", "\n\nClimbing over a fallen tree...", "\n\nNoticing a small animal scurrying across your path..."]
          print(random.choice(strings))
          time.sleep(1)
          print("\n\n")
          pokemon = spawn_pokemon()
          print("A wild " + pokemon + " has appeared!")
          time.sleep(1)

          caught = False
          while not caught:
            choice1 = input("\n(1) Catch it!\n(2) Leave\n")

            if choice1 == "1":
              # check if enough pokeballs
              if pokeball_num > 0:
                # enough pokeballs
                print("\n\nYou throw a pokeball at it!")
                time.sleep(2)
                # 50% chance of catching
                random1 = random.randint(1, 100)

                if random1 in range(1, 51):
                  # Pokémon was caught
                  print("\n\nYou caught the "+ pokemon + "!")
                  inventory["POKEBALL"] -= 1
                  pokeball_num = inventory["POKEBALL"]
                  add_pokemon(pokemon)
                  time.sleep(1.5)
                  clear_screen()
                  caught = True
                else:
                  # pokemon wasn't caught
                  inventory["POKEBALL"] -= 1
                  pokeball_num = inventory["POKEBALL"]
                  print("\n\nThe Pokémon broke free! You have " + str(pokeball_num) + " pokeballs left.")

              else:
                # not enough pokeballs
                print("\n\nYou don't have any more pokeballs!")
                time.sleep(2)
                caught = True

            elif choice1 == "2":
              print("\n\nYou leave the " + pokemon + " alone.")
              caught = True
              time.sleep(1)
              clear_screen()

        else:
          # didn't find pokemon - 60% chance
          random_num1 = random.randint(1, 100)

          if random_num1 in range(1, 91):
            strings1 = ["\n\nNope, nothing here...", "\n\nAgh, no Pokémon here..."]
            print(random.choice(strings1))
            time.sleep(1)
            clear_screen()

          else:
            print("\nYou see a figure standing in the distance. A chill runs down you spine.\n")
            choice = input("(1) Approach the stranger\n(2) Cowardly run away\n")

            if choice == "1":
              print("\n You confront the stranger...\n")
              time.sleep(1)
          
              # Get names
              names = ['Jacob', 'Michael', 'Joshua', 'Matthew', 'Ethan', 'Andrew', 'Daniel', 'Anthony', 'Christopher', 
              'Joseph', 'William', 'Alexander', 'Ryan', 'David', 'Nicholas', 'Emily', 'Madison', 'Ashley', 'Sarah', 'Jessica']

              # Choose random name
              name = random.choice(names)

              interactions = [
                RED+name.upper()+END+": Hey, my name is "+name+", you up for a battle?",
                YELLOW+name.upper()+END+": What's up? My name is "+name+", you interested in a battle?",
                BLUE+name.upper()+END+": Greetings, I'm "+name+"! Wanna battle?",
                CYAN+name.upper()+END+": Yo, "+name+" here. Care for a battle?",
                GREEN+name.upper()+END+": Hello, I'm "+name+"! Up for a Pokémon battle?",
                PURPLE+name.upper()+END+": Well hello there! My name is "+name+", but you can call me the Pokémon master. You up for a little competition?",
                ORANGE+name.upper()+END+": Hey, I'm "+name+"! I'm on a quest to become the very best like no one ever was. Wanna join me in a battle?",
                MAGENTA+name.upper()+END+": Greetings, I'm "+name+"! I'm always looking for new trainers to defeat. Wanna be my next victim?",
                RED+name.upper()+END+": Howdy, I'm "+name+"! I'm always on the lookout for some good competition. You think you're up for a battle?",
                BLUE+name.upper()+END+": Yo, "+name+" at your service! I'm always ready for a battle. You think you can handle me?"
              ]

              lost = [
                RED+name.upper()+END+": You were no match for me!",
                RED+name.upper()+END+": Haha, I'm the winner!",
                RED+name.upper()+END+": Greetings, I just won, wanna try again?",
                RED+name.upper()+END+": Yo, you lost to me",
                RED+name.upper()+END+": I just defeated you in a Pokémon battle",
                RED+name.upper()+END+": I'm the master of this battle",
                RED+name.upper()+END+": I'm the very best like no one ever was and you just proved it",
                RED+name.upper()+END+": You were a worthy opponent but I'm the victor",
                RED+name.upper()+END+": Looks like I'm the champion of this battle",
                RED+name.upper()+END+": I just won and I'm ready for another battle"
              ]

              won = [
                BLUE+name.upper()+END+": I can't believe I lost!",
                BLUE+name.upper()+END+": Wow, you're really good!",
                BLUE+name.upper()+END+": Yo, I lost but... I'LL BE BACK!",
                BLUE+name.upper()+END+": I lost but it was a fairly good battle",
                BLUE+name.upper()+END+": I'll get better and beat you next time",
                BLUE+name.upper()+END+": You were the better trainer this time...",
              ]

              print(random.choice(interactions))
              input("\nPress enter to continue...\n")

              # Start battle with name
              won_or_lost = battle(name)

              if won_or_lost == "win":
                print("")
                print(random.choice(won))
                time.sleep(1.5)

              elif won_or_lost == "lose":
                print("")
                print(random.choice(lost))
                time.sleep(1.5)
            
            elif choice == "2":
              print("\nYou run away and continue looking for Pokémon.")
              time.sleep(1.5)
              clear_screen()

      elif choice == "2":
        continue_walking = False

    print("\n\nLeaving the area...")
    time.sleep(4)
    main(met_lucy)

  elif location == "quest":
    print("(1) Enter ", PURPLE, "LUCY'S QUEST SHOP", END)
    print("(2) Go to ", YELLOW, "Bro Town Research Institute", END)
    print("(3) Exit Town")
    choice = input("\n")

    if choice == "1":
       quest_shop()

    elif choice == "2":
       btrs()

    elif choice == "3":
       main(met_lucy)

    else:
       print("\nUnrecognised input.")
       input("Press enter to continue...")
       town("")

    return

  else: 
    clear_screen()
    print("Something went wrong...")
    time.sleep(3)
    return

def main(met_lucy):
  clear_screen()
  stats("Apartment")
  choices("Apartment", met_lucy)

start()