

def printStudents(students):

    ''' Print all students in list.
    :param students: given list of students containing name and grade
    :return: student dlist
    '''
    if len(students)==0:
        print("there are no students in the list")
    for x in students:
        print('name=',x[0],'grade= ', x[1])

def testAddstudent():
    students = []
    addstudent(students,['ads',5])
    assert students == [['ads',5]]
    try:
        addstudent(students,["ads",])
        assert False
    except ValueError:
        assert True
def addstudent(students,newstudent):
    '''
    exercise 2 add a new student
    :param students:
    :return:
    '''

def findStudentByname(students,name):
     '''
     Ex3
     :param students:
     :param name:
     :return:
     '''

def testFindStudentByname():
    assert findStudentByname([],'asd')
    '''not all'''
def deleteStudentByName(students,name):
    '''
    ex4
    :param students:
    :param name:
    :return:
    '''
    if findStudentByname(students,name) !=-1:
        del students[findStudentByname(students,name)]
        return True
    else:
        return False

def testdeleteStudent():
    assert deleteStudentByName([],'asd')==False
    assert deleteStudentByName([['asd',6],"asd"])


listOfStudents = [('Adel', 7), ('Danut', 10), ('Vladut', 5), ('marius', 8)]

def filterGradeHigher(students,minimumGrade):
    '''
    get students from the list with the grade higher than the given value
    :param students:
    :param minimumGrade:
    :return: selected students
    '''
    final=[]
    for i in students:
        if i[1]>minimumGrade:
            final.append(i)
    return final

def testfilterGradeHigher():
    for i in range(1,11):
        assert filterGradeHigher([],i)==[]
    assert filterGradeHigher([['a',5],['b',6],['c',7],5])==()

def filterStudentMaxiGrade(students):
    '''
    ex 6
    :param students:
    :return: students whit maximum grade
    '''
    list=[]
    for i in students:
        if i[1]==findMaxGrade(students):
            list.append(i)
    return list


def findMaxGrade(students):
    max=1
    for x in students:
        if x[1]>max:
            max=x[1]
    return max
