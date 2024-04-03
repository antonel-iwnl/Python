from unittest import TestCase
from domain.lab8A4 import *
import numpy as np


class TestVector(TestCase):
    def setUp(self):
        self.vector = MyVector(1, 'y', 1, [1, 2, 3, 4, 5])

    def testCreateVector(self):
        self.assertEqual(self.vector.name_id, 1)
        self.assertEqual(self.vector.colour, 'y')
        self.assertEqual(self.vector.type, 1)

    def testSetName_Id(self):
        self.vector.name_id = 7
        self.assertEqual(self.vector.name_id, 7)

    def testSetColour(self):
        self.vector.colour = 'g'
        self.assertEqual(self.vector.colour, 'g')

    def testSetType(self):
        self.vector.type = 3
        self.assertEqual(self.vector.type, 3)

    def testSetValues(self):
        self.vector.values = [2]
        self.assertEqual(self.vector.values, [2])

    def testStringRepresentation(self):
        self.assertEqual(str(self.vector), "MyVector(1, y, 1, [1 2 3 4 5])")
    
    def testAddScalar(self):
        self.vector.values = [1, 3, 4]
        new_list = list(np.array(self.vector.values + 2))
        print(new_list)
        self.assertEqual(new_list, [3, 5, 6])

    def testAddTwoVectors(self):
        self.vector.values = [1, 2, 3]
        new_list = list(np.array(self.vector.values + [1, 2, 3]))
        print(new_list)
        self.assertEqual(new_list, [2, 4, 6])

    def testSubtractTwoVectors(self):
        self.vector.values = [2, 3, 4]
        new_list = list(np.array(self.vector.values - [1, 1, 1]))
        print(new_list)
        self.assertEqual(new_list, [1, 2, 3])

    def testMultiplyTwoVectors(self):
        self.vector.values = [1, 2, 3]
        value = float(np.sum(np.multiply(np.array(self.vector.values), [1, 2, 3])))
        print(value)
        self.assertEqual(value, 14)

    def testSumOfElements(self):
        self.vector.values = [1, 3, 4]
        sum_of_elements = float(np.sum(self.vector.values))
        print(sum_of_elements)
        self.assertEqual(sum_of_elements, 8)

    def testProdOfElements(self):
        self.vector.values = [1, 3, 4]
        prod_of_elements = float(np.product(self.vector.values))
        print(prod_of_elements)
        self.assertEqual(prod_of_elements, 12)

    def testAverageOfElements(self):
        self.vector.values = [1, 2, 3]
        avg = float(np.average(self.vector.values))
        print(avg)
        self.assertEqual(avg, 2)

    def testMinOfElements(self):
        self.vector.values = [1, 2, 3]
        minn = float(np.min(self.vector.values))
        print(minn)
        self.assertEqual(minn, 1)

    def testMaxOfElements(self):
        self.vector.values = [1, 3, 4]
        maxx = float(np.max(self.vector.values))
        print(maxx)
        self.assertEqual(maxx, 4)


class TestRepository(TestCase):
    def setUp(self):
        self.repo1 = VectorRepository([
            MyVector(1, 'b', 1, [5, 9, 6]),
            MyVector(2, 'r', 2, [8]),
            MyVector(3, 'y', 3, [9, 7]),
            MyVector(4, 'm', 4, []),
            MyVector(5, 'g', 5, [4, 6]),
        ])
        self.repo2 = VectorRepository([
            MyVector(6, "b", 1, []),
            MyVector(7, "r", 2, [8]),
            MyVector(8, "y", 3, [8, 6]),
            MyVector(9, "m", 4, [5]),
            MyVector(10, "g", 1, [4, 8]),
            MyVector(11, "r", 2, [8, 7, 6]),
            MyVector(12, "b", 3, [7]),
        ])

    def testCreateVectorRepository(self):
        self.assertEqual(VectorRepository.getVectorCount(self.repo1), 5)
        self.assertEqual(VectorRepository.getVectorCount(self.repo2), 7)

    def testAddVector(self):
        self.repo1.addVector(13, 'b', 2, [2, 3, 4, 1])
        self.assertEqual(VectorRepository.getVectorCount(self.repo1), 6)

    def testUpdateVectorAtIndex(self):
        self.repo1.updateVectorAtIndex(0, 29, 'g', 2, [8, 4, 2, 1])
        print(self.repo1.getVectorAtIndex(0))
        self.assertEqual(str(self.repo1.getVectorAtIndex(0)), "MyVector(29, g, 2, [8 4 2 1])")



    def testUpdateVectorByName(self):
        self.repo2.updateVectorByNameId(12, 'm', 4, [9, 9, 9])
        print(self.repo2.getIndexOfVectoryByNameId(12))
        self.assertEqual(str(self.repo2.getVectorAtIndex(self.repo2.getIndexOfVectoryByNameId(12))), "MyVector(12, m, 4, [9 9 9])")

    def testDeleteAtIndex(self):
        self.repo1.delVectorByIndex(1)
        self.assertEqual(self.repo1.getVectorCount(), 4)

    def testDeleteAtName(self):
        self.repo2.delVectorByNameId(12)
        self.assertEqual(self.repo2.getVectorCount(), 6)


