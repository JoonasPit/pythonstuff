    
def readFile(filename):
    file = open(filename,"r")
    content = file.readlines()
    file.close()   
    return content
def main():
    filename = input(("Anna tiedoston nimi: "))
  
    try:
        readStuff = readFile(filename)
        numtest = int(readStuff[0])
        print("Saatiin tulos", numtest+313)
    except ValueError:
        print("Tiedoston sisältö virheellinen!")
    except IOError:
        print("Virheellinen tiedostonnimi")
if __name__ == "__main__":
    main()