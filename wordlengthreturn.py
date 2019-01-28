def testlength(userword):
    wordlength = userword
    wordlength = len(userword)
    return wordlength
def main():
    gucci = True
    while gucci:
        userword = input("Anna sana: ")
        if userword == "Lopeta":
            gucci = False
        elif userword =="":
            print("Et antanut syötettä")
        else:
            print("Sana on ",testlength(userword))

if __name__ == "__main__":
    main()