def lees_inhoud(bestandnaam):
    bestand = open(bestandnaam)
    namenlijst = []
    knipplekken = []
    for regel in bestand:
        naam, knipplek= regel.split(" ")
        namenlijst.append(naam)
        knipplekken.append(knipplek.replace('^','').rstrip())
    return namenlijst, knipplekken



def match(namenlijst, knipplekken, sequentie):
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
