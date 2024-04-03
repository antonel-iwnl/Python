def detdates(yr, dy):
    leapyr = 0
    month = 1
    dm = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (yr % 4 == 0 and (yr % 100 != 0 or yr % 400 == 0)):
        dm[1] += 1
    i = 0
    while(dy > dm[i]):
        dy -= dm[i]
        month += 1
        i += 1
    return str(dy) + "." + str(month) + "." + str(yr)
yr = int(input("year= "))
dy = int(input("day= "))
print(detdates(yr, dy))