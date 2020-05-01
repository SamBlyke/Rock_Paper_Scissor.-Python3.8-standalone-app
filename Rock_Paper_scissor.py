import random
import time

print("                 Welcome to the game of Rock-Paper-Scissor.")

Opt=["R","P","S"]
Opt_full=["ROCK","PAPER","SCISSOR"]

game_over_num=0
u=None

def game_logic():
    global game_over_num
    global u
    print("r --> ROCK")
    print("p --> PAPER")
    print("s --> SCISSOR")
    print("*Just press Enter to exit")
    
    u=str(input("Enter : "));u=u.upper()
    c=random.randint(0,2);c=Opt[c]
    if(u=="E"):
        game_over_num=-1

    while(game_over_num==0):
    
        if(u==c):
            game_over_num=0
            print("            ____ Same result bu both computer and the user. ____")
            break
        elif(u==Opt[0] and c==Opt[1]):
            print("            ____ Computer opted for %s while user opted for %s ____ " % (Opt_full[0] , Opt_full[1]))
            game_over_num=1
            break
        elif(u==Opt[1] and c==Opt[0]):
            print("            ____ Computer opted for %s while user opted for %s ____ " % (Opt_full[1] , Opt_full[0]))
            game_over_num=2
            break
        elif(u==Opt[1] and c==Opt[2]):
            print("            ____ Computer opted for %s while user opted for %s ____ " % (Opt_full[2] , Opt_full[1]))
            game_over_num=1
            break
        elif(u==Opt[2] and c==Opt[1]):
            print("            ____ Computer opted for %s while user opted for %s ____ " % (Opt_full[1] , Opt_full[2]))
            game_over_num=2
            break
        elif(u==Opt[0] and c==Opt[2]):
            print("            ____ Computer opted for %s while user opted for %s ____ " % (Opt_full[2] , Opt_full[0]))
            game_over_num=2
            break
        elif(u==Opt[2] and c==Opt[0]):
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
    elif(u=="E"):
        break
    game_over_num=0
    game_logic()
    




        
