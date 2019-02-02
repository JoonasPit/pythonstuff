class Kilpailija:
    """Kilpailija: sisältää pisteet ja värin"""    
  
    def __init__(self, vari, pisteet):
        self.vari = vari
        self.pisteet = pisteet
    def goal(self):
        self.pisteet = int(self.pisteet +1)
        return self.pisteet
    
    def result(self):
    #    return '{} {} {} {} {}'.format("Olen", self.vari, "ja minulla on", self.pisteet,"pistettä!")
        print("Olen", self.vari, "ja minulla on", self.pisteet,"pistettä!")

def main():
    eka = Kilpailija("sininen", 5)
    user1 = input("Anna minulle väri: ")
    user1 = Kilpailija(user1, 0)
    user2 = input("Anna minulle väri: ")
    user2 = Kilpailija(user2, 0)
    user1.result()
    user2.result()
    print(Kilpailija.__doc__)
if __name__ == "__main__":
    main()
