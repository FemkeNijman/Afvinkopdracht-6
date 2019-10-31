def nummers():
    """
input: een gekozen cijfer
uitput: aantalcijfers en cijferlijst
"""
    aantalcijfers = 5
    cijferlijst = []
    for i in range(aantalcijfers):
        cijfer = (float(input("Geef een cijfer: ")))
        #gekozen cijfers worden in een lijst gezet
        cijferlijst += [cijfer]

    return aantalcijfers, cijferlijst

def gemiddeldeberekenen(aantalcijfers, cijferlijst):
    """input: aantalcijfers en cijferlijst
output: het berekende gemiddelde van de lijst
"""
    gemiddelde = (sum(cijferlijst)/aantalcijfers)
    return gemiddelde


def main():
    aantalcijfers, cijferlijst = nummers()
    print(cijferlijst)
    print("Het totaalaantal van de cijfers is: ",sum(cijferlijst))
    gemiddelde = gemiddeldeberekenen(aantalcijfers, cijferlijst)
    print("Het gemiddelde van de cijfers is: ", gemiddelde)
    print("Het hoogste getal is: ", max(cijferlijst))
    print("Het laagste getal is: ", min(cijferlijst))
main()
