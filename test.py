def sortedval(score_list, value):
    #Create a sorted list with participants with score higher than value given
    if (checkValue(value) == True):
        sortl = score_list
        sortl.sort()
        sortlvalue = []
        for i in range(len(score_list)):
            if (sortl[i] >= value):
                sortlvalue.append(sortl[i])
        return sortlvalue
    else:
        raise ValueError('Value set incorrectly!')
    
def removeseq(score_list, from_index, to_index):
    #We slice the list from specified indexes
    del score_list[from_index:to_index + 1]


def checkValue(value):
    #used to check if value is appropriate
    val = int(value)
    if (0 < val and val < 101):
        return True
    else:
        print("Value is set incorrectly!")
        return False


l = [5, 7, 19, 25, 75, 3, 6]
assert sortedval([1, 4, 6, 5], 2) == [4, 5, 6]
try:
    sortedval([1, 4, 7, 3, 12], 105)
    assert False
except ValueError:
    assert True

removeseq(l, 1, 5)
print(l)