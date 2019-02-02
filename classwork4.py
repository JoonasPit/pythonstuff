class asiakas:
    """luokka määrittelee toimitettavat esineet"""

    kori = []
    def lisaa(self):
        esine = input("lisää esine ")
        self.kori.append(esine)
    def kassalle(self):
        print("Korissa oli")
        for i in range(0,len(self.kori)):
            print(self.kori[i], end ="")

def main():
    henkilo = asiakas()
    while True:
        valinta = input("Lisätäänkö tuote vai mennäänkö kassalle: ")
        if valinta == "kassalle":
            henkilo.kassalle()
            break
        else:
            henkilo.lisaa()

if __name__ == "__main__":
    main()