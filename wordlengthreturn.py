def testlength(userword):
    wordlength = userword
    wordlength = len(userword)
    return wordlength
def main():
    gucci = True
    while gucci:
        userword = input("Give me a word (end with Lopeta): ")
        if userword == "Lopeta":
            gucci = False
        elif userword =="":
            print("Et antanut syötettä")
        else:
            print("The word is",testlength(userword),"characters long.")

if __name__ == "__main__":
    main()