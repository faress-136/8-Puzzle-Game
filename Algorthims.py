import time
from heapdict import heapdict
from Heuristic import *
from state import *


def BFS(state):
    Start = time.time()
    frontier = [state]  # empty list (Queue)
    explored = set()  # set explored
    Map = {state: state}

    while len(frontier) > 0:  # as long as frontier not empty enter while
        currentState = frontier.pop(0)
        explored.add(currentState)
        if Goal(currentState):
            break
        children = getNextStates(currentState)
        for child in children:
            if child not in frontier and child not in explored:
                frontier.append(child)
                Map[child] = currentState
    TotalTime = time.time() - Start
    print(" BFS PATH :  \n ")
    getPath(Map)
    print("Number of Expanded Nodes in BFS : " + str(len(explored)) + " Nodes \n")
    print("BFS Total Time : " + str(TotalTime) + " Seconds \n")


def DFS(state):
    Start = time.time()
    frontier = [state]
    explored = set()
    Map = {state: state}

    while len(frontier) > 0:
        currentState = frontier.pop()
        explored.add(currentState)

        if Goal(currentState):
            break
        children = getNextStates(currentState)
        for child in children:
            if child not in frontier and child not in explored:
                frontier.append(child)
                Map[child] = currentState

    TotalTime = time.time() - Start
    print(" DFS PATH :  \n ")
    getPath(Map)
    print("Number of Expanded Nodes in DFS : " + str(len(explored)) + " Nodes \n")
    print("DFS Total Time : " + str(TotalTime) + " Seconds \n")


def AStarManhattan(initialState):
    StartTime = time.time()
    frontier = heapdict()
    frontier[initialState] = calculateManhattanHeuristic(initialState)
    G = {initialState: 0}
    H = {initialState: calculateManhattanHeuristic(initialState)}
    explored = set()
    Map = {initialState: initialState}

    while len(frontier) > 0:
        currentState = frontier.popitem()[0]
        explored.add(currentState)
        if Goal(currentState):
            break
        children = getNextStates(currentState)
        for child in children:
            if child not in frontier and child not in explored:
                G[child] = G[currentState] + 1
                H[child] = calculateManhattanHeuristic(child)
                frontier[child] = H[child] + G[child]
                Map[child] = currentState
            elif child in frontier:
                NG = G[currentState] + 1
                if H[child] + NG < frontier[child]: # H is constant just comparing depth as it comes from a  diff branch
                    G[child] = NG
                    frontier[child] = H[child] + G[child]
                    Map[child] = currentState
    TotalTime = time.time() - StartTime
    print("A-Star Manhattan PATH :  \n ")
    getPath(Map)
    print("Number of Expanded Nodes in A-Star Manhattan : " + str(len(explored)) + " Nodes \n")
    print("A-Star Manhattan completed in " + str(TotalTime) + " Seconds \n")


def AStarEc(initialState):
    StartTime = time.time()
    frontier = heapdict()
    frontier[initialState] = calculateEuclideanHeuristic(initialState)
    G = {initialState: 0}
    H = {initialState: calculateEuclideanHeuristic(initialState)}
    explored = set()
    Map = {initialState: initialState}

    while len(frontier) > 0:
        currentState = frontier.popitem()[0]
        explored.add(currentState)
        if Goal(currentState):
            break
        children = getNextStates(currentState)
        for child in children:
            if child not in frontier and child not in explored:
                G[child] = G[currentState] + 1
                H[child] = calculateEuclideanHeuristic(child)
                frontier[child] = H[child] + G[child]
                Map[child] = currentState
            elif child in frontier:
                NG = G[currentState] + 1
                if H[child] + NG < frontier[child]:
                    G[child] = NG
                    frontier[child] = H[child] + G[child]
                    Map[child] = currentState
    TotalTime = time.time() - StartTime
    print("A-Star Euclidean PATH :  \n ")
    getPath(Map)
    print("Number of Expanded Nodes in A-Star Euclidean : " + str(len(explored)) + " Nodes \n")
    print("AStar completed in " + str(TotalTime) + " Seconds \n")
