#!/usr/python

n = int(input("Enter your number of months here please: "))
k = int(input("Enter your number of off-springs/subunits here please: "))

def Fibonacci_Rabbit(n,k):
    if n <= 0:
        print("Incorrect input")
    elif n == 1 and 0< k <= 5:
        return 1
    elif n == 2 and 0< k <= 5:
        return 1
    elif 3<= n <= 40 and 0< k <= 5:
        return (Fibonacci_Rabbit(n - 1, k) + k*(Fibonacci_Rabbit(n - 2, k)))

print(Fibonacci_Rabbit(n, k))
