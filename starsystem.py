import random

# Function to generate a random system name (similar to LV427 in Alien)
def generate_random_name():
    return f"LV{random.randint(100, 999)}"

"""
SKIP 1 and 4
"""

import random
import string

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
    
    #name
    star_system["name"] = random.choice(string.ascii_letters).capitalize() + random.choice(string.ascii_letters).capitalize() + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))

    #MAIN WORLD UPP
    star_system["main world UPP"] = {}

    #main world size
    size_dict = {
        10: "10,000mi",
        9: "9,000mi",
        8: "8,000mi",
        7: "7,000mi",
        6: "6,000mi",
        5: "5,000mi",
        4: "4,000mi",
        3: "3,000mi",
        2: "2,000mi",
        1: "1,000mi",
        0: "Asteroid"
    }

    size_roll = random.randint(2, 12) - 2

    for i, j in size_dict.items():
        if size_roll >= i:
            star_system["main world UPP"]["world size"] = j
            break
    
    #atmosphere
    atmos_dict = {
        15: "Thin, low",
        14: "Ellipsoid",
        13: "Dense, high",
        12: "Insidious",
        11: "Corrosive",
        10: "Exotic",
        9: "Dense, tainted",
        8: "Dense",
        7: "Standard, tainted",
        6: "Standard",
        5: "Thin",
        4: "Thin, tainted",
        3: "Very thin",
        2: "Very thin, tainted",
        1: "Trace",
        0: "No atmosphere"
    }

    atmos_roll = 0 if size_roll == 0 else max(0, random.randint(2, 12) - 7 + size_roll)

    for i, j in atmos_dict.items():
        if atmos_roll >= i:
            star_system["main world UPP"]["atmosphere"] = j
            break

    #hydrographics
    hydro_dict = {
        10: "No land masses",
        9: "90% water",
        8: "80% water",
        7: "70% water",
        6: "60% water",
        5: "50% water",
        4: "40% water",
        3: "30% water",
        2: "20% water",
        1: "10% water",
        0: "No land masses"
    }

    #hydro_roll = 0 if size_roll == 0 else max(0, random.randint(2, 12) - 7 + size_roll)
    #hydro_roll = 0 if size_roll <= 1 elif random.randint(2, 12) - 7 + size_roll - 4 atmos_roll <= 1 or atmos_roll >= 10
    #
    # CHECK LOGIC IT IS PROLLY BROKEN
    #
    hydro_roll = 0
    if size_roll <= 1:
        hydro_roll = 0
    elif atmos_roll <= 1 or atmos_roll >= 10:
        hydro_roll = random.randint(2, 12) - 7 + size_roll - 4

    #hydro_roll = 0 if size_roll <= 1 else (0 if random.randint(2, 12) - 7 + atmos_roll - 4 + atmos_roll <= 1 or atmos_roll >= 10 else random.randint(1, 10))

    for i, j in hydro_dict.items():
        if hydro_roll >= i:
            star_system["main world UPP"]["hydrographics"] = j
            break
    
    #population
    pop_dict = {
        10: "Tens of billions",
        9: "Billions of inhabitants",
        8: "Hundreds of millions",
        7: "Tens of millions",
        6: "Millions of inhabitants",
        5: "Millions of inhabitans",
        4: "Tens of thousands",
        3: "Thousands of inhabitants",
        2: "Hundreds of inhabitants",
        1: "Tens of inhabitants",
        0: "No inhabitants"
    }

    pop_roll = random.randint(2, 12) - 2

    for i, j in pop_dict.items():
        if pop_roll >= i:
            star_system["main world UPP"]["population"] = j
            break
        
    #government 
    #generate size, atmosphere, hydrographics, population, government level, law level and tech level
    return star_system


star_system = generate_star_system()

print(star_system)