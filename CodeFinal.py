#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 11:17:06 2017

@author: mead
"""
import numpy as np

# Going to write code to take care of the Monty Hall simulation
# How many simulations
num_sims = 10000
# Randomly generate the door with the car behind it
carDoor = list(map(int, np.ceil(np.random.sample(num_sims) * 3)))
# Randomly generate a first guess
firstGuess = list(map(int, np.ceil(np.random.sample(num_sims) * 3)))
# Want to pick a random goat to reveal (unless the person has picked a goat as their first guess
# -1 is the lower goat door and +1 is the higher goat door
goatReveal = list(map(int, (np.ceil(np.random.sample(num_sims) * 2) - 1.5) * 2))
# The following is the data structure we use as input to the function
gameBegins = list(map(lambda x,y,z: [x,y,z], carDoor, firstGuess, goatReveal))
    
# Here we'll follow the strategy where you keep your guess after a goat is revealed
def funcMontyHall(gameBegins, printStatement, switchStrat):
    # Get the door with the car
    carDoor = gameBegins[0]
    # Get the first guess
    firstGuess = gameBegins[1]
    # Get the random goat that we'd prefer to reveal
    goatReveal = gameBegins[2]
    # Establishing what doors have goats behind them
    if(carDoor == 1):
        goatDoorLower = 2
    else:
        goatDoorLower = 1
    if(carDoor == 3):
        goatDoorHigher = 2
    else:
        goatDoorHigher = 3
    # There is a lot of user-info that can be suppressed as desired
    if(printStatement):
        print("Welcome to Monty Hall simulation! The simulation will pick a door from 1-3!")
        print("The simulation picked door " + str(firstGuess))
    # In the following else-if clause, we're trying establish which goat door 
    # will be revealed to the player after their first guess
    if(firstGuess in [goatDoorLower, goatDoorHigher]):
        if(firstGuess == goatDoorLower):
            goatDoorOpen = goatDoorHigher
        else:
            goatDoorOpen = goatDoorLower
    else:
        if(goatReveal == -1):
            goatDoorOpen = goatDoorLower
        else:
            goatDoorOpen = goatDoorHigher
            
    if(printStatement):
        print("Monty reveals that there is a goat behind door " + str(goatDoorOpen))
    # The following is using user input to decide whether or not to stay on the same door or to switch
    if(switchStrat == False):
        # Pick the same door that you originally picked
        secondGuess = firstGuess
        if(printStatement):
            print("This portion of the simulation uses the strategy where you keep the door you \
                  picked for your second guess. So your second guess is " + str(secondGuess))
    else:
        # Switch from the door that you originally picked
        secondGuess = [door not in [goatDoorOpen, firstGuess] for door in [1,2,3]].index(True) + 1
        if(printStatement):
            print("This portion of the simulation uses the strategy where you switched from the the door you first picked \
                  picked for your second guess. So your second guess is " + str(secondGuess))
    if(secondGuess == carDoor):
        if(printStatement):
            print("You win! The car was behind door " + str(carDoor))
        # YOU WIN
        return 1
    else:
        if(printStatement):
            print("You lose! The car was behind door " + str(carDoor))
        # YOU LOSE
        return 0

# Now run the simulation using the switching strategy
switchingStratOutput = list(map(lambda x: funcMontyHall(x, True, switchStrat = True), gameBegins))
# What percent of the time does this result in victory?
sum(switchingStratOutput) * 1.0 / len(switchingStratOutput)
# Output: ~66.6%, as expected

# Now run the simulation using the staying strategy
stayingStratOutput = list(map(lambda x: funcMontyHall(x, True, switchStrat = False), gameBegins))
# What percent of the time does this result in victory?
sum(stayingStratOutput) * 1.0 / len(stayingStratOutput)
# Output: ~33.3%, as expected

