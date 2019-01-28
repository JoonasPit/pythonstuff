import re
def testaa(testattava):
    if bool(re.search("[a-zA-Z]", testattava)):
        if bool(re.search("[0-9]",testattava)):
            if len(testattava) > 5:
                    
                return True

        

def main():
    testattava = input("Anna salasana: ")
    tulos = testaa(testattava)

    if tulos == True:
        print("salasana on ok")
    else:
        print("not cool")
if __name__ == "__main__":
    main()
