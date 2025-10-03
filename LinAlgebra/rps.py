import random as rng

def bot_choice(bot_picked):
    random=rng.randint(1,3)
    match random:
        case 1:
            bot_picked = "Rock"
        case 2:
            bot_picked = "Paper"
        case 3:
            bot_picked ="Scissors"

print("1. Rock\n2. Paper\n3. Scissors\n4. Quit")
choice=input()
bot=bot_choice(bot_picked="")

