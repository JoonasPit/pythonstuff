import sys
def listAdd(shoppinglist):
    addtolist = input("Mitä lisätään?: ")
    shoppinglist.append(addtolist)

def listRemove(shoppinglist):
    amount = 0
    for b in shoppinglist:
        amount = amount + 1
    
    print("Listalla on ", amount, "alkiota.")
    try:
        whatremove = int(input("Monesko niistä poistetaan?: "))
    except ValueError:
        print("Virheellinen valinta.")
        listRemove(shoppinglist)
    if whatremove > amount:
        print("Virheellinen valinta.")
        askWhattodo()
    shoppinglist.pop(whatremove)

def printall(shoppinglist):

    try:
        shoppinglist[0]
        print("Listalla oli tuotteet:")
        for i in shoppinglist:
            print(i)
    except IndexError:
        print("Listalla oli tuotteet:")
    sys.exit(0)                 # I feel like I took a shortcut here... 
                                # should have printed in main function
def askWhattodo():
    run = True
    shoppinglist = []

    while run == True:
        try:
            userinput = int(input("Haluatko\n(1)Lisätä listaan\n(2)Poistaa listalta vai\n(3)Lopettaa?: "))   
        except ValueError:
            print("Must be a number")
            askWhattodo()
        if userinput == 3:
            printall(shoppinglist)
            run = False
            break
        elif userinput == 2:
            listRemove(shoppinglist)
            continue
        elif userinput ==1:
            listAdd(shoppinglist)
            continue
        else:
            print("Virheellinen valinta.")
            continue
def main():
    askWhattodo()
if __name__ == "__main__":
    main()