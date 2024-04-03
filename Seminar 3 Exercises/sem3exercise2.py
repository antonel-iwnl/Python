from re import S


def toString(list_Of_Numbers):
    s = ''
    for value in list_Of_Numbers:
        s += str(value)
    return S