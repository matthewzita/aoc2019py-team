import easygui
import time

AOCDAY = "05"

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

    # def run(self, noun, verb):
    def run(self, inputStream):
        memory = self.program.copy()
        # if noun != None:
        #     memory[1] = noun
        # if verb != None:
        #     memory[2] = verb
        outputStream = []

        programCounter = 0
        
        while memory[programCounter] != 99:

            opCode = memory[programCounter] % 100
            paramA = (memory[programCounter] % 1000) // 100     # floors
            paramB = (memory[programCounter] % 10000) // 1000
            paramC = (memory[programCounter] % 100000) // 10000

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
                elif paramC == 1:
                    memory[programCounter+3] = num1 + num2
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
                elif paramC == 1:
                    memory[programCounter+3] = num1 * num2
                else:
                    print("Error: Bad Parameter C")

                programCounter += 4

            elif opCode == 3:
                if paramA == 0:
                    memory[memory[programCounter+1]] = inputStream.pop()
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
                    else:
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

def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string
    
    computer = Computer(lines[0])

    result = computer.run([1])
    return(f"The last output value was {result[-1]}!")

def part2(lines):
    # Code the solution to part 2 here, returning the answer as a string
    
    computer = Computer(lines[0])

    result = computer.run([5])
    print(result)
    return(f"The last output value was {result[-1]}!")

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