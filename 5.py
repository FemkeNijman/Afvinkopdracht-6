def bestandopen(bestandnaam):
    """opent een bestand, haalt alle witregels weg en zet ze in data
    
    input:
    bestandnaam - string
    output:
    return data - string
    """
    bestand = open(bestandnaam)
    data = 0

    for regel in bestand:
        data += int(regel.rstrip())
        
    return data

def main():
    totaal = bestandopen(input("Geef een bestandnaam: "))
    print("Het totale aantal is: ", totaal)
main()
