from gettext import find


listOfStudents = [['Abel', 8], ['Maria', 10], ['Andrei', 9], ['Paul', 6], ['Cristi', 5]]

def printStudents(students):
    #Print all students in the list
    for x in students:
        print("Name = ", x[0], "grade = ", x[1])

def addStudents(students, newStudent):
    #ex 2
    #add a new student to the listOfStudents
    if (len(newStudent) != 2):
        raise ValueError("The newStudent is not valid")
    students.append(newStudent)

def testaddStudent():
    students = []
    addStudents(students, ['asd', 6])
    assert students == [['asd', 6]]


def findStudentByName(students, name):
    #Find the index of a given student by name
    #listOfStudents is a list
    #name of the searched student is a str
    #index -> the position of the student
    for i, x in enumerate(students):
        if x[0] == name:
            return i
    return -1

def deleteStudentByName(students, name):
    #ex 4
    #Delete a student by given name
    idx = findStudentByName(students, name)
    if (idx != -1):
        students.pop(idx)
        return True
    else:
        return False


def testfindStudentByName():
    assert findStudentByName([], 'asd') == -1
    assert findStudentByName(['asd', 6], 'asd') == 0
    assert findStudentByName([['def', 6], ['asd', 6], ['asd', 5]], 'asd') == 1

def testdeleteStudentByName():
    assert deleteStudentByName([], ) == False
    assert deleteStudentByName(['asd', 6], 'asd') == True
    assert deleteStudentByName([['def', 6], ['asd', 6], ['asd', 5]], 'asd') == True

