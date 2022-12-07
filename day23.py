import copy

def main():
    cost = { "2": 1, "4": 10, "6": 100, "8": 1000, }

    hallway = ["." for _ in range(11)]
    rooms = [
        Room(2, ["4", "8"]),
        Room(4, ["4", "6"]),
        Room(6, ["8", "2"]),
        Room(8, ["2", "6"])
    ]
    state = State(hallway, rooms, heuristic(hallway, rooms, cost))
    result = aStar(state, cost)
    print(f"Part 1: {result}") # Runs in about 10 seconds

    rooms = [
        Room(2, ["4", "8", "8", "8"]),
        Room(4, ["4", "6", "4", "6"]),
        Room(6, ["8", "4", "2", "2"]),
        Room(8, ["2", "2", "6", "6"])
    ]
    state = State(hallway, rooms, heuristic(hallway, rooms, cost))
    result = aStar(state, cost)
    print(f"Part 2: {result}") # Runs in about 4 minutes


def aStar(state, cost):
    queue = [state]
    visitedCosts = {}
    while len(queue) > 0:
        queue.sort(key = lambda a : a.distanceToGoal + a.totalCost)
        state = queue.pop(0)
        if state.distanceToGoal == 0:
            break

        for x, pod in enumerate(state.hallway):
            if pod == ".": continue
            s = moveToRoom(state, x, 0, cost)            
            if s: enqueue(s, visitedCosts, queue)

        for room in state.rooms:
            for y, pod in enumerate(room.pods):
                if pod == ".": continue
                s = moveToRoom(state, room.x, y+1, cost)
                if s: enqueue(s, visitedCosts, queue)

                for xHall, pod in enumerate(state.hallway):
                    if pod != ".": continue
                    s = moveToHall(state, room.x, y+1,  xHall, cost)
                    if s: enqueue(s, visitedCosts, queue)

    return state.totalCost 

def moveToRoom(state, x, y, cost):
    if y == 0:
        pod = state.hallway[x]
    else:
        pod = state.rooms[int(x/2) - 1].pods[y - 1]

    targetX = int(pod)
    room = state.rooms[int(targetX/2) -1].pods

    # CHECK IF POD IS ALREADY HOME AND NO OTHER PODS ARE BLOCKED BY IT
    if int(pod) == x and not blockingOtherPod(room, pod, y):
        return

    # CHECK IF ROOM IS BLOCKED BY OTHER KINDS OF PODS
    for p in room:
        if p != "." and p != pod:
            return
    
    if pathBlocked(state, x, y, targetX):
        return

    # MOVE POD TO NEW POSITION
    newState = copy.deepcopy(state)
    newRoom = newState.rooms[int(int(pod)/2) - 1].pods
    y2 = 1
    for i in range(len(room)-1, -1, -1):
        if room[i] == ".":
            newRoom[i] = pod
            y2 = i + 1
            break

    # SET PREVIOUS POSITION TO EMPTY
    if y == 0:
        newState.hallway[x] = "."
    else:
        newState.rooms[int(x/2) - 1].pods[y-1] = "."

    # CALCULATE COST OF MOVE
    steps = y + abs(targetX - x) + y2
    c = cost[pod] * steps
    newState.totalCost += c
    newState.distanceToGoal = heuristic(newState.hallway, newState.rooms, cost)

    # print(stateToString(state))
    # print("-----")
    # print(stateToString(newState))

    return newState

def moveToHall(state, x, y, xHall, cost):
    if pathBlocked(state, x, y, xHall) or xHall in [2, 4, 6, 8]:
        return

    room = state.rooms[int(x/2)-1].pods
    pod = room[y-1]
    if int(pod) == x and not blockingOtherPod(room, pod, y-1):
        return
    
    newState = copy.deepcopy(state)
    newState.hallway[xHall] = pod
    newState.rooms[int(x/2) - 1].pods[y-1] = "."

    steps = y + abs(xHall - x)
    c = cost[pod] * steps
    newState.totalCost += c
    newState.distanceToGoal = heuristic(newState.hallway, newState.rooms, cost)

    return newState

def pathBlocked(state, x, y, targetX):
    if y > 1:
        room = state.rooms[int(x/2)-1].pods
        for i in range(y-1, 0, -1):
            if room[i-1] != ".":
                return True
    
    for x in range(min(x, targetX) + 1, max(x, targetX)):
        if state.hallway[x] != ".":
            return True
    
    return False

def blockingOtherPod(room, pod, y):
    for i in range(y+1, len(room)):
        if room[i] != pod:
            return True
    return False

def enqueue(s, visitedCosts, queue):
    ss = stateToString(s)
    if ss in visitedCosts:
        if visitedCosts[ss] <= s.totalCost:
            return
    visitedCosts[ss] = s.totalCost
    queue.append(s)

# Not very accurate heuristic
def heuristic(hallway, rooms, cost):
    sum = 0

    for x, pod in enumerate(hallway):
        if pod == ".":
            continue
        sum += distanceToGoal(x, 0, pod)
    
    for room in rooms:
        for y, pod in enumerate(room.pods):
            if pod == ".":
                continue
            sum += cost.get(pod) * distanceToGoal(room.x, y + 1, pod)
    
    return sum
def distanceToGoal(x, y, pod):
    if int(pod) == x:
        return 0 
    return abs(x - int(pod)) + y + 2

def stateToString(state):
    if state == None:
        return
    r = state.rooms
    string = "#############\n"
    string += f"#{''.join(state.hallway)}#\n"
    string += f"###{r[0].pods[0]}#{r[1].pods[0]}#{r[2].pods[0]}#{r[3].pods[0]}###\n"
    for i in range(1, len(r[0].pods)):
        string += f"  #{r[0].pods[i]}#{r[1].pods[i]}#{r[2].pods[i]}#{r[3].pods[i]}#  \n"
    string += f"  #########"
    return string

class State:
    def __init__(self, hallway, rooms, distanceToGoal):
        self.hallway = hallway
        self.rooms = rooms
        self.distanceToGoal = distanceToGoal
        self.totalCost = 0
class Room:
    def __init__(self, x, pods):
        self.x = x
        self.pods = pods

main()
