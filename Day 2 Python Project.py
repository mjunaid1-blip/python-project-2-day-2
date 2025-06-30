                         #Making ROCK PAPER SEASSOR GAME
import random as rd
objects=["rock","paper","scissor"]
print("welcome to rock paper scissors game ")
choice=int(input("press 1 to enter the game press 0 to exit the game"))

if(choice==1):
    player_1_choice=str(input("player 1 turn press b to begin"))

    if(player_1_choice.lower()=="b"):
        player_1_object=rd.choice(objects)
        print(player_1_object)
        player_2_choice=str(input("player 2 turn press b to begin"))

        if(player_2_choice.lower()=="b"):
            
            player_2_object=rd.choice(objects)
            print(player_2_object)
            if player_1_object == player_2_object:
                print("match draw")

            elif(player_1_object=="rock" and player_2_object=="scissor"):
                print("player 1 wins")

            elif(player_1_object=="paper" and player_2_object=="rock"):
                print("player 1 wins")
                
            elif(player_1_object=="scissor" and player_2_object=="paper"):
                print("player 1 wins")

            elif(player_1_object=="rock" and player_2_object=="paper"):
                print("player 2 wins")

            elif(player_1_object=="paper" and player_2_object=="scissor"):
                print("player 2 wins")

            elif(player_1_object=="scissor" and player_2_object=="rock"):
                print("player 2 wins")

            else:
                print("invalid input")
