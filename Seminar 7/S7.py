import utils.helpers as h


class Student:
    def __init__(self, id_, name, group, grades):
        """
        Create a student object with id, name and grade
        :param id_:
        :type id_: int
        :param name:
        :type name: str
        :param grade:
        :type grade: int
        """
        self.__id = id_
        self.__name = name
        self.__group = group
        self.__grades = []
        for grade in grades:
            if h.checkGrade(grade):
                self.__grades.append(grade)
            else:
                raise ValueError("grade is not correct!")

    # the name of the function becomes the name of the property
    # refer as s.name
    @property
    def name(self):
        """
        Get the name of the student
        :return:
        :rtype: str
        """
        return self.__name

    @property
    def group(self):
        """
        Get the group of the student
        :return:
        :rtype: str
        """
        return self.__group

    @property
    def id(self):
        """
        Get the id of the student
        :return:
        :rtype: int
        """
        return self.__id

    @property
    def grades(self):
        """
        Get the grade of the student
        :return:
        :rtype: int
        """
        return self.__grades[:]

    @name.setter
    def name(self, newName):
        """
        Set the name of the student
        :return:
        :rtype: str
        """
        self.__name = newName

    @group.setter
    def group(self, newGroup):
        """
        Set the group of the student
        """
        self.__name = newGroup

    @id.setter
    def id(self, newId):
        """
        Set the id of the student
        :return:
        :rtype: int
        """
        self.__id = newId

    def maximumGrade(self):
        """
        Get the maximum grade of the student
        :return:
        :rtype: int
        """
        if len(self.__grades) == 0:
            raise ValueError("Student has no grades!")
        return max(self.__grades)

    def minimumGrade(self):
        """
        Get the minimum grade of the student
        :return:
        :rtype: int
        """
        if len(self.__grades) == 0:
            raise ValueError("Student has no grades!")
        return min(self.__grades)

    def averageGrade(self):
        """
        Get the maximum grade of the student
        :return:
        :rtype: float
        """
        if len(self.__grades) == 0:
            raise ValueError("Student has no grades!")
        return sum(self.__grades) / len(self.__grades)

    def __repr__(self):
        """
        Return the string representation of the student.
        :return:
        :rtype:
        """
        # return "Student(" + str(self.__id) + ", " + self.__name + ", " + str(self.__grade) + ")"
        grades = "[" + ", ".join([str(grade) for grade in self.__grades]) + "]"
        return f"Student({self.__id}, {self.__name}, {grades})"

    def __str__(self):
        """
        Function called when converting object into string
        :return:
        :rtype:
        """
        return self.__repr__()

    def __eq__(self, other):
        """
        Check if two student objects are equal by comparing the their properties
        :param other:
        :type other: Student
        :return:
        :rtype: bool
        """
        sameGrades = True
        if len(self.__grades) != len(other.__grades):
            sameGrades = False
        else:
            for index in range(len(self.__grades)):
                if self.__grades[index] != other.__grades[index]:
                    sameGrades = False
                    break
        return self.__id == other.__id and self.__name == other.__name and self.__group == other.__group and sameGrades


class StudentRepository:
    def __init__(self, initialStudents=None):
        """
        Creating a repository containing students
        """
        self.__listOfStudents = []
        if initialStudents is not None:
            # check if the ids are unique
            for student in initialStudents:
                if isinstance(student, Student) and self.__isIdUnique(student.id):
                    self.__listOfStudents.append(student)

    def addStudent(self, id_, name, grade):
        """
        S6. ex. 1
        Add a new student to the repository
        :param id_:
        :type id_: int
        :param name:
        :type name: str
        :param grade:
        :type grade: int
        :return:
        :rtype:
        """
        if not self.__isIdUnique(id_):
            raise ValueError("This id is already in the list!")
        else:
            self.__listOfStudents.append(Student(id_, name, grade))

    def getStudentCount(self):
        """
        S6. ex. 3
        Get the number of students in the repostiroy
        :return:
        :rtype: int
        """
        return len(self.__listOfStudents)

    def getIndexOfStudent(self, id_):
        """
        S6. ex. 4
        Get the index of a student identified by his/her id.
        :param id_:
        :type id_: int
        :return:
        :rtype: int
        """
        for index, student in enumerate(self.__listOfStudents):
            if student.id == id_:
                return index
        return -1

    def getStudents(self):
        """
        S6. ex. 5
        Get all students from the repository.
        Return a copy of the list! Otherwise, the user can change the content of the list.
        :return:
        :rtype: list
        """
        return self.__listOfStudents[:]

    def getAtIndex(self, index):
        """
        S6. ex. 6.
        Get student at a specified index.
        :param index:
        :type index: int
        :return:
        :rtype: Student
        """
        if self.__isIndexCorrect(index):
            return self.__listOfStudents[index]
        else:
            raise IndexError(f"Index is not correct!")

    def __getitem__(self, index):
        return self.getAtIndex(index)

    def getByID(self, id):
        """
        S6. ex. 7.
        get student by id
        :param id:
        :type id:
        :return:
        :rtype:
        """
        if self.__isIdUnique(id):
            raise ValueError
        else:
            return self.getAtIndex(self.getIndexOfStudent(id))

    def getMaximumGrade(self):
        """
        Get the maximum grade from all the students in the repository
        :return:
        :rtype: int
        """
        if len(self.__listOfStudents) == 0:
            raise ValueError("There are no students in the repository!")
        maxGrade = 0
        for student in self.__listOfStudents:
            if student.maximumGrade() > maxGrade:
                maxGrade = student.maximumGrade()
        return maxGrade

    def studentsWithMaximumGrades(self):
        """
        S7. ex. 1.
        Get students with the maximum grade
        :return:
        :rtype: StudentRepository
        """
        students = []
        maximumGrade = self.getMaximumGrade()
        for student in self.__listOfStudents:
            if student.maximumGrade() == maximumGrade:
                students.append(student)
        return StudentRepository(students)

    def getMaximumAverageGrade(self):
        """
        Get the maximum grade from all the students in the repository
        :return:
        :rtype: int
        """
        if len(self.__listOfStudents) == 0:
            raise ValueError("There are no students in the repository!")
        maxGrade = 0
        for student in self.__listOfStudents:
            if student.averageGrade() > maxGrade:
                maxGrade = student.averageGrade()
        return maxGrade

    def studentsWithMaximumAverageGrades(self):
        """
        S7. ex. 2.
        Get students with the maximum average grade
        :return:
        :rtype: StudentRepository
        """
        students = []
        maximumGrade = self.getMaximumAverageGrade()
        for student in self.__listOfStudents:
            if student.averageGrade() == maximumGrade:
                students.append(student)
        return StudentRepository(students)

    def getAverageOfMaximumsInGroup(self, group):
        """
        S7. ex. 3.
        Get average of maimum grades in a given group
        :param group:
        :type group: str
        :return:
        :rtype: float
        """
        grades = []
        for student in self.__listOfStudents:
            if student.group == group:
                grades.append(student.maximumGrade())
        if len(grades) == 0:
            raise ValueError("There are no students in the specific group!")
        else:
            return sum(grades) / len(grades)

    def getMinimumGradeInGroup(self, group):
        """
        S7. ex. 4.
        Get the minimum grade of any student from a group
        :param group:
        :type group: str
        :return:
        :rtype: int
        """
        grades = []
        for student in self.__listOfStudents:
            if student.group == group:
                grades.append(student.minimumGrade())
        if len(grades) == 0:
            raise ValueError("There are no students in the specific group!")
        else:
            return min(grades)

    def updateGradeByID(self, grades):
        """
        S7. ex. 5.
        Update the grades of a student specified by ID.
        :param grades:
        :type grades: list
        """
        pass

    def getStudentIDsByName(self, name):
        """
        S7. ex. 6.
        Get id(s) of student(s) with a given name
        :param name:
        :type name: str
        :return:
        :rtype: list
        """
        ids = []
        for student in self.__listOfStudents:
            if student.name == name:
                ids.append(student.id)
        return ids

    def __isIndexCorrect(self, index):
        """
        Check if the index is correct in the list of student
        :param index:
        :type index: int
        :return:
        :rtype: bool
        """
        return 0 <= index < len(self.__listOfStudents) or 0 == index == len(self.__listOfStudents)

    def __isIdUnique(self, id_):
        """
        Check if the given id is already in the list.
        :param id_:
        :type id_: int
        :return:
        :rtype: bool
        """
        for student in self.__listOfStudents:
            if student.id == id_:
                return False
        return True

    def __repr__(self):
        """
        Return the string representation of the class.
        :return:
        :rtype: str
        """
        if len(self.__listOfStudents) == 0:
            return "No students!"
        else:
            str_repr = ""
            for student in self.__listOfStudents:
                str_repr += str(student) + "\n"
            return str_repr


# if __name__ == "__main__":
#     s = Student(1, 'A', 6)
#     print(s)

sr = StudentRepository()
Student1 = (1, "A", 9)
Student2 = (2, "B", 7)
Student3 = (3, "C", 3)
sr.addStudent(1, "A", 9)
sr.addStudent(2, "B", 7)
sr.addStudent(3, "C", 3)
print(sr.studentsWithMaximumGrades())
