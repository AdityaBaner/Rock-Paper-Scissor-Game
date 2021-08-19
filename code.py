import random
def gameWin(a,b):               # Function to choose the winner
    if a==b:
        return None
    elif a=='r':                # Computers Choice is Rock
        if b=='p':                  # You choose Paper
            return True
        elif b=='s':                # You choose Scissor
            return False

    elif a=='p':                # Computers Choice is Paper
        if b=='s':                  # You choose Scissor
            return True
        elif b=='r':                # You choose Rock
            return False

    elif a=='s':                # Computers Choice is Scissor
        if b=='r':                  # You choose Rock
            return True
        elif b=='p':                # You choose Paper
            return False




# print("Comp turn: Rock(r) Paper(p) Scissor(s) ")

f=True
while(f):
    dict={ 'r':'Rock' , 'p':'Paper' , 's':'Scissor' }
    ch='rps'
    a=random.choice(ch)             # Computer makes a random choice
    b=input("\nPlayer's turn: Rock(r) Paper(p) Scissor(s): ").lower()           # You choose a input 

    if b not in dict:
        print('\nWrong Choice\n')
    else:
        winner = gameWin(a,b)

        print(f'\nComp chose: {dict[a]}')
        print(f'You chose: {dict[b]}')

        if winner==None:
            print('\nGame Tie\n\n')               # You chose the same input as that of computer
        elif winner:
            print("\nHurray , You Win !\n\n")
        else:
            print("\nAlas , You Lose !\n\n")

    ch=input(".......Do you wanna play again.......\n  Press 'Y' for YES || 'N' for No: ")
    if ch=='Y' or ch=='y':
        f=True
    else:
        f=False
        print('\n....ThankYou for Playing....\n')        
