class Peli:
    
    def __init__(self, vari, pisteet):
        self.vari = vari
        self.pisteet = pisteet
    
    def goal(self):
        self.pisteet = int(self.pisteet +1)
        return self.pisteet
    
    def result(self):
    #    return '{} {} {} {} {}'.format("Olen", self.vari, "ja minulla on", self.pisteet,"pistettä!")
        print("Olen", self.vari, "ja minulla on", self.pisteet,"pistettä!")
eka = Peli("sininen", 0)
eka.goal()
eka.result()




