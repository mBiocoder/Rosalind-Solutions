#!/usr/python3

a = int(input("Your a value: "))
b = int(input("Your b value: "))

sum = 0
if a < b < 10000:
   for i in range(a, b+1):
       if i %2 ==1:
           sum = sum +i
   print(sum)

