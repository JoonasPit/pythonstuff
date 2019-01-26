file = open("merkkijonoja.txt", "r")
content = file.readlines()


for i in content:
	i = i[:-1]
	if i.isalnum()==False:
		print(i, "sisältää virheellisiä merkkejä.")
	else:
		print(i, "kelpaa salasanaksi.")

file.close()
