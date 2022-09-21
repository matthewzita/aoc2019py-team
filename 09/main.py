import easygui
import time
import itertools
import math



AOCDAY = "09"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

class ComputerState:
    def __init__(self, programString):
        self.memory = [int(number) for number in programString.split(",")]
        self.programCounter = 0
        self.offset = 0

    def memCheck(self, address):

        while len(self.memory) <= address:
            self.memory.append(0)

    def run(self,inputStream):

        outputStream = []

        opCode = self.memory[self.programCounter]
        while self.memory[self.programCounter] != 99:
            opCode = self.memory[self.programCounter] % 100
            paramA = self.memory[self.programCounter] % 1000 // 100
            paramB = self.memory[self.programCounter] % 10000 // 1000
            paramC = self.memory[self.programCounter] % 100000 // 10000

            self.memCheck(self.programCounter+3)
            address = 0
            if paramA == 0:
                address = self.memory[self.programCounter+1]
            elif paramA == 2:
                address = self.memory[self.programCounter+1] + self.offset
            self.memCheck(address)

            if paramB == 0:
                address = self.memory[self.programCounter+2]
            elif paramB == 2:
                address = self.memory[self.programCounter+2] + self.offset
            self.memCheck(address)

            if paramC == 0:
                address = self.memory[self.programCounter+3]
            elif paramC == 2:
                address = self.memory[self.programCounter+3] + self.offset
            self.memCheck(address)

            if opCode == 1:
                
                if paramA == 0:
                    num1 = self.memory[self.memory[self.programCounter+1]]
                elif paramA == 1:
                    num1 = self.memory[self.programCounter+1]
                elif paramA == 2:
                    num1 = self.memory[self.memory[self.programCounter+1] + self.offset]
                else:
                    print("Error: Bad Parameter A")
                if paramB == 0:
                    num2 = self.memory[self.memory[self.programCounter+2]]
                elif paramB == 1:
                    num2 = self.memory[self.programCounter+2]
                elif paramB == 2:
                    num2 = self.memory[self.memory[self.programCounter+2] + self.offset]
                else:
                    print("Error: Bad Parameter B")
                if paramC == 0:
                    self.memory[self.memory[self.programCounter+3]] = num1 + num2
                elif paramC == 2:
                    self.memory[self.memory[self.programCounter+3] + self.offset] = num1 + num2
                else:
                    print("Error: Bad Parameter C")
                self.programCounter += 4
            elif opCode == 2:
                if paramA == 0:
                    num1 = self.memory[self.memory[self.programCounter+1]]
                elif paramA == 1:
                    num1 = self.memory[self.programCounter+1]
                elif paramA == 2:
                    num1 = self.memory[self.memory[self.programCounter+1] + self.offset]
                else:
                    print("Error: Bad Parameter A")
                if paramB == 0:
                    num2 = self.memory[self.memory[self.programCounter+2]]
                elif paramB == 1:
                    num2 = self.memory[self.programCounter+2]
                elif paramB == 2:
                    num2 = self.memory[self.memory[self.programCounter+2] + self.offset]
                else:
                    print("Error: Bad Parameter B")
                if paramC == 0:
                    self.memory[self.memory[self.programCounter+3]] = num1 * num2
                elif paramC == 2:
                    self.memory[self.memory[self.programCounter+3] + self.offset] = num1 * num2
                else:
                    print("Error: Bad Parameter C")
                self.programCounter += 4
            elif opCode == 3:
                if paramA == 0:
                    if len(inputStream) < 1:
                        return outputStream,opCode
                    self.memory[self.memory[self.programCounter+1]] = inputStream.pop(0)
                elif paramA == 2:
                    if len(inputStream) < 1:
                        return outputStream,opCode
                    self.memory[self.memory[self.programCounter+1] + self.offset] = inputStream.pop(0)
                else:
                    print("Error: Bad Parameter A")
                self.programCounter += 2
                
            elif opCode == 4:
                if paramA == 0:
                    outputStream.append(self.memory[self.memory[self.programCounter+1]])
                elif paramA == 1:
                    outputStream.append(self.memory[self.programCounter+1])
                elif paramA == 2:
                    outputStream.append(self.memory[self.memory[self.programCounter+1] + self.offset])
                else:
                    print("Error: Bad Parameter A")
                self.programCounter += 2
            elif opCode == 5 or opCode == 6:
                if paramA == 0:
                    num1 = self.memory[self.memory[self.programCounter+1]]
                elif paramA == 1:
                    num1 = self.memory[self.programCounter+1]
                elif paramA == 2:
                    num1 = self.memory[self.memory[self.programCounter+1] + self.offset]
                else:
                    print("Error: Bad Parameter A")
                if paramB == 0:
                    address = self.memory[self.memory[self.programCounter+2]]
                elif paramB == 1:
                    address = self.memory[self.programCounter+2]
                elif paramB == 2:
                    address = self.memory[self.memory[self.programCounter+2] + self.offset]
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
                elif paramA == 2:
                    num1 = self.memory[self.memory[self.programCounter+1] + self.offset]
                else:
                    print("Error: Bad Parameter A")
                if paramB == 0:
                    num2 = self.memory[self.memory[self.programCounter+2]]
                elif paramB == 1:
                    num2 = self.memory[self.programCounter+2]
                elif paramB == 2:
                    num2 = self.memory[self.memory[self.programCounter+2] + self.offset]
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
                elif paramC == 2:
                    if opCode == 7:
                        if num1 < num2:
                            self.memory[self.memory[self.programCounter+3] + self.offset] = 1
                        else:
                            self.memory[self.memory[self.programCounter+3] + self.offset] = 0
                    if opCode == 8:
                        if num1 == num2:
                            self.memory[self.memory[self.programCounter+3] + self.offset] = 1
                        else:
                            self.memory[self.memory[self.programCounter+3] + self.offset] = 0
                else:
                    print("Error: Bad Parameter C")

                self.programCounter += 4

            elif opCode == 9:
                if paramA == 0:
                    self.offset += self.memory[self.memory[self.programCounter+1]]
                elif paramA == 1:
                    self.offset += self.memory[self.programCounter+1]
                elif paramA == 2:
                    self.offset += self.memory[self.memory[self.programCounter+1] + self.offset]
                else:
                    print("Error: Bad Parameter A")
                self.programCounter += 2

            else:
                print("Error: Unknown opcode")
                break
        opCode = self.memory[self.programCounter]
        return outputStream,opCode

def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string
    
    computer = ComputerState(lines[0])

    output = computer.run([1])[0][0]
    
    return(f"The BOOST keycode of the validation program is {output}")


def part2(lines):
    # Code the solution to part 1 here, returning the answer as a string

    computer = ComputerState(lines[0])

    output = computer.run([2])[0][0]
    
    return(f"The coordinates of the distress signal are {output}")

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