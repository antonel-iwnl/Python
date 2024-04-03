def checkColour(colour):
    if (colour == 'r' or colour == 'g' or colour == 'b' or colour == 'y' or colour == 'm'):
        return True
    else:
        return False

def checkIndex(index, length):
    if (index <= length and index >= 0):
        return True
    else:
        return False
    