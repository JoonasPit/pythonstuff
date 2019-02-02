def readfile():
    try:
        print("Sanat laitettuna aakkosjärjestykseen: ")
        file = open("sanoja.txt","r")
        content = file.readlines()
        mylist = []
        for i in content:
            mylist.append(i[:-1])
        mylist.sort()
        for b in mylist:
            print(b)
    except IOError:
        print("wrong file")
def main():
    readfile()
if __name__ == "__main__":
    main()