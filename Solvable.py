def isSolvable(boardState):
    array = [int(x) for x in str(boardState)]
    sortedList, inversions = Inversions(array)
    if inversions % 2 == 0:
        return True
    else:
        return False


def Merge(left, right):
    mergedList = list()
    inversions, l, r = 0, 0, 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            mergedList.append(left[l])
            l += 1
        else:
            mergedList.append(right[r])
            if right[r] != 0:
                inversions += (len(left) - l)
            r += 1
    mergedList += left[l:]
    mergedList += right[r:]
    return mergedList, inversions


def Inversions(Lists):
    if len(Lists) <= 1:
        return Lists, 0
    midIndex = len(Lists) // 2
    leftList, leftInversions = Inversions(Lists[:midIndex])
    rightList, rightInversions = Inversions(Lists[midIndex:])
    mergedList, mergedInversions = Merge(leftList, rightList)
    mergedInversions += (leftInversions + rightInversions)
    return mergedList, mergedInversions
