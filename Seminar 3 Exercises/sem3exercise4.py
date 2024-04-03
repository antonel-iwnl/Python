l = [5, 1, 8, 7]
def myFilter(listOfNumbers):
    for i in range(len(listOfNumbers)):
        if isPowerOf2(listOfNumbers[i]):
            del listOfNumbers[i] #delete element
            i -= 1

#or
    i = 0
    while i < len(listOfNumbers):
        if isPowerOf2(listOfNumbers[i]):
            del listOfNumbers[i] #delete element or we can use l = l[:1] + l[i-1]
            i -= 1
        i += 1