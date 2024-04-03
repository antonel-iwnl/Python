def mySort(listOfValues, condition, desc=False):
    ordered = False
    onFinalPosition = 0
    while not ordered:
        ordered = True
        for i in range(len(listOfValues) - onFinalPosition - 1):
            if not condition(listOfValues[i], listOfValues[i + 1]):
                aux = listOfValues[i]
                listOfValues[i] = listOfValues[i + 1]
                listOfValues[i + 1] = aux
                ordered = False
        onFinalPosition += 1
    return listOfValues