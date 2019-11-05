def nummers():
    """Vraagt 5x een cijfer en zet deze in een list genaamd cijferlijst
    
    input:
    cijfer - float
    uitput:
    return aantalcijfers, cijerlijst - list
    """
    aantalcijfers = 5
    cijferlijst = []
    for i in range(aantalcijfers):
        cijfer = (float(input("Geef een cijfer: ")))
        #gekozen cijfers worden in een lijst gezet
        cijferlijst += [cijfer]

    return aantalcijfers, cijferlijst

def gemiddeldeberekenen(aantalcijfers, cijferlijst):
    """berekent het gemiddelde van de cijfers in de cijferlijst
    
    input:
    aantalcijfers - int
    cijferlijst - list
    output: 
    return gemiddelde - float
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
