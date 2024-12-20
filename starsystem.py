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

    atmos_roll = 0 if size_roll == 0 else max(0, min(random.randint(2, 12) - 7 + size_roll, 15))

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
        0: "No free standing water"
    }
    
    if size_roll <= 1:
        hydro_roll = 0
    elif atmos_roll <= 1 or atmos_roll >= 10:
        hydro_roll = max(0, min(random.randint(2, 12) - 7 + size_roll - 4, 10))
    else:
        hydro_roll = max(0, min(random.randint(2, 12) - 7 + size_roll, 10))

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

    pop_roll =  random.randint(2, 12) - 2

    for i, j in pop_dict.items():
        if pop_roll >= i:
            star_system["main world UPP"]["population"] = j
            break

    #government 
    gov_dict = {
        13: "Religious Dictatorship",
        12: "Charismatic Oligarchy",
        11: "Non-Charismatic Leader",
        10: "Charismatic Dictator",
        9: "Impersonal Bureaucracy",
        8: "Civil Service Bureaucracy",
        7: "Balkanization",
        6: "Captive Government",
        5: "Feudal Technocracy",
        4: "Representative Democracy",
        3: "Self-Perpetuating Oligarchy",
        2: "Participating Democracy",
        1: "Company/Corporation",
        0: "No government structure"
    }

    gov_roll = max(0, min(random.randint(2, 12) - 7 + pop_roll, 13)) 

    for i, j in gov_dict.items():
        if gov_roll >= i:
            star_system["main world UPP"]["government"] = j
            break

    #law level
    law_dict = {
        10: "Weapon possession is prohibited",
        9: "Possession of any weapon outside one’s residence is prohibited",
        8: "Long blade weapons are controlled",
        7: "Shotguns are prohibited",
        6: "Most firearms prohibited",
        5: "Personal concealable firearms prohibited",
        4: "Light assault weapons prohibited",
        3: "Weapons of a strict military nature prohibited",
        2: "Portable energy weapons prohibited",
        1: "Body pistols undetectable by standard detectors, explosives, and poison gas prohibited",
        0: "No prohibitions"
    }
    law_roll = max(0, min(10, random.randint(2, 12) - 7 + gov_roll, 10))

    for i, j in law_dict.items():
        if law_roll >= i:
            star_system["main world UPP"]["law level"] = j
            break

    #technological level
    tech_dict = {
        15: "Technical maximum Imperial",
        14: "Above average Imperial",    
        13: "Above average Imperial",
        12: "Average Imperial",          
        11: "Average Imperial",    
        10: "Interstellar community",
        9: "circa 1990 to 2000",
        8: "circa 1980 to 1989",
        7: "circa 1970 to 1979",
        6: "circa 1940 to 1969",
        5: "circa 1900 to 1939",
        4: "circa 1860 to 1900",
        3: "circa 1700 to 1860",
        2: "circa 1400 to 1700",
        1: "Bronze Age to Middle Ages",
        0: "Stone Age. Primitive"
    }

    #dm begins 💀💀
    dm = 0

    #star port dm
    star_port_modifiers = {'A': 6, 'B': 4, 'C': 2, 'X': -4}
    dm += star_port_modifiers.get(star_system["system contents"]["star port"], 0)

    #size dm
    if size_roll <= 1:
        dm += 2
    elif 2 <= size_roll <= 4:
        dm += 1

    #atmosphere dm
    if atmos_roll <= 3 or (atmos_roll >= 10 and atmos_roll != 15):
        dm += 1

    #hydro dm
    if hydro_roll in {9, 10}:
        dm += 1 if hydro_roll == 9 else 2

    #pp dm
    if 1 <= pop_roll <= 5:
        dm += 1
    elif pop_roll == 9:
        dm += 2
    elif pop_roll == 10:
        dm += 4

    #gov dm
    if gov_roll in {0, 5}:
        dm += 1
    elif gov_roll == 13:
        dm -= 2
    
    tech_roll = max(0, min(random.randint(1,6) + dm, 15))

    for i, j in tech_dict.items():
        if tech_roll >= i:
            star_system["main world UPP"]["technological level"] = j
            break
        
    #the end
    return star_system

print(generate_star_system())