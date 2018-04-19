#! /usr/bin/env python3

#a = "čokoláda"

def obrat(a):
	return a[::-1]

#print(obrat(a))


def sude(v):
	licha_cisla = []
	for l in v:
		if l%2 != 0:
			licha_cisla.append(l)
	return licha_cisla

def delitelne_3(licha_cisla):
	cisla_bez_3 = []
	for x in licha_cisla:
		
		if int(x)%3 == 0:
			cisla_bez_3.append(x)
	return cisla_bez_3


def delitelne_6(cisla_bez_3):
	delitelne6 = []
	for f in cisla_bez_3:
		if f%6 == 0:
			delitelne6.append(f)
	return delitelne6

xx = [x for x in range(40)]
licha_cisla = sude(xx)
print(licha_cisla)
cisla_bez_3 = delitelne_3(licha_cisla)
print(cisla_bez_3)
delitelne6 = delitelne_6(cisla_bez_3)

print(delitelne_6(delitelne6))
