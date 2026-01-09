import random

def run_monty_hall_simulation(num_trials):

    switch_wins = 0
    stay_wins = 0

    print(f"Running simulation with {num_trials} trials...\n")

    for _ in range(num_trials):
        doors = [0, 1, 2]
        car_door = random.choice(doors)

        choice = random.choice(doors)

        doors_for_monty = [door for door in doors if door != car_door and door != choice]
        monty_opens = random.choice(doors_for_monty)

        if choice == car_door:
            stay_wins += 1

        switch_choice = [door for door in doors if door != choice and door != monty_opens][0]
        
        if switch_choice == car_door:
            switch_wins += 1

    stay_win_rate = (stay_wins / num_trials) * 100
    switch_win_rate = (switch_wins / num_trials) * 100

    print(f"Stay : {stay_wins} win(s)({stay_win_rate:.2f}%)")
    print(f"Switch: {switch_wins} win(s)({switch_win_rate:.2f}%)")
    
    print("\nConclusion:")
    if switch_win_rate > stay_win_rate:
        print("The simulation confirms that SWITCHING is the better strategy.")
    else:
        print("The simulation results are inconclusive (unlikely with high N).")


run_monty_hall_simulation(1000)