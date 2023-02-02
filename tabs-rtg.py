import random

# I know this would be neater as a dictionary rather than two lists, but it works so I won't bother changing it.
unit = ['Clubber (Tribal)', 'Protector (Tribal)', 'Spear Thrower (Tribal)', 'Stoner (Tribal)', 'Bone Mage (Tribal)', 'Chieftan (Tribal)', 'Mammoth (Tribal)', 'Halfling (Farmer)', 'Farmer (Farmer)', 'Hay Baler (Farmer)', 'Potionseller (Farmer)', 'Harvester (Farmer)', 'Wheelbarrow (Farmer)', 'Scarecrow (Farmer)', 'Bard (Medieval)', 'Squire (Medieval)', 'Archer (Medieval)', 'Healer (Medieval)', 'Knight (Medieval)', 'Catapult (Medieval)', 'The King (Medieval)', 'Shield Bearer (Ancient)', 'Sarissa (Ancient)', 'Hoplite (Ancient)', 'Snake Archer (Ancient)', 'Ballista (Ancient)', 'Minotaur (Ancient)', 'Zeus (Ancient)', 'Headbutter (Viking)', 'Ice Archer (Viking)', 'Brawler (Viking)', 'Berserker (Viking)', 'Valkyrie (Viking)', 'Longship (Viking)', 'Jarl (Viking)', 'Samurai (Dynasty)', 'Firework Archer (Dynasty)', 'Monk (Dynasty)', 'Ninja (Dynasty)', 'Dragon (Dynasty)', 'Hwacha (Dynasty)', 'Monkey King (Dynasty)', 'Painter (Renaissance)', 'Fencer (Renaissance)', 'Balloon Archer (Renaissance)', 'Musketeer (Renaissance)', 'Halberd (Renaissance)', 'Jouster (Renaissance)', 'Da Vinci Tank (Renaissance)', 'Flintlock (Pirate)', 'Blunderbuss (Pirate)', 'Bomb Thrower (Pirate)', 'Harpooner (Pirate)', 'Cannon (Pirate)', 'Captain (Pirate)', 'Pirate Queen (Pirate)', 'Skeleton Warrior (Spooky)', 'Skeleton Archer (Spooky)', 'Candlehead (Spooky)', 'Vampire (Spooky)', 'Pumpkin Catapult (Spooky)', 'Swordcaster (Spooky)', 'Reaper (Spooky)', 'Dynamite Thrower (Wild West)', 'Miner (Wild West)', 'Cactus (Wild West)', 'Gunslinger (Wild West)', 'Lasso (Wild West)', 'Deadeye (Wild West)', 'Quick Draw (Wild West)']
cost = [70, 80, 120, 160, 300, 400, 2200, 50, 80, 140, 340, 500, 1000, 1200, 60, 100, 140, 180, 650, 1000, 1500, 100, 120, 180, 300, 900, 1600, 2000, 90, 160, 220, 250, 500, 1000, 1500, 140, 180, 250, 500, 1000, 1500, 2000, 50, 150, 200, 250, 400, 1000, 4000, 100, 160, 250, 300, 1000, 1500, 2500, 80, 180, 200, 200, 1000, 1000, 2500, 100, 200, 400, 650, 740, 900, 1200]
FinalTeam = []
budget = 0

def start():
    while True:
        try:
            global budget
            budget = int(input())
            if budget < 50:
                print("That can't buy anything! Enter a higher budget.")
            break
        except ValueError:
            print("Please enter numbers only!")
            continue

def generate():
    randunit = random.randrange(len(unit))
    global budget
    unitLimit = int(budget / cost[randunit])
    if unitLimit == 0:
        return
    elif unitLimit == 1:
        unitCount = 1
    else:
        unitCount = random.randrange(1, unitLimit)
    FinalTeam.append(str(unit[randunit] + " ×" + str(unitCount)))
    budget -= (cost[randunit] * unitCount)
    unit.pop(randunit)
    cost.pop(randunit)
#    print("Your current team is: " + str(FinalTeam))
#    print("Your remaining budget is " + str(budget))

print("Enter the budget for your team.")

while budget < 50:
    start()

hobbit = random.randrange(100)
if hobbit == 64:
    unitCount = int(budget / 50)
    FinalTeam.append(str("Halfling ×" + str(unitCount)))
    budget -= (50 * unitCount)

while budget >= 50 and unit:
    generate()

print()
print("YOUR RANDOM TEAM IS:\n~~~~~~~~~~~~~~~~~~~~")
print(*FinalTeam, sep = "\n")
print("~~~~~~~~~~~~~~~~~~~~\n")
if budget == 0:
    print("Your team perfectly fit your budget!")
elif budget > 4000:
    print("Your team came in " + str(budget) + " gold under budget. Perhaps your budget was too high?")
else:
    print("Your team came in " + str(budget) + " gold under budget.")
input("Press Enter to close window.")