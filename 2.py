import random


def randomgetalmaken():
    """maakt een random getal tussen 0 en 9
    
    input:
    output:
    return randomgetal
    """
    randomgetal = random.randint(0,9)
    return randomgetal

def listmaken(maken):
    """wanneer het antwoord "y" is wordt er een lotterynumber met random getallen gemaakt door deze aan een list toe te voegen.
    
    input: 
    maken - string
    output: 
    return loterijnummer
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
    
