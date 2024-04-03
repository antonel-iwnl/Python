import utilities.usefulfunctions as utils


def add(score_list, value):
    #This is used to add a new value to the end of the list
    if (utils.checkValue(value) == True):
        oldl[:] = score_list[:]
        score_list.append(value)
    else:
        pass

def insert(score_list, index, value):
    #We add a new value to a specified index in the list
    oldl[:] = score_list[:]
    if (utils.checkindex(score_list, index) == True and utils.checkValue(value) == True):
        score_list.insert(index, value)
    else:
        pass

def remove(score_list, index):
    #We delete an element at a specified index from the list
    oldl[:] = score_list[:]
    if (utils.checkindex(score_list, index) == True):
        score_list.pop(index)
    else:
        pass
    
def removeseq(score_list, from_index, to_index):
    #We slice the list from specified indexes
    oldl[:] = score_list[:]
    if (utils.checkfromtoidx(score_list, from_index, to_index) == True):
        del score_list[from_index:to_index + 1]
    else:
        pass
    
def replace(score_list, index, new_value):
    #Replace the value at given index with the given new_value
    if (utils.checkindex(score_list, index) == True and utils.checkValue(new_value) == True):
        oldl[:] = score_list[:]
        score_list[index] = new_value
    else:
        pass
    
def less(score_list, value):
    #Get the participants from the list that have the score less than the given value
    indexlist = []
    if (utils.checkValue(value) == True):
        for i in range(len(score_list)):
            if (score_list[i] < value):
                indexlist.append(i)
        return indexlist
    else:
        pass

def sorted(score_list):
    #Just sort the list by their scores
    sortl = []
    indexlist = []
    sortl = score_list[:]
    sortl.sort()
    sortl = list(set(sortl))
    for i in range(len(sortl)):
        for j in range(len(score_list)):
            if (score_list[j] == sortl[i]):
                indexlist.append(j)
    return indexlist

def sortedval(score_list, value):
    #Create a sorted list with participants with score higher than value given
    if (utils.checkValue(value) == True):
        sortl = []
        indexlist = []
        sortl = score_list[:]
        sortl.sort()
        sortl = list(set(sortl))
        for i in range(len(sortl)):
            for j in range(len(score_list)):
                if (score_list[j] == sortl[i] and score_list[j] > value):
                    indexlist.append(j)
        return indexlist
        # indexlist = [] #enumerate, sortl.sort(key='function to get the index')
        # #KEEP THE INDEXES, THIS WAY WE ALWAYS GET INDEX 0 1 2 3 4
        # for i in range(len(score_list)):
        #     if (sortl[i] >= value):
        #         indexlist.append(i)
        # return indexlist
    else:
        pass

def avg(score_list, from_index, to_index):
    #We get the average score of the participants starting from index:from_index, up to to_index, with
    #to_index included
    if (utils.checkfromtoidx(score_list, from_index, to_index) == True):
        scorel = score_list[from_index:to_index + 1]
        average = sum(scorel) / len(scorel) #idk if it should be rounded or not
        return average
    else:
        pass

def minim(score_list, from_index, to_index):
    #We get the minimum score of the participants starting from index:from_index, up to to_index, with
    #to_index included
    if (utils.checkfromtoidx(score_list, from_index, to_index) == True):
        scorel = score_list[from_index:to_index + 1]
        minimum = min(scorel)
        return minimum
    else:
        pass
    

def mul(score_list, value, from_index, to_index):
    #We get a list with all the values starting from index:from_index and up to to_index, with
    #to_index included, where all the scores are multiples of value given
    if (utils.checkfromtoidx(score_list, from_index, to_index) == True):
        scorel = score_list[from_index:to_index + 1]
        mul_list = []
        for i in range(len(scorel)):
            if (scorel[i] % value == 0):
                mul_list.append(scorel[i])
        return mul_list
    else:
        pass

def filter_mul(score_list, value):
    #create a list with participants that have the score a multiple of the given value
    if (utils.checkValue(value) == True):
        oldl[:] = score_list[:]
        length = len(score_list)
        i = 0
        while (i <= length - 1):
            if (score_list[i] % value != 0):
                del score_list[i]
                length -= 1
                i -= 1
            i += 1
    else:
        pass

    
def filter_greater (score_list, value):
    #we modify the list such that we keep only the participants that have the score higher than the given value
    if (utils.checkValue(value) == True):
        oldl[:] = score_list[:]
        i = 0
        length = len(score_list)
        while (i <= length - 1):
            if (score_list[i] < value):
                del score_list[i]
                i -= 1
                length -= 1
            i += 1
    else:
        pass
            
def undo(score_list):
    #we create a list with the previous list and everytime we call this function we delete the last element
    # if we want to undo the undo:
    # undol[:] = oldl[:]
    score_list[:] = oldl[:]
    return score_list
    

l = [5, 8, 9, 3, 4, 5, 6, 9, 3, 5, 1, 12, 421, 532, 652]
oldl = []
undol = []

# print("lista originala", l)
# add(l, 5)
# print("add 5", l)
# insert(l, 6, 999)
# print("insert ind = 6, value 999", l)
# remove(l, 5)
# print("remove ind = 5", l)
# removeseq(l, 3, 12)
# print("remove from 3 to 12", l)
# ol = [5, 8, 9]
# nl = [91, 91, 91]
# replace(l, ol, nl)
# print("replace [5, 8, 9] with [91, 91, 91]", l)
# insert(l, 100, 5)
# print ("even if index is set to 100 but we only have 6 elements", l)
#i have to give a lot more tests and do error checking