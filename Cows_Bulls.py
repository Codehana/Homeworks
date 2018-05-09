#! /usr/bin/env python3
#veta = input("Napište větu. ")

def obrat_vetu(veta):
	veta = veta.split(" ")
	return " ".join(veta[::-1])
#print(obrat_vetu(veta))

#Malé velké kotě žije na poušti.


#Cows and bulls:
def cows_bulls(number, guess_number):	
	cow = 0
	bull= 0
	for x in range(len(guess_number)):
		if guess_number[x] == number[x]:
			cow = cow + 1
		else:
			bull = bull + 1
	
	return cow,bull 

playing = True
attempt = 0
number = "1356"

while playing:
	
	guess_number = (input("Enter the number: "))
	
	count = cows_bulls(number, guess_number)
	attempt = attempt +1
	print("{}:Cows  {}:Bulls".format(count[0],count[1]))
	if count[0] == 4:
		playing = False
		print("You're winner!")
		print("Pokusy: ",attempt)
