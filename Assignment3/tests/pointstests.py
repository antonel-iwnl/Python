from domain.lab6_A3 import *



def testCreatePoint():
    try:
        MyPoint(2, 5, "red")
        assert False
    except ValueError:
        assert True

def testAttributes():
    p = MyPoint(2, 5, "red")
    assert p.color() == "red"
    assert p.coord_x() == 2
    assert p.coord_y() == 5

def testCreatePointRepository():
    pr = pointsRepository()
    assert pr.getPointAtIndex(0) == None
    pr = pointsRepository([MyPoint(5, 7, 'red')])
    assert pr.getPointAtIndex(0) == MyPoint(5, 7, 'red')
    try:
        pr.addPoints(-3, 5, 'yellow')
        assert False
    except ValueError:
        assert True
    
def testgetPointAtIndex():
    pr = pointsRepository() 
    pr.addPoints(-3, 5, 'red')
    pr.addPoints(5, 8, 'yellow')
    pr.addPoints(-2, -4, 'blue')
    assert pr.getPointAtIndex(0) == [-3, 5, 'red']
    assert pr.getPointAtIndex(1) == [5, 8, 'yellow']
    assert pr.getPointAtIndex(2) == [-2, -4, 'blue']

def testGetPointColor():
    pr = pointsRepository()
    pr.addPoints(2, 5, 'red')
    assert pr.getPointsColor('red') == [2, 5, 'red']
    
def getPointsSquare():
    pr = pointsRepository()
    pr.addPoints(2, 5, "red")
    pr.addPoints(2, 6, 'blue')
    pr.addPoints(3, 9, 'green')
    pr.addPoints(-5, 6, 'yellow')
    try:
        pr.getPointsSquare(1, 900, 900, 1)
        assert False
    except ValueError:
        assert True

def testMinDistance():
    pr = pointsRepository()
    pr.addPoints(2, 5, "red")
    pr.addPoints(2, 6, 'blue')
    pr.addPoints(3, 9, 'green')
    pr.addPoints(-5, 6, 'yellow')
    assert pr.minDistance(0, 1) == 1

def testDelPointByIndex():
    pr = pointsRepository()
    pr.addPoints(2, 5, "red")
    pr.addPoints(2, 6, 'blue')
    pr.addPoints(3, 9, 'green')
    pr.addPoints(-5, 6, 'yellow')
    try:
        pr.delPointByIndex(1)
        assert False
    except IndexError:
        assert True

def testGetCircle():
    pr = pointsRepository()
    pr.addPoints(2, 5, "red")
    pr.addPoints(2, 6, 'blue')
    pr.addPoints(3, 9, 'green')
    pr.addPoints(-5, 6, 'yellow')
    try:
        pr.getCircle(5, 2, 10)
        assert False
    except ValueError:
        assert True
    
def testNumberOfPointsByColor():
    pr = pointsRepository()
    pr.addPoints(2, 5, "red")
    pr.addPoints(2, 6, 'blue')
    pr.addPoints(3, 9, 'green')
    pr.addPoints(-5, 6, 'yellow')
    pr.addPoints(1, 1, 'blue')
    pr.addPoints(-5, -7, 'blue')
    pr.addPoints(-3, -2, 'yellow')
    assert pr.numberOfPointsByColor('blue') == 3
    assert pr.numberOfPointsByColor('yellow') == 2
    assert pr.numberOfPointsByColor('red') == 1



