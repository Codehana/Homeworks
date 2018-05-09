#!/usr/bin/python3


while True:
	x = int(input("Co chcete rozměnit? "))
	def automat(x):
		
		padesat = 0
		dvacet = 0
		deset = 0
		pet = 0
		dve = 0
		jedna = 0
		
		while x != 0:
			if x//50 >= 1:
				padesat = x//50
				x = x - padesat*50
			elif x//20 >= 1:
				dvacet = x//20
				x = x - dvacet*20
			elif x//10 >= 1:
				deset = x//10
				x = x - deset*10
			elif x//5 >= 1:
				pet = x//5
				x = x - pet*5
			elif x//2 >= 1:
				dve = x//2
				x = x - dve*2
			else:
				jedna = x
				x = x - jedna
		print("Padesát:",padesat)
		print("Dvacet:",dvacet)
		print("Deset:",deset)
		print("Pět:",pet)
		print("Dvě:",dve)
		print("Jedna:",jedna)
		return("")
	
	print(automat(x))


