from domain.lab6_A3 import *
from tests import pointstests

def dataExamples():
    pr = pointsRepository()
    print('ex. 1: add a point to the repository')
    pr.addPoints(2, 5, 'red')
    print(pr.getPoints())


    pr.addPoints(2, 6, 'blue')
    pr.addPoints(3, 9, 'green')
    pr.addPoints(-5, 6, 'yellow')


    print('ex. 3: get point at index = 2')
    print(pr.getPointAtIndex(2))

    pr.addPoints(-5, -3, 'red')
    pr.addPoints(-9, -5, 'red')
    pr.addPoints(-8, 3, 'yellow')
    pr.addPoints(14, 5, 'blue')
    pr.addPoints(9, 9, 'blue')


    print('ex. 4: get all points of color = red')
    print(pr.getPointsColor('red'))

    print('ex. 6: get min distance between point 2 and 3')
    print(pr.minDistance(2, 3))

    print('ex. 8: delete a point by index = 2')
    print("List of points before deletion:", pr.getPoints())
    pr.delPointByIndex(2)
    print("List of points after deletion", pr.getPoints())

    print('ex. 10: plot all points into a chart')
    pr.PlotInChart()

    print('ex. 14: get the number of points of a color = yellow')
    print(pr.getPointsColor('yellow'))



def printMenu():
    print("MENU:")
    print("-1 - print data examples")
    print(" m - print menu")
    print(" 1 - add a new point")
    print(" 2 - get all points")
    print(" 3 - get point at index")
    print(" 4 - get all points of a given color")
    print(" 5 - get points inside a given square")
    print(" 6 - get the min distance between two points")
    print(" 7 - update a point at a given index")
    print(" 8 - delete a point by index")
    print(" 9 - delete all points inside a given square")
    print("10 - plot all points into a chart")
    print("11 - get all points inside a given circle")
    print("14 - get number of points of a given color")
    print("18 - delete a point by coordinates")
    print(" x - exit program")

def start():
    pr = pointsRepository()
    printMenu()
    command = None
    while command != 'x':
        command = input(">>> ")
        if command == '1':
            x = int(input("Coordinate x: "))
            y = int(input("Coordinate y: "))
            color = str(input("Color: "))
            pr.addPoints(x, y, color)
        elif command == 'm':
            printMenu()
        elif command == '-1':
            dataExamples()
        elif command == '2':
            print(pr.getPoints())
        elif command == '3':
            if (h.checkindex(index)):
                index = int(input("Input an index: "))
                print(pr.getPointAtIndex(index))
            else:
                print("index is incorrect!")
        elif command == '4':
            color = str(input("Input a color: "))
            print(pr.getPointsColor(color))
        elif command == '5':
            cornerx = int(input("Input corner x coord: "))
            cornery = int(input("Input corner y coord: "))
            length = int(input("Input length: "))
            print(pr.getPointsSquare(cornerx, cornery, length))
        elif command == '6':
            index1 = int(input("Input 1st index: "))
            index2 = int(input("Input 2nd index: "))
            print(pr.minDistance(index1, index2))
        elif command == '7':
            index = int(input("Input an index: "))
            print(pr.updateAtIndex(index))
        elif command == '8':
            index = int(input("Input an index: "))
            pr.delPointByIndex(index)
        elif command == '9':
            cornerx = int(input("Input corner x coord: "))
            cornery = int(input("Input corner y coord: "))
            length = int(input("Input length: "))
            pr.delPointsSquare(cornerx, cornery, length)
        elif command == '10':
            pr.PlotInChart()
        elif command == '11':
            centerx = int(input("Input center x coord: "))
            centery = int(input("Input center y coord: "))
            radius = int(input("Input radius: "))
            pr.getCircle(centerx, centery, radius)
        elif command == '14':
            color = str(input("Input a color: "))
            print(pr.numberOfPointsByColor(color))
        elif command == '18':
            coordx = int(input("Input an x coord: "))
            coordy = int(input("Input an y coord: "))
            pr.delPointCoord(coordx, coordy)
        