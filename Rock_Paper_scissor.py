import random
import time

print("                 Welcome to the game of Rock-Paper-Scissor.")

Opt=["R","P","S"]
Opt_full=["ROCK","PAPER","SCISSOR"]

game_over_num=0
user_choice=None

def game_logic():
    global game_over_num
    global user_choice
    print("r --> ROCK")
    print("p --> PAPER")
    print("s --> SCISSOR")
    print("*Just press Enter to exit")
    
    user_choice=str(input("Enter : "));user_choice=user_choice.upper()
    comp_choice=random.randint(0,2);ccomp_choice=Opt[comp_choice]
    if(user_choice=="E"):
        game_over_num=-1

    while(game_over_num==0):
    
        if(user_choice == comp_choice):
            game_over_num=0
            print("            ____ Same result bu both computer and the user. ____")
            break
        elif(user_choice==Opt[0] and comp_choice==Opt[1]):
            print("            ____ Computer opted for %s while user opted for %s ____ " % (Opt_full[0] , Opt_full[1]))
            game_over_num=1
            break
        elif(user_choice==Opt[1] and comp_choice==Opt[0]):
            print("            ____ Computer opted for %s while user opted for %s ____ " % (Opt_full[1] , Opt_full[0]))
            game_over_num=2
            break
        elif(user_choice==Opt[1] and comp_choice==Opt[2]):
            print("            ____ Computer opted for %s while user opted for %s ____ " % (Opt_full[2] , Opt_full[1]))
            game_over_num=1
            break
        elif(user_choice==Opt[2] and comp_choice==Opt[1]):
            print("            ____ Computer opted for %s while user opted for %s ____ " % (Opt_full[1] , Opt_full[2]))
            game_over_num=2
            break
        elif(user_choice==Opt[0] and comp_choice==Opt[2]):
            print("            ____ Computer opted for %s while user opted for %s ____ " % (Opt_full[2] , Opt_full[0]))
            game_over_num=2
            break
        elif(user_choice==Opt[2] and comp_choice==Opt[0]):
            print("            ____ Computer opted for %s while user opted for %s ____ " % (Opt_full[0] , Opt_full[2]))
            game_over_num=1
            break
        else:
            game_over_num=-1
            print("Your input doesn't comply.")

game_logic()

while True:
    if(game_over_num==1):
        print("                         Computer won this time".upper())
    elif(game_over_num==2):
        print("                        User, You've won this time".upper())
    elif(game_over_num==-1):
        print("                        EXITING")
        time.sleep(0.5)
        break
    elif(user_choice=="E"):
        break
    game_over_num=0
    game_logic()
    




        
