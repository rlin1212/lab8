import random
import time

def playerintro(): #introduction to the game, setting the scene
    playername = input("Please enter a playername:") #asking for player name
    print('Welcome '+playername)
    time.sleep(1)
    print('It is the year 2050.')
    time.sleep(1)
    print('Ever since year 2020, our country has been ravaged by plagues and viruses, destroying much of the population.')
    time.sleep(4)
    print("Each superpower deployed all of their arms, nukes, soldiers to scour all the rescources they could.")
    time.sleep(5)
    print('You are one of the select few who survived')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    
def playerintro_pt2(): #assinging a mission the player
    print("We survived the nuclear fallout and the desolate wasteland.")
    time.sleep(4)
    print('Humanity bounced back, as it always does.')
    time.sleep(4)
    print('But the food reserves are dwindeling and necessities are becoming scarce.')
    time.sleep(4)
    print('You, are part of a select NASA crew to search space for a habitable world that humanity could thrive in.')
    time. sleep(4)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('You buckle into your seat on the space craft along with your fellow crew members.')
    time.sleep(4)
    print('"Space Shuttle Explorer to flight control" your captain says, "we are ready for take off"')    
    time.sleep(4)
    print("'Heard' you hear come out of the speaker.")
    time.sleep(4)
    print("'Takeoff in 5 seconds' the voice in the speaker says")
    time.sleep(4)
    print("You turn your head and see a woman next to you, she asks,'are you ready!?'")
    input("What do you respond yes or no?:")
    time.sleep(0.5)
    print("3.")
    time.sleep(0.5)
    print('2.')
    time.sleep(0.5)
    print("1.")
    time.sleep(0.5)
    print('takeoff.')

playerintro()
playerintro_pt2()
