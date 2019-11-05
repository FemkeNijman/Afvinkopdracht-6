def woordenschrijven(aantalwoorden, bestandnaam):
    """maakt een nieuw bestand met getypte woorden
    
    input:
    aantalwoorden - int
    bestandnaam - string
    output:
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
