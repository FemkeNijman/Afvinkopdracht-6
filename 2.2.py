def bestandopen(bestandnaam):
    """opent een bestand  en zet de eerste 5 zinnen in data
    
    input: 
    bestandsnaam - string
    output: 
    return data - string
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
