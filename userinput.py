keepgoing = True

while keepgoing:
	printable = input("Kirjoita jotain: ")
	if  printable == "lopeta":
		keepgoing = False
		print("Lopetit ohjelman.")
	else:
		print(printable)






