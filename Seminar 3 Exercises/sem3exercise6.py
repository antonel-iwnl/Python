def isEven(number):
    return number % 2 == 0

def deletesEven(l):
    end = len(l) - 1
    while end:
        if isEven(l[end]):
            del l[end]
        end -= 1
 
 
 
 
    # #or
    # start = 0
    # while start < len(l):
    #     if isEven(l[start]):
    #         del l[start]
    #     else:
    #       start += 1
    
