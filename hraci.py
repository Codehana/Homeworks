#! /usr/bin/env python3

from random import randrange

vysledky1 = []
vysledky2 = []
vysledky3 = []
vysledky4 = []


def hra(vysledky1,vysledky2,vysledky3,vysledky4):
	cislo = [randrange(1,7),randrange(1,7),randrange(1,7),randrange(1,7),randrange(1,7)]
	cislo2 = [randrange(1,7),randrange(1,7),randrange(1,7),randrange(1,7),randrange(1,7)]
	cislo3 = [randrange(1,7),randrange(1,7),randrange(1,7),randrange(1,7),randrange(1,7)]
	cislo4 = [randrange(1,7),randrange(1,7),randrange(1,7),randrange(1,7),randrange(1,7)]
	x=0
	y=0
	z=0
	w=0		
	for x in cislo:
		vysledky1.append(x)
			
	for y in cislo2:
		vysledky2.append(y)
			
	for z in cislo3:
		vysledky3.append(z)
			
	for w in cislo4:
		vysledky4.append(w)
	print("vysledky1 ={}".format(vysledky1))
	print("vysledky2 ={}".format(vysledky2))
	print("vysledky3 ={}".format(vysledky3))
	print("vysledky4 ={}".format(vysledky4))
	print("")
	
	#jednotlívá kola
	a = [vysledky1[0], vysledky2[0], vysledky3[0], vysledky4[0]]
	b = [vysledky1[1], vysledky2[1], vysledky3[1], vysledky4[1]]
	c = [vysledky1[2], vysledky2[2], vysledky3[2], vysledky4[2]]
	d = [vysledky1[3], vysledky2[3], vysledky3[3], vysledky4[3]]
	e = [vysledky1[4], vysledky2[4], vysledky3[4], vysledky4[4]]
	pocet_her = [a,b,c,d,e]	
	
	#maximální hodnoty v každém kole
	aa = max(a)
	bb = max(b)
	cc = max(c)
	dd = max(d)
	ee = max(e)
	
	celkovy_vitez = [] #zde se budou hromadit body za jednotlivá kola pro hráče
	
	#protože budeme maxima po kole vždy odstraňovat, čísla v seznamu se budou měnit své pozice, budeme 		pozice zase "vracet" zpět
	aaa = 0
	bbb = 0
	ccc = 0
	ddd = 0
	eee = 0

	print("První kolo:")
	while aa in a:
		print("	Vítěz je hráč č.",(a.index(max(a)))+1+aaa)
		celkovy_vitez.append(a.index(max(a))+1+aaa)
		aaa = aaa+1
		a.remove(aa)
		
	print("Druhé kolo:")
	while bb in b:
		print("	Vítěz je hráč č.",(b.index(max(b)))+1+bbb)
		celkovy_vitez.append(b.index(max(b))+1+bbb)
		bbb = bbb+1
		b.remove(bb)

	print("Třetí kolo:")
	while cc in c:
		print("	Vítěz je hráč č.",(c.index(max(c)))+1+ccc)
		celkovy_vitez.append(c.index(max(c))+1+ccc)
		ccc = ccc+1
		c.remove(cc)

	print("Čtvrté kolo:")
	while dd in d:
		print("	Vítěz je hráč č.",(d.index(max(d)))+1+ddd)
		celkovy_vitez.append(d.index(max(d))+1+ddd)
		ddd = ddd+1
		d.remove(dd)

	print("Páté kolo:")
	while ee in e:
		print("	Vítěz je hráč č.",(e.index(max(e)))+1+eee)
		celkovy_vitez.append(e.index(max(e))+1+eee)
		eee = eee+1
		e.remove(ee)
	c4 = 4
	c3 = 3
	c2 = 2
	c1 = 1

	hrac1 = 0
	hrac2 = 0
	hrac3 = 0
	hrac4 = 0
	
	while len(celkovy_vitez) != 0:
		if c4 in celkovy_vitez:	
			hrac4 = hrac4 + 1
			celkovy_vitez.remove(c4)
			
		if c3 in celkovy_vitez:
			hrac3 = hrac3 + 1
			celkovy_vitez.remove(c3)
			
		if c2 in celkovy_vitez:
			hrac2 = hrac2 + 1
			celkovy_vitez.remove(c2)
		
		if c1 in celkovy_vitez:
			hrac1 = hrac1 + 1
			celkovy_vitez.remove(c1)
	print("")
	print("Celkové vítězství:")		
	hraci = [hrac1,hrac2,hrac3,hrac4]
	hraci_max = max(hraci)
	maxx = 0

	while hraci_max in hraci:
		print("	Celkovým vítězem je hráč č.",(hraci.index(max(hraci)))+1+maxx)
		maxx = maxx+1
		hraci.remove(hraci_max)
			 
	return("Díky za hru!")
	
print(hra(vysledky1,vysledky2,vysledky3,vysledky4))










