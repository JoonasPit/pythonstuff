import random
def cointoss():
    i = 0
    while i < 5:
        a = 0
        i = i+1
        a = random.randint(1,2)
        if a == 1:
            print("Kruuna!")
        else:
            print("Klaava!")
def main():
    print("Heitetään kolikkoa viidesti:")
    cointoss()
if __name__ == "__main__":
    main()