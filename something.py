playername = input("Please enter a playername:")
print('Welcome '+playername)
playerclass = input('Please select a class- KNIGHT, WIZARD, KING: ')
if playerclass == 'KING':
    print("You have a crown.")
elif playerclass == 'WIZARD':
    print("You have strong magic power.")
elif playerclass == 'KNIGHT':
    print("You have strong agility and srength stats.")
