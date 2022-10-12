import easygui
import time

AOCDAY = "11"

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

class RunResult:
    def __init__(self, outputStream, opCode):
        self.outputStream = outputStream
        self.opCode = opCode

class ComputerState2:
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

class Pixel:
    def __init__(self,x,y,colour=0):
        self.x = x
        self.y = y
        self.colour = colour
    def __str__(self):
        return f"({self.x},{self.y})"
    def __repr__(self):
        return f"({self.x},{self.y})"
    def __eq__(self,other):
        return self.x == other.x and self.y == other.y
    def __add__(self,other):
        return Pixel(self.x + other.x, self.y+other.y, self.colour)

def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string
    computer = ComputerState2(lines[0])
    # output = computer.run([0])
    paintedPixels = []
    computerState = 3
    currentPixel = Pixel(0,0,0)
    directions = [Pixel(0,1),Pixel(1,0),Pixel(0,-1),Pixel(-1,0)]
    currentDirection = 0
    while computerState == 3:
    # for i in range(10):
        result = computer.run([currentPixel.colour])
        output = result.outputStream
        computerState = result.opCode
        currentPixel.colour = output[0]
        if currentPixel not in paintedPixels:
            paintedPixels.append(currentPixel)
        if output[1] == 1:
            currentDirection = (currentDirection + 1) % 4
        else:
            currentDirection = (currentDirection - 1) % 4
        newPixel = currentPixel + directions[currentDirection]
        if newPixel not in paintedPixels:
            currentPixel = newPixel
            newPixel.colour = 0
        else:
            currentPixel = paintedPixels[paintedPixels.index(newPixel)]
    return(f"The number of painted pixels is {len(paintedPixels)}")

def part2(lines):
    # Code the solution to part 2 here, returning the answer as a string
    computer = ComputerState2(lines[0])
    paintedPixels = []
    computerState = 3
    currentPixel = Pixel(0,0,1)
    directions = [Pixel(0,1),Pixel(1,0),Pixel(0,-1),Pixel(-1,0)]
    currentDirection = 0
    while computerState == 3:
        result = computer.run([currentPixel.colour])
        output = result.outputStream
        computerState = result.opCode
        currentPixel.colour = output[0]
        if currentPixel not in paintedPixels:
            paintedPixels.append(currentPixel)
        if output[1] == 1:
            currentDirection = (currentDirection + 1) % 4
        else:
            currentDirection = (currentDirection - 1) % 4
        newPixel = currentPixel + directions[currentDirection]
        if newPixel not in paintedPixels:
            currentPixel = newPixel
            newPixel.colour = 0
        else:
            currentPixel = paintedPixels[paintedPixels.index(newPixel)]
    whitePixels = []
    for pixel in paintedPixels:
        if pixel.colour == 1:
            whitePixels.append(pixel)
    minX = 0
    maxX = 0
    minY = 0
    maxY = 0
    for pixel in whitePixels:
        minX = min(minX, pixel.x)
        maxX = max(maxX, pixel.x)
        minY = min(minY, pixel.y)
        maxY = max(maxY, pixel.y)

    for y in range(maxY, minY - 1, -1):
        printLine = ""
        for x in range(minX, maxX+1, 1):
            if Pixel(x, y, 0) in whitePixels:
                printLine += "██"
            else:
                printLine += "  "
        print(printLine)

    return(f"Read the code above.")

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