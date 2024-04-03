import unittest
from domain.person import *
from infrastructure.repositories import *

def dataExamples():
    h = Hospital([
            Department(1, 'Alpha', 14, [
            Patient('Antonio', 'Rochnean', '5030524245060', 'disease1'),
            Patient('David', 'Simon', '1890712123070', 'disease1'),
            Patient('Sarah', 'Bryant', '6081211019891', 'disease2'),
            Patient('Mariah', 'Nicolae', '2830412019906', 'disease3'),
            Patient('Andrei', 'Spataru', '1970707195457', 'disease3')
            ]),
            Department(2, 'Bravo', 7, [
                Patient('Mihai', 'Crasmaru', '5020524268021', 'disease1'),
                Patient('Raluca', 'Bledea', '6010219387001', 'disease1'),
                Patient('Alexandra', 'Mihai', '6030902248111', 'disease1'),
                Patient('Vasile', 'Bledea', '5051001249252', 'disease2'),
                Patient('Stefan', 'Hrusca', '1571208238605', 'disease3')
            ])
            ])
    d1 = Department(1, 'Alpha', 14, [
            Patient('Antonio', 'Rochnean', '5030524245060', 'disease1'),
            Patient('David', 'Simon', '1890712123070', 'disease1'),
            Patient('Sarah', 'Bryant', '6081211019891', 'disease2'),
            Patient('Mariah', 'Nicolae', '2830412019906', 'disease3'),
            Patient('Andrei', 'Spataru', '1970707195457', 'disease3')
        ])
    d2 = Department(2, 'Bravo', 7, [
                Patient('Mihai', 'Crasmaru', '5020524268021', 'disease1'),
                Patient('Raluca', 'Bledea', '6010219387001', 'disease1'),
                Patient('Alexandra', 'Mihai', '6030902248111', 'disease1'),
                Patient('Vasile', 'Bledea', '5051001249252', 'disease2'),
                Patient('Stefan', 'Hrusca', '1571208238605', 'disease3')
        ])
    print('Hospital Repository:')
    print(str(h))
    print('d1: ')
    print(str(d1))
    print('d2: ')
    print(str(d2))
    print('Ex. 3: sort patients in departmets by PNC')
    print('d1: ')
    print(str(d1.sortByPNC()))
    print('')
    print('d2: ')
    print(str(d2.sortByPNC()))
    print('')
    print('Ex. 4: Sort Departments by Number of Patients')
    print(str(h.sortDepByNrOfPatients()))
    print('')
    print('Ex. 5: Sort Departments by Number of Patients With the age above 20')
    print(str(h.sortDepByPatientsAge(20)))
    print('')
    print('Ex. 6: Sort departments by Number of Patients and the patients alphabetically')
    print(str(h.sortDepNrOfPatientsAlfabetically()))
    print('')
    print('Ex. 7: Identify departments where there are patients under a given age = 19')
    print(str(h.getDepPatientsUnderAge(19)))
    print('')
    print('Ex. 8: Identify Patients from a given department (id = 1) for which the first name or last name contain a given string = S')
    print(str(h.getDepWithPatients(1, 'S')))
    print('')
    print('Ex. 9: Identify departments where there are patients with a given first name = Antonio')
    print(str(h.getDepWithPatientName('Antonio')))
    print('')

def run_all():
    loader = unittest.TestLoader()
    suite = loader.discover("Assignment5/tests", pattern="tests.py")
    unittest.TextTestRunner().run(suite)

def start():
    run_all()

def printMenu():
    print("MENU:")
    print("-1 - print data examples")
    print(" m - print menu")
    print(" 1 - add a new department")
    print(" 2 - get all departments")
    print(" 3 - get department at index")
    print(" 4 - update a department at given index")
    print(" 5 - delete a department by index")
    print(" 6 - sort the patients in a department by PNC")
    print(" 7 - sort departments by number of patients")
    print(" 8 - identify patients from department index for which first name or last name contain a given string")
    print(" 9 - identify department/departments where there are patients with given first name")
    print("10 - Form groups of k patients from the same department and the same disease (k is a value given by the user)")
    print(" x - exit program")

def start():
    run_all()
    printMenu()
    command = None
    h = Hospital([
            Department(1, 'Alpha', 14,[
            Patient('Antonio', 'Rochnean', '5030524245060', 'disease1'),
            Patient('David', 'Simon', '1890712123070', 'disease1'),
            Patient('Sarah', 'Bryant', '6081211019891', 'disease2'),
            Patient('Mariah', 'Nicolae', '2830412019906', 'disease3'),
            Patient('Andrei', 'Spataru', '1970707195457', 'disease3')
            ])])
    while command != 'x':
        command = input(">>> ")
        if command == '-1':
            dataExamples()
        elif command == 'm':
            printMenu()
        elif command == '1':
            h.addDepartment()
        elif command == '2':
            print(str(h))
        elif command == '3':
            index = int(input("Input an index: "))
            h.getDepAtIndex(index)
        elif command == '4':
            h.updateDepartment()
        elif command == '5':
            index = int(input("Input an index: "))
            h.deleteDepartment(index)
        elif command == '6':
            index = int(input("Input an index: "))
            print(h.sortDepByIndexPNC(index))
        elif command == '7':
            print(h.sortDepByNrOfPatients())
        elif command == '8':
            id = int(input("Input the id of the department: "))
            string = str(input("Input the string: "))
            print(h.getDepWithPatients(id, string))
        elif command == '9':
            name = str(input("Input the name: "))
            print(h.getDepWithPatientName(name))
        elif command == '10':
            k = int(input("Input number of patients in a group: "))
            h.groupDepartmentsSameDisease(k)
        elif command == '11':
            k = int(input("Input the number of departments: "))
            p = int(input("Input the number of patients"))
            print(h.groupDepartments(k, p))