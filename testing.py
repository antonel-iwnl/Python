def sumOfFirstNumbers(n):
    s = 0
    for i in range(1, n+1):
        s = s + i
    return s

def mySum(n):
    res = 0
    for i in range(n):
        res = res + i
    return res


print(sumOfFirstNumbers(5), 'prima')
print(mySum(5), 'a doua')