import random as rng

print("Hello fellow user ! This is the walking game, where you have a maximum of 100 steps to take ! Each turn you are allowed to take 10 steps, and more steps = more bad events happening ! Have fun !")
needed_steps=100
motivSteps=0
trouser=False
wetclothes=0
Artgirl=0
while needed_steps >0:
    print("How many steps do you wanna take ? Note : You have ",needed_steps,"left")
    steps=int(input())
    if steps >10 :
        while steps>10:
            print("Sorry you dingus, but the maximum for each turn is 10 steps ! Try again you dumbass !")
            steps=int(input())
    
    chances = rng.randint(2,steps)
    if motivSteps >0:
        steps+=2
        motivSteps-=1
    if trouser == True and steps == 2 :
        steps=4
        print("trouse work")
    if wetclothes>0 :
        steps-=2
        wetclothes-=2
        print("wet work")
    match chances:
        case 0 :
            print("Nothing happened, fellow traveller !")
        case 1 :
            event1=rng.randint(0,3)
            match event1:
                case 0:
                    print("The turtle won in the race against the rabbit... But not this time ! You stepped onto the turtle and slipped(+2 steps)")
                    needed_steps+=2
                case 1:
                    print("You were cautious while you were stepping, so it's fine !")
                case 2:
                    print("Your eyes look wary of your surroundings as you took a step... only to not notice the floor was made out of ice ! Will you slip and fall or somehow win against \nthe icy floor ?!")
                    iceEvent=rng.randint(0,4)
                    if iceEvent == 4 :
                        print("You managed to stabilize yourself and slide across the ice ! -10 steps")
                        needed_steps-=10
                    elif iceEvent !=4 :
                        print("Unfortunately you slipped and fell on your ass, +4 steps")
                        needed_steps+=4
                case 3:
                    print("Baby steps are crucial ! To run is to walk !")
                    print("Seeing such motivating words, your next 2 turns will have 2 additional steps that will not affect the RNG !")
                    motivSteps=2
        case 2:
            event2=rng.randint(0,4)
            if trouser == True :
                while event2==0 :
                    event2=rng.randint(0,4)
            if Artgirl ==1 :
                while event2 ==3 :
                    event2=rng.randint(0,4)
            if wetclothes >0 :
                while event2 == 1 :
                    event2=rng.randint(0,4)
            match event2 :
                case 0 :
                    print("A pair of steps mean... something, but each pair of steps make a lot of meaning ! +2 Mult for each time this event appears")
                    print("Kidding, you now have Paired Trousers ! Every 2 steps is 4 steps !")
                    trouser=True
                case 1 :
                    print("While trying to walk two steps at the same time, you accidentally crossed your feet and fell into the river. Your clothes are now wet !")
                    print("-2 steps for 2 turns")
                    wetclothes=2
                case 2 :
                    print("While listening your music, you seemingly walked more than 2 steps and came out... fine ! Probably shouldn't do that too much. -3 steps")
                    steps+=3
                case 3 :
                    print("There's a girl who caught your eyes, a black haired girl who was walking around a lake with her art equipment. You couldn't help but fall for her at first sight")
                    print("While you were gazing at her... She saw you and waved, as you could see her face and your heart was stunned in place. She left you in awe... Quite literally, she left the lake while you were in awe")
                    Artgirl=1
                case 4 : 
                    print("Two steps... You know who else took two steps ?[Hint : The answer is in all caps]")
                    answer=input()
                    if answer == "MY MOM" :
                        print("Nice ! High Five ! Mentioning of five, I'll take away 5 steps of yours !")
                        steps+=5
                    else :
                        print("Come on... It's a regular refrence ! Just for that, take this")
                        print("[Explosion happens] + 15 steps")
                        needed_steps+=15
                        
    
    needed_steps-=steps
                    
 

print("You won !")