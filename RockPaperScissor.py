from random import randint
game=["rock", "paper", "scissor"]
computer=game[randint(0,2)]
player = True
print("Type stop to exit the game")
while (player==True):
    
    player = input()
    if computer == player:
        print("Tie")
        player = True
    elif(computer == "rock"):
        if(player == "scissor"):
            print("lost")
            player = True
        if(player == "paper"):
            print("won")
            player = True
    elif(computer == "paper"):
        if(player == "rock"):
            print("lost")
            player = True
        if(player == "scissor"):
            print("won")
            player = True
    elif(computer == "scissor"):
        if(player == "rock"):
            print("won")
            player = True
        if(player == "paper"):
            print("lost")
            player = True
    elif(player == "stop"):
        player = False
    
    

    


