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
    def __init__(self,dir,dis):
        self.dir = dir
        self.dis = dis

def parseLines(lines):
    path1 = []
    path2 = []
    for pair in lines[0].split(","):
        path1.append(Step(pair[0],int(pair[1:])))
    for pair in lines[1].split(","):
        path2.append(Step(pair[0],int(pair[1:])))
    return path1, path2

def manhatthanDistance(cross):
    x = abs(int(cross.split(",")[0]))
    y = abs(int(cross.split(",")[1]))
    return x + y

DIRS = {"U":(0,1),"D":(0,-1),"L":(-1,0),"R":(1,0)}

def findSize(path1, path2):
    x, y, maxX, maxY, minX, minY = 0, 0, 0, 0, 0, 0

    for step in path1:
        x += DIRS[step.dir][0] * step.dis
        y += DIRS[step.dir][1] * step.dis
        maxX = max(x, maxX)
        maxY = max(y, maxY)
        minX = min(x, minX)
        minY = min(y, minY)
    x,y = 0, 0
    for step in path2:
        x += DIRS[step.dir][0] * step.dis
        y += DIRS[step.dir][1] * step.dis
        maxX = max(x, maxX)
        maxY = max(y, maxY)
        minX = min(x, minX)
        minY = min(y, minY)
    size = max([maxX,maxY,abs(minX),abs(minY)])
    return size

def part1(lines):
    path1, path2 = parseLines(lines)
    size = findSize(path1, path2)

    grid = [[False for i in range(size*2+1)] for j in range(size*2+1)]

    x = size
    y = size
    for step in path1:
        for i in range(step.dis):
            x += DIRS[step.dir][0]
            y += DIRS[step.dir][1]
            grid[y][x] = True
    x = size
    y = size
    intersections = []
    for step in path2:
        for i in range(step.dis):
            x += DIRS[step.dir][0]
            y += DIRS[step.dir][1]
            if grid[y][x] == True:
                intersections.append(str(x-size) + "," + str(y-size))
    
    intersections.sort(key=lambda x:manhatthanDistance(x))

    return(f"The closest intersection point is {manhatthanDistance(intersections[0])} away") 

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