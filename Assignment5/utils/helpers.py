from datetime import date

def checkPNC(givenPNC):
    if (len(givenPNC) == 13):
        return True
    else:
        return False

def getAge(givenPNC):
    firstletter = int(givenPNC[0])
    today = date.today()
    if firstletter == 5 or firstletter == 6:
        year = 2000 + int(givenPNC[1]) * 10 + int(givenPNC[2])
        month = int(givenPNC[3]) * 10 + int(givenPNC[4])
        day = int(givenPNC[5]) * 10 + int(givenPNC[6])
    elif firstletter == 1 or firstletter == 2:
        year = 1900 + int(givenPNC[1]) * 10 + int(givenPNC[2])
        month = int(givenPNC[3]) * 10 + int(givenPNC[4])
        day = int(givenPNC[5]) * 10 + int(givenPNC[6])
    age = today.year - year
    if (today.month <= month):
        if (today.day < day):
            age -= 1
    return int(age)


