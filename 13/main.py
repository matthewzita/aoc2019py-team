import easygui
import time
import os

AOCDAY = "13"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

class RunResult:
    def __init__(self, outputStream, opCode):
        self.outputStream = outputStream
        self.opCode = opCode

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

        INSTRUCTIONLENGTHS = {
            '1': 4,
            '2': 4,
            '3': 2,
            '4': 2,
            '5': 3,
            '6': 3,
            '7': 4,
            '8': 4,
            '9': 2
        }

        opCode = self.memory[self.programCounter] % 100
        while self.memory[self.programCounter] != 99:

            opCode = self.memory[self.programCounter] % 100
            paramA = self.memory[self.programCounter] % 1000 // 100
            paramB = self.memory[self.programCounter] % 10000 // 1000
            paramC = self.memory[self.programCounter] % 100000 // 10000

            addressA = 0
            if paramA == 0:
                addressA = self.memory[self.programCounter+1]
            elif paramA == 1:
                addressA = self.programCounter+1
            elif paramA == 2:
                addressA = self.memory[self.programCounter+1] + self.offset
            self.memCheck(addressA)

            if(INSTRUCTIONLENGTHS[str(opCode)] >= 3):
                addressB = 0
                if paramB == 0:
                    addressB = self.memory[self.programCounter+2]
                elif paramB == 1:
                    addressB = self.programCounter+2
                elif paramB == 2:
                    addressB = self.memory[self.programCounter+2] + self.offset
                self.memCheck(addressB)

            if(INSTRUCTIONLENGTHS[str(opCode)] >= 4):
                addressC = 0
                if paramC == 0:
                    addressC = self.memory[self.programCounter+3]
                elif paramC == 1:
                    addressC = self.programCounter+3
                elif paramC == 2:
                    addressC = self.memory[self.programCounter+3] + self.offset
                self.memCheck(addressC)

            # print(self.programCounter, opCode, paramA, paramB, paramC, addressA, addressB, addressC)
            # print(self.memory)

            if opCode == 1:
                self.memory[addressC] = self.memory[addressA] + self.memory[addressB]

            elif opCode == 2:
                self.memory[addressC] = self.memory[addressA] * self.memory[addressB]

            elif opCode == 3:
                if len(inputStream) < 1:
                    return RunResult(outputStream,opCode)
                self.memory[addressA] = inputStream.pop(0)

            elif opCode == 4:
                outputStream.append(self.memory[addressA])

            elif opCode == 5:
                if self.memory[addressA] != 0:
                    self.programCounter = self.memory[addressB] - 3

            elif opCode == 6:
                if self.memory[addressA] == 0:
                    self.programCounter = self.memory[addressB] - 3

            elif opCode == 7:
                if self.memory[addressA] < self.memory[addressB]:
                    self.memory[addressC] = 1
                else:
                    self.memory[addressC] = 0

            elif opCode == 8:
                if self.memory[addressA] == self.memory[addressB]:
                    self.memory[addressC] = 1
                else:
                    self.memory[addressC] = 0

            elif opCode == 9:
                self.offset += self.memory[addressA]

            else:
                print("Error: Unknown opcode")
                break

            self.programCounter += INSTRUCTIONLENGTHS[str(opCode)]

        opCode = self.memory[self.programCounter] % 100
        return RunResult(outputStream,opCode)

def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string
    computer = ComputerState(lines[0])
    result = computer.run([])

    output = result.outputStream

    max_x = max_y = 0
    block_count = 0
    for i in range(0, len(output), 3):
        max_x = max(max_x, output[i])
        max_y = max(max_y, output[i+1])
        if output[i+2] == 2:
            block_count += 1

    screen = [[0 for i in range(max_x+1)] for j in range(max_y+1)]

    sprites = {0: " ", 1: "█", 2: "▒", 3: "▀", 4: "o"}

    for i in range(0, len(output), 3):
        screen[output[i+1]][output[i]] = sprites[output[i+2]]

    return f"There are {block_count} blocks on the screen."

def updateScreen(screen, output):
    sprites = {0: " ", 1: "█", 2: "▒", 3: "▀", 4: "o"}

    # BUILD SCREEN
    for i in range(0, len(output), 3):
        if output[i] != -1:
            if output[i+2] == 4: # check if it's a ball
                ball_x = output[i]
            if output[i+2] == 3: # check if it's a paddle
                paddle_x = output[i]
            screen[output[i+1]][output[i]] = sprites[output[i+2]]

def printScreen(screen, score):
    # PRINT SCREEN
    for line in screen:
        print("".join(line))

    # PRINT SCORE
    print(f"Score: {score}")

def part2(lines):
    # Code the solution to part 2 here, returning the answer as a string
    computer = ComputerState(lines[0])

    computer.memory[0] = 2

    result = computer.run([]) # run empty first for computer to wait for input

    output = result.outputStream

    max_x = max_y = 0
    score = 0
    for i in range(0, len(output), 3):
        max_x = max(max_x, output[i])
        max_y = max(max_y, output[i+1])

    screen = [[0 for i in range(max_x+1)] for j in range(max_y+1)]


    ball_x = paddle_x = 0
    # BUILD SCREEN
    for i in range(0, len(output), 3):
        if output[i] == -1:
            score = output[i+2]
        else:
            if output[i+2] == 4: # check if it's a ball
                ball_x = output[i]
            if output[i+2] == 3: # check if it's a paddle
                paddle_x = output[i]

    # # Uncomment to watch gameplay
    # os.system("cls") # clear console
    # updateScreen(screen, output)
    # printScreen(screen, score)

    while result.opCode != 99:

        if ball_x < paddle_x:
            controls = -1
        elif ball_x > paddle_x:
            controls = 1
        else:
            controls = 0

        # # Uncomment to play by hand
        # controls = int(input("-1: Left, 0: Neutral 1: Right -> "))

        result = computer.run([controls])
        output = result.outputStream

        # BUILD SCREEN
        for i in range(0, len(output), 3):
            if output[i] == -1:
                score = output[i+2]
            else:
                if output[i+2] == 4: # check if it's a ball
                    ball_x = output[i]
                if output[i+2] == 3: # check if it's a paddle
                    paddle_x = output[i]

        # # Uncomment to watch gameplay
        # os.system("cls") # clear console
        # updateScreen(screen, output)
        # printScreen(screen, score)

    return(f"The final score after destroying all blocks is {score}")

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