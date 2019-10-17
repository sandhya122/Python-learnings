from string import lower

print("""Select Any of following :
...ROCK...
...PAPER...
...SCISSOR... 
""")

while True:

    FUser = lower(raw_input("Player 1: Please enter your selection"))
    SUser = lower(raw_input("Player 2: Please enter your selection"))

    if FUser!=SUser:
        if FUser=="rock" and SUser=="paper":
            print ("Player1 won....!!!")
        elif FUser=="paper" and SUser=="rock":
            print ("Player2 won....!!!")
        elif FUser=="rock" and SUser=="scissor":
            print ("Player1 won....!!!")
        elif FUser=="scissor" and SUser=="rock":
            print ("Player2 won....!!!")
        elif FUser=="scissor" and SUser=="paper":
            print ("Player1 won....!!!")
        elif FUser=="paper" and SUser=="scissor":
            print ("Player2 won....!!!")
        else:
            print ("Enter correct choice")


    else:
        print ("Boom...It's a tie")

    replay = raw_input("If you want to play again, enter yes")
    if replay!= "yes":
        print ("TATA....")
        break
