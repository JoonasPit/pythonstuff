number = int(input("Anna ensimmäinen luku: "))
number2 = int(input("Anna toinen luku: "))
print("(1) +")
print("(2) -")
print("(3) *")
print("(4) /")


choice = int(input("Tee valinta (1-4): "))

if (choice == 1):
	print("Tulos on: ", number +  number2)
elif (choice == 2):
	print("Tulos on: ", number - number2)
elif (choice == 3):
	print("Tulos on: ", number * number2)
elif (choice == 4):
	print("Tulos on: ",float(number / number2))
else:
	print("Valintaa ei tunnistettu.")
