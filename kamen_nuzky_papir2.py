#! /usr/bin/env python3


from random import randrange
pocitac = 0
x = 0


def K_N_P(pocitac,x):	
	d={1:"kamen",2:"nuzky",3:"papir"}
	l=[1,2,3]
	Vy = 0
	PC = 0
	for l in range(3):
			
		pocitac = randrange(1,4)
		x = input("Váš tah bude kamen, nuzky nebo papir? ")
		print("Počítač vybral {}.".format(d[pocitac]))

		if x == d[pocitac]:
			print("remíza = nikdo nemá bod.")
		
		elif x == "kamen":			
			if pocitac == 2: 
				print("Máte bod.")
				Vy = Vy + 1
				
			else:
				print("PC má bod.")
				PC = PC +1	
				
		elif x == "nuzky":			
			if pocitac == 3: 
				Vy = Vy + 1
				print("Máte bod.")
				
			else:
				PC = PC + 1
				print("PC má bod.")
				
		elif x == "papir":			
			if pocitac == 1: 
				Vy = Vy + 1
				print("Máte bod.")	
			else:				
				PC = PC + 1
				print("PC má bod.")
				
		else:
			print("Nerozumím")
	if PC > Vy:
		print("Prohrál/a jste :( ")
	elif PC == Vy:
		print("Je to plichta!")
	else:
		print("Vyhrál/a jste! Gratuluji! ;) ")

	return("PC: {} " "Vy:{}".format(PC,Vy))
	
	
		
print(K_N_P(pocitac,x))


						
