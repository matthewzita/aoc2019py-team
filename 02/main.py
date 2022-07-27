import easygui
import time
import math


AOCDAY = "02"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines





def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string
    
    memory=[]
    programCounter = 0 
    for number in lines[0].split(","):
        memory.append(int(number))

    memory[1] = 12
    memory[2] = 2

    while memory[programCounter] != 99:
       
        if memory[programCounter] == 1:
            memory[memory[programCounter+3]] = memory[memory[programCounter+1]] + memory[memory[programCounter+2]]
            programCounter += 4

        elif memory[programCounter] == 2:
            memory[memory[programCounter+3]] = memory[memory[programCounter+1]] * memory[memory[programCounter+2]]
            programCounter += 4

    return(f"The value at memory address 0 is {memory[0]}!") 

def runComputer(memory, inputA, inputB):
    programCounter = 0 

    memory[1] = inputA
    memory[2] = inputB

    while memory[programCounter] != 99:
       
        if memory[programCounter] == 1:
            memory[memory[programCounter+3]] = memory[memory[programCounter+1]] + memory[memory[programCounter+2]]
            programCounter += 4

        elif memory[programCounter] == 2:
            memory[memory[programCounter+3]] = memory[memory[programCounter+1]] * memory[memory[programCounter+2]]
            programCounter += 4
    return memory[0]

def part2(lines):
    # Code the solution to part 2 here, returning the answer as a string
    
    TARGET = 19690720 #all caps b/c it is a constant (convention)

    for i in range(100):
        for j in range(100):
            memory=[]
            for number in lines[0].split(","):
                memory.append(int(number))
            if runComputer(memory,i,j) == TARGET:
                return(f"The program that produces the desired result is {100*i+j}")
            

    return(f"ANSWER HERE")

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