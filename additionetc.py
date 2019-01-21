number = int(input("Anna ensimmäinen luku: "))
number2 = int(input("Anna toinen luku: "))

while(True):
	print("(1) +")
	print("(2) -")
	print("(3) *")
	print("(4) /")
	print("(5) Vaihda luvut")
	print("(6) Lopeta")

	print("Valitut luvut: ",number, number2)
	choice = int(input("Tee valinta (1-6): "))

	if (choice == 1):
		print("Tulos on: ", number +  number2)
	elif (choice == 2):
		print("Tulos on: ", number - number2)
	elif (choice == 3):
		print("Tulos on: ", number * number2)
	elif (choice == 4):
		print("Tulos on: ",float(number / number2))
	elif (choice == 5):
		number = int(input("Anna uusi ensimmäinen luku: "))
		number2 = int(input("Anna uusi toinen luku: "))
	elif (choice == 6):
		break
	else:
		print("Valintaa ei tunnistettu.")
