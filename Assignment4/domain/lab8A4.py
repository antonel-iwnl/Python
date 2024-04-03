import utils.helpers as h
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.markers import MarkerStyle


class MyVector:
    def __init__(self, name_id, colour, type, values = []):
        self.__name_id = name_id
        if (h.checkColour(colour)):
            self.__colour = colour
        else:
            raise ValueError("Colour set incorrectly!")
        if (type >= 1):
            self.__type = type
        else:
            raise ValueError("Type set incorrectly!")
        self.__values = []
        self.__values = np.array(values)


    @property
    def name_id(self):
        return self.__name_id

    @property
    def colour(self):
        return self.__colour

    @property
    def type(self):
        return self.__type

    @property
    def values(self):
        return self.__values[:]

    @name_id.setter
    def name_id(self, newName_id):
        self.__name_id = newName_id

    @colour.setter
    def colour(self, newColour):
        if (h.checkColour(newColour) == True):
            self.__colour = newColour
        else:
            raise ValueError("Color set incorrectly!")

    @type.setter
    def type(self, newType):
        if (newType >= 1):
            self.__type = newType
        else:
            raise ValueError("Type set incorrectly!")

    @values.setter
    def values(self, newValues):
        self.__values = np.array(newValues)


    def __add__(self, newVector):
        #Add a vector's values to the self vactor
        return MyVector(self.__name_id, self.__colour, self.__type, self.__values + newVector.__values)

    def add_scalar(self, scalar):
        #Add a scalar to the values of a vector
        return MyVector(self.__name_id, self.__colour, self.__type, np.array(self.__values) + scalar)

    def __repr__(self):
        return f"MyVector({self.__name_id}, {self.__colour}, {self.__type}, {np.array(self.__values)})"

    def __str__(self):
        return self.__repr__()

    def __eq__(self, newVector):
        #Update a vector
        return self.__name_id == newVector.__name_id and self.__colour == newVector.__color and self.__type == newVector.__type and np.array(
            self.__values) == np.array(newVector.__values)

    def add_vectors(self, newVector):
        #Add two vectors together and get the resulting values
        if (len(self.__values) == len(newVector.__values)):
            return np.add(np.array(self.__values), np.array(newVector.__values))
        else:
            raise ValueError("Length of the two vectors are not equal!")

    def subtract_vectors(self, newVector):
        #Substract two vectors and get the resulting values
        if (len(self.__values) == len(newVector.__values)):
            return np.subtract(np.array(self.__values), np.array(newVector.__values))
        else:
            raise ValueError("Length of the two vectors are not equal!")
        

    def multiply_vectors(self, newVector):
        #Multiply two vectors and get the resulting values
        if (len(self.__values) == len(newVector.__values)):
            return np.dot(np.array(self.__values), np.array(newVector.__values))
        else:
            raise ValueError("Length of the two vectors are not equal!")

    def sum(self):
        #Calculate the sum of all the values in the vector
        return np.sum(self.__values)

    def product(self):
        #Calculate the product of all the values from a vector
        return np.product(self.__values)

    def avg(self):
        #Calculate the average of all the values from a vector
        return np.average(self.__values)

    def minimum(self):
        #Calculate the minimum of all the values in a vector
        return np.min(self.__values)

    def maximum(self):
        #Calculate the maximum of all the values in a vector
        return np.max(self.__values)

class VectorRepository:
    # __markerPreset = ['o', 's', '^', 'D'] #So we get the specific marker style {circle, square, triangle, diamond} for plotting
    __markerPreset = {1 : 'o', 2 : 's', 3: '^'}

    def __init__(self, initialVectors=None):
        #Initialises the MyVector instances to a repository
        self.__list_of_vectors = []
        if initialVectors is not None:
            for vector in initialVectors:
                if isinstance(vector, MyVector) and self.__isIdUnique(vector.name_id):
                    self.__list_of_vectors.append(vector)
    
    def addVector(self, name_id, color, type, values=[]):
        """
        ex. 1
        Add a new vector to the repository
        :param name_id:
        :type name_id: int
        :param color:
        :type color: str
        :param type:
        :type color: int
        :param values:
        :type values: list
        :return:
        :rtype:
        """
        if (self.__isIdUnique(name_id)):
            self.__list_of_vectors.append(MyVector(name_id, color, type, values))

    def getVectors(self):
        #ex. 2
        #Get all vectors inside the repository
        return self.__list_of_vectors[:]
    
    def getVectorAtIndex(self, index):
        #ex. 3
        #Get the vector at a given index
        if (h.checkIndex(index, len(self.__list_of_vectors)) == True):
            return self.__list_of_vectors[index]
        else:
            raise IndexError("Index set incorrectly!")
    
    def updateVectorAtIndex(self, index, new_name_id, new_color, new_type, new_values=[]):
        #ex. 4
        #Update the vector at a given index
        if (h.checkIndex(index, len(self.__list_of_vectors)) == True and self.__isIdUnique(new_name_id) and h.checkColour(new_color) == True and new_type >= 1):
            vector = self.getVectorAtIndex(index)
            vector.colour = new_color
            vector.name_id = new_name_id
            vector.type = new_type
            vector.values = new_values
            
        else:
            raise IndexError("Index/ID set incorrectly!")

    def updateVectorByNameId(self, input_name_id, new_color, new_type, new_values = []):
        #ex. 5
        #Update vector by given name_id
        index = len(self.__list_of_vectors) - 1
        update = False
        while (index >= 0):
            vector = self.__list_of_vectors[index]
            if (vector.name_id == input_name_id):
                if(h.checkColour(new_color) == True and new_type >= 1):
                    vector.colour = new_color
                    vector.type = new_type
                    vector.values = new_values
                    update = True
            index -= 1
        if (update == False):
            raise ValueError("name_id not in the repository!")
            
        
    def delVectorByIndex(self, index):
        #ex. 6
        #Delete a vector by given index
        if (h.checkIndex(index, len(self.__list_of_vectors)) == True):
            del self.__list_of_vectors[index]
        else:
            raise IndexError("Index set incorrectly!")

    def delVectorByNameId(self, input_name_id):
        #ex. 7
        #Delete a vector by given name_id
        index = len(self.__list_of_vectors) - 1
        while (index >= 0):
            vector = self.__list_of_vectors[index]
            if (vector.name_id == input_name_id):
                del self.__list_of_vectors[index]
                break
            index -= 1

    def PlotInChart(self):
        #ex. 8
        #plot all vectors in a chart
        for vector in self.__list_of_vectors:
            plt.plot(np.linspace(0, len(vector.values) - 1, len(vector.values)), vector.values, vector.colour + self.__markerPreset.get(vector.type - 1, 'D'))
            #marker.get(1, 'D')
        plt.show()

    def __isIdUnique(self, name_id):
        #Check if ids are unique
        """
        Check if the given id is already in the list
        :param name_id:
        :type name_id: int
        :return:
        :rtype: bool
        """
        for vector in self.__list_of_vectors:
            if vector.name_id == name_id:
                return False
        return True

    def getVectorCount(self):
        #Returns how many vectors are in the repository
        return len(self.__list_of_vectors)
    
    def getVectorAtIndex(self, index):
        #Returns the vector from a given index
        if h.checkIndex(index, len(self.__list_of_vectors)) == True:
            return self.__list_of_vectors[index]
        else:
            raise IndexError("Index set incorrectly!")
    
    def getIndexOfVectoryByNameId(self, name_id):
        #Gets the index of the vector by using only its name_id
        index = len(self.__list_of_vectors) - 1
        while (index >= 0):
            vector = self.__list_of_vectors[index]
            if (vector.name_id == name_id):
                return index
            index -= 1
        




if __name__ == "__main__":
    v1 = MyVector(1, 'r', 1, [1, 2, 3, 4])
    v2 = MyVector(2, 'r', 1, [6, 7, 2, 3])
    # print(MyVector.__add__(v1, v2))
    # VectorRepository.addVector(1, 'r', 1, [1, 2, 3, 4])
    v = VectorRepository()
    v.addVector(1, 'r', 1, [6, 7, 8, 9])
    v.addVector(2, 'r', 2, [1, 2, 5, 9])
    v.PlotInChart()
    