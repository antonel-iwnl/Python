import utils.helpers as h


class Patient:
    def __init__(self, first_name, last_name, PNC, disease):
        """
        Create a patient object with properties first_name, last_name, PNC and disease.
        :param first_name:
        :type first_name: str
        :param last_name:
        :type last_name: str
        :param PNC:
        :type PNC: int
        :param disease:
        :type disease: str
        """
        self.__first_name = first_name
        self.__last_name = last_name
        self.__disease = disease
        if h.checkPNC(PNC):
            self.__PNC = PNC
        else:
            raise ValueError("PNC is not valid!")

    # getter functions for the properties
    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def PNC(self):
        return self.__PNC

    @property
    def disease(self):
        return self.__disease

    @property
    def age(self):
        return h.getAge(self.__PNC)

    @first_name.setter
    def first_name(self, newFirstName):
        self.__first_name = newFirstName

    @last_name.setter
    def last_name(self, newLastName):
        self.__last_name = newLastName

    @PNC.setter
    def PNC(self, newPNC):
        self.__PNC = newPNC

    @disease.setter
    def disease(self, newDisease):
        self.__disease = newDisease

    def __repr__(self):
        """
        Return the string representation of the patient.
        :return:
        :rtype:
        """
        return f"Patient({self.__first_name}, {self.__last_name}, {self.__PNC}, {self.__disease})"

    def __str__(self):
        """
        Function called when converting object into string
        :return:
        :rtype:
        """
        return self.__repr__()
    


# p = Patient('Antonio', 'Rochnean', '5030524245060', 'orb')
# print(p.age)