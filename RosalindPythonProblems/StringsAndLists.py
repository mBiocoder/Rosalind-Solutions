#!/usr/python3

string = input("Enter your string here: ")
a = int(input("Your a value: "))
b = int(input("Your b value: "))
c = int(input("Your c value: "))
d = int(input("Your d value: "))


if 1 <= len(string) <= 200:
    first_substring = string[a:b+1]
    second_substring = string[c: d+1]
    print(first_substring + " " + second_substring)
else:
   print("Enter your string in proper range!")

