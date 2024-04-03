# import domain.students
# domain.students.printStudents([])

# from domain import students
# students.printStudents([])

# from domain import students as ss
# ss.printStudents([])

from domain.students import *
# printStudents([])


def testAddStudents():
    students = []
    addStudent(students, ['asd', 5])
    assert students == [['asd', 5]]

    try:
        addStudent(students, ['asd', 1, 2])
        assert False
    except ValueError:
        assert True

    try:
        addStudent(students, ['asd'])
        assert False
    except ValueError:
        assert True

    try:
        addStudent(students, ['asd', 0])
        assert False
    except ValueError:
        assert True

    try:
        addStudent(students, ['asd', 11])
        assert False
    except ValueError:
        assert True


def testFindStudentByName():
    assert findStudentByName([], 'asd') == -1
    assert findStudentByName([['asd', 6]], 'asd') == 0
    assert findStudentByName([['def', 6], ['asd', 8], ['asd', 3]], 'asd') == 1


def testDeleteStudentByName():
    assert deleteStudentByName([], 'asd') == False
    assert deleteStudentByName([['asd', 6]], 'asd') == True
    assert deleteStudentByName([['def', 6], ['asd', 8], ['asd', 3]], 'asd') == True


def testFilterGradeHigher():
    for i in range(1, 11):
        assert filterGradeHigher([], i) == []

    assert filterGradeHigher([['a', 5], ['b', 6], ['c', 7]], 5) == [['b', 6], ['c', 7]]
    assert filterGradeHigher([['a', 5], ['b', 6], ['c', 7]], 8) == []


def testFilterStudentsMaxGrade():
    assert filterStudentsMaxGrade([]) == []
    assert filterStudentsMaxGrade([['a', 6]]) == [['a', 6]]
    assert filterStudentsMaxGrade([['a', 6], ['b', 8], ['c', 8]]) == [['b', 8], ['c', 8]]


def runAllTests():
    testAddStudents()
    testFindStudentByName()
    testDeleteStudentByName()
    testFilterGradeHigher()
    testFilterStudentsMaxGrade()
