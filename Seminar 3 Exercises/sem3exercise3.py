l = [5, 1, 8, 7]

def isPowerOf2(number):
    if number == 1:
        return True
    else:
        while number > 1 and number % 2 != 1:
            number //= 2
        return number == 1
def specialSum(listOfNumbers):
    s = 0
    for value in listOfNumbers:
        if isPowerOf2(value):
            s += value
    return s
print (specialSum([])) # =0
print (specialSum([l])) # =9