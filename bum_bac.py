#! /usr/bin/env python3

a = int(input("Kolik bude a? "))
b = int(input("Kolik bude b? "))

posloupnost = range(a,b) or range(b,a)

for x in posloupnost:
	if(x%2 == 1) and(x%6 == 0):		
		print("bum" + "bac")
	elif(x%6 == 0):
		print("bac")
	elif(x%2 == 1):
		print("bum")
	else: 
		print(x)
