import re
def main():
    with open('input22.txt', 'r') as puzzleInput:
        onOff = {'n': 1, 'f': -1}
        cuboids = []
        for i in puzzleInput.readlines():
            cuboid = [onOff[i[1]]]
            [cuboid.append(int(j)) for j in re.findall("(-?\d+)", i)]
            cuboids.append(cuboid)
    # A cuboid is represented as: [onOff, x1, x2, y1, y2, z1, z2]

    initCuboids = []
    for cub in cuboids:
        if -50 <= cub[1] and cub[1] <= 50: # Laxy check that worked for my input.
            initCuboids.append(cub)
    initialization = calculateState(initCuboids)
    print(f"Part 1: {cubeCount(initialization)}")
    part2 = calculateState(cuboids)
    print(f"Part 2: {cubeCount(part2)}") # Takes about 35s to run

def calculateState(cuboids):
    reactor = []
    for newCub in cuboids:
        add = []
        if newCub[0] == 1: 
            add = [newCub]
        for oldCub in reactor:
            iterCub = intersection(oldCub, newCub)
            if iterCub != None:
                add.append(iterCub)
        reactor.extend(add)
    return reactor
def intersection(old, new):
    ic = [-old[0]]
    ic.append(max(old[1], new[1]))
    ic.append(min(old[2], new[2]))
    ic.append(max(old[3], new[3]))
    ic.append(min(old[4], new[4]))
    ic.append(max(old[5], new[5]))
    ic.append(min(old[6], new[6]))
    if ic[1] > ic[2] or ic[3] > ic[4] or ic[5] > ic[6]:
        return None
    return ic

def cubeCount(cuboids):
    sum = 0
    for c in cuboids:
        vol = c[0]
        vol *= c[2] - c[1] + 1
        vol *= c[4] - c[3] + 1
        vol *= c[6] - c[5] + 1
        sum += vol
    return sum


main()