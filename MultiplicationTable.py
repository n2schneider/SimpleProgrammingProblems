#!/usr/bin/env python3
# Write a program that prints a multiplication table for numbers up to 12.
for x in range (1,13):
	for y in range (1,13):
		print(str(x) + '*' + str(y) + '=' + str(x*y))