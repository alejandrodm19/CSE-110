# """"""""
# File: Adventure_game1.py
# Author: Alejandro Malvacias

# Assignment 05 and 06
# """"""""

#First statement, and introduction to the game
print("Welcome to my adventure game :D") 
first_choice = input("Do you want to play an adventure game? YES or NO: ")
#Main section
if first_choice.lower() == "yes":
    match_flashlight = input("You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. Which one do you want to pick up? ")

#Match Alternative

    if match_flashlight.lower() == "match":
        run_hide = input("You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out. Do you want to RUN or HIDE behind a tree? ")
        if run_hide.lower() == "run":
            print("You chose 'RUN.' The bear has seen you.")
            askforhelp_keepitrunning = input("You hear a helicopter in the sky, but you're not sure if it's near. You can ASK FOR HELP or KEEP RUNNING, but your life in the game depends on your decisions. ")
            if askforhelp_keepitrunning.lower() == "ask for help":
                print("You choose 'ASK FOR HELP.' The helicopter saw you and is coming to help.")
            elif askforhelp_keepitrunning.lower() == "keep running":
                print("You choose 'KEEP RUNNING.' You lose! The bear eats you. End of the game.")
            else:
                print("Invalid option. Please try again.")
        elif run_hide.lower() == "hide":
            print("You chose 'HIDE.' You made a wise decision, and the bear has decided to leave.")
            askforhelp_keepitrunning = input("You hear a helicopter near by, and you can use the match to signal it. However, the bear may see you. You can also keep running. Do you want to ASK FOR HELP or KEEP RUNNING?")
            if askforhelp_keepitrunning.lower() == "ask for help":
                print("You choose 'ASK FOR HELP.' The helicopter saw you and is coming to help.")
            elif askforhelp_keepitrunning.lower() == "keep running":
                print("You choose 'KEEP RUNNING.' You lose! The bear eats you. End of the game.")
            else:
                print("Invalid option. please try again.")
        else:
            print("Invalid option. Please try again.")

#Flashlight alternative

    elif match_flashlight.lower() == "flashlight":
        follow_look = input("You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side. Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise? ")
        if follow_look.lower() == "follow":
            print("You chose 'FOLLOW.' You follow the path and make it back home, but not before seeing an angry grizzly bear in the distance.")
        elif follow_look.lower() == "look":
            print("You chose 'LOOK.' You find an enraged grizzly bear among the trees.")
            facethebear_or_staycalm = input("Now that you see there is an angry bear, you have two more options, the first one is 'FACE THE BEAR' and go even the bear is there, the other one is 'STAY CALM' and wait that the bear go out of the woods ")
            if facethebear_or_staycalm.lower() == 'stay calm':
                print("You choose 'STAY CALM' you are safe! the bear going to keep his way and dont going to hurt you")
            elif facethebear_or_staycalm.lower() == 'face the bear':
                print("You choose 'FACE THE BEAR' now the bear going to eat you! You lose, please try again and take better options")
            else:
                print("Invalid option. Please try again.")
        else:
            print("Invalid option. please try again.")
    else:
        print("Ivalid option. Please try again.")

#Footer Section

#If you say "NO" this its the alternative
elif first_choice.lower() == "no":
  print("Ohhhh i see it")
  second_choice = input("Will you play TOMORROW or NEXT WEEK? ")
  if second_choice.lower() == "tomorrow":
    print("Okay thats good for me")
  elif second_choice.lower() == "next week":
    print("Oh :( Hope that you find a game that you can enjoy")
  else:
    print("Incorrect word")
else:
  print("Oh no, please try again and put the correct word")