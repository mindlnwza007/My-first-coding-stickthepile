# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 10:11:59 2021
HW03_2Stickthepile version2
@author: Mind
"""


n = int(input("How many sticks in the pile: "))
print("There are", n, "in the pile")
name = input("What is your name : ")  # player name
while n > 0:
    if n % 3 == 1:  # Condition i <= 2 and Dangerous area let's hooman pick first
        i = int(input(name+",how many sticks you will take (1 or 2)"))
        if i < 1 or i > 2:
            print("Don't cheat, Hooman !!")
            continue
            print(i)
        
        n = n-i
        if n > 0:
            print("There are", n, "sticks in the pile")
        elif n == 0:
            print(name, ", takes the last stick")
            print("PYTHON WIN !!!")  # Human lose python win
            break

        if n % 3 == 0: # to make python smarter
            x = 2
        elif n % 3 == 2:
            x = 1
        print("Python turn, I take", x, "stick(s)")

        n = n - x
        if n > 0:
            print("There are", n, "sticks in the pile")
        elif n == 0:
            print("Python, takes the last stick")
            print(name, "Win (Python felling sad :C)")  # Human win python lose
            break
    else: #outoff dangerous area let's Python pick first to 100% win rate
        if n % 3 == 0: # to make python smarter
            x = 2
        elif n % 3 == 2:
            x = 1
        print("Python turn, I take", x, "stick(s)")

        n = n - x
        if n > 0:
            print("There are", n, "sticks in the pile")
        elif n == 0:
            print("Python, takes the last stick")
            print(name, "Win (Python felling sad :C)")  # Human win python lose
            break
    #Hooman turn
        i = int(input(name+",how many sticks you will take (1 or 2)"))
        if i < 1 or i > 2:
            print("Don't cheat, Hooman !!")
            continue
            print(i)
        n = n-i
        if n > 0:
            print("There are", n, "sticks in the pile")
        elif n == 0:
            print(name, ", takes the last stick")
            print("PYTHON WIN !!!")  # Human lose python win
            break
