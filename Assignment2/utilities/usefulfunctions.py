def sortedl(score_list):
    #Create a sorted list by the participants' value
    sorted_list = sorted(score_list)
    return sorted_list

def checkindex(score_list, index):
    #used to check if index is valid
    if (index > len(score_list) or index < 0):
        print("Index value is set incorrectly!")
        return False
    else:
        return True
    
def checkfromtoidx(score_list, from_index, to_index):
    #used to check if from_index and to_index are valid
    if (to_index > len(score_list) or to_index < 0):
        print("to_index value is set incorrectly!")
        return False
    if (from_index < 0 or from_index > len(score_list)):
        print("from_index value set incorrectly!")
        return False
    if (from_index > to_index):
        print("Indexes values are set incorrectly!")
        return False
    return True

def checkValue(value):
    #used to check if value is appropriate
    val = int(value)
    if (0 < val and val < 101):
        return True
    else:
        print("Value is set incorrectly!")
        return False

        