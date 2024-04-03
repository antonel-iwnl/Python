from utils.helpers import *


def testMaximumGrade():
    assert maximumGrade([]) == 0
    assert maximumGrade([['a', 6], ['b', 6]]) == 6
    assert maximumGrade([['a', 6], ['b', 7]]) == 7


def runAllTests():
    testMaximumGrade()