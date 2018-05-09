#! /usr/bin/env python3
 
a=2
b=4 
c=5

import kvadr
v = kvadr.objem(a,b,c)
s = kvadr.plocha(a,b,c)

print(("Kvádr o stranách {},{},{} má objem {}").format(a,b,c,v))
print(("Kvádr o stranách {},{},{} má plochu {}").format(a,b,c,s))


import krychle
v = krychle.objem(a)
s = krychle.plocha(a)

print(("Krychle o stranách {} má objem {}").format(a,v))
print(("Krychle o stranách {} má plochu {}").format(a,s))

