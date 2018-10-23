#!/usr/bin/env python3
# Write a program that asks the user for a number n and gives them the possibility to choose between computing the sum and computing the product of 1,…,n.
number = input("Please Enter a number\n")
number = int(number)
choice = input("Would you like the Product or Summation of this number? \n 1 - Product \n 2 - Summation\n")
choice = int(choice)
if choice == 1:
	answer = number*number
elif choice == 2:
	answer = number + number
else:
	print("You have chose a invalid choice so I choose option 1")
	answer = number*number
print(answer)
