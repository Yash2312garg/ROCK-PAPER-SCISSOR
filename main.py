import random
raw_user_input3=input("enter P to play and Q to quit: ")
user_input3=raw_user_input3.title()
countb=0
countu=0
count=0

while user_input3!='Q':
    user_input1 = int(input("Enter any number:"))
    random.seed(user_input1)
    bot = random.choice('RPS')

    raw_user_input2=input(("Enter rock/paper/scissor: "))
    user_input2=raw_user_input2.title()
    if bot=='R' and user_input2=='Rock':
        print("the game is tied! ")
        countb+=0
        countu+=0
    elif bot=='S' and user_input2=='Scissor':
        print("The game is tied! ")
        countb += 0
        countu += 0
    elif bot=='P' and user_input2=='Paper':
        print("The game is tied! ")
        countb += 0
        countu += 0
    elif bot=='R' and user_input2=='Raper':
        print("You win! ")
        countu += 1
    elif bot=='R' and user_input2=='Scissor':
        print("Bot wins! ")
        countb += 1
    elif bot=='S' and user_input2=='Paper':
        print("Bot wins! ")
        countb += 1
    elif bot=='S' and user_input2=='Rock':
        print("You win! ")
        countu += 1
    elif bot=='P' and user_input2=='Rock':
        print("Bot wins! ")
        countb += 1
    elif bot=='P' and user_input2=='Scissor':
        print("You win! ")
        countu += 1
    raw_user_input3 = input("Enter P to play and Q to quit: ")
    user_input3=raw_user_input3.title()
    count+=1
if countu>countb:
    difference=countu-countb
    print(f"user wins the game by {difference} points! ")
if countu<countb:
    difference=countb-countu
    print(f"bot wins the game by {difference} points! ")
if countu==countb:
    print("Game is tied! ")
print(f"You have played {count} games! ")
print("""thankyou for playing !!!  
Back to main menu! """)


