def maximumGrade(students):
    """
    Get the maximum grade of all students.
    :param students: list of students
    :type students: list
    :return: maximum grade
    :rtype: int
    """
    maximum = 0
    for i in students:
        if i[1] > maximum:
            maximum = i[1]
    return maximum
