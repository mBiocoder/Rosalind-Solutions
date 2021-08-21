#!/usr/python3

s = input("Enter your string here: ")

dict = {}

for word in s.split(' '):
    #print (word)
    if word not in dict:
        dict[word] = 1
    else:
        dict[word] += 1

for key, value in dict.items():
    print (key + ' ' + str(value))





