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

    starport_dict = {
        12: "X",
        10: "E",
        9: "D",
        7: "C",
        5: "B",
        2: "A"
    }

    tech_dict = {
        12: "advanced",
        9: "high",
        7: "moderate",
        4: "low",
        1: "primitive"
    }
    

    
    roll_presence = random.randint(2, 12)
    for threshold, presence in starport_dict.items():
        if roll_presence >= threshold:
            star_system["starport"] = presence
            break 
    roll_tech = random.randint(2, 12)
    
    for threshold, tech in tech_dict.items():
        if roll_tech >= threshold:
            star_system["tech_level"] = tech
            break

    return star_system


star_system = generate_star_system()
print(star_system)