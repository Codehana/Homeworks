#! /usr/bin/env python3

import random

def bludiste():
	blud = []
	radek = -1
	w = 24
	for b in range(25):
		blud.append([])
		for x in range(25):
			blud[-1].append(0)
	while w != 0:
		w = w -1
		if w == 23:
			z = blud[-1]
			z[random.choice(range(24))] = "  "
			umisteni = int(z.index("  "))
		radek2 = radek -1
		z = blud[radek]
		z1 = blud[radek2]
		U = random.choice([-1,0,1])
		U1 = random.choice([-1,1])
		umisteni = umisteni + U + U1
		if 0 <= umisteni <= 24:
			z[umisteni] = "  "
			radek = radek2
		else:
			w = w + 1
			radek = radek + 1
	return(blud)
print(bludiste())

