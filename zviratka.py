#! /usr/bin/env python3


zvirata = {"ovce" : "4", "panda" : "4", "slepic : e""2", "pavouk" : "8", "slon" : "4" , "sova" : "2", "moucha" : "6" , "ryba" : "0" , "zebra" : "4" , "lemur" : "4"}


print("Zvířata, která mají 4 a více nohou:")
for zvire in zvirata.keys():
	if zvirata[zvire] >= "4":
		print(zvire)
# Vytisknou se zvířata, ktrá mají 4+ nohou


lepsi_zvirata = dict(
ovce = dict(srst = "chlupy", pocet_oci = "2", ocas = "ano", pocet_nohou = 0), 
panda = dict(srst = "chlupy", pocet_oci = "2", ocas = "ano", pocet_nohou = 0), 
slepice = dict(srst  = "peří", pocet_oci = "2", ocas = "ne", pocet_nohou = 0), 
pavouk = dict(srst = "chlupy", pocet_oci = "6", ocas = "ne", pocet_nohou = 0), 
slon = dict(srst = "kůže", pocet_oci = "2", ocas = "ano", pocet_nohou = 0), 
sova = dict(srst = "peří", pocet_oci = "2", ocas = "ne", pocet_nohou = 0), 
moucha = dict(srst = "chlupy", pocet_oci = "2", ocas = "ne", pocet_nohou = 0), 
ryba = dict(srst = "šupiny", pocet_oci = "2", ocas = "ano", pocet_nohou = 0), 
zebra = dict(srst = "chlupy", pocet_oci = "2", ocas = "ano", pocet_nohou = 0),
lemur = dict(srst = "chlupy", pocet_oci  = "2", ocas = "ano", pocet_nohou = 0)
)

x = 0
y = 0

for x in zvirata:
	animal = lepsi_zvirata[x]
	y = zvirata[x]
	animal["pocet_nohou"] = y
# Zařadí počet nohou ze slovníku "zvirata" do "lepsi_zvirata"

print("Zvířata, která nejsou chlupatá a mají ocas:")
for z,w in lepsi_zvirata.items():
	if w.get("srst") != "chlupy" and w.get("ocas") == "ano":
		print(z)
# Vybere z "lepsi_zvirata" ta, která nejsou chlupatá a mají ocas
