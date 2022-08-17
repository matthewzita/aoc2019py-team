import easygui
import time
import math


AOCDAY = "04"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def part1Validate(num):
    numString = str(num)

    # check for ascending
    ascending = True
    for i in range(len(numString)-1):
        if numString[i] > numString[i+1]:
            ascending = False

    adjacent = False
    for i in range(len(numString)-1):
        if numString[i] == numString[i+1]:
            adjacent = True

    return ascending and adjacent
    

def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string
    startNum = int(lines[0].split("-")[0])
    endNum = int(lines[0].split("-")[1])

    validateCount = 0
    for num in range(startNum, endNum+1):
        if part1Validate(num):
            validateCount += 1
    

    return(f"There are {validateCount} different passwords within the range") 

def part2Validate(num):
    numString = str(num)
    ascending = True
    for i in range(len(numString)-1):
        if numString[i] > numString[i+1]:
            ascending = False
    
    adjacent = False
    for i in range(1,len(numString)-2):
        if numString[i] == numString[i+1] and numString[i] != numString[i+2] and numString[i] != numString[i-1]:
            adjacent = True
    
    if len(numString) > 2:
        if numString[0] == numString[1] and numString[0] != numString[2]:
            adjacent = True
        if numString[-1] == numString[-2] and numString[-1] != numString[-3]:
            adjacent = True
    elif len(numString) == 2:
        if numString[0] == numString[1]:
            adjacent = True
    else:
        return False

    return ascending and adjacent

def part2(lines):
    # Code the solution to part 2 here, returning the answer as a string
    startNum = int(lines[0].split("-")[0])
    endNum = int(lines[0].split("-")[1])

    validateCount = 0
    for num in range(startNum, endNum+1):
        if part2Validate(num):
            validateCount += 1
    

    return(f"There are {validateCount} different passwords within the range")

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