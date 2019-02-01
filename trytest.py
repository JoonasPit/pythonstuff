num = input("Anna luku: ")
try:
    num = int(num)
    print("Syöte oli kelvollinen.")
except Exception:
    print("Virheellinen syöte!")