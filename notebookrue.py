start = True

while start:
	print("(1) Read notebook\n(2) Add to notebook\n(3) Empty notebook\n(4) Quit")
	userselection = int(input("What do you wish to do? : "))
	if userselection == 1:
		file = open("muistio.txt","r")
		content = file.readlines()
		for i in content:
			print(i)
	
		file.close()
	elif userselection == 2:
		file = open("muistio.txt","a")
		addText = input("Add note: ")
		file.write(addText)
		file.close()	
	elif userselection == 3:
		file = open("muistio.txt","w")
		file.close()
		print("Notebook emptied.")

	elif userselection == 4:
		print("Exiting.")
		start = False


