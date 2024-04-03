from unittest import TestCase
from domain.person import *
from infrastructure.repositories import *

class TestPatient(TestCase):
    def setUp(self):
        self.patient = Patient('Antonio', 'Rochnean', '5030524245060', 'orb')

    def testCreatePatient(self):
        self.assertEqual(self.patient.first_name, 'Antonio')
        self.assertEqual(self.patient.last_name, 'Rochnean')
        self.assertEqual(self.patient.PNC, '5030524245060')
        self.assertEqual(self.patient.age, 19)
    
    def testSetFirst_Name(self):
        self.patient.first_name = 'Stefan'
        self.assertEqual(self.patient.first_name, 'Stefan')
    
    def testSetLast_Name(self):
        self.patient.last_name = 'Hrusca'
        self.assertEqual(self.patient.last_name, 'Hrusca')

    def testSetPNC(self):
        self.patient.PNC = '1840624240705'
        self.assertEqual(self.patient.PNC, '1840624240705')
    
    def testSetDisease(self):
        self.patient.disease = 'semi-orb'
        self.assertEqual(self.patient.disease, 'semi-orb')

    def testStringRepresentation(self):
        self.assertEqual(str(self.patient), "Patient(Antonio, Rochnean, 5030524245060, orb)")

class TestDepartments(TestCase):
    def setUp(self):
        self.repo1 = Department(1, 'Alpha', 14, [
            Patient('Antonio', 'Rochnean', '5030524245060', 'disease1'),
            Patient('David', 'Simon', '1890712123070', 'disease1'),
            Patient('Sarah', 'Bryant', '6081211019891', 'disease2'),
            Patient('Mariah', 'Nicolae', '2830412019906', 'disease3'),
            Patient('Andrei', 'Spataru', '1970707195457', 'disease3')
        ])
        
    def testCreateDepartments(self):
        self.assertEqual(Department.NRPatients(self.repo1), 5)

    def testSortByPNC(self):
        self.repo1.sortByPNC()
        self.assertEqual(str(self.repo1), 
        "Department(1, Alpha, 14, [Patient(David, Simon, 1890712123070, disease1), Patient(Andrei, Spataru, 1970707195457, disease3), Patient(Mariah, Nicolae, 2830412019906, disease3), Patient(Antonio, Rochnean, 5030524245060, disease1), Patient(Sarah, Bryant, 6081211019891, disease2)])"
        )
    
    def testGetPatientsString(self):
        #TODO implement test after you finish creating the function because i do not know what the teacher wants
        pass

class TestHospital(TestCase):
    def setUp(self):
        self.repo1 = Hospital([
            Department(1, 'Alpha', 14, [
            Patient('Antonio', 'Rochnean', '5030524245060', 'disease1'),
            Patient('David', 'Simon', '1890712123070', 'disease1'),
            Patient('Sarah', 'Bryant', '6081211019891', 'disease2'),
            Patient('Mariah', 'Nicolae', '2830412019906', 'disease3'),
            Patient('Andrei', 'Spataru', '1970707195457', 'disease3')
            ]),
            Department(2, 'Bravo', 7, [
                Patient('Mihai', 'Crasmaru', '5020524268021', 'disease1'),
                Patient('Raluca', 'Bledea', '6010219387001', 'disease1'),
                Patient('Alexandra', 'Mihai', '6030902248111', 'disease1'),
                Patient('Vasile', 'Bledea', '5051001249252', 'disease2'),
                Patient('Stefan', 'Hrusca', '1571208238605', 'disease3')
            ]),
            Department(3, 'Charlie', 3, [
                Patient('Lavinia', 'Michnea', '6030514247802', 'disease1'),
                Patient('Stefania', 'Mocanu', '6020312247731', 'disease2')
            ])
        ])
    
    def testCreateHospital(self):
        self.assertEqual(Hospital.getDepartments(self.repo1), 3)
    
    def testSortDepByNrOfPatients(self):
        self.repo1.sortDepByNrOfPatients()
        self.assertEqual(str(self.repo1),
        "Hospital([Department(3, Charlie, 3, [Patient(Lavinia, Michnea, 6030514247802, disease1), Patient(Stefania, Mocanu, 6020312247731, disease2)]), Department(2, Bravo, 7, [Patient(Mihai, Crasmaru, 5020524268021, disease1), Patient(Raluca, Bledea, 6010219387001, disease1), Patient(Alexandra, Mihai, 6030902248111, disease1), Patient(Vasile, Bledea, 5051001249252, disease2), Patient(Stefan, Hrusca, 1571208238605, disease3)]), Department(1, Alpha, 14, [Patient(Antonio, Rochnean, 5030524245060, disease1), Patient(David, Simon, 1890712123070, disease1), Patient(Sarah, Bryant, 6081211019891, disease2), Patient(Mariah, Nicolae, 2830412019906, disease3), Patient(Andrei, Spataru, 1970707195457, disease3)])])"
        )
    
    def testSortDepByPatientsAge(self):
        age = 19
        self.repo1.sortDepByPatientsAge(age)
        self.maxDiff = None
        self.assertEqual(str(self.repo1), 
        "Hospital([Department(3, Charlie, 3, [Patient(Lavinia, Michnea, 6030514247802, disease1), Patient(Stefania, Mocanu, 6020312247731, disease2)]), Department(1, Alpha, 14, [Patient(Antonio, Rochnean, 5030524245060, disease1), Patient(David, Simon, 1890712123070, disease1), Patient(Sarah, Bryant, 6081211019891, disease2), Patient(Mariah, Nicolae, 2830412019906, disease3), Patient(Andrei, Spataru, 1970707195457, disease3)]), Department(2, Bravo, 7, [Patient(Mihai, Crasmaru, 5020524268021, disease1), Patient(Raluca, Bledea, 6010219387001, disease1), Patient(Alexandra, Mihai, 6030902248111, disease1), Patient(Vasile, Bledea, 5051001249252, disease2), Patient(Stefan, Hrusca, 1571208238605, disease3)])])"
        )
    
    def testSortDepNrOfPatientsAlfabetically(self):
        self.repo1.sortDepNrOfPatientsAlfabetically()
        self.maxDiff = None
        self.assertEqual(str(self.repo1), "Hospital([Department(3, Charlie, 3, [Patient(Lavinia, Michnea, 6030514247802, disease1), Patient(Stefania, Mocanu, 6020312247731, disease2)]), Department(2, Bravo, 7, [Patient(Alexandra, Mihai, 6030902248111, disease1), Patient(Mihai, Crasmaru, 5020524268021, disease1), Patient(Raluca, Bledea, 6010219387001, disease1), Patient(Stefan, Hrusca, 1571208238605, disease3), Patient(Vasile, Bledea, 5051001249252, disease2)]), Department(1, Alpha, 14, [Patient(Andrei, Spataru, 1970707195457, disease3), Patient(Antonio, Rochnean, 5030524245060, disease1), Patient(David, Simon, 1890712123070, disease1), Patient(Mariah, Nicolae, 2830412019906, disease3), Patient(Sarah, Bryant, 6081211019891, disease2)])])")
    
    def testGetDepPatientsUnderAge(self):
        age = 16
        assert str(self.repo1.getDepPatientsUnderAge(age)) == "[Department(1, Alpha, 14, [Patient(Antonio, Rochnean, 5030524245060, disease1), Patient(David, Simon, 1890712123070, disease1), Patient(Sarah, Bryant, 6081211019891, disease2), Patient(Mariah, Nicolae, 2830412019906, disease3), Patient(Andrei, Spataru, 1970707195457, disease3)])]"

    def testGetDepWithPatientName(self):
        name = 'Mihai'
        assert str(self.repo1.getDepWithPatientName(name)) == "[Department(2, Bravo, 7, [Patient(Mihai, Crasmaru, 5020524268021, disease1), Patient(Raluca, Bledea, 6010219387001, disease1), Patient(Alexandra, Mihai, 6030902248111, disease1), Patient(Vasile, Bledea, 5051001249252, disease2), Patient(Stefan, Hrusca, 1571208238605, disease3)])]"

    def testGetDepWithPatients(self):
        givenstring = 'S'
        assert str(self.repo1.getDepWithPatients(1, 'S')) == "[Patient(David, Simon, 1890712123070, disease1), Patient(Sarah, Bryant, 6081211019891, disease2), Patient(Andrei, Spataru, 1970707195457, disease3)]"