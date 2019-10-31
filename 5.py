def bestandopen(bestandnaam):
    """
input: bestandnaam
output: data vanuit het bestand
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
