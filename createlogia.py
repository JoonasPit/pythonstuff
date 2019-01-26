tiedosto = input("Minkä niminen tiedosto luodaan?: ")
text = input("Mitä kirjoitetaan tiedostoon?: ")
file = open(tiedosto,"w")
file.write(text)
file.close()

print("Luotiin tiedosto ",tiedosto,"ja siihen tallennettiin teksti: ", text)

