from infrastructure.repositories import *

class HospitalController:
    def __init__(self, initialDepartments=None):
        self.__hospitalRepo = Hospital(initialDepartments)
    
    def __str__(self):
        return f"In controller:\n{self.__hospitalRepo}"
    
    def addDepartment(self):
        #Adds a department
        self.__hospitalRepo.addDepartment()
    
    def deleteDepartment(self):
        #Deletes a department by given index
        index = int(input("Input an index: "))
        self.__hospitalRepo.deleteDepartment(index)
    
    def updateDepartment(self):
        #Updates a department by given index
        self.__hospitalRepo.updateDepartment()
    
    def printHospital(self):
        #Prints the hospital in the controller
        print(self.__hospitalRepo)