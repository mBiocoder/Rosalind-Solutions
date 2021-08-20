#!/usr/python

def MortalFibonacci(n, m):
    living = [1, 1]
    for i in range(2, n):
        # first reproduction
        tmp = living[i - 1] + living[i - 2]
        # then death
        if i == m:
            tmp = tmp - 1
        if i > m:
            tmp = tmp - living[i - m - 1]
        living.append(tmp)
    return living[-1] #return letzte Element der Liste

# months/generations
n = int(input("Enter your number of months here please: "))
# survival time
m = int(input("Enter your survival time here please: "))

print(MortalFibonacci(n, m))
