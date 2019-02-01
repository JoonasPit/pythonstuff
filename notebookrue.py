import time



def addTime():
	return time.strftime("%X %x")

def main ():
	
	start = True
	while start:
		print("(1) Read notebook\n(2) Add note\n(3) Empty notebook\n(4) Exit")
		userselection = int(input("What do you wish to do? : "))
		if userselection == 1:
			file = open("muistio.txt","r")
			content = file.readlines()
			for i in content:
				print(i, end = "")
		
			file.close()
		elif userselection == 2:
			file = open("muistio.txt","a")
			addText = "\n" +  input("Add note: ") + ":::" + addTime()
			file.write(addText)

			file.close()	
		elif userselection == 3:
			file = open("muistio.txt","w")
			file.close()
			print("Notebook emptied.")

		elif userselection == 4:
			print("Exiting.")
			start = False

if __name__ == "__main__":
	main()
