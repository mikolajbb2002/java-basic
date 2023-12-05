print("Welcome to the game! Your goal is to find a treasure")
first_choice=input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n")
if first_choice=="left":
    second_choice = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
    if second_choice=="wait":
        third_choice= input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
        if third_choice=="yellow":
            print("You found the treasure! You Win!")
        elif third_choice=="red":
            print("It's a room full of fire. Game Over.")
        elif third_choice=="blue":
            print("You enter a room of beasts. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")

else:

    print("You fell into a hole. Game Over.")
