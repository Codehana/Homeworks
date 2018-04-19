#! /usr/bin/env python3

y = int(input("Kolik km chcete ujet? "))
def spotreba_auta(y):
	
	if y/100 > 1:
		y_1 = y/100
		y_2 = y_1*6
		y_3 = y_2/60
		y_4 = int(y_3)*60*32
	else:
		print("Není třeba tankovat.")
	return("Budete tankovat {}krát.".format(int(y_3)),"Budete platit celkem {}kč.".format(y_4))

	
print(spotreba_auta(y))

