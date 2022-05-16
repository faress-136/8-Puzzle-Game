import random


def Goal(boardState):
    if boardState == 12345678:
        return True
    else:
        return False


def findIndexOf(boardState, element):
    temp = boardState
    for i in range(9):
        if temp % 10 == element:  # Check if  the last digit is "toBeFound"
            return (8 - i) // 3, (8 - i) % 3  # equation to get i,j of a certain element in the board
        temp = temp // 10  # Remove last digit


def swap(boardState, position1, position2):  # Swap Function
    tempBoardState = str(boardState)
    if boardState < 100000000:  # Check if 0 is in the beginning
        tempBoardState = '0' + tempBoardState  # Concatinate 0 to the start
    tempBoardState = list(tempBoardState)  # Converts From  String to list to Swap
    tempBoardState[position1], tempBoardState[position2] = tempBoardState[position2], tempBoardState[position1]  # Swap
    return int(''.join(tempBoardState))  # Returns back to Int


def getNextStates(boardState):  # Getting All the Possible States
    states = []
    i, j = findIndexOf(boardState, 0)  # Find 0's Index
    position1 = 3 * i + j  # Calculate Decimal Position
    if i > 0:  # Blocked From The Top
        position2 = 3 * (i - 1) + j  # Calculate Decimal Position Of Above
        states.append(swap(boardState, position1, position2))
    if i < 2:  # Blocked From The Bottom
        position2 = 3 * (i + 1) + j  # Calculate Decimal Position Of Below
        states.append(swap(boardState, position1, position2))
    if j < 2:  # Blocked From The Right
        position2 = 3 * i + (j + 1)  # Calculate Decimal Position Of Left
        states.append(swap(boardState, position1, position2))
    if j > 0:  # Blocked From The Left
        position2 = 3 * i + (j - 1)  # Calculate Decimal Position Of Right
        states.append(swap(boardState, position1, position2))
    return states


def getRandomState():  # Generates Random
    arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
    random.shuffle(arr)
    randomState = int(''.join(arr))
    return randomState


def getElementAtIndex(boardState, i, j):
    temp = boardState
    # print("Index" + str(((8 - ((3 * i) + j)) % 10)))    123456780
    digit = temp // 10 ** (8 - ((3 * i) + j)) % 10  # 8 is the max digit we subtract from it moving down the number
    # (3*i+j) to get index example 8 - 7  then using equation
    return digit  # equation to get element at position i,j in the
    # https://stackoverflow.com/questions/39644638/how-to-take-the-nth-digit-of-a-number-in-python


def getPath(parentMap):
    child = 12345678
    parent = parentMap[child]
    path = [child]
    while child != parent:
        child = parent
        parent = parentMap[child]
        path.append(child)
    n = len(path)
    # print(n)
    cost = n - 1
    for i in range(n):
        printBoardState(path.pop())  # pop parents of 012345678
    print("DEPTH COST : " + str(cost) + " Nodes  \n")


def printBoardState(boardState):
    print("\n")
    for i in range(3):
        for j in range(3):
            element = getElementAtIndex(boardState, i, j)
            if element != 0:
                print(element, end="\t")
            else:
                print(' ', end="\t"),
        print('\n')
    print('---------\n')

