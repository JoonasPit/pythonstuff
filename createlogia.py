tiedosto = input("What will the file be named: ")
text = input("What to write in the file: ")
file = open(tiedosto,"w")
file.write(text)
file.close()

print("Created file ",tiedosto,"and wrote: ", text)

