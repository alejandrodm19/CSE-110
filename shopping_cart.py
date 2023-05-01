# """""""""
# Author: Alejandro Malvacias 
# File: shopping_cart.py
# """""""""
print("Welcome to the Shopping Cart Program!")
#Empty list
#Empty variable
#The "Play_again" variable to repeat the loop
action = ""
view_cart_list = []
play_again = "yes"
#Main Loop
while action != "5" and play_again == "yes":
    print("Please select one of the following")
    print("\n 1. Add item \n 2. View cart \n 3. Remove item \n 4. Compute total \n 5. Quit \n 6. This is the last option, please choose this when you finish the program" )
    action = input("Please enter an action: ")
    #If an Else Section
    if action == "1": #First Action
        item_add = input("What item would you like to add? ")
        item_price = float(input(f"What is the price of {item_add}? "))
        view_cart_list.append((item_add, item_price))
        print(f"{item_add} has been added to the cart")
    elif action == "2": #Second Action
        if view_cart_list:
            print(f"The contents of the cart are: ")
            for i, (item, price) in enumerate (view_cart_list, 1):
                print(f"{i}. {item} - ${price}")
        else:
            print("Your cart is empty")
    elif action == "3": #Third Action
        item = int(input("What item would you like to remove?: "))
        if item -1 in range(len(view_cart_list)):
            removed_item = view_cart_list.pop(item - 1)  
            print(f"{removed_item[0]} has been removed from the cart")
        else:
            print("Invalid item number")
    elif action == "4": #Fourth Action
        total = sum([price for item in view_cart_list])
        print(f"The total price of the items in the shopping cart is: ${total:.2f}")
    elif action == "5": #Fifth Action
        print("Thank you goodbye")
    elif action == "6": #Sixth Action, with an especial case
        joke = input("Congrats, you are so far out of the shopping cart. \n But do you want to hear a bad joke about shopping carts?: ")
        if joke.lower() == "yes":
            print("I feel sorry for shopping carts!\nThey're always getting pushed around!")
            play_again = input("\nWould you like to play again?: ")
        elif joke.lower() == "no":
            print("Ohh well, hope I can see you again!")
            break #Break action
    elif action >= "7": #If action is greater than 7 then it is an invalid option
        print("Invalid action, please try again")
