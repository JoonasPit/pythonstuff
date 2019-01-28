import random
## Jalka1 voittaa torakka3
## Ydinase2 voittaa jalka1
## torakka3 voittaa ydinase2

def kps():
    a = random.randint(1,3)
    if a == 1:
        a = "Jalka"
    elif a == 2:
        a = "Ydinase"
    elif a == 3:
        a = "Torakka"
    return a
def main():
    i = True
    round = 0
    wins = 0
    draws = 0
    losses = 0
    while i:
        round = round + 1
        computerselection = kps()
        userselection = input("Jalka, Ydinase vai Torakka? (Lopeta lopettaa): ")
        
        if userselection != "Lopeta":
            print("Sinä valitsit:", userselection)
            print("Tietokone valitsi:", kps())
            if userselection == computerselection:
                print("Tasapeli!")
                draws = draws + 1
            elif computerselection == userselection:
                print("Tasapeli!")
                draws = draws
            elif userselection == "Jalka" and computerselection == "Ydinase":
                print("Hävisit!")
                losses = losses +1
            elif userselection == "Jalka" and computerselection == "Torakka":
                print("Voitit!")
                wins = wins + 1
            elif userselection == "Ydinase" and computerselection == "Torakka":
                print("Hävisit!")
                losses = losses + 1
            elif userselection == "Ydinase" and computerselection == "Jalka":
                print("Voitit!")
                wins = wins +1
            elif userselection == "Torakka" and computerselection == "Ydinase":
                print("Voitit!")
                wins = wins + 1
            elif userselection == "Torakka" and computerselection == "Jalka":
                print("Hävisit!")
                losses = losses + 1

        elif userselection == "Lopeta":
            round = round -1
            print("Pelasit",round,"kierrosta, joista voitit", wins,"ja pelasit tasan",draws,"peliä.")
            i = False
       
if __name__ == "__main__":
    main()