import utils.helpers as help

def printStudents(students):
    """
    ex. 1.
    Print all student in the list.
    :param students: given list of students containing name s and grades
    :type students: list
    """
    if len(students) == 0:
        print("There are no students in the list!")
    for x in students:
        print("Name = ", x[0], "\tgrade = ", x[1])


def addStudent(students, newStudent):
    """
    ex. 2.
    Add a new student to the list
    :param students: list of students
    :type students: list
    :param newStudent: list representing the student
    :type newStudent: list
    :return:
    :rtype:
    """
    if len(newStudent) != 2:
        raise ValueError("the value is not valid")
    if not 1 <= newStudent[1] <= 10:
        raise ValueError("incorrect grade")
    students.append(newStudent)


def findStudentByName(students, name):
    """
    ex. 3.
    Find the index of a given student by name
    :param students: list of students
    :type students: list
    :param name: name of the searched student
    :type name: str
    :return: position of the student
    :rtype: int
    """
    for i,x in enumerate(students) :
        if x[0]==name:
            return i
    return -1


def deleteStudentByName(students, name):
    """
    ex. 4.
    Delete a student from the list with the given name
    :param students: given list of students
    :type students: list
    :param name: name of the student
    :type name: str
    :return:
    :rtype: bool
    """
    positionOfStudent = findStudentByName(students, name)
    if positionOfStudent==-1:
        return False
    students.pop(positionOfStudent)
    # del students[positionOfStudent]
    return True

def filterGradeHigher(students, minimumGrade):
    """
    Get students from the list with grade higher than the given value
    :param students: list of students
    :type students: list
    :param minimumGrade:
    :type minimumGrade: int
    :return: selected students
    :rtype: list
    """
    final=[]
    for i in students:
        if i[1]>minimumGrade:
            final.append(i)
    return final

def filterStudentsMaxGrade(students):
    """
    ex. 6.
    :param students: list od students
    :type students: list
    :return: students with maximum grade
    :rtype: list
    """
    x=help.maximumGrade(students)
    maxStudents=[]
    for i in students:
        if i[1]==x:
            maxStudents.append(i)
    return maxStudents

