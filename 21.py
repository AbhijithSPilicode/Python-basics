sport=input("enter the sport").lower()
score1=int(input("enter player1 score:"))
score2=int(input("enter player2 score:"))
if sport=="badminton":
    if score1==score2:
        print("game is draw")
    elif score1>score2:
        print("player1 won")
    else:
        print("player2 won")

elif sport=="golf":
     if score1==score2:
        print("game is draw")
     elif score1 < score2:
        print("player1 won")
     else:
        print("player2 won")

else:
    print("unknown sport")

