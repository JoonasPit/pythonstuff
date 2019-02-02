import time

def newBooknote():
    filename = input("Anna tiedoston nimi: ")
    try:
        file = open(filename,"r")
        file.close()
        usernamedLoop(filename)
    except IOError:
        print("Tiedostoa ei löydy, luodaan tiedosto.") 
        file = open(filename,"w")
        file.close()
        usernamedLoop(filename)
def testNote():
    file = open("muistio.txt","r")
    file.close()
def createDefNote():
    file = open("muistio.txt","w")
    file.close()
def addTime():
	return time.strftime("%X %x")
def usernamedLoop(filename):
    stert = True
    while stert:
        print("Käytetään muistiota", filename)
        print("(1) Lue muistikirjaa\n(2) Lisää merkintä\n(3) Tyhjennä muistikirja\n(4) Vaihda muistiota\n(5) Lopeta")
        userselection = int(input("Mitä haluat tehdä? : "))
        if userselection == 1:
            file = open(filename,"r")
            content = file.readlines()
            for i in content:
                print(i, end = "")
            print("\n")
            file.close()
        elif userselection == 2:
            file = open(filename,"a")
            addText = "\n" +  input("Lisää merkintä: ") + ":::" + addTime()
            file.write(addText)

            file.close()

        elif userselection == 3:
            file = open(filename,"w")
            file.close()
            print("Muistio tyhjennetty.")

        elif userselection == 4:
            newBooknote()
            stert = False
        elif userselection == 5:
            print("Lopetetaan.")
            stert = False
            



def main ():
    start = True
    try:
        testNote()
    except IOError:
        print("Oletusmuistiota ei löydy, luodaan tiedosto.")
        createDefNote()
    while start:
       
        print("Käytetään muistiota: muistio.txt\n(1) Lue muistikirjaa\n(2) Lisää merkintä\n(3) Tyhjennä muistikirja\n(4) Vaihda muistiota\n(5) Lopeta")
        userselection = int(input("Mitä haluat tehdä? : "))
        if userselection == 1:
            file = open("muistio.txt","r")
            content = file.readlines() 
            for i in content:
                print(i, end = "")
            print("\n")
            file.close()
        elif userselection == 2:
            file = open("muistio.txt","a")
            addText = "\n" +  input("Kirjoita uusi: ") + ":::" + addTime()
            file.write(addText)

            file.close()

        elif userselection == 3:
            file = open("muistio.txt","w")
            file.close()
            print("Muistio tyhjennetty.")

        elif userselection == 4:
            newBooknote()
            start = False

        elif userselection == 5:
            print("Lopetetaan.")
            start = False

if __name__ == "__main__":
	main()
