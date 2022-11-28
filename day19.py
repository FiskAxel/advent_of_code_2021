import re
import copy

def main():
    with open('input19.txt', 'r') as puzzleInput:
        input = puzzleInput.read().split('\n\n')
        scanners = []
        for line in input:
            positions = re.findall("\n(-?\d+),(-?\d+),(-?\d+)", line)
            scan1 = []
            for pos in positions:
                scan1.append([int(cord) for cord in pos])
            scanners.append(Scanner(scan1, 0))
    
    minCommon = 12
    processedScans = [scanners.pop(0).scan]
    sortOnCommonDistances(scanners, processedScans[-1])
    scannerPositions = [[0, 0, 0]]
    while scanners:
        scanner = scanners.pop(0)
        scan, sPos = findMatch(scanner.scan, processedScans[-1], minCommon)
        processedScans.append(scan)
        scannerPositions.append(sPos)
        while 0 < len(scanners):
            sortOnCommonDistances(scanners, processedScans[-1])
            if scanners[0].commonDistances < (minCommon * (minCommon - 1)) / 2:
                processedScans = processedScans[-1:] + processedScans[:-1]
                continue
            break

    beacons = processedScans.pop(0)
    for scan in processedScans:
        for beacon in scan:
            if beacon not in beacons:
                beacons.append(beacon)

    maxDistance = 0
    for pos1 in scannerPositions:
        for pos2 in scannerPositions:
            distance = manhattan(pos1, pos2)
            if maxDistance < distance:
                maxDistance = distance

    print(f"Part 1: {len(beacons)}") # Runs in about 12 seconds
    print(f"Part 2: {maxDistance}")

def findMatch(scan, beacons, minC):
    orientations = [
        [ 1,  1,  1,  0, 1, 2], # x  y  z
        [ 1, -1,  1,  0, 2, 1], # x -z  y
        [ 1, -1, -1,  0, 1, 2], # x -y -z
        [ 1,  1, -1,  0, 2, 1], # x  z -y

        [-1,  1, -1,  0, 1, 2], #-x  y -z
        [-1, -1, -1,  0, 2, 1], #-x -y -z
        [-1, -1,  1,  0, 1, 2], #-x -y  z
        [-1,  1,  1,  0, 2, 1], #-x  z  y

        [ 1, -1,  1,  1, 0, 2], # y -x  z
        [ 1, -1, -1,  1, 2, 0], # y -z -x
        [ 1,  1, -1,  1, 0, 2], # y  x -z
        [ 1,  1,  1,  1, 2, 0], # y  z  x

        [-1,  1,  1,  1, 0, 2], #-y  x  z
        [-1, -1,  1,  1, 2, 0], #-y -z  x
        [-1, -1, -1,  1, 0, 2], #-y -x -z
        [-1,  1, -1,  1, 2, 0], #-y  z -x

        [ 1,  1, -1,  2, 1, 0], # z  y -x
        [ 1,  1,  1,  2, 0, 1], # z  x  y
        [ 1, -1,  1,  2, 1, 0], # z -y  x
        [ 1, -1, -1,  2, 0, 1], # z -x -y

        [-1,  1,  1,  2, 1, 0], #-z  y  x
        [-1, -1,  1,  2, 0, 1], #-z -x  y
        [-1, -1, -1,  2, 1, 0], #-z -y -x
        [-1,  1, -1,  2, 0, 1], #-z  x -y
    ]
    
    for i, pos1 in enumerate(scan):
        for pos2 in beacons:
            for o in orientations:
                scanC = copy.deepcopy(scan)
                for s in scanC:
                    xyz = [cor for cor in s]
                    s[0] = o[0] * xyz[o[3]]
                    s[1] = o[1] * xyz[o[4]]
                    s[2] = o[2] * xyz[o[5]]
                convertScan(scanC, scanC[i], pos2)
                if minC <= commonBeacons(scanC, beacons, minC): 
                    scannerPosition = [0, 0, 0]
                    scannerPosition[0] = scanC[i][0] - o[0] * pos1[o[3]]
                    scannerPosition[1] = scanC[i][1] - o[1] * pos1[o[4]]
                    scannerPosition[2] = scanC[i][2] - o[2] * pos1[o[5]]
                    return scanC, scannerPosition
    return [], None

# Converts scan so pos1 (from scan) and pos2 (from other scan) represents the same position
def convertScan(scan, pos1, pos2):
    dx = pos1[0] - pos2[0]
    dy = pos1[1] - pos2[1]
    dz = pos1[2] - pos2[2]
    for pos in scan:
        pos[0] -= dx
        pos[1] -= dy
        pos[2] -= dz

def commonBeacons(a, b, min):
    sum = 0
    for beacon in a:
        if beacon in b:
            sum += 1
        if sum == min:
            return sum
    return sum

def sortOnCommonDistances(scanners, beacons):
    for scanner in scanners:
        scanner.commonDistances = commonDistances(scanner.scan, beacons)
    scanners.sort(key=lambda s: s.commonDistances, reverse=True)
def commonDistances(scan1, scan2):
    dis1 = getDistances(scan1)
    dis2 = getDistances(scan2)
    sum = 0
    for d1 in dis1:
        if d1 in dis2:
            sum += 1
    return sum / 2
def getDistances(scan):
    distances = []
    for pos1 in scan:
        for pos2 in scan:
            if pos1 == pos2:
                continue
            distance = squaredManhattan(pos1, pos2)
            distances.append(distance)
    return distances
def squaredManhattan(pos1, pos2):
    dis = 1
    dis *= abs(pos1[0] - pos2[0])
    dis *= abs(pos1[1] - pos2[1]) 
    dis *= abs(pos1[2] - pos2[2])
    return dis

def manhattan(pos1, pos2):
    dis = 0
    dis += abs(pos1[0] - pos2[0])
    dis += abs(pos1[1] - pos2[1]) 
    dis += abs(pos1[2] - pos2[2])
    return dis

    for p in scan:
        x, y = p[0], p[1]
        p[0] = -y
        p[1] = x
    convertScan(scan, pos1, pos2)

# Just to be able to sort on most commonDistances between beacons
class Scanner:
    def __init__(self, scan, commonDistances):
        self.scan = scan
        self.commonDistances = commonDistances

main()