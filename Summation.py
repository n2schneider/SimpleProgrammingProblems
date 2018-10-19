#!/usr/bin/env python3
# Write a program that asks the user for a number n and prints the sum of the numbers 1 to n
number = input("Please Enter a number\n")
number = int(number)
answer = 0
for i in range(number+1):
	answer = answer + i

print(answer)
