document = open("esimerkki.txt","r")
contents = document.readlines()
print("Tiedostosta luettiin teksti: ")

for i in (contents):

	print(i)

document.close
