def bestandopen(bestandnaam):
    """input: bestandsnaam
output: data
"""
    bestand = open(bestandnaam)
    data = ""

    for i in range(5):
        data += bestand.readline()

    return data

def main():
    bestand = bestandopen(input("Geef een bestandnaam: "))
    print(bestand)
    
main()
