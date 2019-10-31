import random


def randomgetalmaken():
    """
output: een random getal tussen 0 en 9
"""
    randomgetal = random.randint(0,9)
    return randomgetal

def listmaken(maken):
    """input: maken, antwoord op de vraag of er een loterijnummer gemaakt moet worden
output: loterijnummer
"""
    lotterynumber = []    
    if maken == "y":
        for i in range(9):
            randomgetal = randomgetalmaken()
            lotterynumber += [randomgetal]

    while lotterynumber != []:
        return lotterynumber

def main():
    maken = input("Wil je een loterijnummer genereren?(y/n)")
    lotterynumber = listmaken(maken)
    print(lotterynumber)
main()
    
