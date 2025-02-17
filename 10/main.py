from tkinter import N
import easygui
import time
import math


AOCDAY = "10"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def slopeTo(self, other):

        if (other.x - self.x) == 0:
            return -99999999

        return (other.y - self.y) / (other.x - self.x)

    def angleTo(self, other):
        angle = math.atan2(other.y - self.y, other.x - self.x)
        angle = math.degrees(angle) + 90

        if angle < 0:
            angle += 360

        return angle

    def distanceTo(self, other):
        return abs(other.x - self.x) + abs(other.y - self.y)

    def __eq__(self, other):
        return ((self.x, self.y) == (other.x, other.y))

    def __ne__(self, other):
        return ((self.x, self.y) != (other.x, other.y))

    def __str__(self):
        return f"({self.x}, {self.y})"

class Scanner(Point):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.scanned = []
        self.scan_count = 0
        self.destroy_count = 0

    def printScanned(self, upper_bound):
        print("\nScanned asteroids:")
        for i, asteroid in enumerate(self.scanned):
            if i == upper_bound:
                return
            print(f"COORDS: {asteroid}  ANGLE: {asteroid.angle} DIST: {asteroid.distance}")

    def scan(self, asteroids):

        self.scanned = []
        for asteroid in asteroids:

            if self == asteroid:
                continue

            angle = self.angleTo(asteroid)
            distance = self.distanceTo(asteroid)

            just_scanned = self.ScannedAsteroid(asteroid.x, asteroid.y, angle, distance)

            can_add = True
            for i, scanned_asteroid in enumerate(self.scanned):
                if (just_scanned.angle == scanned_asteroid.angle):

                    if just_scanned.distance < scanned_asteroid.distance:
                        self.scanned.pop(i)
                        break
                    else:
                        can_add = False
            
            if can_add:
                self.scanned.append(just_scanned)

        self.scanned.sort()
        self.scanned_count = len(self.scanned)

    def laser(self, asteroids, stop_count):

        last_destroyed = None
        for i in range(len(self.scanned)):
            self.destroy_count += 1

            if self.destroy_count == stop_count:
                self.scanned = self.scanned[:i+1]
                last_destroyed = self.scanned[-1]

        aftermath = []
        for asteroid in asteroids:
            if asteroid not in self.scanned:
                aftermath.append(asteroid)

        return aftermath, last_destroyed

    class ScannedAsteroid(Point):

        def __init__(self, x, y, angle, distance):
            super().__init__(x, y)
            self.angle = angle
            self.distance = distance

        def __eq__(self, other):

            if type(other) is Point:
                return super().__eq__(other)

            return self.angle == other.angle

        def __lt__(self, other):

            if self.angle == other.angle:
                return self.distance < other.distance

            return (self.angle < other.angle)

        def __gt__(self, other):

            if self.angle == other.angle:
                return self.distance > other.distance

            return (self.angle > other.angle)

def parseLines(lines):

    # Build a 2D array from input
    points = []
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == '#':
                points.append(Point(x, y))

    return points

def printAsteroids(asteroids):
    for asteroid in asteroids:
        print(asteroid, end=" ")
    print("\n")

def printMap(asteroids, scanner, width, height):

    print()
    for y in range(height):
        for x in range(width):
            point = Point(x, y)
            if point in asteroids:
                if point == scanner:
                    print("@", end="")
                else:
                    print("#", end="")
            else:
                print(".", end="")

            
        print()

def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string

    asteroids = parseLines(lines)

    max_count = 0
    for scanner in [Scanner(asteroid.x, asteroid.y) for asteroid in asteroids]:
        scanner.scan(asteroids)
        max_count = max(max_count, scanner.scanned_count)

    return(f"The number of asteroids the scanner can see is {max_count}") 

def part2(lines):
    # Code the solution to part 2 here, returning the answer as a string
    
    asteroids = parseLines(lines)

    scanner = None
    max_count = 0
    for potential_scanner in [Scanner(asteroid.x, asteroid.y) for asteroid in asteroids]:
        potential_scanner.scan(asteroids)

        if potential_scanner.scanned_count > max_count:
            scanner = potential_scanner
            max_count = scanner.scanned_count
            
    WIDTH = len(lines[0])
    HEIGHT = len(lines)

    printMap(asteroids, scanner, WIDTH, HEIGHT)

    last_destroyed = None
    # Nth_ASTEROID = len(asteroids)-1
    Nth_ASTEROID = 200
    while last_destroyed is None:
        scanner.scan(asteroids)
        asteroids, last_destroyed = scanner.laser(asteroids, Nth_ASTEROID)
        printMap(asteroids, scanner, WIDTH, HEIGHT)
    
    return f"The {Nth_ASTEROID}th asteroid that will be destroyed is {last_destroyed}"


def main():
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