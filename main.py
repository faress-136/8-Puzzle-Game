from Solvable import *
from Algorthims import *

if __name__ == '__main__':
    print("\n")
    state = getRandomState()

    while not isSolvable(state):
        print(str(state) + " is UNSOLVABLE  \n")
        print("Generating New State >>>  \n")
        state = getRandomState()

    printBoardState(state)
    print("\n\n")
    AStarManhattan(state)
    BFS(state)
    AStarEc(state)
    DFS(state)
