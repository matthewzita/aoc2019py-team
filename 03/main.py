import easygui
import time
import math


AOCDAY = "03"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

class Step:
    def __init__(self, dir, dis):
        self.dir = dir
        self.dis = dis

def parseLines(lines):
    path1 = []
    path2 = []
    for pair in lines[0].split(","):
        path1.append(Step(pair[0], int(pair[1:])))

    for pair in lines[1].split(","):
        path2.append(Step(pair[0], int(pair[1:])))

    return path1, path2

def manhattanDistance(point):

    x = abs(int(point.split(",")[0]))
    y = abs(int(point.split(",")[1]))

    return x+y

def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string
    
    path1, path2 = parseLines(lines)

    path1_points = []
    x = 0
    y = 0
    for step in path1:
        for i in range(step.dis):

            if step.dir == "U":
                y += 1

            elif step.dir == "D":
                y -= 1

            elif step.dir == "R":
                x += 1

            elif step.dir == "L":
                x -= 1
            
            path1_points.append(f"{x},{y}")

    print(path1_points)

    crosspoints = []
    path2_points = []
    x = 0
    y = 0
    for step in path2:
        for i in range(step.dis):

            if step.dir == "U":
                y += 1

            elif step.dir == "D":
                y -= 1

            elif step.dir == "R":
                x += 1

            elif step.dir == "L":
                x -= 1
            
            path2_points.append(f"{x},{y}")

            if path2_points[-1] in path1_points:
                crosspoints.append(path2_points[-1])
                print(path2_points[-1])
        
    crosspoints.sort(key=manhattanDistance)

    return f"The manhattan distance of the closest crosspoint is {manhattanDistance(crosspoints[0])} away"

def part2(lines):
    # Code the solution to part 2 here, returning the answer as a string
    
    

    pass

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