def nrof1s(x):
    nr1 = 1
    while (x > 1):
        if (x % 2 == 1):
            nr1 = nr1 + 1
        x = x // 2 #we need the integer number
    return nr1
x = int(input("x= "))
print (nrof1s(x))

#547 / 2 = 223 / 2
