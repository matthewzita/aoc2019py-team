import easygui
import time
import math


AOCDAY = "14"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

class Recipe:

    def __init__(self, components, quantity):
        self.components = components
        self.quantity = quantity
        
def parseLines(lines):

    reactions = {}
    for line in lines:
        product = line.split(" ")[-1]
        quantity = int(line.split(" ")[-2])

        components = {}
        for component_string in line.split(" => ")[0].split(", "):
            components[component_string.split(" ")[1]] = int(component_string.split(" ")[0])

        reactions[product] = Recipe(components, quantity)

    return reactions

def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string
    
    reactions = parseLines(lines)
    reactions["ORE"] = Recipe({"ORE": 1}, 1)
    
    required_components = {"FUEL": 1, "ORE": 0}
    leftovers = {}

    while len(required_components) > 1:

        making = list(required_components)[0]
        making_quantity = required_components.pop(making)
        recipe_quantity = reactions[making].quantity

        # Leftovers math
        number_of_reactions = math.ceil(making_quantity/recipe_quantity)
        leftover_quantity = number_of_reactions * recipe_quantity - making_quantity
        leftovers[making] = leftover_quantity

        for component_key in reactions[making].components:
            component_quantity = reactions[making].components[component_key] * number_of_reactions

            if component_key in leftovers:
                component_quantity -= leftovers[component_key]

                if component_quantity >= 0:
                    leftovers.pop(component_key)
                elif component_quantity < 0:
                    leftovers[component_key] = component_quantity*-1
                    component_quantity = 0
                
            if component_quantity > 0:
                if component_key in required_components:
                    required_components[component_key] += component_quantity
                else:
                    required_components[component_key] = component_quantity

    return(f"The amount of ores needed is {required_components['ORE']}.")

def oresNeeded(reactions, fuel_target):

    required_components = {"FUEL": fuel_target, "ORE": 0}
    leftovers = {}

    while len(required_components) > 1:

        making = list(required_components)[0]
        making_quantity = required_components.pop(making)
        recipe_quantity = reactions[making].quantity

        # Leftovers math
        number_of_reactions = math.ceil(making_quantity/recipe_quantity)
        leftover_quantity = number_of_reactions * recipe_quantity - making_quantity
        leftovers[making] = leftover_quantity

        for component_key in reactions[making].components:
            component_quantity = reactions[making].components[component_key] * number_of_reactions

            if component_key in leftovers:
                component_quantity -= leftovers[component_key]

                if component_quantity >= 0:
                    leftovers.pop(component_key)
                elif component_quantity < 0:
                    leftovers[component_key] = component_quantity*-1
                    component_quantity = 0
                
            if component_quantity > 0:
                if component_key in required_components:
                    required_components[component_key] += component_quantity
                else:
                    required_components[component_key] = component_quantity

    return required_components['ORE']

def part2(lines):
    # Code the solution to part 2 here, returning the answer as a string
    
    reactions = parseLines(lines)
    reactions["ORE"] = Recipe({"ORE": 1}, 1)
    

    target_ores = 1000000000000
    closest_over = 1000000000000
    closest_under = 1
    current = closest_under
    while closest_over - closest_under != 1:
        result = oresNeeded(reactions, current)

        if result > target_ores:
            closest_over = min(closest_over, current)
        else:
            closest_under = max(closest_under, current)

        current = (current*target_ores)//result
        if current == closest_under:
            current += 1
    
    return(f"The maximum amount of FUEL that can be produced is {closest_under}.")

def main ():
    # Opens a dialog to select the input file
    # Times and runs both solutions
    # Prints the results
    fileName = easygui.fileopenbox(default=f"./"+AOCDAY+"/"+"*.txt")
    if fileName == None:
        print("ERROR: No file selected.")
        return
    lines = readFile(fileName)
    p1StartTime = time.perf_counter()
    p1Result = part1(lines)
    p1EndTime = time.perf_counter()
    p2StartTime = time.perf_counter()
    p2Result = part2(lines)
    p2EndTime = time.perf_counter()
    print("Advent of Code 2019 Day " + AOCDAY + ":")
    print("  Part 1 Execution Time: " + str(round((p1EndTime - p1StartTime)*1000,3)) + " milliseconds")
    print("  Part 1 Result: " + str(p1Result))
    print("  Part 2 Execution Time: " + str(round((p2EndTime - p2StartTime)*1000,3)) + " milliseconds")
    print("  Part 2 Result: " + str(p2Result))

main()