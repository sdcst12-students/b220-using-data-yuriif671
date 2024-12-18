import random

# Function to generate a random system name (similar to LV427 in Alien)
def generate_random_name():
    return f"LV{random.randint(100, 999)}"

"""
SKIP 1 and 4
"""

import random

def generate_star_system():
    star_system = {}
    
    #SYSTEM CONTENTS TABLE
    star_system["system contents"] = {}

    #starport
    starport_dict = {
        12: "X",
        10: "E",
        9: "D",
        7: "C",
        5: "B",
        2: "A"
    }
    
    roll_starport = random.randint(2, 12)
    for i, j in starport_dict.items():
        if roll_starport >= i:
            star_system["system contents"]["star port"] = j
            break 

    #navalbase
    navalbase_dict = {
        8: "yes",
        2: "no"
    }

    #do not roll if startport C D E X
    roll_navalbase = 0 if star_system["system contents"]["star port"] in ['C', 'D', 'E', 'X'] else random.randint(2, 12)
    

    for i, j in navalbase_dict.items():
        if roll_navalbase >= i:
            star_system["system contents"]["naval base"] = j
            break

    #scoutbase
    scoutbase_dict = {
        7: "yes",
        2: "no"
    }

    #roll_scoutbase = random.randint(2, 12)
    #if star_system["system contents"]["star port"] == 'C':
    #    roll_scoutbase -= 1
    #elif star_system["system contents"]["star port"] == 'B':
    #    roll_scoutbase -= 2
    #elif star_system["system contents"]["star port"] == 'A':
    #    roll_scoutbase -= 3
    #elif star_system["system contents"]["star port"] == 'E' or star_system["system contents"]["star port"] == 'X':
    #    roll_scoutbase = 0
    
    #ugly one liner but what it does is it applies DMs (dice modifiers) based on the star port type
    roll_scoutbase = 0 if star_system["system contents"]["star port"] in ['E', 'X'] else max(2, random.randint(2, 12) - {'C': 1, 'B': 2, 'A': 3}.get(star_system["system contents"]["star port"], 0))

    print(roll_scoutbase)

    for i, j in scoutbase_dict.items():
        if roll_scoutbase >= i:
            star_system["system contents"]["scout base"] = j
            break

    #gas giant
    gasgiant_dict = {
        10: "no",
        2: "yes"
    }
    
    roll_gasgiant = random.randint(2, 12)
    for i, j in gasgiant_dict.items():
        if roll_gasgiant >= i:
            star_system["system contents"]["gas giant"] = j
            break

    #gas giant
    planetoids_dict = {
        7: "no",
        2: "yes"
    }
    
    roll_planetoids = random.randint(2, 12)
    for i, j in planetoids_dict.items():
        if roll_planetoids >= i:
            star_system["system contents"]["planetoids"] = j
            break 

    return star_system


star_system = generate_star_system()
print(star_system)