def woordenschrijven(aantalwoorden, bestandnaam):
"""
input: aantalwoorden en bestandnaam

output: een nieuw bestand met geschreven woorden
"""
    bestand = open(bestandnaam, "w")
    
    for i in range(aantalwoorden):
        woord = input("Schrijf een woord: ")
        bestand.write(woord)


def main():
    bestandnaam = "nieuwbestand.txt"
    aantalwoorden = int(input("Hoeveel woorden wil je schrijven? "))
    woordenschrijven(aantalwoorden, bestandnaam)
main()
