import random
import string

#Turning the star system script from procedural into oop

class StarSystem:
    def __init__(self):
        self.name = self.generateName()
        self.contents = self.generateContents()
        self.main_world_upp = self.generateUPP()
    
    def generateName(self):
        return random.choice(string.ascii_letters).capitalize() + random.choice(string.ascii_letters).capitalize() + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))

    #less redundancy thanks to this function
    def getValueRoll(self, roll, value_dict):
        for threshold, value in sorted(value_dict.items(), reverse=True):
            if roll >= threshold:
                return value
        return None
    
    def generateContents(self):
        contents = {}

        # Starport
        starport_dict = {
            12: "X",
            10: "E",
            9: "D",
            7: "C",
            5: "B",
            2: "A"
        }
        roll_starport = random.randint(2, 12)
        contents["star port"] = self.getValueRoll(roll_starport, starport_dict)

        # Navalbase
        navalbase_dict = {
            8: "yes",
            2: "no"
        }
        roll_navalbase = 0 if contents.get("star port") in ['C', 'D', 'E', 'X'] else random.randint(2, 12)
        contents["naval base"] = self.getValueRoll(roll_navalbase, navalbase_dict)

        # Scoutbase
        scoutbase_dict = {
            7: "yes",
            2: "no"
        }
        roll_scoutbase = 0 if contents.get("star port") in ['E', 'X'] else max(2, random.randint(2, 12) - {'C': 1, 'B': 2, 'A': 3}.get(contents.get("star port"), 0))
        contents["scout base"] = self.getValueRoll(roll_scoutbase, scoutbase_dict)

        # Gas giant
        gasgiant_dict = {
            10: "no",
            2: "yes"
        }
        roll_gasgiant = random.randint(2, 12)
        contents["gas giant"] = self.getValueRoll(roll_gasgiant, gasgiant_dict)

        # Planetoids
        planetoids_dict = {
            7: "no",
            2: "yes"
        }
        roll_planetoids = random.randint(2, 12)
        contents["planetoids"] = self.getValueRoll(roll_planetoids, planetoids_dict)

        return contents
    
    # Main world UPP, which is: size, atmosphere, hydrographics, population, government, law level, technological level
    def generateUPP(self):
        main_world_upp = {}

        # Size
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
        main_world_upp["world size"] = self.getValueRoll(size_roll, size_dict)

        # Atmosphere
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
        main_world_upp["atmosphere"] = self.getValueRoll(atmos_roll, atmos_dict)

        # Hydrographics
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
        hydro_roll = 0 if size_roll <= 1 else max(0, min(random.randint(2, 12) - 7 + size_roll - 4, 10)) if atmos_roll <= 1 or atmos_roll >= 10 else max(0, min(random.randint(2, 12) - 7 + size_roll, 10))
        main_world_upp["hydrographics"] = self.getValueRoll(hydro_roll, hydro_dict)

        # Population
        pop_dict = {
            10: "Tens of billions",
            9: "Billions of inhabitants",
            8: "Hundreds of millions",
            7: "Tens of millions",
            6: "Millions of inhabitants",
            5: "Millions of inhabitants",
            4: "Tens of thousands",
            3: "Thousands of inhabitants",
            2: "Hundreds of inhabitants",
            1: "Tens of inhabitants",
            0: "No inhabitants"
        }
        pop_roll = random.randint(2, 12) - 2
        main_world_upp["population"] = self.getValueRoll(pop_roll, pop_dict)

        # Government
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
        main_world_upp["government"] = self.getValueRoll(gov_roll, gov_dict)

        # Law level
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
        main_world_upp["law level"] = self.getValueRoll(law_roll, law_dict)

        # Technological level
        tech_dict = {
            15: "Technical maximum Imperial",
            14: "Above average Imperial",
            13: "Above average Imperial",
            12: "Average Imperial",
            11: "Average Imperial",
            10: "Interstellar community",
            9: "Circa 1990 to 2000",
            8: "Circa 1980 to 1989",
            7: "Circa 1970 to 1979",
            6: "Circa 1940 to 1969",
            5: "Circa 1900 to 1939",
            4: "Circa 1860 to 1900",
            3: "Circa 1700 to 1860",
            2: "Circa 1400 to 1700",
            1: "Bronze Age to Middle Ages",
            0: "Stone Age. Primitive"
        }
        #dm calc (calc is short for calculations)
        dm = 0
        star_port_modifiers = {'A': 6, 'B': 4, 'C': 2, 'X': -4}
        dm += star_port_modifiers.get(self.contents.get("star port"), 0)
        if size_roll <= 1: dm += 2
        elif 2 <= size_roll <= 4: dm += 1
        if atmos_roll <= 3 or (atmos_roll >= 10 and atmos_roll != 15): dm += 1
        if hydro_roll in {9, 10}: dm += 1 if hydro_roll == 9 else 2
        if 1 <= pop_roll <= 5: dm += 1
        elif pop_roll == 9: dm += 2
        elif pop_roll == 10: dm += 4
        if gov_roll in {0, 5}: dm += 1
        elif gov_roll == 13: dm -= 2

        tech_roll = max(0, min(random.randint(1, 6) + dm, 15))
        main_world_upp["technological level"] = self.getValueRoll(tech_roll, tech_dict)

        return main_world_upp
    
    def outputDict(self):
        return {
            "name": self.name,
            "system contents": self.contents,
            "main world UPP": self.main_world_upp
        }

star_system = StarSystem()
print(star_system.outputDict())