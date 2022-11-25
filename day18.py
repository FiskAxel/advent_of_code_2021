import math
import copy

def main():
    with open('input18.txt', 'r') as puzzleInput:
        numbers = []
        for line in puzzleInput.readlines():
            line = line.strip()
            root = bulidTree(snailNumNode(), line, [0]).left
            root.parent = None
            numbers.append(root)
            strTree = stringifyTree(root)
            if strTree != line:
                print("THE SNAIL NUMBER'S TREE REPRESENTATION DOES NOT SEEM CORRECT")
                print(f"Expected: {line}")
                print(f"Got     : {strTree}")

    
    numbers1 = copy.deepcopy(numbers)
    result = numbers1.pop(0)
    for num in numbers1:
        result = reduce(result, num)
    print(f"Part 1: {magnitude(result)}")

    maxMagnitude = 0
    for i, _ in enumerate(numbers):
        numbers2 = copy.deepcopy(numbers)
        num1 = numbers2.pop(i)
        for n2 in numbers2:
            n1 = copy.deepcopy(num1)
            result = reduce(n1, n2)
            mag = magnitude(result)
            if maxMagnitude < mag:
                maxMagnitude = mag
    print(f"Part 2: {maxMagnitude}") # Part 2 took about 20 seconds to run.



class snailNumNode:
    def __init__(self, parent=None, left=None, right=None):
        self.parent = parent
        self.left = left
        self.right = right
def bulidTree(root, input, i):
    while i[0] < len(input):
        c = input[i[0]]
        i[0] += 1
        if c == '[':
            if root.left == None:
                root.left = bulidTree(snailNumNode(root), input, i)
            else:
                root.right = bulidTree(snailNumNode(root), input, i)
        elif c == ']':
            return root
        elif '0' <= c <= '9':
            if root.left == None:
                root.left = int(c)
            else:
                root.right = int(c)
    return root
def addNumbers(a, b):
    p = snailNumNode(None, a, b)
    a.parent = p
    b.parent = p
    return p

def reduce(num1, num2):
    sum = addNumbers(num1, num2)
    while True:
        n = nodeNestedIn4(sum, 0)
        if n != None:
            explode(n)
            continue
        n = bigValueNode(sum)
        if n != None:
            splitNum(n)
            continue
        break
    return sum

def nodeNestedIn4(root, d):
    if isinstance(root, int):
        return
    if d == 4:
        return root
    if root.left != None:
        node = nodeNestedIn4(root.left, d + 1)
        if node != None:
            return node
    if root.right!= None:
        node = nodeNestedIn4(root.right, d + 1)
        if node != None:
            return node
def explode(node):
    l = node.left
    r = node.right
    increaseOneStepLeft(node, l)
    increaseOneStepRight(node, r)
    p = node.parent
    if p.left == node:
        p.left = 0
    else:
        p.right = 0
def increaseOneStepLeft(n, v):
    while n == n.parent.left:
        n = n.parent
        if n.parent == None:
            return
    n = n.parent
    if isinstance(n.left, int):
        n.left += v
    else:
        n = n.left
        while not isinstance(n.right, int):
            n = n.right
        n.right += v
def increaseOneStepRight(n, v):
    while n == n.parent.right:
        n = n.parent
        if n.parent == None:
            return
    n = n.parent
    if isinstance(n.right, int):
        n.right += v
    else:
        n = n.right
        while not isinstance(n.left, int):
            n = n.left
        n.left += v

def bigValueNode(root):
    if isinstance(root.left, int) and root.left > 9:
        return root
    if root.left != None and not isinstance(root.left, int):
        node = bigValueNode(root.left)
        if node != None:
            return node
    if root.right != None and not isinstance(root.right, int):
        node = bigValueNode(root.right)
        if node != None:
            return node
    if isinstance(root.right, int) and root.right > 9:
        return root
def splitNum(node):
    v = node.left
    if isinstance(v, int) and v >= 10:
        l = math.floor(v / 2)
        r = math.ceil(v / 2)
        node.left = snailNumNode(node, l, r)
    else: 
        v = node.right
        l = math.floor(v / 2)
        r = math.ceil(v / 2)
        node.right = snailNumNode(node, l, r)

def magnitude(root):
    mag = 0
    l = root.left
    r = root.right
    if isinstance(l, int):
        mag += l * 3
    else:
        mag += magnitude(l) * 3
    if isinstance(r, int):
        mag += r * 2
    else:
        mag += magnitude(r) * 2
    return mag


#Debugging
def printTree(root):
    print("[", end="")
    printTheTree(root)
    print("]")
def printTheTree(root):
    l = root.left
    r = root.right
    if isinstance(l, int):
        print(l, end="")
        print(',', end="")
    else:
        print('[', end="")
        printTheTree(l)
        print(']', end="")
        print(',', end="")
    if isinstance(r, int):
        print(r, end="")
    else:
        print('[', end="")
        printTheTree(r)
        print(']', end="")
def stringifyTree(root): # Just to not have to pass in the list at top level
    return stringifyTheTree(root, [])
def stringifyTheTree(root, string):
    l = root.left
    r = root.right
    if isinstance(l, int):
        string.append(str(l))
        string.append(',')
    else:
        string.append('[')
        stringifyTheTree(l, string)
        string.append(']')
        string.append(',')
    if isinstance(r, int):
        string.append(str(r))
    else:
        string.append('[')
        stringifyTheTree(r, string)
        string.append(']')

    if root.parent == None:
        return '[' + ''.join(string) + ']'

main()