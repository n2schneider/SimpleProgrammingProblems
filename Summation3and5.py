#!/usr/bin/env python3
# Modify the previous program such that only multiples of three or five are considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17
number = input("Please Enter a number\n")
number = int(number)
answer = 0
for i in range(number+1):
	if(i % 3 == 0 or i % 5 == 0):
		answer = answer + i
	

print(answer)
