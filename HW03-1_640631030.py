# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 00:19:33 2021

@author: Mind
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 13:33:23 2021
Hw02_Human vs python stick taker
@author: Mind
"""

n = int(input("How many sticks in the pile: "))
print("There are", n, "in the pile")
name = input("What is your name : ")  # player name
while n > 0:
    # Condition i <= 2
    i = int(input(name+",how many sticks you will take (1 or 2)"))
    if i < 0:
        print("No you cannot take less than 1 stick !!")
        continue
        print(i)
    elif i >= 3:
        print("No you cannot take more than 2 sticks !!")
        continue
        print(i)
    elif i == 0:
        print("You need to take some sticks !!")
        continue
        print(i)

    n = n-i
    if n > 0:
        print("There are", n, "sticks in the pile")
    elif n == 0:
        print(name, ", takes the last stick")
        print("PYTHON WIN !!!")  # Human lose python win
        break

    if n == 1:  
        x = 1
    elif n == 2:
        x = 1
    elif n == 3:
        x = 2
    elif n == 5: # to make python smarter 
        x = 1
    elif n == 6:
        x = 2
    elif n == 8:
        x = 1
    elif n == 9:
        x = 2
    elif n%2 == 0: #even number pick 2
        x = 2
    elif n%2 == 1: #odd number pick 1
        x = 1
    print("Python turn, I take", x, "stick(s)")

    n = n - x
    if n > 0:
        print("There are", n, "sticks in the pile")
    elif n == 0:
        print("Python, takes the last stick")
        print(name, "Win (Python felling sad :C)")  # Human win python lose
##Python always win if n = 4,7,10,...