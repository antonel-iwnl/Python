from domain import students
from tests import runAllTests


def dataExamples():
    listOfStudents = [["Adel", 7], ["Maria", 10], ["Andrei", 9], ["Paul", 6], ["Cristi", 8]]
    print("ex.1.")
    students.printStudents(listOfStudents)

    print("ex.2.")
    students.addStudent(listOfStudents, ["Marian", 7])
    students.printStudents(listOfStudents)

    print("ex.3.")
    print(students.findStudentByName(listOfStudents, "Cristi"))

    print("ex.4.")
    print(students.deleteStudentByName(listOfStudents, "Adel"))
    students.printStudents(listOfStudents)

    print("ex.5.")
    students.printStudents(students.filterGradeHigher(listOfStudents, 5))
    print()
    students.printStudents(students.filterGradeHigher(listOfStudents, 8))

    print("ex.6.")
    students.printStudents(students.filterStudentsMaxGrade(listOfStudents))
    listOfStudents[0][1] = 9
    print()
    students.printStudents(students.filterStudentsMaxGrade(listOfStudents))


def printMenu():
    print("MENU:")
    print("-2 - print data examples")
    print("-1 - print menu")
    print(" 0 - exit program")
    print(" 1 - add a new student")
    print("...")


def start():
    runAllTests()
    print("All tests run successfully!")
    print()
    printMenu()
    command = None
    while command != 0:  # while True
        command = int(input(">>> "))
        if command == -2:
            dataExamples()
        elif command == -1:
            printMenu()
        elif command == 0:
            print("program ended")
        elif command == 1:
            # read name
            # read grade --- check if it can be converted to integer
            # call addStudent
            # print the result
            pass
        elif command == 2:
            pass
        else:
            print("invalid command")
