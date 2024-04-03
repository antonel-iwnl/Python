def checkcolor(colorgiven):
    if (colorgiven == "red" or colorgiven == "magenta" or colorgiven == "yellow" or colorgiven == "green" or colorgiven == "blue"):
        return True
    else:
        return False
    
def checkindex(indexgiven):
    if (indexgiven >= 0):
        return True
    else:
        return False