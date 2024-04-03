def computeTheAge(cd, cm, cy, bd, bm, by):
    age = 0
    if (by == cy):
        age = 0
    if (by < cy and bm == cm and bd >= cm):
        age = cy - by
    if (by < cy and bm == cm and bd < cd):
        age = (cy - by) - 1
    if (by < cy and bm < cm):
        age = cy - by
    if (by < cy and bm > cm):
        age = (cy - by) - 1
    return age

cday = int(input("current day= "))
cmonth = int(input("current month= "))
cyear = int(input("current year= "))
bday = int(input("birth day= "))
bmonth = int(input("birth month= "))
byear = int(input("birth year= "))
print (computeTheAge(cday, cmonth, cyear, bday, bmonth, byear))

