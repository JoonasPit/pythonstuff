def printfunction(userword):
    nextword = userword
    print(nextword) 
def main():
    gucci = True
    while gucci:
        userword = input("Give me a word (End with Lopeta) ")
        if userword == "Lopeta":
            gucci = False
        elif len(userword) < 5:
            print("Oletustulostus")
        else:
            printfunction(userword)

if __name__ == "__main__":
    main()