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
    time.sleep(5)
def playerinmars(): #plot in space
    print("In space, you see the prettiest, most surreal views that are nearly unimaginable")
    print(" having lived your entire life on Earth.")
    time.sleep(4)
    print("You explore planets and end up on Mars to find that there are alien life forms living there")
    time.sleep(4)
    print("Your captain orders you to get your guns and equip yourself for battle.")
    time.sleep(1)
    mars_answer = input("How do you respond (Yes/No):") #If statement player makes a choice here

    if mars_answer == "No":
        time.sleep(1)
        print("No! This is wrong, we just got here and it would be unjust for us to terrorize them.")
        time.sleep(1)
        print("The Captain turns to you.. How DARE YOU disobey my orders and threaten our goal of saving humanity!")
        time.sleep(1)
        revoltanswer = input("Start a revolt against the captain? (Yes/No):)
        if revoltanswer = "Yes":
            time.sleep(1)
            print("You tell the captain and the crew members,'Those who think its wrong to kill these aliens, take my side!'")
            time.sleep(1)
            print("Your crew sides with you and tie up the captain.")
            time.sleep(1)
            print("Your captain screams, 'HOW DARE YOU ALL JEOPARDIZE THE LIVES OF EVERYONE ON EARTH FOR MEASLY ALIEN LIVES!!")
            print("YOU CAN NEVER KILL MY DREAM TO LIVE ON MARS'")
            time.sleep(3)
            print('The captain breaks free and aims a gun at you.')
            time.sleep(2)
            gunresponse = input("How do you react? (Fight/Insult him):"
                if gunresponse == "Fight":
                elif gunresponse == "Insult him":
                    time.sleep(1)
                    print("You wouldn't dare shoot, you don't have the guts to.")
                    time.sleep(2)
                    print("The captain screams, 'AARGH, I WILL NOT LET A SUBORDINATE JEOPORDIZE THE MISSION")
                    time.sleep(2)
                    print("He fires the gun, and it hits you in the heart.")
                    time.sleep(2)
        elif revoltanswer = "No":
            time.sleep(1)
            print("I will not revolt against you as a leader, but I also refuse to help the slaughter of these aliens!")
    elif mars_answer == "Yes":
        time.sleep(1)
        print("Yes captain, we are ready for battle.")

def playerwakesup():
    print(".........")

playerintro()
playerintro_pt2()
playerinmars()
playerwakesup()

playagain = "Yes"
while playagain == "yes": #giving the player an option to continue playing
    playerintro()
    playerintro_pt2()
    playerinmars() 
    playagain = input("Do you want to play again (Yes/No):")
