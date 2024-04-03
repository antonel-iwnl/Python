def commonDigits(N, M):
    nrcifre = 0
    f1 = [0] * 10
    f2 = [0] * 10
    while (N > 0):
        f1[N % 10] += 1
        N = N // 10
    while (M > 0):
        f2[M % 10] += 1
        M = M // 10
    for i in range(10):
        if (f1[i] > 0 and f2[i] > 0):
            nrcifre += 1
    return nrcifre

def printcomdigits(N, M):
    d = []
    f1 = [0] * 10
    f2 = [0] * 10
    while (N > 0):
        f1[N % 10] += 1
        N = N // 10
    while (M > 0):
        f2[M % 10] += 1
        M = M // 10
    for i in range(10):
        if (f1[i] > 0 and f2[i] > 0):
            d.append(i)
    return d
N = int(input("N= " )) #21348
M = int(input("M= " )) #14513
print(commonDigits(N, M))
print(printcomdigits(N, M))