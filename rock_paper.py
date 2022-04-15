# -*- coding: utf-8 -*-

dash='''
┬─┐┌─┐┌─┐┬┌─  ┌─┐┌─┐┌─┐┌─┐┬─┐  ┌─┐┌─┐┬┌─┐┌─┐┌─┐┬─┐┌─┐
├┬┘│ ││  ├┴┐  ├─┘├─┤├─┘├┤ ├┬┘  └─┐│  │└─┐└─┐│ │├┬┘└─┐
┴└─└─┘└─┘┴ ┴  ┴  ┴ ┴┴  └─┘┴└─  └─┘└─┘┴└─┘└─┘└─┘┴└─└─┘
'''
print(dash)
from ast import Pass
import random

user_choice= input("Enter your choice:\n 1: Rock \n 2: Paper \n 3: Scissors\n")

computer_choice=random.randint(1,3)
print(computer_choice)

if user_choice == computer_choice:
    print('Tie')
elif (user_choice == 3 and computer_choice == 2) or (user_choice == 2 and computer_choice==1 ) or(user_choice == 1 and computer_choice== 3):
    print("You win")
else:
     print("You loss")

