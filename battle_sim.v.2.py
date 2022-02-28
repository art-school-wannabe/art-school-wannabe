
# import necissary files
import random, time


# file handling

# import player data from existing file
try:
    exec(open("smiles_DataFiles.py").read())

# import starting player data into a new file
except:
    file = open("smiles_DataFiles.py", "a+")
    stat_block = f"""
# define player stats
player_level = 1
player_health = 48
mana = 40
player_attackmulti = ((player_level / 10) + 1)
player_attackbonus = (2 + player_level)
player_ac = (4 + player_level)

# define random variables
distance = 1
duration = 0
drink = 1

# define player inventory
total_experience = 0
total_gold = 80
total_health_potions = random.randint(0,3)
total_mana_potions = random.randint(0,3)
total_arrows = random.randint(12,16)
"""
    file.write(stat_block)
    file.close()

    # import player data from new file
    exec(open("smiles_DataFiles.py").read())


# define player class
