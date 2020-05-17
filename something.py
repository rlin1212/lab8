import random
import time

def playerintro():
    playername = input("Please enter a playername:") #asking for player name
    print('Welcome '+playername)
    time.sleep(2)
    print('It is the year 2050')
    time.sleep(2)
    print('Ever since year 2020, our country has been ravaged by plagues and viruses, destroying much of the population.')
    time.sleep(4)
    print('Next came the wars, each superpower deployed all of their arms, nukes, soldiers to scour all the rescources they could.')
    time.sleep(4)
    print('You are one of the select few who survived')
    print('.')
    print('.')

def playerclass():
    playerclass = input('Please select a class- KNIGHT, WIZARD, KING: ') #having player choose class
    if playerclass == 'KING':
        print("You have a crown.")
    elif playerclass == 'WIZARD':
        print("You have strong magic power.")
    elif playerclass == 'KNIGHT':
        print("You have strong agility and srength stats.")
