import utils.helpers as h
from domain.person import *
from utils.sort import mySort
from utils.search import myFilter
from utils.back_track import getSolutions


class Department:
    def __init__(self, id, name, number_of_beds, initialPatients=None):
        #Initialises the department with properties: id, name, number of beds, and the list of patients
        self.__id = id
        self.__name = name
        self.__number_of_beds = number_of_beds
        self.__listOfPatients = []
        if initialPatients is not None:
            for Patient in initialPatients:
                if self.__number_of_beds > len(self.listOfPatients):
                    self.__listOfPatients.append(Patient)
                else:
                    raise ValueError("No more beds available!")

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def number_of_beds(self):
        return self.__number_of_beds

    @property
    def listOfPatients(self):
        return self.__listOfPatients[:]


    @id.setter
    def id(self, newID):
        self.__id = newID

    @name.setter
    def name(self, newName):
        self.__name = newName

    @number_of_beds.setter
    def number_of_beds(self, newNumberOfBeds):
        self.__number_of_beds = newNumberOfBeds

    def NRPatients(self):
        #Returns how many patients there are in a department
        return len(self.__listOfPatients)
    
    def NRPatientsAge(self, age):
        count = 0
        for patient in self.__listOfPatients:
            if patient.age > age:
                count += 1
        return count

    def isPatientUnderAge(self, age):
        #If the patients's age is lower than the upper bound age
        for patient in self.__listOfPatients:
            if patient.age < age:
                return True
        return False

    def __repr__(self):
        """
        Return the string representation of the department.
        :return:
        :rtype:
        """
        return f"Department({self.__id}, {self.__name}, {self.__number_of_beds}, {self.__listOfPatients})"

    def __str__(self):
        """
        Function called when converting object into string
        :return:
        :rtype:
        """
        return self.__repr__()
    
    def addPatient(self):
        #Adds a patient to the department
        if (self.NRPatients() < self.__number_of_beds):
            pfirst_name = str(input("Input patient first name: "))
            plast_name = str(input("Input patient last name: "))
            pPNC = str(input("Input patient PNC: "))
            pdisease = str(input("Input patient disease: "))
            self.__listOfPatients.append(Patient(pfirst_name, plast_name, pPNC, pdisease))
        else:
            print("This department has no more beds available!")

    def sortByPNC(self):
        #ex. 3: Sort all patients in a department by PNC
        return Department(
            self.__id, self.__name, self.__number_of_beds, mySort(self.__listOfPatients, lambda x, y: x.PNC < y.PNC)
        )
    
    def getPatientsString(self, givenstring):
        #Searches for patients that have a given string in their name
        pstr = []
        for patient in self.__listOfPatients:
            if givenstring in patient.first_name or givenstring in patient.last_name:
                pstr.append(patient)
        return pstr

    def patientWithName(self, givenname):
        #Searches the patient for correct name
        for patient in self.__listOfPatients:
            if givenname == patient.first_name or givenname == patient.last_name:
                return True
        return False
    
    def patientsAlfabetically(self):
        #Gets the patients in a department alphabetically
        return Department(self.__id, self.__name, self.__number_of_beds, mySort(self.__listOfPatients, lambda x, y: x.first_name < y.first_name))

    def unique_values(currentSolution):
        if len(currentSolution) == len(set(currentSolution)):
            return True
        else:
            return False

    def groupPatientsByDisease(self, k):
        filtered = myFilter(self.__listOfPatients, lambda x: x.disease)
        print(getSolutions(filtered, isConsistentFn=self.unique_values, isSolutionFn=lambda currentSolution: len(currentSolution) == k))
        


    # def sortAlphabetically(self):
    #     return Department(
    #         self.__id, self.__name, self.__number_of_beds, mySort(self.__listOfPatients, lambda x: x.last_name())
    #     )
    
    

class Hospital:
    def __init__(self, initialDepartments=None):
        """
        Creating a repository containing the departments
        """
        self.__listOfDepartments = []
        if initialDepartments is not None:
            for department in initialDepartments:
                if isinstance(department, Department) and self.__isIdUnique(department.id):
                    self.__listOfDepartments.append(department)
 
    def __isIdUnique(self, id):
        #Check if ids are unique
        """
        Check if the given id is already in the list
        :param name_id:
        :type name_id: int
        :return:
        :rtype: bool
        """
        for department in self.__listOfDepartments:
            if department.id == id:
                return False
        return True
    
    def updateDepartment(self):
        #Updates a deparment with new values
        index = int(input("Input the index of the department which you want to update: "))
        newId = int(input("Input a new id: "))
        if self.__isIdUnique(self, newId):
            newName = str(input("Input a new name for the department: "))
            newNumberOfBeds = int(input("Input a new number of beds: "))
            self.__listOfDepartments[index].id = newId
            self.__listOfDepartments[index].name = newName
            self.__listOfDepartments[index].number_of_beds = newNumberOfBeds
            n = int(input("Input the number of patients in the department: "))
            if (n <= newNumberOfBeds):
                myPatients = []
                while n > 0:
                    pfirst_name = str(input("Input patient first name: "))
                    plast_name = str(input("Input patient last name: "))
                    pPNC = str(input("Input patient PNC: "))
                    pdisease = str(input("Input patient disease: "))
                    myPatients.append(Patient(pfirst_name, plast_name, pPNC, pdisease))
                    n -= 1
                self.__listOfDepartments[index].__listOfPatients = myPatients
            else:
                print("Patients cannot be fit in the department!")
    
    def addDepartment(self):
        #Adds a new department tot the list
        n = int(input("Input the number of patients in the department: "))
        did = int(input("Input the id of the department: "))
        dname = str(input("Input the name of the department: "))
        dnumber_of_beds = int(input("Input the number of beds available in the department: "))
        if self.__isIdUnique(did):
            if (n <= dnumber_of_beds):
                myPatients = []
                while n > 0:
                    pfirst_name = str(input("Input patient first name: "))
                    plast_name = str(input("Input patient last name: "))
                    pPNC = str(input("Input patient PNC: "))
                    pdisease = str(input("Input patient disease: "))
                    myPatients.append(Patient(pfirst_name, plast_name, pPNC, pdisease))
                    n -= 1
                self.__listOfDepartments.append(Department(did, dname, dnumber_of_beds, myPatients))
            else:
                print("Patients cannot be fit in the department!")
        else:
            print("This id is already in use!")
        
    def getDepAtIndex(self, index):
        #Gets a department at given index
        return self.__listOfDepartments[index]
    
    def deleteDepartment(self, index):
        #Deletes a department at given index
        del self.__listOfDepartments[index]

    def sortDepByNrOfPatients(self):
        #ex. 4: Sort Departments by Number of Patients
        return Hospital(
            mySort(self.__listOfDepartments, lambda x, y: x.NRPatients() < y.NRPatients())
            )
    
    def sortDepByPatientsAge(self, age):
        #ex. 5: Sort Departments by Number of Patients with the age above
        #A given age value
        return Hospital(
            mySort(self.__listOfDepartments, lambda x, y: x.NRPatientsAge(age) < y.NRPatientsAge(age))
        )
    
    def sortDepNrOfPatientsAlfabetically(self):
        #ex. 6: Sort departments by the number of patients and the patients 
        #in a department alphabetically
        sorted = Hospital(myFilter(self.__listOfDepartments, lambda x: x.patientsAlfabetically()))
        return Hospital(
            mySort(self.__listOfDepartments, lambda x, y: x.NRPatients() < y.NRPatients())
        )

    def getDepPatientsUnderAge(self, age):
        #ex. 7: Identify departments where there are patients under a given age
        departs = []
        aged = age
        for department in self.__listOfDepartments:
            if department.isPatientUnderAge(aged):
                departs.append(department)
        return departs
    
    def getDepWithPatients(self, givenid, givenstring):
        #ex. 8: Identify patients from a given department for which the first name or last name contain a given string
        pstr = []
        for department in self.__listOfDepartments:
            if givenid == department.id:
                pstr = department.getPatientsString(givenstring)
        return pstr

    def getDepWithPatientName(self, givenname):
        #ex. 9: Identify department/departments where there are patients with a given first name
        departs = []
        for department in self.__listOfDepartments:
            if department.patientWithName(givenname):
                departs.append(department)
        return departs
    
    def getDepartments(self):
        #Returns how many departments there are in the repository
        return len(self.__listOfDepartments)
    
    def sortDepByIndexPNC(self, index):
        #sorts a department given by index with pnc
        return self.__listOfDepartments[index].sortByPNC()

    def __repr__(self):
        """
        Return the string representation of the Hospital.
        :return:
        :rtype:
        """
        return f"Hospital({self.__listOfDepartments})"

    def __str__(self):
        """
        Function called when converting object into string
        :return:
        :rtype:
        """
        return self.__repr__()
    
    def groupDepartmentsSameDisease(self, k):
        for department in self.__listOfDepartments:
            return department.groupPatientsByDisease(k)
    
 
    def groupDepartments(self, k, p):
        filtered = myFilter(self.__listOfDepartments, lambda x: x.disease)
        return getSolutions(filtered, doesElementExistFn=lambda element: element.getNRPatients() <= p, isSolutionFn=lambda currentSolution: len(currentSolution) == k)
    



#ex. 10/11 filter departments/patients in advance and generate the k-group with the indices and replace the elements in the list
#example in the seminar, hopefully not that hard to implement :DDDDDD
#actually it is the 'isconsistent' function
#just call a filter before the isconsistent


# h = Hospital([
#             Department(1, 'Alpha', 14, [
#             Patient('Antonio', 'Rochnean', '5030524245060', 'disease1'),
#             Patient('David', 'Simon', '1890712123070', 'disease1'),
#             Patient('Sarah', 'Bryant', '6081211019891', 'disease2'),
#             Patient('Mariah', 'Nicolae', '2830412019906', 'disease3'),
#             Patient('Andrei', 'Spataru', '1970707195457', 'disease3')
#             ]),
#             Department(2, 'Bravo', 7, [
#                 Patient('Mihai', 'Crasmaru', '5020524268021', 'disease1'),
#                 Patient('Raluca', 'Bledea', '6010219387001', 'disease1'),
#                 Patient('Alexandra', 'Mihai', '6030902248111', 'disease1'),
#                 Patient('Vasile', 'Mihai', '5051001249252', 'disease2'),
#                 Patient('Stefan', 'Hrusca', '1571208238605', 'disease3')
#             ])
#             ])
# print(h.getDepWithPatients(1, 'S'))