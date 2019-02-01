import math

def countsin(number, number2):
	return math.sin(number/number2)
	

def countcos(number, number2):
	return math.cos(number/number2)


def main():
	number = int(input("Anna ensimmäinen luku: "))
	number2 = int(input("Anna toinen luku: "))
	while(True):
		print("(1) +")
		print("(2) -")
		print("(3) *")
		print("(4) /")
		print("(5) sin(luku1/luku2)")
		print("(6) cos(luku1/luku2)")
		print("(7) Vaihda luvut")
		print("(8) Lopeta")
	
		print("Valitut luvut: ",number, number2)
		choice = int(input("Tee valinta (1-8): "))

		if (choice == 1):
			print("Tulos on: ", number +  number2)
		elif (choice == 2):
			print("Tulos on: ", number - number2)
		elif (choice == 3):
			print("Tulos on: ", number * number2)
		elif (choice == 4):
			print("Tulos on: ",float(number / number2))
		elif (choice == 5):
			print("Tulos on: ", countsin(number, number2))
		elif (choice == 6):
			print("Tulos on: ", countcos(number, number2))
		elif (choice == 7):
			number = int(input("Anna uusi ensimmäinen luku: "))
			number2 = int(input("Anna uusi toinen luku: "))
		elif (choice == 8):
			break
		else:
			print("Valintaa ei tunnistettu.")

if __name__ == "__main__":
	main() 	