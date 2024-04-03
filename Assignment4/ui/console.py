from domain.lab8A4 import *
import unittest

def dataExamples():
    vr = VectorRepository()
    v1 = MyVector(1, 'r', 1, [1, 2, 3, 4])
    v2 = MyVector(2, 'r', 1, [6, 7, 2, 3])
    vr.addVector(1, 'y', 1, [1, 4, 9, 16, 25])
    vr.addVector(2, 'g', 2, [1, 2.5, 4, 5.5])
    vr.addVector(3, 'r', 5, [1, 2, 3])
    print(vr.getVectors())
    print("Adding a vector with values {4, 'm', 3, [1, 6, 4]")
    vr.addVector(4, 'm', 3, [1, 6, 4])
    print(vr.getVectors())
    print("Get vector at index = 2")
    print(vr.getVectorAtIndex(2))
    print("Update vector at index = 2 with name_id = 6, color = 'y', type = 7, values = [4, 5, 9]")
    vr.updateVectorAtIndex(2, 6, 'y', 7, [4, 5, 9])
    print(vr.getVectorAtIndex(2))
    print("Update vector that has name_id = 2, with color = 'm', type = 2, values = [3, 4, 9, 16, 25]")
    vr.updateVectorByNameId(1, 'm', 2, [3, 4, 9, 16, 25])
    print(vr.getVectors())
    print("Delete vector at index = 2")
    vr.delVectorByIndex(2)
    print(vr.getVectors())
    print("Delete vector by name_id = 4")
    vr.delVectorByNameId(4)
    print(vr.getVectors())
    print("Add 2 more vectors: 9, 'g', 4, [1, 5.7, 4.9, 9]; 15, 'g', 4, [3, 4, 9]")
    vr.addVector(9, 'g', 4, [1, 5.7, 4.9, 9])
    vr.addVector(15, 'g', 4, [3, 4, 9])
    print(vr.getVectors())
    print("Plot vectors into a chart")
    vr.PlotInChart()
    print("Use 2 MyVector instances to test sum, avg, min, max: v1 = MyVector(1, 'r', 1, [1, 2, 3, 4]), v2 = MyVector(2, 'r', 1, [6, 7, 2, 3])")
    print("Add two MyVector instances together")
    print(MyVector.__add__(v1, v2))
    print("Sum for v1")
    print(v1.sum())
    print("avg for v1")
    print(v1.avg())
    print("min for v1")
    print(v1.minimum())
    print("max for v1")
    print(v1.maximum())
    print("Sum for v2")
    print(v2.sum())
    print("avg for v2")
    print(v2.avg())
    print("min for v2")
    print(v2.minimum())
    print("max for v2")
    print(v2.maximum())


def run_all():
    loader = unittest.TestLoader()
    suite = loader.discover("Assignment4/tests", pattern="labtests.py")
    unittest.TextTestRunner().run(suite)


def printMenu():
    print("MENU:")
    print("-1 - print data examples")
    print(" m - print menu")
    print(" 1 - add a new vector")
    print(" 2 - get all vectors")
    print(" 3 - get vector at index")
    print(" 4 - update a vector at given index")
    print(" 5 - update a vector by given name_id")
    print(" 6 - delete a vector by index")
    print(" 7 - delete a vector by name_id")
    print(" 8 - Plot all points in a chart")
    print(" x - exit program")

def start():
    vr = VectorRepository()
    run_all()
    printMenu()
    vr.addVector(1, 'y', 3, [1, 2, 3, 4])
    vr.addVector(2, 'r', 1, [9, 8, 7, 6])
    vr.addVector(3, 'm', 2, [1, 5, 9, 3])
    vr.addVector(4, 'm', 4, [1, 3, 5, 4])
    vr.addVector(5, 'b', 4, [7, 9, 9])
    vr.addVector(6, 'y', 100, [3, 6])
    command = None
    while command != 'x':
        command = input(">>> ")
        if command == '1':
            name_id = int(input("Input an id: "))
            color = input("Input a color: ")
            type = int(input("Input a type: "))
            values = []
            n = int(input("Input number of values for the vector: "))
            for i in range(0, n):
                x = int(input("Input a value: "))
                values.append(x)
            vr.addVector(name_id, color, type, values)
        elif command == '2':
            print(vr.getVectors())
        elif command == '3':
            index = int(input("Input an index: "))
            print(vr.getVectorAtIndex(index))
        elif command == '4':
            index = int(input("Input an index: "))
            name_id = int(input("Input a new id: "))
            color = input("Input a new color: ")
            type = int(input("Input a new type: "))
            values = []
            n = int(input("Input number of values for the vector: "))
            for i in range(0, n):
                x = int(input("Input a new value: "))
                values.append(x)
            vr.updateVectorAtIndex(index, name_id, color, type, values)
        elif command == '5':
            name_id = int(input("Input an id: "))
            color = input("Input a new color: ")
            type = int(input("Input a new type: "))
            values = []
            n = int(input("Input number of values for the vector: "))
            for i in range(0, n):
                x = int(input("Input a new value: "))
                values.append(x)
            vr.updateVectorByNameId(name_id, color, type, values)
        elif command == '6':
            index = int(input("Input an index: "))
            vr.delVectorByIndex(index)
        elif command == '7':
            name_id = int(input("Input a name_id: "))
            vr.delVectorByNameId(name_id)
        elif command == '8':
            vr.PlotInChart()
        elif command == 'm':
            printMenu()
        elif command == '-1':
            dataExamples()
        elif command == '2':
            print(vr.getVectors())