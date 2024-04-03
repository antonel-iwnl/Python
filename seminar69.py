def getpermutations(solution, init, nextElementFn, doesElementExistFn):
    solution.append(init)
    nextElementValue = nextElementFn(solution, -1) #(solution, len[solution] - 1)
    while doesElementExistFn(nextElementValue):
        if isConsistent(solution):
            yield solution
        else:
            yield from generateRecursiveSolutions(solution[:], initElementFn(init), nextElementFn, doesElementExistFn)


#controller -> controller class with a repository: hospital
#