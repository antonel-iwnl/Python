def functio(list):
    s = len(list) - 1
    while (s):
        if list[s] % 2 == 0:
            del list[s]
            break
        s -= 1
    while (s and list[s] % 2 == 0):
        del list[s]
        s -= 1