def nrdig5(x):
    d = 0
    dig5 = 0
    while (x > 1):
        d = x % 10
        if (d == 5):
            dig5 += 1
        x = x // 10
    return dig5
def nr5higher(list):
    nrnumere = 0
    for i in range(len(list) - 2):
        if (nrdig5(list[i]) > nrdig5(list[i + 1])):
            nrnumere += 1
            print(list[i], list[i + 1])
    return nrnumere
var = []
var.append(int(input()))
i = 0
while (var[i] != 0):
    var.append(int(input()))
    i += 1
print(nr5higher(var))
