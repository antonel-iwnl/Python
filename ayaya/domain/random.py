class Something():
    def __init__(self, property1, property2):
        self.__property1 = property1
        self.__property2 = property2
        #Maybe you have to check something with an if
        pass

    @property
    def property1(self):
        return self.__property1
    
    @property
    def property2(self):
        return self.__property2
    
    @property1.setter
    def property1(self, newProp):
        self.__property1 = newProp
    
    @property2.setter
    def property2(self, newProp):
        self.__property2 = newProp
    
    def __repr__(self):
        """
        Return the string representation of the Something.
        :return:
        :rtype:
        """
        return f"Something({self.__property1}, {self.__property2})"

    def __str__(self):
        """
        Function called when converting object into string
        :return:
        :rtype:
        """
        return self.__repr__()