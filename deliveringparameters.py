def toinenpotenssi(numbervar1):
    powersecond = numbervar1 * numbervar1
    return powersecond

def main():
    numbervar1 = int(input("Give me a number: "))
    print("Toinen potenssi on",toinenpotenssi(numbervar1))
if __name__ == "__main__":
    main()