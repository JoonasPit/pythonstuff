class emo:
    arvo = 0
    tila = "Toiminnassa"
    def printer(self):
     return print("Minä olen emoluokka")

class lapsi(emo):
    def overwrite(self):
        return print("Minä olen lapsiluokka")

def main():
    x = emo()
    y= lapsi()
    print(x.tila)
    x.printer()
    print(y.tila)
    y.overwrite()
    

if __name__ == "__main__":
    main()