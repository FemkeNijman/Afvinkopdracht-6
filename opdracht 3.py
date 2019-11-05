def lees_inhoud(bestandnaam):
    """opent het bestand, split op enters en haalt dakjes weg. Hij splitst ook delen van het bestand in lijsten
    
    input:
    bestandnaam - string
    output:
    return namelijst, knipplekken - list
    """
    bestand = open(bestandnaam)
    namenlijst = []
    knipplekken = []
    for regel in bestand:
        naam, knipplek= regel.split(" ")
        namenlijst.append(naam)
        knipplekken.append(knipplek.replace('^','').rstrip())
    return namenlijst, knipplekken



def match(namenlijst, knipplekken, sequentie):
    """gaat de sequentie na en kijkt of de sequentie matched met een knipplek. Hij kijkt ook welke naam bij welke knipplek hoort.
    
    input:
    namenlijst, knipplekken - list
    sequentie - string
    output: 
    """
    for i in range(len(knipplekken)):
        positie = sequentie.find(knipplekken[i])
        if positie != -1:
            print("Match met", namenlijst[i], "op positie", positie)
            print(sequentie)
            print(" "*(positie-1), knipplekken[i])



def main():
    sequentie = "ACTAGCAACCTCAAACAGACACCATGGTGCACCTGACTCCTGTGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCC"
    bestandnaam = "enzymlijst.txt"
    namenlijst, knipplekken = lees_inhoud(bestandnaam)
    match(namenlijst, knipplekken, sequentie)
main()
