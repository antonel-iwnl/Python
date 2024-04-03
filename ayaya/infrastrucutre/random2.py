from domain.random import Something

class SomethingRepository():
    def __init__(self, initialSomething):
        """
        Creating a repository containing the departments
        """
        self.__listOfSomething = []
        if initialSomething is not None:
            for something in initialSomething:
                if isinstance(something, Something) and self.__isXUnique(something.X):
                    self.__listOfSomething.append(something)
                
    #WRITE TESTS!!!!!
            
    def isXUnique(self, X):
        """
        Checks if the X is unique
        """
        for something in self.__listOfSomething:
            if something.x == X:
                return False
            return True
        
    def __repr__(self):
        """
        Return the string representation of the SomethingRepository.
        :return:
        :rtype:
        """
        return f"SomethingRepository({self.__listOfSomething})"

    def __str__(self):
        """
        Function called when converting object into string
        :return:
        :rtype:
        """
        return self.__repr__()