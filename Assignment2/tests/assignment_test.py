from domain.lab3_A2_P2 import *

def testaddnumbers():
    score_list = []
    add(score_list, 5)
    assert score_list == [5]

def testinsert():
    try:
        insert([1, 4, 5, 7], 15, 12)
        pass
    except ValueError:
        assert True
    try:
        insert([1, 4, 5, 7], 3, 150)
        pass
    except ValueError:
        assert True
    
def testremove():

    try:
        remove([1, 4, 5, 7], 2)
        pass
    except ValueError:
        assert True
    try:
        remove([1, 4, 5, 7], 14)
        pass
    except ValueError:
        assert True
    
def testremoveseq():
    try:
        removeseq([1, 4, 5, 7], 1, 3)
        pass
    except ValueError:
        assert True

def testreplace():
    try:
        replace([1, 4, 5, 7], 12, 15)
        pass
    except ValueError:
        assert True
    try:
        replace([1, 4, 5, 7], 2, 150)
        pass
    except ValueError:
        assert True

def testless():
    try:
        less([1, 4, 5, 7], 150)
        pass
    except ValueError:
        assert True

def testsortedval():
    try:
        sortedval([1, 15, 6, 4, 7, 19, 13], 150)
        pass
    except ValueError:
        assert True

def testavg():
    try:
        avg([1, 4, 5, 7], 0, 15)
        pass
    except ValueError:
        assert True
    try:
        avg([1, 4, 5, 7], 15, 3)
        pass
    except ValueError:
        assert True
    try:
        avg([1, 4, 5, 7], 3, 1)
        pass
    except ValueError:
        assert True

def testminim():
    assert minim([1, 4, 5, 7], 1, 3) == 4
    try:
        minim([1, 4, 5, 7], 15, 3)
        pass
    except ValueError: 
        assert True
    try:
        minim([1, 4, 5, 7], 2, 15)
        pass
    except ValueError:
        assert True
    try:
        minim([1, 4, 5, 7], 3, 1)
        pass
    except ValueError:
        assert True

def testmul():
    assert mul([1, 4, 5, 7], 5, 0, 3) == [5]
    try:
        mul([1, 4, 5, 7], 150, 0, 3)
        pass
    except ValueError:
        assert True
    try:
        mul([1, 4, 5, 7], 5, 15, 3)
        pass
    except ValueError:
        assert True
    try:
        mul([1, 4, 5, 7], 5, 3, 15)
        pass
    except ValueError:
        assert True
    try:
        mul([1, 4, 5, 7], 5, 3, 1)
        pass
    except ValueError:
        assert True

def testfilter_mul():
    try:
        filter_mul([1, 4, 5, 7], 150)
        pass
    except ValueError:
        assert True
def testfilter_greater():
    try:
        filter_greater([1, 4, 5, 7], 150)
        pass
    except ValueError:
        assert True

def runTests():
    testaddnumbers()
    testinsert()
    testremove()
    testremoveseq()
    testreplace()
    testless()
    testsortedval() 
    testavg()
    testminim()
    testmul()
    testfilter_mul()
    testfilter_greater()
