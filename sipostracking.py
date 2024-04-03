def myBacktracking(param, myList, constraints):
    '''
    Forms groups of elements from the myList.
    IN: a list, a list, a list with functions.
    OUT: one or more lists with indices
    CONDIS: -
    '''
    domain = [  i  for i in range(-1, len(myList))   ]
    
    k = 0 #indexul curent din solutie 'sol

    sol = [] #solutia, la fiecare pas, lista cu indici

    sol.append(initSolution(domain))

    while(k >= 0):
        isSelected = False
        while not isSelected and sol[k] < getLast(domain):
            sol[k] = getNext( sol[k] )
            isSelected = isConsistent( sol, myList, constraints )
        
        if isSelected:
            if isSolution(sol, param):
                #print("YIELDEZ!!!!", sol)
                yield sol
            else:
                k = k+1
                sol.append(initSolution(domain))
        else:
            sol.pop()
            k = k - 1