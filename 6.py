import random

def roll(number_of_throws):
    """geeft een random getal tussen 1 en 6 voor het gegeven aantal keer.
    
    input:
    number_of_throws - int
    output:
    return getallenlijst - list
    """
    getallenlijst = []
    if number_of_throws > 0:
        for i in range(number_of_throws):
            getal = random.randint(1,6)
            getallenlijst += [getal]
    else:
        print("Geef een positief getal")

    while getallenlijst != []:
        return getallenlijst
            

def main():
    number_of_throws = int(input("Hoe vaak wil je gooien? "))
    getallenlijst = roll(number_of_throws)
    print(getallenlijst)
main()
