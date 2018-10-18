#!/usr/bin/env python3
# Write a program that asks the user for their name and greets them with their name.
# Modify the previous program such that only the users Alice and Bob are greeted with their names.
Name = input('Enter your name:')
if (Name == 'Alice' or Name == 'Bob'):
	print('Hello, ' + Name)
else:
	print('You are not the choosen one.')