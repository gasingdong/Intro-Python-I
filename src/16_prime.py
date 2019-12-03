import sys

args = sys.argv
isPrime = True
num = int(args[1])
limit = int(pow(num, 0.5)) + 1

if num > 2:
    for x in range(2, limit):
        if num % x == 0:
            isPrime = False
            break
else:
    isPrime = num == 2

print("Prime!" if isPrime else "Not Prime")
