def teileHerrsche(L, startIndex, endIndex):
    if not L:
        return False

    if (endIndex == startIndex):
        if L[startIndex] == 0:
            return True
        else:
            return False

    if (endIndex > startIndex):
        midIndex = startIndex + (endIndex - startIndex)//2
        print(f"Start: {startIndex} End: {endIndex} Midindex: {midIndex}")
        print(f"Liste = {L[startIndex:endIndex]} Mitte: {L[midIndex]}\n")
        if L[midIndex] == 0:
            return True
        else:
            links = teileHerrsche(L, startIndex, midIndex)
            rechts =teileHerrsche(L, midIndex+1, endIndex)
            if links == True or rechts == True:
                return True
            else:
                return False
        

def startTeileHerrsche(L):
    return teileHerrsche(L, 0, len(L)-1)
