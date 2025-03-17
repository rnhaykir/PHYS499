# Simulate 3-door game
import random
import argparse
import os

# Simulate the game N times
# Return the number of times a game player guessed correctly.
def simulate(N):
    correct_guess_count = 0
    for i in range (0, N):
        # Game organizers select a door randomly and places a car behind it
        door_with_car = select_door()
        # Game player selects a door randomly hoping that the car is behind it
        guessed_door_no = select_door()
        # Game host opens the door with no car
        open_door_no = open_door(guessed_door_no, door_with_car)
        # Game player switches their choice 
        switched_door_no = [x for x in ["A", "B", "C"] if x != open_door_no and x != guessed_door_no][0]
        # Did the player guess correctly?
        if door_with_car == switched_door_no:
            correct_guess_count += 1
    return correct_guess_count

# Simulate the choice of the door with a car behind it
def select_door():
    # Draw a random number between 0 and 1. If between 0 and 1/3, then
    # door 1 selected, if between 1/3 and 2/3, then door 2, otherwise
    # door 3.
    r = random.random()
    if r < (1.0 / 3.0):
        return "A"
    elif r >= (1.0 / 3.0) and r < (2.0 / 3.0):
        return "B"
    # r > 2/3
    return "C"

# Simulate the choice of the door that will be opened by the host
def open_door(guessed_door, door_with_car):
    doors = ["A", "B", "C"]
    # If the player's first choice is the door with car, then we remove that door number from the door list
    # if not, then we remove player's first choice and door with car from the list
    if guessed_door == door_with_car:
        doors.remove(guessed_door)
    else:
        doors.remove(guessed_door)
        doors.remove(door_with_car)
    # If the first condition holds, host will choose one of two doors left 
    opened_door = random.choice(doors)
    return opened_door

# One line command and output file
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    
    N = [10000, 100000, 1000000]
    hits = [simulate(n) for n in N]
    percentages = [(100.0 * hits[i]) / N[i] for i in range(3)]
    for i, n in enumerate(N):
        print(f"Percentage of times guess was right for {n} times played = % {percentages[i]:.2f}")
        
    output_file = "output.txt"
    with open(output_file, "w") as file:
        for i, n in enumerate(N):
            file.write(f"Percentage of times guess was right for {n} times played = % {percentages[i]:.2f}\n")


    try:
        if os.path.exists(output_file):
            if os.name == "posix":
                os.system(f"open {output_file}")
            elif os.name == "nt":  # Windows
                os.startfile(output_file)  
        else:
            print("No file found.")
    except Exception as e:
        print(f"Error opening file: {e}")
