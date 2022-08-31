import easygui
import time
import math


AOCDAY = "06"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

class Node:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []

    """
    Check if target exists
    """
    def contains(self, target):
        exists = False

        if self.name == target:
            return True

        # recursively check for taret exists
        for child in self.children:
            if child.contains(target):
                exists = True

        return exists

    def add_child(self, name, parent):
        self.children.append(Node(name, parent))

    def get_node(self, name):

        if self.name == name:
            return self
        
        for child in self.children:
            result = child.get_node(name)

            if result != None:
                return result

        return None

    def orbit_count(self, length):
        total = 0

        for child in self.children:
            total += child.orbit_count(length+1)
        
        total += length

        return total

    def find_you_san(self):

        for child in self.children:

            # print(self.name)
            # print("YOU: "+str(child.contains("YOU")))
            # print("SAN: "+str(child.contains("SAN")))

            if child.contains("YOU") and not child.contains("SAN"):
                return self
            
            if child.contains("YOU") and child.contains("SAN"):
                return child.find_you_san()
    
        return None

    def distance_to(self, target, length):

        if self.name == target:
            return length

        for child in self.children:
            if child.contains(target):
                return child.distance_to(target, length+1)

        return None

def parse_lines(lines):

    orbits = []
    for line in lines:
        orbits.append(line.split(")"))

    return orbits

def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string

    # Root node (COM)
    tree = Node("COM", None)

    orbits = parse_lines(lines)

    while len(orbits) > 0:
        found_one = False

        for i, orbit in enumerate(orbits):

            if not found_one:

                if tree.contains(orbit[0]):
                    parent = tree.get_node(orbit[0])
                    parent.add_child(orbit[1], parent)
                    orbits.pop(i)

    return(f"The total number of orbits in the system is {tree.orbit_count(0)}") 

def part2(lines):
    # Code the solution to part 2 here, returning the answer as a string
    
    # Root node (COM)
    tree = Node("COM", None)

    orbits = parse_lines(lines)

    while len(orbits) > 0:
        remove_list = []
        for i, orbit in enumerate(orbits):
            if tree.contains(orbit[0]):
                parent = tree.get_node(orbit[0])
                parent.add_child(orbit[1], parent)
                remove_list.append(i)
        for i in reversed(remove_list):
            orbits.pop(i)

    intersection = tree.find_you_san()

    total_distance = intersection.distance_to("YOU", 0) + intersection.distance_to("SAN", 0) - 2

    return(f"The distance from YOU to SAN is {total_distance}")

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