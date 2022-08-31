import easygui
import time
import itertools

AOCDAY = "07"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

class Computer:
    def __init__(self, programString):
        self.program = [int(number) for number in programString.split(",")]

    def run(self,inputStream):

        memory = self.program.copy()
        outputStream = []
        programCounter = 0
        
        while memory[programCounter] != 99:
            opCode = memory[programCounter] % 100
            paramA = memory[programCounter] % 1000 // 100
            paramB = memory[programCounter] % 10000 // 1000
            paramC = memory[programCounter] % 100000 // 10000

            if opCode == 1:
                if paramA == 0:
                    num1 = memory[memory[programCounter+1]]
                elif paramA == 1:
                    num1 = memory[programCounter+1]
                else:
                    print("Error: Bad Parameter A")
                if paramB == 0:
                    num2 = memory[memory[programCounter+2]]
                elif paramB == 1:
                    num2 = memory[programCounter+2]
                else:
                    print("Error: Bad Parameter B")
                if paramC == 0:
                    memory[memory[programCounter+3]] = num1 + num2
                else:
                    print("Error: Bad Parameter C")
                programCounter += 4
            elif opCode == 2:
                if paramA == 0:
                    num1 = memory[memory[programCounter+1]]
                elif paramA == 1:
                    num1 = memory[programCounter+1]
                else:
                    print("Error: Bad Parameter A")
                if paramB == 0:
                    num2 = memory[memory[programCounter+2]]
                elif paramB == 1:
                    num2 = memory[programCounter+2]
                else:
                    print("Error: Bad Parameter B")
                if paramC == 0:
                    memory[memory[programCounter+3]] = num1 * num2
                else:
                    print("Error: Bad Parameter C")
                programCounter += 4
            elif opCode == 3:
                if paramA == 0:
                    memory[memory[programCounter+1]] = inputStream.pop(0)
                else:
                    print("Error: Bad Parameter A")
                programCounter += 2
                
            elif opCode == 4:
                if paramA == 0:
                    outputStream.append(memory[memory[programCounter+1]])
                elif paramA == 1:
                    outputStream.append(memory[programCounter+1])
                else:
                    print("Error: Bad Parameter A")
                programCounter += 2
            elif opCode == 5 or opCode == 6:
                if paramA == 0:
                    num1 = memory[memory[programCounter+1]]
                elif paramA == 1:
                    num1 = memory[programCounter+1]
                else:
                    print("Error: Bad Parameter A")
                if paramB == 0:
                    address = memory[memory[programCounter+2]]
                elif paramB == 1:
                    address = memory[programCounter+2]
                else:
                    print("Error: Bad Parameter B")
                if opCode == 5:
                    if num1 != 0:
                        programCounter = address
                    else:
                        programCounter += 3
                else:
                    if num1 == 0:
                        programCounter = address
                    else:
                        programCounter += 3

            elif opCode == 7 or opCode == 8:
                if paramA == 0:
                    num1 = memory[memory[programCounter+1]]
                elif paramA == 1:
                    num1 = memory[programCounter+1]
                else:
                    print("Error: Bad Parameter A")
                if paramB == 0:
                    num2 = memory[memory[programCounter+2]]
                elif paramB == 1:
                    num2 = memory[programCounter+2]
                else:
                    print("Error: Bad Parameter B")
                if paramC == 0:
                    if opCode == 7:
                        if num1 < num2:
                            memory[memory[programCounter+3]] = 1
                        else:
                            memory[memory[programCounter+3]] = 0
                    if opCode == 8:
                        if num1 == num2:
                            memory[memory[programCounter+3]] = 1
                        else:
                            memory[memory[programCounter+3]] = 0
                else:
                    print("Error: Bad Parameter C")

                programCounter += 4

            else:
                print("Error: Unknown opcode")
                break

        return outputStream

class ComputerState:
    def __init__(self, programString):
        self.memory = [int(number) for number in programString.split(",")]
        self.programCounter = 0
        
    def run(self,inputStream):

        outputStream = []
        
        opCode = self.memory[self.programCounter]
        while self.memory[self.programCounter] != 99:
            opCode = self.memory[self.programCounter] % 100
            paramA = self.memory[self.programCounter] % 1000 // 100
            paramB = self.memory[self.programCounter] % 10000 // 1000
            paramC = self.memory[self.programCounter] % 100000 // 10000

            if opCode == 1:
                if paramA == 0:
                    num1 = self.memory[self.memory[self.programCounter+1]]
                elif paramA == 1:
                    num1 = self.memory[self.programCounter+1]
                else:
                    print("Error: Bad Parameter A")
                if paramB == 0:
                    num2 = self.memory[self.memory[self.programCounter+2]]
                elif paramB == 1:
                    num2 = self.memory[self.programCounter+2]
                else:
                    print("Error: Bad Parameter B")
                if paramC == 0:
                    self.memory[self.memory[self.programCounter+3]] = num1 + num2
                else:
                    print("Error: Bad Parameter C")
                self.programCounter += 4
            elif opCode == 2:
                if paramA == 0:
                    num1 = self.memory[self.memory[self.programCounter+1]]
                elif paramA == 1:
                    num1 = self.memory[self.programCounter+1]
                else:
                    print("Error: Bad Parameter A")
                if paramB == 0:
                    num2 = self.memory[self.memory[self.programCounter+2]]
                elif paramB == 1:
                    num2 = self.memory[self.programCounter+2]
                else:
                    print("Error: Bad Parameter B")
                if paramC == 0:
                    self.memory[self.memory[self.programCounter+3]] = num1 * num2
                else:
                    print("Error: Bad Parameter C")
                self.programCounter += 4
            elif opCode == 3:
                if paramA == 0:
                    if len(inputStream) < 1:
                        return outputStream, opCode
                    self.memory[self.memory[self.programCounter+1]] = inputStream.pop(0)
                else:
                    print("Error: Bad Parameter A")
                self.programCounter += 2
                
            elif opCode == 4:
                if paramA == 0:
                    outputStream.append(self.memory[self.memory[self.programCounter+1]])
                elif paramA == 1:
                    outputStream.append(self.memory[self.programCounter+1])
                else:
                    print("Error: Bad Parameter A")
                self.programCounter += 2
            elif opCode == 5 or opCode == 6:
                if paramA == 0:
                    num1 = self.memory[self.memory[self.programCounter+1]]
                elif paramA == 1:
                    num1 = self.memory[self.programCounter+1]
                else:
                    print("Error: Bad Parameter A")
                if paramB == 0:
                    address = self.memory[self.memory[self.programCounter+2]]
                elif paramB == 1:
                    address = self.memory[self.programCounter+2]
                else:
                    print("Error: Bad Parameter B")
                if opCode == 5:
                    if num1 != 0:
                        self.programCounter = address
                    else:
                        self.programCounter += 3
                else:
                    if num1 == 0:
                        self.programCounter = address
                    else:
                        self.programCounter += 3

            elif opCode == 7 or opCode == 8:
                if paramA == 0:
                    num1 = self.memory[self.memory[self.programCounter+1]]
                elif paramA == 1:
                    num1 = self.memory[self.programCounter+1]
                else:
                    print("Error: Bad Parameter A")
                if paramB == 0:
                    num2 = self.memory[self.memory[self.programCounter+2]]
                elif paramB == 1:
                    num2 = self.memory[self.programCounter+2]
                else:
                    print("Error: Bad Parameter B")
                if paramC == 0:
                    if opCode == 7:
                        if num1 < num2:
                            self.memory[self.memory[self.programCounter+3]] = 1
                        else:
                            self.memory[self.memory[self.programCounter+3]] = 0
                    if opCode == 8:
                        if num1 == num2:
                            self.memory[self.memory[self.programCounter+3]] = 1
                        else:
                            self.memory[self.memory[self.programCounter+3]] = 0
                else:
                    print("Error: Bad Parameter C")

                self.programCounter += 4

            else:
                print("Error: Unknown opcode")
                break

        opCode = self.memory[self.programCounter]
        return outputStream, opCode

def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string
    
    amplifiers = [ComputerState(lines[0]) for amplifer in range(5)]
    combinations = list(itertools.permutations([0,1,2,3,4]))

    maxResult = 0

    for phase in combinations:

        doneCount = 0
        amplifiers = [ComputerState(lines[0]) for amplifer in range(5)]
        
        # Run the program in each amplifier
        signal = 0
        for i in range(5):
            signal, opCode = amplifiers[i].run([phase[i], signal])
            signal = signal[-1]
            if opCode == 99:
                doneCount += 1

        while doneCount < 5:
            for i in range(5):
                signal, opCode = amplifiers[i].run([signal])
                signal = signal[-1]

                if opCode == 99:
                    doneCount += 1

        maxResult = max(maxResult, signal)

    return(f"The last output value was {maxResult}!")

def part2(lines):

    amplifiers = [ComputerState(lines[0]) for amplifer in range(5)]
    combinations = list(itertools.permutations([5,6,7,8,9]))

    maxResult = 0

    for phase in combinations:

        doneCount = 0
        amplifiers = [ComputerState(lines[0]) for amplifer in range(5)]
        
        # Run the program in each amplifier
        signal = 0
        for i in range(5):
            signal, opCode = amplifiers[i].run([phase[i], signal])
            signal = signal[-1]
            if opCode == 99:
                doneCount += 1

        while doneCount < 5:
            for i in range(5):
                signal, opCode = amplifiers[i].run([signal])
                signal = signal[-1]

                if opCode == 99:
                    doneCount += 1

        maxResult = max(maxResult, signal)

    return(f"The last output value was {maxResult}!")

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