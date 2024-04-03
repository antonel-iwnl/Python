#A sum is perfect if the sum of its divisors equals to itself.
n = int(input("n ="))
s = 0
# n // 2
for i in range(1, int(n / 2) + 1):
    if (n % i == 0):
        s += i
#print (n == s)
if (s == n):
    print(True)
else:
    print(False)
