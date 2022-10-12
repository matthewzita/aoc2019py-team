import easygui
import time
import math


AOCDAY = "12"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

class Vector3D:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

class Moon:

    def __init__(self, position):
        self.position = position
        self.velocity = Vector3D(0, 0, 0)

    def attractedBy(self, other):

        if self.position.x > other.position.x:
            self.velocity.x -= 1
        elif self.position.x < other.position.x:
            self.velocity.x += 1

        if self.position.y > other.position.y:
            self.velocity.y -= 1
        elif self.position.y < other.position.y:
            self.velocity.y += 1

        if self.position.z > other.position.z:
            self.velocity.z -= 1
        elif self.position.z < other.position.z:
            self.velocity.z += 1

    def move(self):
        self.position += self.velocity

    def energy(self):

        potential = abs(self.position.x) + abs(self.position.y) + abs(self.position.z)
        kinetic = abs(self.velocity.x) + abs(self.velocity.y) + abs(self.velocity.z)

        return potential*kinetic

    def __str__(self):
        return f"Position: {self.position.x}, {self.position.y}, {self.position.z}\t Velocity: {self.velocity.x}, {self.velocity.y}, {self.velocity.z}"

def parseLines(lines):

    moons = []

    for line in lines:
        x = int(line[line.find('=')+1: line.find(',')])
        line = line[line.find(',')+1: ]
        y = int(line[line.find('=')+1: line.find(',')])
        line = line[line.find(',')+1: ]
        z = int(line[line.find('=')+1: line.find('>')])

        moons.append(Moon(Vector3D(x, y, z)))

    return moons

def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string
    
    moons = parseLines(lines)

    for i in range(1000):

        for moon in moons:
            for other in moons:
                moon.attractedBy(other)

        for moon in moons:
            moon.move()

    total_energy = 0
    for moon in moons:
        total_energy += moon.energy()

    return(f"Total energy of the system after 1000 steps is {total_energy}") 

def part2(lines):
    # Code the solution to part 2 here, returning the answer as a string
    
    moons = parseLines(lines)

    initial_x = ""
    initial_y = ""
    initial_z = ""

    for moon in moons:
        initial_x += f"{moon.position.x}, {moon.velocity.x}, "
        initial_y += f"{moon.position.y}, {moon.velocity.y}, "
        initial_z += f"{moon.position.z}, {moon.velocity.z}, "

    period_x = 0
    period_y = 0
    period_z = 0

    steps = 0
    while period_x*period_y*period_z == 0:

        for moon in moons:
            for other in moons:
                moon.attractedBy(other)

        for moon in moons:
            moon.move()

        steps += 1

        current_x = ""
        current_y = ""
        current_z = ""

        for moon in moons:
            current_x += f"{moon.position.x}, {moon.velocity.x}, "
            current_y += f"{moon.position.y}, {moon.velocity.y}, "
            current_z += f"{moon.position.z}, {moon.velocity.z}, "

        if initial_x == current_x and period_x == 0:
            period_x = steps

        if initial_y == current_y and period_y == 0:
            period_y = steps

        if initial_z == current_z and period_z == 0:
            period_z = steps

    return(f"It takes {math.lcm(period_x, period_y, period_z)} steps for this system to repeat") 

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