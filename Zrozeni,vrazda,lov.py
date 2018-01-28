#! /usr/bin/env python3

import random

pocet_zvirat = int(input("Kolik bude zvířátek? "))
seznam_zvirat = []
def genesis(pocet_zvirat):
	while pocet_zvirat != 0:
		pocet_zvirat = pocet_zvirat - 1
		casti = {"nohy":[2,3,4], "kozich":["True","False"], "jidlo":["maso","oboje","vegie"]}
		z = {"pocet_nohou":random.choice(casti["nohy"]), "kozisek":random.choice(casti["kozich"]), "potrava":random.choice(casti["jidlo"])}
		seznam_zvirat.append(z)
	
	return(seznam_zvirat)
	
print(genesis(pocet_zvirat))	
print()


umrtnost = int(input("Kolik procent zvířat zahyne? "))
def armagedon(seznam_zvirat,umrtnost):
	pocet_odstraneni = int(len(seznam_zvirat) * (umrtnost/100))
	while pocet_odstraneni != 0:
		seznam_zvirat.remove(random.choice(seznam_zvirat))
		pocet_odstraneni = pocet_odstraneni - 1

	return(seznam_zvirat)
seznam_zvirat = armagedon(seznam_zvirat,umrtnost)
print(seznam_zvirat)
print()

