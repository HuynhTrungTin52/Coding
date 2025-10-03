import random as rng

print("Welcome to BlackJack, just get to 21 as close as you can ! Just make sure not to get overboard")
value=0
start1=rng.randint(1,11)
start2=rng.randint(1,11)
value=start1+start2
ace=False
while value <21 :
    
    if start1 ==11 or start2 == 11 :
        ace=True
        if start1==11 and start2 ==11:
            value =21
    print("Your starting hand is :",value)
    print("Hit or Stand ?")
    choice=input()
    if choice == "Hit":
        if ace==True :
            value-=10
        value+=rng.randint(1,11)
        if(value>21) :
            print("Your hand is :",value)
            print("You lost ! Try again next time")
            break
    if choice == "Stand" :
        print("Your current hand is ",value)
        break
    