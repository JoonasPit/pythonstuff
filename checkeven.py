number = int(input("Anna luku: "))
number2 = int(input("Anna toinen luku: "))

if (number % 2 == 0) and (number2 % 2 == 0):

	print("Molemmat luvut ovat parillisia.")

elif (number % 2 == 0) and (number2 % 2 > 0):

	print("Toinen luku on parillinen.")

elif (number % 2 > 0) and (number2 % 2 == 0):

	print("Toinen luku on parillinen.")

elif (number % 2 > 0) and (number2 % 2 > 0):
	print("Molemmat luvut ovat parittomia.")
