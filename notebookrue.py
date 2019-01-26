start = True

while start:
	print("(1) Lue muistikirjaa\n(2) Lisää merkintä\n(3) Tyhjennä muistikirja\n(4) Lopeta")
	userselection = int(input("Mitä haluat tehdä?: "))
	if userselection == 1:
		file = open("muistio.txt","r")
		content = file.readlines()
		for i in content:
			print(i)
	
		file.close()
	elif userselection == 2:
		file = open("muistio.txt","a")
		addText = input("Kirjoita uusi merkintä : ")
		file.write(addText)
		file.close()	
	elif userselection == 3:
		file = open("muistio.txt","w")
		file.close()
		print("Muistio tyhjennetty.")

	elif userselection == 4:
		print("Lopetetaan.")
		start = False


