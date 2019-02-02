import time
import pickle
import sys
def loadpickle():
    try:
        file = open("muistio.dat","rb")
        thestuff = pickle.load(file)
        file.close()
        return thestuff
    except FileNotFoundError:
        testNote()
    except EOFError:
        testNote()
def insertTime():
    return time.strftime("%X %x")
def testNote():
    try:
        file = open("muistio.dat","r")
        file.close()
        return True
    except IOError:
        print("Virhe tiedostossa, luodaan uusi muistio.dat.")
        file = open("muistio.dat","w")
        file.close()

def readNotes(mainlist):
    try:
        for i in mainlist:
            print(i)
    except TypeError:
        notebookloop()
def newnote(mainlist):
    addText = input("Kirjoita uusi merkintä: ") + ":::" + insertTime()
    mainlist.append(addText)
def delNote(mainlist):
    t  = 0
    for i in mainlist:
        t = t +1
    print("Listalla on ",t,"merkintää.")
    delvalue = int(input("Mitä niistä poistetaan?: "))
    realmeans = delvalue -1
    print("Poistettiin merkintä ", mainlist[realmeans])
    mainlist.pop(realmeans)
    
def editanote(mainlist):
    b = 0
    for i in mainlist:
        b = b +1
    print("Listalla on", b,"merkintää.")
    changevalue = int(input("Mitä niistä muutetaan?: "))
    whatusermeans = changevalue - 1
    print(mainlist[whatusermeans])
    newvalue = input("Anna uusi teksti: ")
    mainlist[whatusermeans] = newvalue + ":::" + insertTime()

def savepickle(mainlist):
    tiedosto = open("muistio.dat","wb")
    pickle.dump(mainlist,tiedosto)

def notebookloop():
    start = True
    if testNote() == True:
        mainlist = loadpickle()
    else:
        mainlist = []   
    while start:
        print("(1) Lue muistikirjaa\n(2) Lisää merkintä\n(3) Muokkaa merkintää\n(4) Poista merkintä\n(5) Tallenna ja lopeta")
        userselection = int(input("Mitä haluat tehdä? : "))
        if userselection == 1:
            readNotes(mainlist)
        elif userselection == 2:
            newnote(mainlist)
        elif userselection == 3:
            editanote(mainlist)
        elif userselection == 4:
           delNote(mainlist)
        elif userselection == 5:
            savepickle(mainlist)
            print("Lopetetaan.")
            sys.exit(0)

def main ():
    notebookloop()

if __name__ == "__main__":
	main()
